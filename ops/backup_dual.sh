#!/usr/bin/env bash
# Backup dual: copia backups a /var/backups/myownclone (local secundario)
# Cuando se añadan credenciales de B2/S3, descomentar la sección rclone.

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

# 5. (Futuro) Subir a B2/S3 con rclone
# if command -v rclone >/dev/null 2>&1 && [[ -f "$HOME/.config/rclone/rclone.conf" ]]; then
#   log "Subiendo a B2/S3"
#   rclone copy "$SECONDARY/" myownclone:myownclone-backups/db/ --progress
#   rclone delete myownclone:myownclone-backups/db/ --min-age ${RETENTION}d
# fi

log "Backup dual completado"