#!/usr/bin/env bash
set -Eeuo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
scratch="$(mktemp -d)"
cleanup() {
  chmod -R u+w -- "$scratch" 2>/dev/null || true
  rm -rf -- "$scratch"
}
trap cleanup EXIT

previous="$scratch/previous release;safe"
current="$scratch/current link"
fake_bin="$scratch/bin"
receipt="$scratch/rollback-args"
mkdir -p -- "$previous/ops" "$current/ops" "$fake_bin"

cat >"$fake_bin/docker" <<'DOCKER_EOF'
#!/usr/bin/env bash
exit 0
DOCKER_EOF

cat >"$fake_bin/ssh" <<'SSH_EOF'
#!/usr/bin/env bash
while (($#)); do
  if [[ "$1" == "bash" ]]; then
    exec "$@"
  fi
  shift
done
exit 64
SSH_EOF

chmod +x -- "$fake_bin/docker" "$fake_bin/ssh"
cat >"$fake_bin/ln" <<'LN_EOF'
#!/usr/bin/env bash
printf '%s\n' "$@" >"$ROLLBACK_RECEIPT"
LN_EOF
chmod +x -- "$fake_bin/ln"
PATH="$fake_bin:$PATH" \
ROLLBACK_RECEIPT="$receipt" \
HOST=local \
SSH_BIN="$fake_bin/ssh" \
PREV_RELEASE_LINK="$previous" \
REMOTE_CURRENT_LINK="$current" \
DEPLOY_BACKEND_ROLLBACK_ONLY=1 \
bash "$repo_root/ops/deploy-backend.sh"

mapfile -t args <"$receipt"
[[ "${args[0]}" == "-sfn" ]]
[[ "${args[1]}" == "--" ]]
[[ "${args[2]}" == "$previous" ]]
[[ "${args[3]}" == "$current" ]]
printf 'PASS: rollback preserved quoted paths\n'
