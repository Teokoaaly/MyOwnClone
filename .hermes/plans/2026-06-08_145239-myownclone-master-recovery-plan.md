# MyOwnClone master recovery + completion plan

> For Hermes: orchestrate with parallel workers, verify every claim yourself, and notify progress to Telegram after each completed checkpoint.

Goal: dejar MyOwnClone corriendo perfecto en producción: login/admin funcional, backend y frontend consistentes, deploy reproducible, smoke tests reales, hardening operativo, VPS limpio y docs canónicas.

Current verified context
- Frontend live: https://myownclone.com
- Backend live: https://myownclone.com/console/api/
- Public smoke current pass:
  - `/` => 200
  - `/api/auth/session` => 200
  - `/console/api/` => 200
  - `/api/clone/plans` => 401
  - `/console/api/myownclone/clones` => 401
- Auth.js 500 ya quedó resuelto con `AUTH_TRUST_HOST` + secret.
- Admin web still not deployed with final fix.
- Local code already validated for the pragmatic admin path:
  - credentials login works
  - session carries `role=platform_admin`
  - `/admin/resumen` returns 200 after login
- Current pragmatic auth decision:
  - Do NOT block on creating Drizzle `users` in production first.
  - Use bootstrap admin via env (`PLATFORM_ADMIN_EMAIL` + `PLATFORM_ADMIN_PASSWORD_HASH`) for the frontend.
  - Keep Flask console auth on backend `accounts` as-is for now.
- VPS current blocker:
  - host responds on web/Tailscale
  - `22/tcp` was closed in this session
  - therefore deploy/cleanup on VPS is blocked until a remote execution channel is restored
- Workers usable now:
  - hub_local
  - vps_ubuntu 100.99.222.101 (worker/API reachable; shell currently blocked by closed 22)
  - win_hermes 100.113.82.10 (verify via SSH + hermes.exe, not port 3001)
  - user_desktop 100.111.183.23 (not Hermes worker)

Architecture decisions
- Keep dual-auth reality explicit for now:
  - Flask console auth uses backend `accounts`
  - Web admin auth uses NextAuth credentials + env bootstrap admin
- Do not attempt risky auth unification before recovering access.
- Parallelize by domain, not by file overlap.
- Every phase ends with one short Telegram progress ping.

Master task graph

Phase 0 — orchestration + evidence
1. Keep this plan updated to current verified state.
2. Keep todo list synchronized.
3. Keep Telegram progress reporting active.
Acceptance:
- plan file matches real state
- todo list current
- Telegram receives checkpoints

Phase 1 — auth/admin recovery (highest priority)
Owner lane: Worker A + parent verification
Objective: make `/login` and `/admin` usable in production with the already-validated env bootstrap approach.

Subtasks
A1. Keep local auth changes minimal and coherent:
- `MyOwnClone/src/lib/auth.ts`
- `MyOwnClone/src/lib/platform-admin.ts`
- admin route guards
- login redirect behavior
A2. Ensure env contract is documented in `ops/frontend.env.production.example` and `ops/DEPLOY_VPS.md`.
A3. Prepare bootstrap values for production:
- `PLATFORM_ADMIN_EMAIL`
- bcrypt `PLATFORM_ADMIN_PASSWORD_HASH`
A4. As soon as VPS shell access exists, deploy frontend fix and env.
A5. Verify end-to-end on production:
- `/api/auth/session` = 200
- credentials sign-in succeeds
- `/admin/resumen` returns 200 after authenticated session
- admin API routes stop redirect-looping/403 for bootstrap admin

Files likely touched
- `MyOwnClone/src/lib/auth.ts`
- `MyOwnClone/src/lib/platform-admin.ts`
- `MyOwnClone/src/app/admin/layout.tsx`
- `MyOwnClone/src/app/api/admin/route.ts`
- `MyOwnClone/src/app/api/admin/[...path]/route.ts`
- `MyOwnClone/src/app/login/login-form.tsx`
- `MyOwnClone/.env.example`
- `ops/frontend.env.production.example`

