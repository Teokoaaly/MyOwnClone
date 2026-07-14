# Rollback Procedures for Critical Security Fixes

This document provides step-by-step rollback procedures for each P0 security fix. Each procedure includes git revert commands, Docker rollback steps, and database migration rollbacks where applicable.

---

## BE-01: RCE Prevention in deploy.py (shell=True removal)

### What was fixed
The `_run()` function in `api/controllers/deploy.py` used `subprocess.run(shell=True)` which allows command injection attacks. An attacker could send a payload like `; rm -rf /` to execute arbitrary commands.

### Rollback Procedure

#### Step 1: Revert the code change
```bash
cd MyOwnClone
git revert <commit-hash> --no-edit
```

To find the specific commit:
```bash
git log --oneline -10 -- api/controllers/deploy.py
```

#### Step 2: Deploy the reverted backend
```bash
cd ops
./deploy-backend.sh
```

#### Step 3: Verify rollback
```bash
curl -X POST http://localhost:5001/api/deploy \
  -H "X-Deploy-Secret: $DEPLOY_SECRET" \
  -d "command=; ls"
```

**Expected after rollback**: Command injection succeeds (shows file listing). This confirms the vulnerability exists again. **Do not leave system in this state**.

### Emergency Rollback (if deploy script fails)
```bash
# SSH to production server
ssh root@100.99.222.101

# Revert to previous release
cd /opt/myownclone/current
git checkout <previous-commit-hash>

# Restart the service
cd /opt/myownclone/current/ops
docker compose -f docker-compose.backend.prod.yml restart api
```

---

## BE-04: Admin Auto-Creation Removal

### What was fixed
The `_ensure_admin_account()` function in `api/controllers/console/myownclone/admin_platform.py` automatically created admin accounts if they did not exist. This allowed privilege escalation where any user could become a platform admin by accessing admin endpoints.

### Rollback Procedure

#### Step 1: Revert the code change
```bash
cd MyOwnClone
git revert <commit-hash> --no-edit
```

To find the specific commit:
```bash
git log --oneline -10 -- api/controllers/console/myownclone/admin_platform.py
```

#### Step 2: Restart the backend service
```bash
cd ops
docker compose -f docker-compose.backend.prod.yml restart api
```

#### Step 3: Verify rollback
```bash
# Login as a non-existent account
curl -X POST http://localhost:5001/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"attacker@evil.com","password":"anypassword"}'

# Try to access admin endpoint
curl -X GET http://localhost:5001/console/api/myownclone/admin/overview \
  -H "Cookie: session=<attacker-session>"
```

**Expected after rollback**: Non-existent account auto-creates as platform admin. Access is granted. **This is a security vulnerability**.

### Database Considerations
If the fix included database migrations to mark existing auto-created admins:
```bash
# Rollback migration (if applicable)
cd MyOwnClone/api
flask db downgrade <previous-migration-version>
```

---

## FE-01: DOMPurify XSS Sanitization

### What was fixed
`MyOwnClone/src/components/chat/MessageBubble.tsx` used regex-based HTML sanitization which is inadequate against XSS attacks. The fix replaces this with DOMPurify.

### Rollback Procedure

#### Step 1: Revert the code change
```bash
cd MyOwnClone
git revert <commit-hash> --no-edit
```

To find the specific commit:
```bash
git log --oneline -10 -- MyOwnClone/src/components/chat/MessageBubble.tsx
```

#### Step 2: Rebuild the frontend
```bash
cd MyOwnClone
npm run build
```

#### Step 3: Deploy the reverted frontend
```bash
cd ops
./deploy-frontend.sh
```

#### Step 4: Verify rollback
Open the frontend and try these XSS payloads in a chat message:
- `<script>alert('XSS')</script>`
- `<img src=x onerror=alert('XSS')>`
- `<svg onload=alert('XSS')>`
- `<a href="javascript:alert('XSS')">click</a>`

**Expected after rollback**: Scripts execute, alerts fire. **This is an active XSS vulnerability**.

