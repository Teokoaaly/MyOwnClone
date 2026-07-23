# TERRA-06B evidence

| Command | Result |
| --- | --- |
| `pytest -q tests/test_deploy_backend_script.py` before edits | PASS: 6 passed |
| `pytest -q tests/test_postgres_backup_contract.py tests/test_deploy_backend_script.py` | PASS: 11 passed |
| `bash -n ops/backup_postgres.sh ops/verify_postgres_backup.sh ops/install-postgres-backup-systemd.sh` | PASS |
| `git diff --check` | PASS |

Manual QA used a freshly created `mktemp -d` directory with fake `docker` and
`rclone` executables as the only external-process boundaries. The runner
produced a gzip dump, `.sha256`, `.manifest`, and three immutable `rclone copyto`
requests; no remote deletion command was observed. The initial restore check
failed because the checksum referenced the atomic temporary filename. That was
fixed by emitting the final dump basename in the checksum. The re-run reached
`myownclone_20260723_120000.sql.gz: OK`; no local Docker/PostgreSQL service was
used, so a real-container restore was not attempted. Temporary harness paths
were OS-managed `mktemp` directories; no VPS state was changed.
