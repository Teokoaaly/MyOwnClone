#!/usr/bin/env python3
import subprocess

print("=== FASE 1 STATUS ===")

# T1.1 Backup dual
result = subprocess.run(['ls', '/opt/myownclone/current/ops/backup_dual.sh'], capture_output=True, text=True)
print(f"T1.1 Backup dual: {'EXISTS' if result.returncode == 0 else 'MISSING'}")

# T1.2 Indice ivfflat
result = subprocess.run(
    ['sudo', 'docker', 'exec', 'myownclone_postgres', 'psql', '-U', 'postgres', '-d', 'myownclone', '-t', '-c',
     "SELECT count(*) FROM pg_indexes WHERE indexname LIKE '%ivfflat%'"],
    capture_output=True, text=True
)
print(f"T1.2 Indice ivfflat: {result.stdout.strip()}")

# T1.3 Weaviate
result = subprocess.run(['sudo', 'docker', 'ps', '--format', '{{.Names}}'], capture_output=True, text=True)
weaviate = 'weaviate' in result.stdout
print(f"T1.3 Weaviate eliminado: {'YES (correcto)' if not weaviate else 'NO (still running)'}")

# T1.5 Entry point
result = subprocess.run(['ls', '/opt/myownclone/current/api/entrypoint.sh'], capture_output=True, text=True)
print(f"T1.5 Entry point: {'EXISTS' if result.returncode == 0 else 'MISSING'}")

# T1.6 Healthcheck
result = subprocess.run(['curl', '-s', 'http://127.0.0.1:5001/healthz'], capture_output=True, text=True)
print(f"T1.6 Healthcheck: {result.stdout.strip()}")