### Emergency Rollback (if build fails)
```bash
# SSH to production server
ssh root@100.99.222.101

# Revert frontend to previous release
cd /opt/myownclone-frontend/MyOwnClone
git checkout <previous-commit-hash>

# Rebuild and restart
npm run build
systemctl restart myownclone-frontend
```

---

## INF-01: Secure Dockerfile (Multi-stage, Non-root, Gunicorn)

### What was fixed
The root `Dockerfile` was insecure:
- No multi-stage build (large image)
- Ran as root
- Used `flask run` instead of gunicorn
- No healthcheck

The fix replaces it with the secure pattern from `api/Dockerfile`:
- Multi-stage build (builder + runtime)
- Non-root user (appuser:app, uid 1001)
- Gunicorn with proper workers
- HEALTHCHECK instruction

### Rollback Procedure

#### Step 1: Revert the Dockerfile
```bash
cd MyOwnClone
git revert <commit-hash> --no-edit
```

To find the specific commit:
```bash
git log --oneline -10 -- Dockerfile
```

#### Step 2: Rebuild the Docker image
```bash
cd MyOwnClone
docker build -t myownclone_api:latest .
```

#### Step 3: Push to registry (if using remote registry)
```bash
docker tag myownclone_api:latest <registry>/myownclone_api:<rollback-tag>
docker push <registry>/myownclone_api:<rollback-tag>
```

#### Step 4: Deploy on production server
```bash
ssh root@100.99.222.101

cd /opt/myownclone/current/ops

# Pull the rolled-back image
docker pull <registry>/myownclone_api:<rollback-tag>

# Restart services
docker compose -f docker-compose.backend.prod.yml up -d --build --remove-orphans
```

#### Step 5: Verify rollback
```bash
# Check container runs as root (BAD - security vulnerability)
docker exec myownclone_api id

# Expected output after rollback: uid=0(root)
# This confirms the vulnerability exists.

# Check for gunicorn (should NOT be present after rollback)
docker exec myownclone_api ps aux | grep gunicorn

# Expected after rollback: No gunicorn process found
```

### Emergency Rollback via Docker Tag Swap
If you need to rollback without rebuilding:
```bash
# On production server
docker tag myownclone_api:<previous-version> myownclone_api:latest
docker compose -f docker-compose.backend.prod.yml up -d --no-recreate
```

### Verify Security Regression
After rollback, run these checks:
```bash
# 1. Check user is root
docker exec myownclone_api whoami
# Expected: root

# 2. Check for gunicorn
docker exec myownclone_api ps aux
# Expected: flask processes, no gunicorn

# 3. Check image size (should be much larger without multi-stage)
docker images myownclone_api
# Expected: Several hundred MB vs ~150MB with multi-stage
```

---

## Quick Reference: All Rollback Commands

| Fix ID | Description | Revert Command |
|--------|-------------|----------------|
| BE-01 | RCE in deploy.py | `git revert <hash> -- api/controllers/deploy.py` |
| BE-04 | Admin auto-creation | `git revert <hash> -- api/controllers/console/myownclone/admin_platform.py` |
| FE-01 | DOMPurify XSS | `git revert <hash> -- MyOwnClone/src/components/chat/MessageBubble.tsx` |
| INF-01 | Secure Dockerfile | `git revert <hash> -- Dockerfile` |

---

## Post-Rollback Checklist

After any rollback:

1. **Verify the vulnerability exists** (intentionally, to confirm rollback worked)
2. **Schedule re-fix immediately** (rollback is temporary)
3. **Notify team** of security regression
4. **Update incident log** with reason for rollback
5. **Plan proper re-deployment** of the fix

---

## Contacts for Emergency Rollback

- **Backend Lead**: For BE-01, BE-04 rollbacks
- **Frontend Lead**: For FE-01 rollbacks
- **DevOps Lead**: For INF-01 Docker rollbacks
- **Security Team**: For all security-related incidents

---

## Important Notes

- **Never leave a rollback in production**. A rollback is only to restore functionality while the fix is corrected.
- **Document every rollback** in the incident log with timestamp, reason, and who authorized it.
- **Test the re-fix** in staging before deploying after a rollback.
- **Consider feature flags** for future fixes to enable faster rollbacks without code changes.

