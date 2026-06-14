#!/usr/bin/env bash
set -Eeuo pipefail

FRONTEND_URL="${FRONTEND_URL:-http://100.99.222.101}"
BACKEND_URL="${BACKEND_URL:-http://100.99.222.101:5001}"
AUTH_SESSION_PATH="${AUTH_SESSION_PATH:-/api/auth/session}"
PROTECTED_FRONTEND_PATH="${PROTECTED_FRONTEND_PATH:-/api/clone/plans}"
PROTECTED_BACKEND_PATH="${PROTECTED_BACKEND_PATH:-/console/api/myownclone/clones}"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

pass_count=0
fail_count=0

log() {
  printf '[smoke] %s\n' "$*"
}

assert_http() {
  local name="$1"
  local url="$2"
  local expected_code="$3"
  local expect_pattern="${4:-}"
  local body_file="${TMP_DIR}/$(printf '%s' "$name" | tr ' /' '__').body"
  local headers_file="${body_file}.headers"
  local code

  code="$(curl -sS -L -D "$headers_file" -o "$body_file" -w '%{http_code}' "$url")"

  if [[ "$code" != "$expected_code" ]]; then
    log "FALLO ${name}: código ${code}, esperado ${expected_code} (${url})"
    sed -n '1,40p' "$body_file" >&2 || true
    fail_count=$((fail_count + 1))
    return 1
  fi

  if [[ -n "$expect_pattern" ]] && ! grep -Eq "$expect_pattern" "$body_file"; then
    log "FALLO ${name}: body sin patrón ${expect_pattern} (${url})"
    sed -n '1,40p' "$body_file" >&2 || true
    fail_count=$((fail_count + 1))
    return 1
  fi

  log "OK ${name}: ${code} ${url}"
  pass_count=$((pass_count + 1))
}

assert_http "frontend-root" \
  "${FRONTEND_URL}/" \
  "200" \
  "MyOwnClone|Crea un clon de IA|Crear cuenta"

assert_http "frontend-auth-session" \
  "${FRONTEND_URL}${AUTH_SESSION_PATH}" \
  "200" \
  "session|user|null|authenticated"

assert_http "backend-console-root" \
  "${BACKEND_URL}/console/api/" \
  "200" \
  "Console API|swagger|openapi"

assert_http "backend-healthz" \
  "${BACKEND_URL}/healthz" \
  "200" \
  "ok"

assert_http "backend-readyz" \
  "${BACKEND_URL}/readyz" \
  "200" \
  "ready|database|redis"

assert_http "frontend-protected-route" \
  "${FRONTEND_URL}${PROTECTED_FRONTEND_PATH}" \
  "401" \
  "Unauthorized|error"

assert_http "backend-protected-route" \
  "${BACKEND_URL}${PROTECTED_BACKEND_PATH}" \
  "401" \
  "Unauthorized|missing Bearer token|error"

log "Resumen: ${pass_count} OK, ${fail_count} fallos"
[[ "$fail_count" -eq 0 ]]
