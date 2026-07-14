#!/usr/bin/env bash
# Docker Security Test Helper
# Verifies Dockerfiles meet security baseline: non-root user, multi-stage, no hardcoded secrets
# Exit codes: 0 = pass (secure), 1 = fail (insecure), 2 = error

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
COMPOSE_FILE="$PROJECT_ROOT/ops/docker-compose.backend.prod.yml"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counters
PASS_COUNT=0
FAIL_COUNT=0
WARN_COUNT=0

print_header() {
    echo ""
    echo "========================================"
    echo "Docker Security Test: $1"
    echo "========================================"
}

print_pass() {
    echo -e "${GREEN}[PASS]${NC} $1"
    ((PASS_COUNT++))
}

print_fail() {
    echo -e "${RED}[FAIL]${NC} $1"
    ((FAIL_COUNT++))
}

print_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
    ((WARN_COUNT++))
}

# Check 1: Dockerfile uses non-root user
check_non_root_user() {
    local dockerfile="$1"
    print_header "Checking for non-root user in $dockerfile"

    if [[ ! -f "$dockerfile" ]]; then
        print_fail "Dockerfile not found: $dockerfile"
        return 1
    fi

    # Look for USER instruction with non-root user (not root, not 0)
    if grep -qE 'USER\s+(appuser|node|nginx|gunicorn|postgres|redis|www-data|[^:]+\.(?!root)[^:]*|100[0-9]:)' "$dockerfile" 2>/dev/null; then
        print_pass "Non-root user found (USER instruction with non-root account)"
        return 0
    fi

    # Check if useradd/groupadd creates non-root user
    if grep -qE '(useradd|groupadd).*(?!--system\s+--uid\s+0|--gid\s+0)' "$dockerfile" 2>/dev/null; then
        if grep -qE '(useradd|groupadd).*(?!--system\s+--uid\s+0|--gid\s+0)' "$dockerfile" | grep -qv 'uid.*0\|gid.*0' 2>/dev/null; then
            print_pass "Non-root user creation found"
            return 0
        fi
    fi

    print_fail "No non-root user found - container runs as root"
    return 1
}

# Check 2: Dockerfile uses multi-stage build
check_multi_stage() {
    local dockerfile="$1"
    print_header "Checking for multi-stage build in $dockerfile"

    if [[ ! -f "$dockerfile" ]]; then
        print_fail "Dockerfile not found: $dockerfile"
        return 1
    fi

    # Count FROM instructions - multi-stage has 2+ FROM statements
    local from_count
    from_count=$(grep -cE '^FROM\s+' "$dockerfile" 2>/dev/null || echo "0")

    if [[ "$from_count" -ge 2 ]]; then
        print_pass "Multi-stage build detected ($from_count FROM statements)"
        return 0
    fi

    print_fail "No multi-stage build found (only $from_count FROM statement)"
    return 1
}

# Check 3: No hardcoded secrets in Dockerfile
check_no_secrets() {
    local dockerfile="$1"
    print_header "Checking for hardcoded secrets in $dockerfile"

    if [[ ! -f "$dockerfile" ]]; then
        print_fail "Dockerfile not found: $dockerfile"
        return 1
    fi

    # Patterns for hardcoded secrets
    local secret_patterns=(
        'password\s*=\s*["'\''][^"'\'']{8,}["'\'']'
        'api_key\s*=\s*["'\''][^"'\'']{8,}["'\'']'
        'secret\s*=\s*["'\''][^"'\'']{8,}["'\'']'
        'token\s*=\s*["'\''][^"'\'']{8,}["'\'']'
        'PRIVATE\s*KEY'
        'BEGIN\s+(RSA|EC|DSA|OPENSSH)\s+PRIVATE\s+KEY'
    )

    local found_secrets=0
    for pattern in "${secret_patterns[@]}"; do
        if grep -iE "$pattern" "$dockerfile" 2>/dev/null | grep -v '^[[:space:]]*#' >/dev/null; then
            print_fail "Hardcoded secret detected: pattern '$pattern'"
            found_secrets=1
        fi
    done

    # Check for EXPOSE with high ports indicating direct prod access
    if grep -qE '^EXPOSE\s+(5432|6379|27017|9200)' "$dockerfile" 2>/dev/null; then
        print_warn "Direct exposure of database port detected"
    fi

    if [[ "$found_secrets" -eq 0 ]]; then
        print_pass "No hardcoded secrets found"
        return 0
    fi

    return 1
}

# Check 4: Resource limits in docker-compose
check_resource_limits() {
    print_header "Checking for resource limits in docker-compose"

    if [[ ! -f "$COMPOSE_FILE" ]]; then
        print_warn "docker-compose file not found: $COMPOSE_FILE"
        return 0  # Warning only, not a hard fail
    fi

    # Check for deploy.resources.limits in any service
    if grep -qE 'deploy:.*resources:.*limits:' "$COMPOSE_FILE" 2>/dev/null; then
        print_pass "Resource limits found in docker-compose"
        return 0
    fi

    # Check for mem_limit or cpu_period (older compose format)
    if grep -qE '(mem_limit|cpu_period|cpu_quota|cpus)' "$COMPOSE_FILE" 2>/dev/null; then
        print_pass "Resource limits found (legacy format)"
        return 0
    fi

    print_warn "No resource limits found in docker-compose (recommended for production)"
    return 0  # Warning only
}

# Check 5: HEALTHCHECK instruction present
check_healthcheck() {
    local dockerfile="$1"
    print_header "Checking for HEALTHCHECK in $dockerfile"

    if [[ ! -f "$dockerfile" ]]; then
        print_fail "Dockerfile not found: $dockerfile"
        return 1
    fi

    if grep -qE '^HEALTHCHECK' "$dockerfile" 2>/dev/null; then
        print_pass "HEALTHCHECK instruction found"
        return 0
    fi

    print_warn "No HEALTHCHECK instruction found (recommended for production)"
    return 0  # Warning only
}

