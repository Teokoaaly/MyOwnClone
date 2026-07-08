#!/usr/bin/env python3
import subprocess
import uuid

print("Adding seed data...")

# Add more tenants
tenants = [
    ('tenant-demo-1', 'Demo Tenant 1', 'pro', 'active'),
    ('tenant-demo-2', 'Demo Tenant 2', 'free', 'active'),
    ('tenant-demo-3', 'Demo Tenant 3', 'enterprise', 'active'),
]

for tid, name, plan, status in tenants:
    sql = "INSERT INTO tenants (id, name, plan, status, created_at) VALUES ('" + tid + "', '" + name + "', '" + plan + "', '" + status + "', NOW()) ON CONFLICT (id) DO NOTHING"
    result = subprocess.run(
        ['sudo', 'docker', 'exec', 'myownclone_postgres', 'psql', '-U', 'postgres', '-d', 'myownclone', '-c', sql],
        capture_output=True, text=True
    )
    print("Tenant " + name + ": OK" if result.returncode == 0 else "ERROR")

# Add more chunks for existing sources
result = subprocess.run(
    ['sudo', 'docker', 'exec', 'myownclone_postgres', 'psql', '-U', 'postgres', '-d', 'myownclone', '-t', '-c',
     'SELECT id FROM sources'],
    capture_output=True, text=True
)
sources = result.stdout.strip().split('\n')

for source_id in sources:
    source_id = source_id.strip()
    if not source_id:
        continue
    for i in range(2):
        chunk_id = str(uuid.uuid4())
        sql = "INSERT INTO chunks (id, source_id, content, token_count, metadata) VALUES ('" + chunk_id + "', '" + source_id + "', 'Additional knowledge chunk " + str(i+1) + " for testing the RAG pipeline. This content helps verify that semantic search works correctly.', 20, '{\"chunk_index\": " + str(i+1) + "}') ON CONFLICT (id) DO NOTHING"
        result = subprocess.run(
            ['sudo', 'docker', 'exec', 'myownclone_postgres', 'psql', '-U', 'postgres', '-d', 'myownclone', '-c', sql],
            capture_output=True, text=True
        )
        print("Chunk " + str(i+1) + " for " + source_id[:8] + ": OK" if result.returncode == 0 else "ERROR")

print("\nSeed data added!")
