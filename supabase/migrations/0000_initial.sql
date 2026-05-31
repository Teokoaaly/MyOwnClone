-- Supabase Initial Migration for Réplica
-- Run this in the Supabase SQL Editor to set up the database

-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Create enum types
DO $$ BEGIN
    CREATE TYPE tenant_status AS ENUM ('active', 'suspended', 'cancelled', 'trial');
EXCEPTION WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE plan AS ENUM ('basic', 'pro', 'scale', 'enterprise', 'trial');
EXCEPTION WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE user_role AS ENUM ('owner', 'admin', 'member', 'platform_admin');
EXCEPTION WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE clone_mode AS ENUM ('pedagogy', 'sales', 'support');
EXCEPTION WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE source_type AS ENUM ('youtube', 'pdf', 'video', 'text', 'web', 'interview');
EXCEPTION WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE source_status AS ENUM ('uploading', 'processing', 'ready', 'error');
EXCEPTION WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE conversation_mode AS ENUM ('pedagogy', 'sales', 'support');
EXCEPTION WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE email_status AS ENUM ('pending', 'sent', 'discarded');
EXCEPTION WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE booking_status AS ENUM ('confirmed', 'cancelled', 'completed', 'no_show');
EXCEPTION WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE memory_type AS ENUM ('memory', 'signature', 'template');
EXCEPTION WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE product_status AS ENUM ('active', 'inactive');
EXCEPTION WHEN duplicate_object THEN null;
END $$;

