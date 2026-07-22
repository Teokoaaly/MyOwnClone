#!/usr/bin/env bash
# MyOwnClone VPS — PostgreSQL backup script
# Uso: ./backup_postgres.sh [KEEP_DAYS]
# KEEP_DAYS: cuantos backups diarios conservar (default: 7)
# Genera: /opt/myownclone/backups/myownclone_YYYYMMDD_HHMMSS.sql.gz
#
# Cron example (ejecutar como root):
#   0 3 * * * /opt/myownclone/current/ops/backup_postgres.sh 7 >> /var/log/myownclone-backup.log 2>&1

set -euo pipefail
umask 077

KEEP_DAYS="${1:-7}"
BACKUP_DIR="/opt/myownclone/backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
CONTAINER="myownclone_postgres"
DB_NAME="myownclone"
FILE="$BACKUP_DIR/${DB_NAME}_${TIMESTAMP}.sql.gz"
PARTIAL_FILE="${FILE}.partial"

cleanup() {
  rm -f -- "$PARTIAL_FILE"
}
trap cleanup EXIT

mkdir -p "$BACKUP_DIR"

echo "[$(date -Iseconds)] Starting backup of $DB_NAME to $FILE"

# pg_dump desde el contenedor, gzip al vuelo
docker exec "$CONTAINER" \
  pg_dump -U postgres -d "$DB_NAME" --format=plain --no-owner --no-privileges 2>/dev/null \
  | gzip > "$PARTIAL_FILE"
gzip -t -- "$PARTIAL_FILE"
mv -- "$PARTIAL_FILE" "$FILE"

SIZE=$(du -h "$FILE" | cut -f1)
echo "[$(date -Iseconds)] Backup complete: $FILE ($SIZE)"

# Rotar: borrar dumps mas antiguos que KEEP_DAYS
find "$BACKUP_DIR" -name "${DB_NAME}_*.sql.gz" -mtime +$((KEEP_DAYS)) -delete 2>/dev/null
REMAINING=$(find "$BACKUP_DIR" -name "${DB_NAME}_*.sql.gz" | wc -l)
echo "[$(date -Iseconds)] Rotation: keeping last $KEEP_DAYS days ($REMAINING backups on disk)"
printf '%s\n' "$FILE"
