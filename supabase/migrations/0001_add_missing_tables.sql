-- Migration: Add missing tables for Python models
-- Run against PostgreSQL database
-- This migration is idempotent - uses CREATE TABLE IF NOT EXISTS

-- ============================================
-- Table: cost_tracking
-- Tracks AI token usage and costs per clone/tenant
-- NOTE: clone_id is stored but no FK constraint since clones table may not exist
-- ============================================
CREATE TABLE IF NOT EXISTS cost_tracking (
    id TEXT PRIMARY KEY,
    clone_id TEXT NOT NULL,
    tenant_id TEXT,
    model VARCHAR(50),
    input_tokens INTEGER NOT NULL DEFAULT 0,
    output_tokens INTEGER NOT NULL DEFAULT 0,
    cost_cents INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ============================================
-- Table: clonify_plans
-- Subscription plans with pricing and features
-- ============================================
CREATE TABLE IF NOT EXISTS clonify_plans (
    id TEXT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    stripe_price_id VARCHAR(100),
    price_cents INTEGER NOT NULL,
    features JSONB,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ============================================
-- Table: impersonation_tokens
-- Tokens for admin impersonation sessions
-- NOTE: Uses admin_user_id to match existing column in database
-- ============================================
CREATE TABLE IF NOT EXISTS impersonation_tokens (
    id TEXT PRIMARY KEY,
    admin_user_id TEXT NOT NULL,
    tenant_id TEXT NOT NULL,
    token VARCHAR(128) NOT NULL UNIQUE,
    expires_at TIMESTAMP NOT NULL,
    used_at TIMESTAMP,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ============================================
-- Table: clone_feedback
-- User feedback on clone conversations
-- ============================================
CREATE TABLE IF NOT EXISTS clone_feedback (
    id TEXT PRIMARY KEY,
    clone_id TEXT NOT NULL,
    conversation_id TEXT,
    message_id TEXT,
    rating VARCHAR(10) NOT NULL,
    comment TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ============================================
-- Table: creator_memory
-- Long-term memory entries for clones (teaching material)
-- ============================================
CREATE TABLE IF NOT EXISTS creator_memory (
    id TEXT PRIMARY KEY,
    clone_id TEXT NOT NULL,
    memory_type VARCHAR(20) NOT NULL DEFAULT 'memory',
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    trigger_condition TEXT,
    priority INTEGER NOT NULL DEFAULT 0,
    active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ============================================
-- Table: email_inbound
-- Inbound email handling with classification
-- ============================================
CREATE TABLE IF NOT EXISTS email_inbound (
    id TEXT PRIMARY KEY,
    clone_id TEXT NOT NULL,
    from_email VARCHAR(255),
    from_name VARCHAR(255),
    subject VARCHAR(500),
    body_text TEXT,
    body_html TEXT,
    labels TEXT[],
    classification VARCHAR(50),
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    thread_id VARCHAR(500),
    received_at TIMESTAMP NOT NULL DEFAULT NOW(),
    responded_at TIMESTAMP,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ============================================
-- Table: email_templates
-- Pre-defined email templates for clone responses
-- ============================================
CREATE TABLE IF NOT EXISTS email_templates (
    id TEXT PRIMARY KEY,
    clone_id TEXT NOT NULL,
    name VARCHAR(255) NOT NULL,
    subject VARCHAR(500),
    body_html TEXT,
    trigger_keywords TEXT[],
    category VARCHAR(50),
    active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- ============================================
-- memory_type enum (may already exist with values: memory, signature, template, pedagogy)
-- Note: PostgreSQL doesn't support ALTER TYPE ... ADD VALUE IF NOT EXISTS in a transaction
-- The enum values are assumed to be present or added manually if needed
-- ============================================

-- ============================================
-- impersonation_log (singular) already exists with admin_id
-- This is just a comment for documentation
-- ============================================

-- ============================================
-- Indexes for new tables (skip if already exist)
-- ============================================
CREATE INDEX IF NOT EXISTS idx_cost_tracking_clone ON cost_tracking(clone_id);
CREATE INDEX IF NOT EXISTS idx_cost_tracking_created ON cost_tracking(created_at);
CREATE INDEX IF NOT EXISTS idx_clone_feedback_clone ON clone_feedback(clone_id);
CREATE INDEX IF NOT EXISTS idx_clone_feedback_conversation ON clone_feedback(conversation_id);
CREATE INDEX IF NOT EXISTS idx_creator_memory_clone ON creator_memory(clone_id);
CREATE INDEX IF NOT EXISTS idx_email_inbound_clone ON email_inbound(clone_id);
CREATE INDEX IF NOT EXISTS idx_email_inbound_status ON email_inbound(status);
CREATE INDEX IF NOT EXISTS idx_email_templates_clone ON email_templates(clone_id);

-- Note: impersonation_tokens indexes already exist:
-- idx_impersonation_tokens_expires
-- idx_impersonation_tokens_token
