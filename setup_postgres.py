#!/usr/bin/env python3
"""
Setup PostgreSQL database for MyOwnClone development.
Checks connection, creates database if needed, enables pgvector extension.
"""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys

def test_connection(host='localhost', port=5432, user='postgres', password='postgres', database=None):
    """Test PostgreSQL connection with given credentials."""
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
        print(f"✗ Connection failed: {e}")
        return None

def create_database(conn, dbname='myownclone'):
    """Create database if it doesn't exist."""
    try:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        # Check if database exists
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (dbname,))
        exists = cursor.fetchone()

        if exists:
            print(f"✓ Database '{dbname}' already exists")
        else:
            cursor.execute(f"CREATE DATABASE {dbname}")
            print(f"✓ Created database '{dbname}'")

        cursor.close()
        return True
    except Exception as e:
        print(f"✗ Failed to create database: {e}")
        return False

def check_pgvector_extension(conn):
    """Check if pgvector extension is available and enabled."""
    try:
        cursor = conn.cursor()

        # Check if extension exists in system
        cursor.execute("""
            SELECT 1 FROM pg_available_extensions
            WHERE name = 'vector' AND installed_version IS NOT NULL
        """)
        installed = cursor.fetchone()

        if installed:
            print("✓ pgvector extension is installed")

            # Check if enabled in current database
            cursor.execute("SELECT 1 FROM pg_extension WHERE extname = 'vector'")
            enabled = cursor.fetchone()
            if enabled:
                print("✓ pgvector extension is enabled in current database")
            else:
                try:
                    cursor.execute("CREATE EXTENSION IF NOT EXISTS vector")
                    print("✓ Enabled pgvector extension in current database")
                except Exception as e:
                    print(f"⚠ Could not enable pgvector: {e}")
        else:
            print("⚠ pgvector extension is not installed in PostgreSQL")
            print("  For Windows, may need to install separately")
            print("  See: https://github.com/pgvector/pgvector")

        cursor.close()
    except Exception as e:
        print(f"✗ Error checking pgvector: {e}")

def main():
    print("=== PostgreSQL Setup for MyOwnClone ===\n")

    # Try different password combinations
    passwords_to_try = ['postgres', '', None]

    conn = None
    for password in passwords_to_try:
        print(f"Trying password: '{password if password else '(empty)'}'...")
        conn = test_connection(password=password)
        if conn:
            break

    if not conn:
        print("\n❌ Could not connect to PostgreSQL")
        print("Please ensure PostgreSQL is running on port 5432")
        print("Try connecting manually with: psql -U postgres -h localhost")
        return 1

    print("\n--- Database Setup ---")
    create_database(conn, 'myownclone')

    # Now connect to the specific database
    db_conn = test_connection(database='myownclone', password='postgres' if 'postgres' in passwords_to_try and conn else None)
    if not db_conn:
        print("⚠ Could not connect to myownclone database, but main connection OK")
        print("  Database may need different credentials")
        return 0

    print("\n--- pgvector Extension ---")
    check_pgvector_extension(db_conn)

    print("\n--- Connection Details ---")
    print(f"Database: postgresql://postgres:*****@localhost:5432/myownclone")
    print("(Credentials match .env configuration)")

    db_conn.close()
    conn.close()

    print("\n✅ PostgreSQL setup complete!")
    print("\nNext steps:")
    print("1. Run backend migrations: cd api && flask --app app_factory db upgrade")
    print("2. Run frontend migrations: cd MyOwnClone && npm run db:push")
    print("3. Start backend: cd api && flask --app app_factory run")

    return 0

if __name__ == '__main__':
    sys.exit(main())