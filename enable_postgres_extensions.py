#!/usr/bin/env python3
"""Enable required PostgreSQL extensions for MyOwnClone."""

import psycopg2
import sys

def enable_extensions():
    """Enable uuid-ossp and vector extensions."""
    try:
        # Connect to the database
        conn = psycopg2.connect(
            host='localhost',
            port=5432,
            user='postgres',
            password='postgres',
            database='myownclone'
        )
        conn.autocommit = True
        cursor = conn.cursor()

        print("Enabling PostgreSQL extensions...")

        # Enable uuid-ossp
        try:
            cursor.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
            print("[OK] Enabled uuid-ossp extension")
        except Exception as e:
            print(f"[WARNING] Failed to enable uuid-ossp: {e}")

        # Enable vector if available
        try:
            cursor.execute('CREATE EXTENSION IF NOT EXISTS vector;')
            print("[OK] Enabled vector extension")
        except Exception as e:
            print(f"[WARNING] Failed to enable vector: {e}")

        # Verify extensions
        cursor.execute("""
            SELECT extname, extversion
            FROM pg_extension
            WHERE extname IN ('uuid-ossp', 'vector')
        """)
        extensions = cursor.fetchall()

        print("\nEnabled extensions:")
        for ext_name, ext_version in extensions:
            print(f"  - {ext_name} (version: {ext_version})")

        cursor.close()
        conn.close()

        return True

    except psycopg2.Error as e:
        print(f"[ERROR] Database connection failed: {e}")
        return False

if __name__ == '__main__':
    if enable_extensions():
        print("\n✅ Extensions enabled successfully")
        sys.exit(0)
  ***REMOVED***:
        print("\n❌ Failed to enable extensions")
        sys.exit(1)