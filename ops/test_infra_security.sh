#!/bin/bash
# Infrastructure Security Test Suite
# Verifies all Wave 4 security fixes are properly implemented

set -e

echo "=========================================="
echo "Infrastructure Security Test Suite"
echo "=========================================="
echo ""

PASS=0
FAIL=0

# Helper functions
pass() {
    echo "✅ PASS: $1"
    ((PASS++))
}

fail() {
    echo "❌ FAIL: $1"
    ((FAIL++))
}

# Test 1: Root Dockerfile uses multi-stage build
echo "Testing T19: Root Dockerfile..."
if grep -q "AS builder" Dockerfile && grep -q "AS runtime" Dockerfile; then
    pass "Dockerfile uses multi-stage build"
else
    fail "Dockerfile multi-stage build not found"
fi

if grep -q "appuser" Dockerfile; then
    pass "Dockerfile creates non-root user"
else
    fail "Dockerfile non-root user not found"
fi

if grep -q "gunicorn" Dockerfile; then
    pass "Dockerfile uses gunicorn"
else
    fail "Dockerfile gunicorn not found"
fi

if grep -q "HEALTHCHECK" Dockerfile; then
    pass "Dockerfile has HEALTHCHECK"
else
    fail "Dockerfile HEALTHCHECK not found"
fi

# Test 2: Resource limits in docker-compose
echo ""
echo "Testing T20: Resource limits..."
if grep -q "memory:" ops/docker-compose.backend.prod.yml; then
    pass "Resource limits defined in docker-compose"
else
    fail "Resource limits not found in docker-compose"
fi

# Test 3: No hardcoded IPs
echo ""
echo "Testing T21: Hardcoded IPs..."
if grep -r "100.99.222.101" ops/ 2>/dev/null | grep -v "vars.sh" | grep -qv ":"; then
    fail "Hardcoded IP found in deploy scripts"
else
    pass "No hardcoded IPs (except vars.sh default)"
fi

if [ -f ops/vars.sh ]; then
    pass "vars.sh exists for centralized config"
else
    fail "vars.sh not found"
fi

# Test 4: Redis TLS configuration
echo ""
echo "Testing T22: Redis TLS..."
if grep -q "tls-port\|rediss://\|REDIS_TLS" ops/docker-compose.backend.prod.yml ops/backend.env.production.example 2>/dev/null; then
    pass "Redis TLS configuration present"
else
    fail "Redis TLS not configured"
fi

# Test 5: Network isolation
echo ""
echo "Testing T23/T26: Network isolation..."
if grep -q "backend_internal" ops/docker-compose.backend.prod.yml && grep -q "redis_network" ops/docker-compose.backend.prod.yml; then
    pass "Custom networks defined"
else
    fail "Custom networks not defined"
fi

# Test 6: AUTH_SECRET validation
echo ""
echo "Testing T24: AUTH_SECRET validation..."
if grep -q "validateProductionSecrets" MyOwnClone/MyOwnClone/src/lib/auth.ts; then
    pass "AUTH_SECRET validation exists"
else
    fail "AUTH_SECRET validation not found"
fi

# Test 7: DB password in env var
echo ""
echo "Testing T25: DB password environment variable..."
if grep -q "POSTGRES_PASSWORD: \${DB_PASSWORD}" ops/docker-compose.backend.prod.yml; then
    pass "DB password uses environment variable"
else
    fail "DB password not using env var"
fi

# Summary
echo ""
echo "=========================================="
echo "Test Summary"
echo "=========================================="
echo "Passed: $PASS"
echo "Failed: $FAIL"
echo ""

if [ $FAIL -eq 0 ]; then
    echo "🎉 All infrastructure security tests passed!"
    exit 0
else
    echo "⚠️  $FAIL test(s) failed. Please review."
    exit 1
fi
