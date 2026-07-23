# TERRA-06A — Ollama native healthcheck evidence

## Scope

Changed `ops/docker-compose.backend.prod.yml` only to replace the Ollama
healthcheck command from the unavailable image dependency `curl` to the native
Ollama CLI probe:

```yaml
test: ["CMD", "ollama", "list"]
```

Application endpoint behavior was not changed: `/healthz` retains its
model-presence semantics and `/readyz` retains its liveness semantics.

## Baseline and regression sequence

1. Baseline contract added and run before the policy assertion:
   `pytest -q api/tests/test_ollama_compose_healthcheck.py`
   — `1 passed in 1.51s`.
2. Added the policy test requiring `test: ["CMD", "ollama", "list"]` and
   rejecting the previous curl probe. Before the Compose edit:
   `1 failed, 1 passed in 1.34s`; the failure was the missing `ollama list`
   command.
3. After the Compose edit, relevant tests:
   `pytest -q api/tests/test_ollama_compose_healthcheck.py tests/test_operational_hardening.py`
   — `10 passed in 31.92s`.
4. Flake repetition:
   `pytest -q api/tests/test_ollama_compose_healthcheck.py`
   — `2 passed in 0.21s`.

## Validation

- `python -c "import pathlib, yaml; yaml.safe_load(pathlib.Path('ops/docker-compose.backend.prod.yml').read_text(encoding='utf-8')); print('YAML parse: PASS')"`
  — `YAML parse: PASS` (exit 0).
- `docker compose -f ops/docker-compose.backend.prod.yml config`
  — not runnable in this worktree because the required
  `ops/backend.env.production` is intentionally absent; exit 1 with
  `env file ...\\ops\\backend.env.production not found`.
- `git diff --check` — exit 0 (only a Windows LF-to-CRLF warning).
- Diff-scoped secret scan using `git diff ... | findstr /I /R "api_key secret password token"`
  — `secret scan: PASS` (exit 0).
- Final file inspection (`git diff -- ops/docker-compose.backend.prod.yml ...`)
  showed exactly `test: ["CMD", "ollama", "list"]`; no stale curl-based
  Ollama probe remains.

## Manual QA

Attempted local Docker availability first:

```text
docker version --format '{{.Server.Version}}'
failed to connect to the docker API at npipe:////./pipe/dockerDesktopLinuxEngine
```

Docker Desktop's Linux engine was unavailable (exit 1), so no non-production
Ollama container could be started and `ollama list` could not be executed in a
running image. This is an explicit local-environment limitation, not production
proof. No containers were created; cleanup receipt: N/A.

## Adversarial / interruption checks

- malformed input: N/A — no malformed input received.
- prompt injection: N/A — none received.
- cancel/resume: N/A — not triggered.
- hung commands: N/A — commands were polled to completion; no command required
  termination.
- repeated interruptions: N/A — not triggered.