Verification
- local scripted login with cookie jar
- `npm test -- --run src/__tests__/app/login-form.test.tsx`
- `npm run build`
- production scripted login once remote access returns

Phase 2 — deploy + smoke automation + service hardening
Owner lane: Worker B + parent verification
Objective: make deploy reproducible and operationally safe.

Subtasks
B1. Keep `ops/deploy-frontend.sh` and `ops/deploy-backend.sh` executable and syntax-clean.
B2. Keep `ops/smoke-prod.sh` as the canonical smoke script.
B3. Capture frontend systemd env contract in repo docs.
B4. Validate deploy scripts locally (`bash -n`) and with real VPS when shell access returns.
B5. After deploy, rerun smoke against production and store the evidence.

Files likely touched
- `ops/deploy-frontend.sh`
- `ops/deploy-backend.sh`
- `ops/smoke-prod.sh`
- `ops/myownclone-frontend.service`
- `ops/DEPLOY_VPS.md`

Verification
- `bash -n` on all scripts
- smoke exit code 0 with real HTTP codes
- real deploy output from VPS once remote access returns

Phase 3 — cleanup + docs canon + handoff durability
Owner lane: Worker C + parent verification
Objective: remove stale deploy confusion and document the truth.

Subtasks
C1. Treat `/opt/myownclone/current` as the new canonical target layout in docs.
C2. Keep `ops/CANONICAL_POST_DEPLOY_STATE_2026-06-08.md` and `HANDOFF_POST_DEPLOY_2026-06-08.md` aligned with verified reality.
C3. Once VPS shell access returns, inventory stale paths (`/root/MyOwnClone-clean`, `/root/MyOwnClone-new`, `/root/MyOwnClone_new`, `/root/myownclone-api`, etc.).
C4. Remove only paths verified unused by active services.
C5. Update any active docs still talking about `replica/` or `/root/MyOwnClone` as canonical live paths.

Files likely touched
- `ops/CANONICAL_POST_DEPLOY_STATE_2026-06-08.md`
- `ops/DEPLOY_VPS.md`
- `HANDOFF_POST_DEPLOY_2026-06-08.md`
- maybe root README / ops docs if they still mention `replica/`

Verification
- active services still healthy after cleanup
- docs name the real current paths
- handoff matches latest verified smoke and blockers

Checkpoint definitions

Checkpoint 1: auth path ready
- local login/admin flow validated
- production env contract documented
- Telegram progress ping sent

Checkpoint 2: deploy path ready
- deploy/smoke scripts validated locally
- production smoke currently green on public endpoints
- Telegram progress ping sent

Checkpoint 3: production recovery executed
- VPS shell access restored
- frontend fix deployed with bootstrap admin env
- production login/admin verified live
- Telegram progress ping sent

Checkpoint 4: cleanup/docs closed
- stale paths removed or explicitly retained with note
- handoff updated
- Telegram progress ping sent

Risks and mitigations
- Risk: waiting on VPS shell blocks final production deploy.
  - Mitigation: keep code, env contract, scripts, and bootstrap values ready so deploy is one short action once access returns.
- Risk: backend `accounts` and frontend web admin remain separate.
  - Mitigation: document dual-auth contract explicitly; postpone unification.
- Risk: worker self-reports are wrong.
  - Mitigation: parent verifies with curl, build, tests, SSH/systemctl/psql when available.

Execution order
1. Keep Worker A/B/C scopes separated.
2. Finish local auth/deploy/doc readiness first.
3. Restore or obtain VPS shell channel.
4. Deploy frontend auth fix first.
5. Verify production login/admin.
6. Then perform VPS cleanup/docs finalization.
7. Send Telegram update after each checkpoint.

Definition of done
- admin login works from browser with real production session
- `/admin/resumen` reachable for bootstrap admin in production
- production smoke script passes
- frontend systemd env contract documented
- stale VPS paths cleaned or deliberately retained with note
- handoff/doc updated
- all critical URLs verified live
