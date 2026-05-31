-- Clone mode enum
DO $$ BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'clone_mode') THEN
    CREATE TYPE clone_mode AS ENUM ('pedagogy', 'support', 'sales');
  END IF;
END $$;

-- Clones table
CREATE TABLE IF NOT EXISTS clone_configs (
  id TEXT PRIMARY KEY,
  tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  personality TEXT,
  tone VARCHAR(50),
  language VARCHAR(10) NOT NULL DEFAULT 'es',
  avatar_url TEXT,
  slug VARCHAR(50) UNIQUE,
  active_modes clone_mode[] DEFAULT '{pedagogy}',
  is_active BOOLEAN NOT NULL DEFAULT true,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Clone mode prompts
CREATE TABLE IF NOT EXISTS clone_mode_prompts (
  id TEXT PRIMARY KEY,
  clone_id TEXT NOT NULL REFERENCES clone_configs(id) ON DELETE CASCADE,
  mode clone_mode NOT NULL,
  system_prompt TEXT NOT NULL,
  active BOOLEAN NOT NULL DEFAULT true,
  created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Sources
CREATE TABLE IF NOT EXISTS sources (
  id TEXT PRIMARY KEY,
  clone_id TEXT NOT NULL REFERENCES clone_configs(id) ON DELETE CASCADE,
  type VARCHAR(20) NOT NULL,
  title VARCHAR(500) NOT NULL,
  url TEXT,
  status VARCHAR(20) NOT NULL DEFAULT 'uploading',
  metadata JSONB,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Chunks (vector embeddings)
CREATE TABLE IF NOT EXISTS chunks (
  id TEXT PRIMARY KEY,
  source_id TEXT NOT NULL REFERENCES sources(id) ON DELETE CASCADE,
  content TEXT NOT NULL,
  token_count INTEGER,
  metadata JSONB
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_clone_configs_tenant ON clone_configs(tenant_id);
CREATE INDEX IF NOT EXISTS idx_clone_mode_prompts_clone ON clone_mode_prompts(clone_id);
CREATE INDEX IF NOT EXISTS idx_sources_clone ON sources(clone_id);
CREATE INDEX IF NOT EXISTS idx_chunks_source ON chunks(source_id);
