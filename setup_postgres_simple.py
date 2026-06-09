#!/usr/bin/env python3
"""
Simple PostgreSQL setup for MyOwnClone development.
"""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys

def test_connection(host='localhost', port=5432, user='postgres', password='postgres', database=None):
    """Test PostgreSQL connection."""
    try:
        conn_params = {
            'host': host,
            'port': port,
            'user': user,
            'password': password
        }
        if database:
            conn_params['database'] = database

        conn = psycopg2.connect(**conn_params)
        print(f"[OK] Connected to PostgreSQL: {user}@{host}:{port}")
        return conn
    except psycopg2.OperationalError as e:
        print(f"[ERROR] Connection failed: {e}")
        return None

def create_database(conn, dbname='myownclone'):
    """Create database if it doesn't exist."""
    try:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (dbname,))
        exists = cursor.fetchone()

        if exists:
            print(f"[OK] Database '{dbname}' already exists")
        else:
            cursor.execute(f"CREATE DATABASE {dbname}")
            print(f"[OK] Created database '{dbname}'")

        cursor.close()
        return True
    except Exception as e:
        print(f"[ERROR] Failed to create database: {e}")
        return False

def check_pgvector(conn):
    """Check pgvector extension."""
    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 1 FROM pg_available_extensions
            WHERE name = 'vector' AND installed_version IS NOT NULL
        """)
        installed = cursor.fetchone()

        if installed:
            print("[OK] pgvector extension is installed")

            cursor.execute("SELECT 1 FROM pg_extension WHERE extname = 'vector'")
            enabled = cursor.fetchone()
            if enabled:
                print("[OK] pgvector extension is enabled")
            else:
                try:
                    cursor.execute("CREATE EXTENSION IF NOT EXISTS vector")
                    print("[OK] Enabled pgvector extension")
                except Exception as e:
                    print(f"[WARNING] Could not enable pgvector: {e}")
        else:
            print("[WARNING] pgvector extension is not installed")
            print("  For Windows: may need to install separately")
            print("  See: https://github.com/pgvector/pgvector")

        cursor.close()
    except Exception as e:
        print(f"[ERROR] Checking pgvector: {e}")

def main():
    print("=== PostgreSQL Setup for MyOwnClone ===")
    print()

    # Try connections
    passwords = ['postgres', '', None]
    conn = None
    password_used = None

    for password in passwords:
        print(f"Trying password: '{password if password else '(empty)'}'...")
        conn = test_connection(password=password)
        if conn:
            password_used = password
            break

    if not conn:
        print("\n[ERROR] Could not connect to PostgreSQL")
        print("Please ensure PostgreSQL is running on port 5432")
        print("Try: psql -U postgres -h localhost")
        return 1

    print("\n--- Database Setup ---")
    create_database(conn, 'myownclone')

    # Connect to specific database
    db_password = 'postgres' if 'postgres' in passwords and password_used == 'postgres' else password_used
    db_conn = test_connection(database='myownclone', password=db_password)

    if not db_conn:
        print("[WARNING] Could not connect to myownclone database")
        print("  Database may need different credentials")
    else:
        print("\n--- pgvector Extension ---")
        check_pgvector(db_conn)
        db_conn.close()

    conn.close()

    print("\n[OK] PostgreSQL setup done!")
    print("\nCredentials in .env: postgres:postgres@localhost:5432/myownclone")

    return 0

if __name__ == '__main__':
    sys.exit(main())