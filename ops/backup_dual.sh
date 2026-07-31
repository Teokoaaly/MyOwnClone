#!/usr/bin/env bash
# Espejo local secundario; la publicación B2 cifrada pertenece a backup_postgres.sh.

set -euo pipefail

PRIMARY="/opt/myownclone/backups"
SECONDARY="/var/backups/myownclone"
RETENTION=7

log() {
  printf '[backup_dual] %s\n' "$*"
}

# 1. Asegurar que secundario existe
mkdir -p "$SECONDARY"
chmod 700 "$SECONDARY"

# 2. Copiar backups primarios al secundario
log "Copiando backups de $PRIMARY a $SECONDARY"
rsync -az --delete "$PRIMARY/" "$SECONDARY/"

# 3. Aplicar retención en secundario
log "Aplicando retención de $RETENTION días en secundario"
find "$SECONDARY" -name "myownclone_*.sql.gz" -mtime +$RETENTION -delete 2>/dev/null || true
find "$SECONDARY" -name "pre-maintenance-*.sql.gz" -mtime +$RETENTION -delete 2>/dev/null || true

# 4. Verificar
COUNT=$(find "$SECONDARY" -name "*.sql.gz" | wc -l)
log "Backups en secundario: $COUNT"

log "Backup dual completado"
