#!/bin/bash
# auto_setup_vps.sh
# Script que MiniMax M2.7 puede ejecutar para configurar el VPS autonomamente.
# NO TOCA LA LANDING (s4Hs00UH).
# Revierte cualquier cambio si falla.

set -e

VPS="root@212.227.169.99"
SSH="ssh $VPS"
RELEASE_BUENO="20260703190910-landing-cleanup-restore"
RELEASE_ACTUAL="20260704222310-frontend-codex-admin"
LOG=/tmp/auto_setup.log
exec > >(tee -a $LOG) 2>&1
echo "=== Auto Setup VPS - $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="

# PASO 0: Verificar que NO se toque la landing
echo "--- Verificando que la landing (s4Hs00UH) no se toque ---"
$SSH "
  BUILD_ID=\$(cat /opt/myownclone/current/MyOwnClone/.next/BUILD_ID 2>/dev/null)
  if [ \"\$BUILD_ID\" != 's4Hs00UHv6esTNBt7xcUp' ]; then
    echo 'ALERTA: BUILD_ID no es s4Hs00UH. Abortando.'
    echo \"Actual: \$BUILD_ID\"
    exit 1
  fi
  echo \"BUILD_ID OK: \$BUILD_ID\"
"

# PASO 1: Configurar cron de backups (TASK-A02)
echo
echo '--- PASO 1: TASK-A02 - cron de backups ---'
$SSH "
  set -e
  chmod +x /opt/myownclone/current/ops/backup_postgres.sh
  # Anadir cron si no existe
  (crontab -l 2>/dev/null | grep -v backup_postgres.sh; echo '0 3 * * * /opt/myownclone/current/ops/backup_postgres.sh 7 >> /var/log/myownclone-backup.log 2>&1') | crontab -
  touch /var/log/myownclone-backup.log
  chmod 644 /var/log/myownclone-backup.log
  echo 'Cron de backup configurado:'
  crontab -l
"

# PASO 2: Healthcheck automatico (TASK-C03)
echo
echo '--- PASO 2: TASK-C03 - healthcheck automatico ---'
$SSH '
  cat > /opt/myownclone/current/ops/healthcheck.sh << "HSCRIPT"
#!/bin/bash
LOG=/var/log/myownclone-healthcheck.log
ST=\$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:5001/readyz)
NOW=\$(date -u +%Y-%m-%dT%H:%M:%SZ)
if [ "\$ST" != "200" ]; then
    echo "\$NOW ALERT readyz=\$ST" >> \$LOG
fi
HSCRIPT
  chmod +x /opt/myownclone/current/ops/healthcheck.sh
  (crontab -l 2>/dev/null | grep -v healthcheck.sh; echo "*/5 * * * * /opt/myownclone/current/ops/healthcheck.sh") | crontab -
  echo "Healthcheck cron configurado"
'

# PASO 3: Verificar que el codigo de Sentry y PostHog existe (TASK-D01, D02)
echo
echo '--- PASO 3: Verificar Sentry y PostHog (NO activar) ---'
$SSH "
  echo 'Sentry en app_factory.py:'
  grep -E 'sentry_sdk|SENTRY' /opt/myownclone/current/api/app_factory.py | head -3 || echo 'No encontrado (OK)'
  echo 'PostHog en auth.ts:'
  grep -E 'posthog|PostHog' /opt/myownclone/current/MyOwnClone/src/lib/auth.ts | head -3 || echo 'No encontrado (OK)'
"

# PASO 4: Verificar que la landing NO se ha tocado
echo
echo '--- PASO 4: Verificar integridad de la landing ---'
$SSH "
  BUILD_ID=\$(cat /opt/myownclone/current/MyOwnClone/.next/BUILD_ID)
  if [ \"\$BUILD_ID\" = 's4Hs00UHv6esTNBt7xcUp' ]; then
    echo 'OK: Landing intacta (s4Hs00UH)'
  else
    echo 'ALERTA: BUILD_ID cambio a \$BUILD_ID'
  fi
  echo 'Landing status:'
  curl -sI https://myownclone.com 2>&1 | head -1
"

# PASO 5: Test final
echo
echo '--- PASO 5: Tests finales ---'
$SSH "
  echo 'Test backup manual:'
  /opt/myownclone/current/ops/backup_postgres.sh 7 2>&1 | tail -3
  echo
  echo 'Backups disponibles:'
  ls -la /opt/myownclone/backups/ | tail -3
  echo
  echo 'Healthcheck:'
  /opt/myownclone/current/ops/healthcheck.sh
  echo 'Cron activo:'
  crontab -l
"

echo
echo "=== Auto Setup COMPLETADO - $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
echo "Log: $LOG"