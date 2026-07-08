#!/usr/bin/env python3
import subprocess
import json

print("=== AUDITORÍA COMPLETA: PLANES MAESTROS vs VPS ===\n")

# FASE 1
print("FASE 1 - Estabilizar:")
result = subprocess.run(['ls', '/opt/myownclone/current/ops/backup_dual.sh'], capture_output=True, text=True)
print(f"  T1.1 Backup dual: {'✅' if result.returncode == 0 else '❌'}")

result = subprocess.run(
    ['sudo', 'docker', 'exec', 'myownclone_postgres', 'psql', '-U', 'postgres', '-d', 'myownclone', '-t', '-c',
     "SELECT count(*) FROM pg_indexes WHERE indexname LIKE '%ivfflat%'"],
    capture_output=True, text=True
)
print(f"  T1.2 Indice ivfflat: {'✅' if '1' in result.stdout else '❌'}")

result = subprocess.run(['sudo', 'docker', 'ps', '--format', '{{.Names}}'], capture_output=True, text=True)
print(f"  T1.3 Weaviate eliminado: {'✅' if 'weaviate' not in result.stdout else '❌'}")

result = subprocess.run(['ls', '/opt/myownclone/current/api/entrypoint.sh'], capture_output=True, text=True)
print(f"  T1.5 Entry point: {'✅' if result.returncode == 0 else '❌ MISSING'}")

result = subprocess.run(['curl', '-s', 'http://127.0.0.1:5001/healthz'], capture_output=True, text=True)
print(f"  T1.6 Healthcheck: {'✅' if 'ready' in result.stdout else '❌'}")

# FASE 2
print("\nFASE 2 - RAG + Modelo IA:")
result = subprocess.run(
    ['sudo', 'docker', 'exec', 'myownclone_postgres', 'psql', '-U', 'postgres', '-d', 'myownclone', '-t', '-c',
     "SELECT count(*) FROM chunks"],
    capture_output=True, text=True
)
print(f"  T2.1 Pipeline ingestion: {'✅' if int(result.stdout.strip()) > 3 else '❌ Only seed data'}")

result = subprocess.run(
    ['sudo', 'docker', 'exec', 'myownclone_postgres', 'psql', '-U', 'postgres', '-d', 'myownclone', '-t', '-c',
     "SELECT count(*) FROM ai_models WHERE is_active = true"],
    capture_output=True, text=True
)
print(f"  T2.2 Modelos activos: {result.stdout.strip()}")

result = subprocess.run(['ls', '/opt/myownclone/current/api/core/queue.py'], capture_output=True, text=True)
print(f"  T2.5 Worker RQ: {'✅' if result.returncode == 0 else '❌'}")

# FASE 3
print("\nFASE 3 - Escalar:")
result = subprocess.run(['ls', '/opt/myownclone/current/api/core/metrics.py'], capture_output=True, text=True)
print(f"  T3.6 Prometheus metrics: {'✅' if result.returncode == 0 else '❌'}")

result = subprocess.run(['ls', '/opt/myownclone/current/api/core/rate_limit.py'], capture_output=True, text=True)
print(f"  T3.1 Rate limiting: {'✅' if result.returncode == 0 else '❌'}")

# Admin UI
print("\nAdmin UI:")
result = subprocess.run(['ls', '/opt/myownclone/current/MyOwnClone/src/app/admin/ia-modelos/page.tsx'], capture_output=True, text=True)
print(f"  IA Modelos page: {'✅' if result.returncode == 0 else '❌'}")

result = subprocess.run(['ls', '/opt/myownclone/current/MyOwnClone/src/app/admin/audit/page.tsx'], capture_output=True, text=True)
print(f"  Audit log page: {'✅' if result.returncode == 0 else '❌'}")

result = subprocess.run(['ls', '/opt/myownclone/current/MyOwnClone/src/app/admin/impersonation/page.tsx'], capture_output=True, text=True)
print(f"  Impersonation page: {'✅' if result.returncode == 0 else '❌'}")

# Security
print("\nSeguridad:")
result = subprocess.run(['curl', '-sI', 'https://myownclone.com'], capture_output=True, text=True)
headers = result.stdout
print(f"  HSTS: {'✅' if 'Strict-Transport-Security' in headers else '❌'}")
print(f"  X-Frame-Options: {'✅' if 'X-Frame-Options' in headers else '❌'}")
print(f"  X-Content-Type: {'✅' if 'X-Content-Type-Options' in headers else '❌'}")
print(f"  Referrer-Policy: {'✅' if 'Referrer-Policy' in headers else '❌'}")