-- Tenants table
CREATE TABLE IF NOT EXISTS tenants (
    id TEXT PRIMARY KEY,
    slug VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    plan plan NOT NULL DEFAULT 'trial',
    status tenant_status NOT NULL DEFAULT 'trial',
    trial_ends_at TIMESTAMP,
    stripe_customer_id TEXT,
    stripe_subscription_id TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    tenant_id TEXT NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    name VARCHAR(255),
    email VARCHAR(255) NOT NULL UNIQUE,
    email_verified TIMESTAMP,
    image TEXT,
    role user_role NOT NULL DEFAULT 'owner',
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- NextAuth accounts
CREATE TABLE IF NOT EXISTS accounts (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    type VARCHAR(255) NOT NULL,
    provider VARCHAR(255) NOT NULL,
    provider_account_id VARCHAR(255) NOT NULL,
    refresh_token TEXT,
    access_token TEXT,
    expires_at TIMESTAMP,
    token_type VARCHAR(255),
    scope TEXT,
    id_token TEXT,
    session_state TEXT
);

-- NextAuth verification tokens
CREATE TABLE IF NOT EXISTS verification_tokens (
    identifier VARCHAR(255) NOT NULL,
    token VARCHAR(255) NOT NULL UNIQUE,
    expires TIMESTAMP NOT NULL
);

-- Clones table
CREATE TABLE IF NOT EXISTS clones (
    id TEXT PRIMARY KEY,
    tenant_id TEXT NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    personality TEXT,
    tone VARCHAR(50),
    language VARCHAR(10) NOT NULL DEFAULT 'es',
    avatar_url TEXT,
    active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Clone modes
CREATE TABLE IF NOT EXISTS clone_modes (
    id TEXT PRIMARY KEY,
    clone_id TEXT NOT NULL REFERENCES clones(id) ON DELETE CASCADE,
    mode clone_mode NOT NULL,
    system_prompt TEXT NOT NULL,
    active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Sources
CREATE TABLE IF NOT EXISTS sources (
    id TEXT PRIMARY KEY,
    clone_id TEXT NOT NULL REFERENCES clones(id) ON DELETE CASCADE,
    type source_type NOT NULL,
    title VARCHAR(500) NOT NULL,
    url TEXT,
    status source_status NOT NULL DEFAULT 'uploading',
    metadata JSONB,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Chunks (requires vector extension)
CREATE TABLE IF NOT EXISTS chunks (
    id TEXT PRIMARY KEY,
    source_id TEXT NOT NULL REFERENCES sources(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    embedding vector(1536) NOT NULL,
    token_count INTEGER,
    metadata JSONB
);

-- IVFFlat index for cosine similarity search
CREATE INDEX IF NOT EXISTS chunks_embedding_idx ON chunks
    USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);

-- Conversations
CREATE TABLE IF NOT EXISTS conversations (
    id TEXT PRIMARY KEY,
    clone_id TEXT NOT NULL REFERENCES clones(id) ON DELETE CASCADE,
    visitor_id VARCHAR(255),
    mode conversation_mode NOT NULL DEFAULT 'pedagogy',
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Messages
CREATE TABLE IF NOT EXISTS messages (
    id TEXT PRIMARY KEY,
    conversation_id TEXT NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
    role VARCHAR(20) NOT NULL,
    content TEXT NOT NULL,
    confidence TEXT,
    sources JSONB,
    feedback VARCHAR(10),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Emails (inbox)
CREATE TABLE IF NOT EXISTS emails (
    id TEXT PRIMARY KEY,
    clone_id TEXT NOT NULL REFERENCES clones(id) ON DELETE CASCADE,
    from_email VARCHAR(255) NOT NULL,
    from_name VARCHAR(255),
    subject TEXT NOT NULL,
    body TEXT NOT NULL,
    draft_reply TEXT,
    status email_status NOT NULL DEFAULT 'pending',
    thread_id TEXT,
    received_at TIMESTAMP NOT NULL DEFAULT NOW(),
    sent_at TIMESTAMP,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Meeting types
CREATE TABLE IF NOT EXISTS meeting_types (
    id TEXT PRIMARY KEY,
    clone_id TEXT NOT NULL REFERENCES clones(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    duration INTEGER NOT NULL,
    price INTEGER NOT NULL DEFAULT 0,
    description TEXT,
    color VARCHAR(7),
    active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Availability
CREATE TABLE IF NOT EXISTS availability (
    id TEXT PRIMARY KEY,
    clone_id TEXT NOT NULL REFERENCES clones(id) ON DELETE CASCADE,
    day_of_week INTEGER NOT NULL,
    start_time VARCHAR(5) NOT NULL,
    end_time VARCHAR(5) NOT NULL
);

-- Bookings
CREATE TABLE IF NOT EXISTS bookings (
    id TEXT PRIMARY KEY,
    meeting_type_id TEXT NOT NULL REFERENCES meeting_types(id) ON DELETE CASCADE,
    visitor_name VARCHAR(255) NOT NULL,
    visitor_email VARCHAR(255) NOT NULL,
    date VARCHAR(10) NOT NULL,
    time VARCHAR(5) NOT NULL,
    status booking_status NOT NULL DEFAULT 'confirmed',
    meeting_url TEXT,
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Memories / Brain
CREATE TABLE IF NOT EXISTS memories (
    id TEXT PRIMARY KEY,
    clone_id TEXT NOT NULL REFERENCES clones(id) ON DELETE CASCADE,
    type memory_type NOT NULL DEFAULT 'memory',
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    trigger_condition TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Analytics
CREATE TABLE IF NOT EXISTS analytics_questions (
    id TEXT PRIMARY KEY,
    clone_id TEXT NOT NULL REFERENCES clones(id) ON DELETE CASCADE,
    question TEXT NOT NULL,
    count INTEGER NOT NULL DEFAULT 1,
    last_asked_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS analytics_gaps (
    id TEXT PRIMARY KEY,
    clone_id TEXT NOT NULL REFERENCES clones(id) ON DELETE CASCADE,
    question TEXT NOT NULL,
    count INTEGER NOT NULL DEFAULT 1,
    suggested_source TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Products
CREATE TABLE IF NOT EXISTS products (
    id TEXT PRIMARY KEY,
    clone_id TEXT NOT NULL REFERENCES clones(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    description TEXT,
    price INTEGER,
    url TEXT,
    image_url TEXT,
    status product_status NOT NULL DEFAULT 'active',
    priority INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Impersonation logs
CREATE TABLE IF NOT EXISTS impersonation_logs (
    id TEXT PRIMARY KEY,
    admin_user_id TEXT NOT NULL,
    tenant_id TEXT NOT NULL,
    reason TEXT NOT NULL,
    started_at TIMESTAMP NOT NULL DEFAULT NOW(),
    ended_at TIMESTAMP
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_clones_tenant ON clones(tenant_id);
CREATE INDEX IF NOT EXISTS idx_sources_clone ON sources(clone_id);
CREATE INDEX IF NOT EXISTS idx_conversations_clone ON conversations(clone_id);
CREATE INDEX IF NOT EXISTS idx_messages_conversation ON messages(conversation_id);
CREATE INDEX IF NOT EXISTS idx_emails_clone_status ON emails(clone_id, status);
CREATE INDEX IF NOT EXISTS idx_bookings_meeting ON bookings(meeting_type_id);
CREATE INDEX IF NOT EXISTS idx_memories_clone ON memories(clone_id);
CREATE INDEX IF NOT EXISTS idx_analytics_questions_clone ON analytics_questions(clone_id);
CREATE INDEX IF NOT EXISTS idx_analytics_gaps_clone ON analytics_gaps(clone_id);
CREATE INDEX IF NOT EXISTS idx_products_clone ON products(clone_id);