# Check 6: Production command uses gunicorn/uwsgi (not flask run directly)
check_production_server() {
    local dockerfile="$1"
    print_header "Checking for production server in $dockerfile"

    if [[ ! -f "$dockerfile" ]]; then
        print_fail "Dockerfile not found: $dockerfile"
        return 1
    fi

    # Check for production WSGI servers
    if grep -qE '(gunicorn|uwsgi|waitress|gunicorn)' "$dockerfile" 2>/dev/null; then
        print_pass "Production WSGI server found (gunicorn/uwsgi)"
        return 0
    fi

    # Check for insecure patterns
    if grep -qE 'flask\s+run' "$dockerfile" 2>/dev/null; then
        print_fail "Development server 'flask run' found (insecure for production)"
        return 1
    fi

    print_warn "No explicit production server found"
    return 0
}

# Main test function for a single Dockerfile
test_dockerfile() {
    local dockerfile="$1"
    local description="$2"

    print_header "Testing $description: $dockerfile"
    echo ""

    local initial_pass=$PASS_COUNT
    local initial_fail=$FAIL_COUNT
    local initial_warn=$WARN_COUNT

    check_non_root_user "$dockerfile"
    check_multi_stage "$dockerfile"
    check_no_secrets "$dockerfile"
    check_healthcheck "$dockerfile"
    check_production_server "$dockerfile"

    local checks_passed=$((PASS_COUNT - initial_pass))
    local checks_failed=$((FAIL_COUNT - initial_fail))
    local checks_warned=$((WARN_COUNT - initial_warn))

    echo ""
    echo "--- Summary for $description ---"
    echo "Passed: $checks_passed, Failed: $checks_failed, Warnings: $checks_warned"

    if [[ "$checks_failed" -gt 0 ]]; then
        return 1
    fi
    return 0
}

# Run all tests
run_all_tests() {
    local api_dockerfile="$PROJECT_ROOT/api/Dockerfile"
    local root_dockerfile="$PROJECT_ROOT/Dockerfile"

    echo ""
    echo "########################################"
    echo "# Docker Security Test Suite"
    echo "# Project: MyOwnClone"
    echo "########################################"

    # Test api/Dockerfile (should be secure)
    if test_dockerfile "$api_dockerfile" "api/Dockerfile (secure reference)"; then
        echo ""
        echo -e "${GREEN}api/Dockerfile PASSED security checks${NC}"
        API_RESULT=0
    else
        echo ""
        echo -e "${RED}api/Dockerfile FAILED security checks${NC}"
        API_RESULT=1
    fi

    # Test root Dockerfile (should be insecure)
    echo ""
    echo "========================================"
    echo "Testing root Dockerfile (expected to fail)"
    echo "========================================"

    if test_dockerfile "$root_dockerfile" "root Dockerfile"; then
        echo ""
        echo -e "${YELLOW}root Dockerfile PASSED (unexpected - may already be fixed)${NC}"
        ROOT_RESULT=0
    else
        echo ""
        echo -e "${GREEN}root Dockerfile FAILED as expected (security issues detected)${NC}"
        ROOT_RESULT=1
    fi

    # Check docker-compose resource limits
    check_resource_limits

    # Final summary
    echo ""
    echo "########################################"
    echo "# Final Summary"
    echo "########################################"
    echo "Total Passed: $PASS_COUNT"
    echo "Total Failed: $FAIL_COUNT"
    echo "Total Warnings: $WARN_COUNT"
    echo ""
    echo "api/Dockerfile:  $([ "$API_RESULT" -eq 0 ] && echo -e "${GREEN}PASS${NC}" || echo -e "${RED}FAIL${NC}")"
    echo "root Dockerfile: $([ "$ROOT_RESULT" -eq 0 ] && echo -e "${GREEN}PASS${NC}" || echo -e "${RED}FAIL${NC} (expected)${NC}")"
    echo ""

    # Validation: api/Dockerfile should pass, root Dockerfile should fail
    if [[ "$API_RESULT" -eq 0 ]] && [[ "$ROOT_RESULT" -ne 0 ]]; then
        echo -e "${GREEN}VALIDATION PASSED: api/Dockerfile is secure, root Dockerfile has issues${NC}"
        exit 0
    else
        echo -e "${RED}VALIDATION FAILED: Security test results not as expected${NC}"
        echo "  Expected: api/Dockerfile passes, root Dockerfile fails"
        echo "  Got: api/Dockerfile=$([ "$API_RESULT" -eq 0 ] && echo 'pass' || echo 'fail'), root Dockerfile=$([ "$ROOT_RESULT" -eq 0 ] && echo 'pass' || echo 'fail')"
        exit 1
    fi
}

# Show usage
usage() {
    echo "Usage: $0 [--dockerfile <path>] [--help]"
    echo ""
    echo "Docker Security Test Helper"
    echo "  --dockerfile <path>  Test a specific Dockerfile"
    echo "  --help               Show this help message"
    echo ""
    echo "Without arguments, runs full test suite comparing api/Dockerfile vs root Dockerfile"
    exit 0
}

# Parse arguments
if [[ $# -eq 0 ]]; then
    run_all_tests
elif [[ "$1" == "--help" ]]; then
    usage
elif [[ "$1" == "--dockerfile" ]] && [[ -n "${2:-}" ]]; then
    test_dockerfile "$2" "specified Dockerfile"
    exit $?
else
    usage
fi

