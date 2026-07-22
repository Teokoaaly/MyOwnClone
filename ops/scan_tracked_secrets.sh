#!/usr/bin/env bash
set -Eeuo pipefail

root="${1:-$(git rev-parse --show-toplevel)}"
status=0
tracked_files="$(mktemp)"
cleanup() {
  rm -f -- "$tracked_files"
}
trap cleanup EXIT
git -C "$root" ls-files -z >"$tracked_files"

while IFS= read -r -d '' relative; do
  path="$root/$relative"
  [[ -f "$path" ]] || continue
  if tr -d '\000' <"$path" | LC_ALL=C grep -aEq -- \
    '-----BEGIN ([A-Z0-9 ]+ )?PRIVATE KEY-----|AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9]{30,}|proxy_set_header[[:space:]]+X-API-Key[[:space:]]+[^$[:space:]";]+'; then
    printf 'SECRET_PATTERN: %s\n' "$relative"
    status=1
  else
    pipeline_status=("${PIPESTATUS[@]}")
    if [[ "${pipeline_status[0]}" -ne 0 || "${pipeline_status[1]}" -gt 1 ]]; then
      printf 'SCAN_ERROR: %s\n' "$relative" >&2
      exit 2
    fi
  fi
done <"$tracked_files"

if [[ "$status" -eq 0 ]]; then
  printf 'PASS: tracked-file binary secret scan\n'
fi
exit "$status"
