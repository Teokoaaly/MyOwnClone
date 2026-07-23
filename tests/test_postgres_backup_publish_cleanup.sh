#!/usr/bin/env bash
set -Eeuo pipefail

root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
tmp="$(mktemp -d)"
trap 'rm -rf -- "$tmp"' EXIT
mkdir -p "$tmp/bin" "$tmp/backups"
if ! command -v setsid >/dev/null 2>&1; then
  printf 'SKIP: setsid is unavailable on this host\n'
  exit 0
fi
cat > "$tmp/bin/docker" <<'EOF'
#!/usr/bin/env bash
printf 'CREATE TABLE publish_cleanup (id integer);\n'
EOF
cat > "$tmp/bin/mv" <<'EOF'
#!/usr/bin/env bash
/bin/mv "$@"
case "${!#}" in
  *.sql.gz) kill -TERM "$PPID" ;;
esac
EOF
chmod +x "$tmp/bin/docker" "$tmp/bin/mv"
set +e
PATH="$tmp/bin:$PATH" BACKUP_DIR="$tmp/backups" BACKEND_CURRENT="$root" \
  BACKUP_TIMESTAMP=20260723_130000 BACKUP_B2_ENV_FILE="$tmp/absent" \
  "$root/ops/backup_postgres.sh" 7
status=$?
set -e
[[ "$status" -eq 143 ]]
[[ -z "$(find "$tmp/backups" -type f -print -quit)" ]]
printf 'PASS: TERM after first final mv leaves no final or temporary artifact\n'
