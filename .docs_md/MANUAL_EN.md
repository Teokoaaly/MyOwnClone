# 📘 MyOwnClone Complete Manual

<p align="center">
  <strong>Multi-tenant SaaS platform for creating, deploying and scaling AI digital clones.</strong><br />
  From end-user perspective to technical deployment and operations guide.
</p>

---

## 📋 Table of Contents

1. [Introduction](#1-introduction)
2. [User Guide](#2-user-guide)
3. [Technical Guide](#3-technical-guide)
4. [Deployment Guide](#4-deployment-guide)
5. [API Reference](#5-api-reference)
6. [Troubleshooting](#6-troubleshooting)
7. [FAQ](#7-faq)

---

# 1. Introduction

## 1.1 What is MyOwnClone?

**MyOwnClone** is a SaaS platform that lets content creators, educators, coaches, and businesses launch their own **AI digital clone**: a conversational assistant trained on their knowledge that can:

- Answer questions in their own tone and style
- Handle customer support 24/7
- Provide product recommendations and sales assistance
- Manage their email inbox
- Book meetings automatically
- Detect knowledge gaps to keep learning

The system uses **RAG (Retrieval-Augmented Generation)**: instead of fine-tuning a model, the clone searches a vector knowledge base for the most relevant information and passes it to the LLM as context, achieving accurate responses without losing the creator's style.

## 1.2 Who is it for?

| Role | Key benefit |
|---|---|
| **Content creator** | An assistant that answers like you, 24/7 |
| **Educator / Coach** | A tutor that teaches using your methodology |
| **Customer support** | Automate responses without losing quality |
| **Sales** | A virtual salesperson that knows the catalog |
| **Developer** | APIs and widget to integrate anywhere |
| **Platform admin** | Manage multiple tenants from one panel |

## 1.3 Plan Model

| Plan | Conversations/day | Emails/month | Sources | Storage | Clones | Team members |
|---|---|---|---|---|---|---|
| **Trial** | 50 | 20 | 5 | 100 MB | 1 | 1 |
| **Basic** | 200 | 100 | 20 | 1 GB | 1 | 1 |
| **Pro** | 1,000 | 500 | 100 | 5 GB | 3 | 3 |
| **Scale** | 5,000 | 2,000 | 500 | 25 GB | 10 | 10 |
| **Enterprise** | 50,000 | 10,000 | 2,000 | 100 GB | 50 | 50 |

When a limit is exceeded, the clone returns an informative message. Upgrades are handled from the billing panel via Stripe.

---

# 2. User Guide

## 2.1 Getting Started

### Registration

1. Go to the [landing page](/) and click **"Create account"**
2. You can sign up with:
   - **Email and password** (direct registration)
   - **Google** (OAuth)
   - **Magic link** (we send a login link to your email)
3. Confirm your email if you used password registration
4. You're automatically taken to the **Command Center** (main dashboard)

### Onboarding

After your first login, an onboarding banner guides you through:

1. **Configure your clone** — name, personality, tone
2. **Add sources** — upload your content
3. **Test the chat** — ask your first question
4. **View analytics** — monitor usage

### Navigation

The interface is divided into:

```
┌──────────────────────────────────────────────────┐
│  MyOwnClone  [Sidebar]              [Profile]    │
├──────────┬───────────────────────────────────────┤
│          │                                       │
│ Sidebar  │        Main content area              │
│          │                                       │
│ Overview │                                       │
│ ─────────│                                       │
│ Search   │                                       │
│ Crawl    │                                       │
│ Extract  │                                       │
│ Research │                                       │
│ ─────────│                                       │
│ Usage    │                                       │
│ Billing  │                                       │
│ Settings │                                       │
│ ─────────│                                       │
│ ① FREE   │                                       │
│   TRIAL  │                                       │
│          │                                       │
│ [User]   │                                       │
└──────────┴───────────────────────────────────────┘
```

The sidebar collapses to a hamburger menu on mobile. Dark/light theme can be toggled from settings.

## 2.2 Command Center (Overview)

The **Command Center** (`/resumen`) is the main dashboard page. It displays:

- **Quick metrics**: total conversations, questions answered, gaps detected
- **Get Started** (quick links):
  - API Key — configure your key
  - Usage — last 30 days chart
  - Docs / Agent Toolkit
- **AI Search**: a text box where you can ask about endpoints, schemas, workflows
- **Recent Queries**: last performed queries

## 2.3 Clones

### 2.3.1 Creating a Clone

From the settings panel you can create a clone with these parameters:

| Parameter | Description | Example |
|---|---|---|
| **Name** | Clone name | "Maria's Assistant" |
| **Slug** | Unique identifier for URLs | `maria-assistant` |
| **Description** | What your clone does | "Educational clone about programming" |
| **Avatar** | Profile image URL | `https://...` |
| **Personality** | How it behaves | "Empathetic, didactic, patient" |
| **Tone** | Communication style | "Casual but professional" |
| **Language** | Main language | `en` / `es` |
| **Active modes** | Available modes | pedagogy, support, sales |

### 2.3.2 Clone Modes

Each clone can operate in **three modes**, each with its own system prompt:

#### 📚 Pedagogy Mode
- Answers questions based on knowledge sources
- Ideal for: courses, books, educational content
- Prompt: "You are an expert tutor who explains clearly..."

#### 🛠️ Support Mode
- Handles incidents and technical questions
- Ideal for: customer service, FAQ, troubleshooting
- Prompt: "You are a support agent who solves problems..."

#### 💼 Sales Mode
- Advises on products and services from the catalog
- Ideal for: ecommerce, consulting, services
- Prompt: "You are a sales advisor who knows the catalog..."

### 2.3.3 Embeddable Widget

You can embed your clone on any website with one line:

```html
<script src="https://yourdomain.com/widget.js" data-clone="my-clone" data-mode="support"></script>
```

Configurable parameters:
- `data-clone` (required): clone slug
- `data-mode` (optional): `pedagogy` | `support` | `sales` (default: `pedagogy`)
- `data-theme` (optional): `light` | `dark`
- `data-position` (optional): `right` | `left` (default: `right`)
- `data-color` (optional): primary color in HEX

## 2.4 Knowledge Sources

Sources are the content your clone will use to answer. They're managed from the **Library** section (`/biblioteca`).

### 2.4.1 Source Types

| Type | Description | Upload method |
|---|---|---|
| **PDF** | PDF documents | File upload |
| **YouTube** | Video transcripts | Video URL |
| **Web** | Web page scraping | URL |
| **Text** | Manually written content | Text editor |
| **Interview** | Structured Q&A | Form input |
| **Video** | Video files (Whisper transcription) | File upload |

### 2.4.2 Processing States

Each source goes through a lifecycle:

```
uploading → processing → ready
                            └→ error (on failure)
```

- **uploading**: file is being uploaded to Supabase Storage
- **processing**: text extraction, chunking, and embedding generation
- **ready**: source is available for semantic search
- **error**: a failure occurred (unsupported format, timeout, etc.)

### 2.4.3 Knowledge Silos

Silos let you organize sources by topic. Each source belongs to one silo:

| Silo | Usage |
|---|---|
| **teach** | Pedagogical content |
| **support** | Support knowledge base |
| **sales** | Product catalog and sales |

When a user chats in "support" mode, the clone only searches sources in the `support` silo, improving response accuracy.

### 2.4.4 Ingestion Process

```
Source (PDF, URL, text)
    │
    ▼
Text extraction
    │
    ▼
Chunking (split into ~500 token fragments)
    │
    ▼
Embedding generation (OpenAI text-embedding-3-small)
    │
    ▼
Storage in pgvector (PostgreSQL)
    │
    ▼
Ready for semantic search!
```

## 2.5 Chat

### 2.5.1 How it Works

The chat is the main interface for interacting with your clone. When you ask a question:

1. Your question is sent to the backend
2. An embedding of the question is generated (OpenAI)
3. pgvector is searched by cosine similarity (top-5 chunks, threshold > 0.75)
4. A system prompt is built with:
   - Clone personality and tone
   - Mode prompt (pedagogy/support/sales)
   - Creator memories
   - Relevant retrieved chunks
5. A response is generated with the LLM (Claude or OpenAI)
6. A **confidence score** is calculated (0.0 - 1.0)
7. If `confidence < 0.7`, a **knowledge gap** is recorded
8. The response is sent to the frontend via **Server-Sent Events** (streaming)

### 2.5.2 Confidence Score and Gap Detection

The confidence score measures how certain the response is:

| Score | Meaning | Action |
|---|---|---|
| 0.9 - 1.0 | High confidence | Normal response |
| 0.7 - 0.9 | Medium confidence | Response with caveat |
| 0.5 - 0.7 | Low confidence | Gap recorded, new source suggested |
| < 0.5 | Very low | Generic response + gap recorded |

Gaps accumulate in `analytics_gaps` and can be reviewed from the analytics panel to know what content is missing.

### 2.5.3 Response Streaming

The frontend receives the response in real-time via SSE:

```
POST /api/clone/{slug}/chat
Content-Type: application/json

{
  "message": "How do I get started?",
  "silo": "teach"
}

Response (stream):
data: {"content": "To get started,"}
data: {"content": " you need to register"}
data: {"content": " your account..."}
data: {"done": true, "confidence": 0.92, "sources": [...]}
```

### 2.5.4 Messages and Feedback

Each message can receive user feedback (thumbs up/down) stored in the `messages.feedback` column to improve quality.

## 2.6 Email Inbox

### 2.6.1 Setup

To receive emails, configure a **SendGrid Inbound Parse** webhook pointing to your endpoint. Incoming emails are stored in the `emails` table.

### 2.6.2 Automatic Classification

The system classifies each incoming email:

- **Category**: inquiry, support, sales, spam
- **Urgency**: high, medium, low
- **Subject**: extracted and processed

### 2.6.3 AI Drafts

For each email, the clone can generate a draft response automatically:

```
POST /api/clone/inbox/{id}/generate-draft
→ { "draft": "Dear customer,\n\nThank you for contacting us..." }
```

The draft is generated in the creator's tone and style, using the clone's relevant information.

### 2.6.4 Auto-Reply

You can configure the clone to auto-reply to emails with high confidence (>0.85). Low-confidence emails are flagged for manual review.

## 2.7 Meetings

### 2.7.1 Configure Availability

From `/reuniones` you can define your weekly availability (days and hours). The system uses the `availability` table to manage time slots.

### 2.7.2 Whereby Integration

Video calls are made via **Whereby Embedded**. When a meeting is booked:

1. A room is created in Whereby
2. A confirmation email with the link is sent
3. The booking is saved in the database

### 2.7.3 Public Booking

Visitors can book meetings directly from the widget or the clone's public page (`/{slug}`).

## 2.8 Analytics

### 2.8.1 Metrics Overview

| Metric | Description |
|---|---|
| **Total conversations** | Total number of conversations |
| **Total messages** | Messages exchanged |
| **Questions answered** | Successfully processed queries |
| **Gaps detected** | Low-confidence questions |
| **Active sessions** | Ongoing conversations |
| **Automation rate** | % of successful auto-responses |

### 2.8.2 Gap Detection

Gaps are questions the clone couldn't answer with enough confidence. Each gap includes:

- The exact question
- How many times it was asked
- Date of last occurrence
- Suggested source (you can add content to cover it)

### 2.8.3 Frequently Asked Questions

The system logs the most frequent questions (`analytics_questions` table) so you can identify patterns and improve your content.

## 2.9 Billing

### 2.9.1 Stripe Portal

From `/facturacion` you can:

- View your current plan
- Change plans (upgrade/downgrade)
- Manage payment method
- View billing history

Everything is handled through the **Stripe Customer Portal**, opened in a secure window.

### 2.9.2 Plan Limits

Limits are enforced in real-time. When a limit is exceeded, the clone informs the user. Limits reset daily or monthly depending on the resource:

- **Conversations/day**: daily reset at 00:00 UTC
- **Emails/month**: reset on billing date
- **Storage**: cumulative, upgrade required to expand

### 2.9.3 Trial Period

New users get a 14-day free trial with the Trial plan. During this period:

- No feature limitations
- No credit card required
- On expiry, a paid plan is required

## 2.10 Settings

### 2.10.1 API Keys

From `/configuracion` you can generate and manage API keys for external integrations. Keys allow:

- Accessing the clone API programmatically
- Integrating the chat in external applications
- Automating source uploads

### 2.10.2 User Profile

Manage your:

- Name and email
- Avatar
- Password
- Language preferences
- Theme (dark/light)

---

# 3. Technical Guide

## 3.1 Overall Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     🌐 Client                               │
│  [Browser (Dashboard)]  [External Widget]  [API Client]    │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              🚀 Next.js 16 (Frontend App)                   │
│                                                             │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────────────┐ │
│  │ App Router  │  │ API Routes   │  │ Middleware (Proxy) │ │
│  │ (SSR/SSG)   │  │ (local DB)   │  │ → Flask backend    │ │
│  └─────────────┘  └──────────────┘  └────────────────────┘ │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Providers: SessionProvider + ThemeProvider + i18n    │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────┬───────────────────────────────────────┘
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
┌──────────────┐ ┌────────┐ ┌──────────┐
│  PostgreSQL  │ │ Redis  │ │ Supabase │
│  + pgvector  │ │ (Rate  │ │ Storage  │
│  (Drizzle)   │ │ Limit) │ │ (Files)  │
└──────────────┘ └────────┘ └──────────┘
          ▲
          │
          ▼
┌─────────────────────────────────────────────────────────────┐
│              🐍 Flask 3 (Backend API)                       │
│                                                             │
│  ┌──────────┐ ┌──────────┐ ┌────────────┐ ┌────────────┐  │
│  │ Console  │ │ Public   │ │ Auth BP   │ │ Deploy BP  │  │
│  │ Blueprint│ │ Blueprint│ │            │ │            │  │
│  └──────────┘ └──────────┘ └────────────┘ └────────────┘  │
│                                                             │
│  Core: ModelManager, RAG Pipeline, Email Processor          │
└─────────────────────┬───────────────────────────────────────┘
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
   ┌──────────┐ ┌──────────┐ ┌──────────┐
   │Anthropic │ │ OpenAI   │ │ Stripe   │
   │ Claude   │ │ Embed/   │ │ Payments │
   │ Chat     │ │ Whisper  │ │          │
   └──────────┘ └──────────┘ └──────────┘
```

### System Layers

| Layer | Technology | Responsibility |
|---|---|---|
| **Presentation** | Next.js 16 + React 19 | SSR, UI, Server/Client Components |
| **Frontend API** | Next.js API Routes | Direct DB queries, proxies |
| **Middleware** | Next.js Edge Middleware | Reverse proxy, tenant detection |
| **Backend API** | Flask 3 + Gunicorn | Business logic, RAG, integrations |
| **Database** | PostgreSQL 15 + pgvector | Relational data + vectors |
| **Cache** | Redis 7 (Upstash) | Rate limiting, sessions |
| **Storage** | Supabase Storage | Files (PDFs, images) |
| **LLM** | Anthropic Claude / OpenAI | Text generation, embeddings |

## 3.2 Frontend in Detail

### 3.2.1 Folder Structure

```
MyOwnClone/src/
├── app/
│   ├── (dashboard)/               # Authenticated route group
│   │   ├── layout.tsx             # Dashboard layout (sidebar + main)
│   │   ├── resumen/               # Command Center
│   │   ├── biblioteca/            # Source management
│   │   ├── cerebro/               # Memory crawl
│   │   ├── inbox/                 # Email inbox
│   │   ├── productos/             # Product catalog
│   │   ├── analiticas/            # Analytics
│   │   ├── facturacion/           # Billing
│   │   ├── configuracion/         # Settings
│   │   ├── reuniones/             # Meetings
│   │   └── registro/              # Registration
│   ├── (public)/[slug]/           # Clone public page
│   ├── admin/                     # Admin panel
│   ├── api/                       # API routes
│   ├── providers.tsx              # Session + Theme providers
│   ├── layout.tsx                 # Root layout
│   └── page.tsx                   # Landing page
├── components/
│   ├── admin/                     # Admin components
│   ├── chat/                      # Chat components
│   ├── dashboard/                 # Dashboard components
│   └── ui/                        # Generic UI components
├── lib/
│   ├── auth.ts                    # NextAuth config
│   ├── db/                        # Drizzle client + schema
│   ├── rag/                       # RAG pipeline (deprecated)
│   ├── stripe.ts                  # Stripe client
│   ├── email.ts                   # Resend emails
│   ├── video.ts                   # Whereby meetings
│   ├── quotas.ts                  # Plan limits
│   └── platform-admin.ts          # Admin auth
├── middleware.ts                  # Proxy + tenant detection
└── i18n/                          # Internationalization
```

### 3.2.2 Server vs Client Components

By default, components in Next.js App Router are **Server Components**. `"use client"` is used only when needed:

**Server Components** (default):
- `layout.tsx` (dashboard, admin, root)
- Pages that only render server data
- Components without interactivity

**Client Components** (`"use client"`):
- `ChatPanel.tsx` — local state, streaming, events
- `Sidebar.tsx` — navigation, mobile state
- `ThemeToggle.tsx` — theme switching
- `SearchCommandBar.tsx` — interactive search
- Components using `useState`, `useEffect`, `useSession`

### 3.2.3 Providers

```tsx
// src/app/providers.tsx
"use client";

import { SessionProvider } from "next-auth/react";
import { ThemeProvider } from "next-themes";

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <SessionProvider>
      <ThemeProvider attribute="class" defaultTheme="light" enableSystem={false}>
        {children}
      </ThemeProvider>
    </SessionProvider>
  );
}
```

### 3.2.4 Design System

Uses **Tailwind CSS v4** with custom CSS variables for theming:

```css
/* Light mode */
:root {
  --bg-page:    #E8E2DD;
  --bg-shell:   #FFFFFF;
  --surface-1:  #FFFFFF;
  --surface-2:  #FAFAF9;
  --text-primary: #1C1917;
  --text-muted: #78716C;
  --accent-warm: #EA580C;
}

/* Dark mode */
.dark {
  --bg-page:    #070708;
  --bg-shell:   #0B0B0C;
  --surface-1:  #121213;
  --text-primary: #F4F4F5;
}
```

### 3.2.5 Typography

- **DM Sans** (variable): Main system font, weights 400-700
- **JetBrains Mono** (variable): Monospace for code and numbers, weights 500-700

## 3.3 Backend in Detail

### 3.3.1 Application Factory

```python
# api/app_factory.py
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    
    app.register_blueprint(console_bp, url_prefix="/console")
    app.register_blueprint(auth_bp, url_prefix="/console/api/auth")
    app.register_blueprint(myownclone_public_bp)
    app.register_blueprint(deploy_bp)
    
    return app
```

### 3.3.2 Blueprints

| Blueprint | Prefix | Endpoints |
|---|---|---|
| **console** | `/console` | Authenticated dashboard API |
| **auth** | `/console/api/auth` | Login, token verification |
| **public** | (root) | Public chat, bookings |
| **deploy** | (root) | Frontend deploy trigger |

## 3.4 Database

### 3.4.1 Drizzle ORM Schema (Frontend)

The frontend uses **Drizzle ORM** with PostgreSQL. Connection in `src/lib/db/index.ts`:

```tsx
import { drizzle } from "drizzle-orm/node-postgres";
import { Pool } from "pg";
import * as schema from "./schema";

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});

export const db = drizzle(pool, { schema });
export { schema };
```

### 3.4.2 Tables

#### `tenants`
| Column | Type | Description |
|---|---|---|
| `id` | `text PK` | UUID |
| `slug` | `text UNIQUE` | Unique identifier |
| `name` | `text NOT NULL` | Tenant name |
| `plan` | `enum` | `trial`, `basic`, `pro`, `scale`, `enterprise` |
| `status` | `enum` | `active`, `suspended`, `cancelled`, `trial` |
| `trial_ends_at` | `timestamp` | Trial end date |
| `stripe_customer_id` | `text` | Stripe customer ID |
| `stripe_subscription_id` | `text` | Stripe subscription ID |

#### `users`
| Column | Type | Description |
|---|---|---|
| `id` | `text PK` | UUID |
| `tenant_id` | `text FK → tenants.id` | Parent tenant |
| `name` | `text` | User's name |
| `email` | `text UNIQUE` | Email |
| `password_hash` | `text` | bcrypt password hash |
| `email_verified` | `timestamp` | Email verification date |
| `image` | `text` | Avatar URL |
| `role` | `enum` | `owner`, `admin`, `member`, `platform_admin` |

#### `clone_configs`
| Column | Type | Description |
|---|---|---|
| `id` | `text PK` | UUID |
| `tenant_id` | `text FK → tenants.id` | Owner tenant |
| `name` | `text NOT NULL` | Clone name |
| `slug` | `text UNIQUE` | URL slug |
| `description` | `text` | Description |
| `avatar_url` | `text` | Avatar URL |
| `personality` | `text` | Personality |
| `tone` | `text` | Communication tone |
| `language` | `text` | `en` / `es` |
| `custom_domain` | `text` | Custom domain |
| `active_modes` | `json` | Active modes |

#### `sources`
| Column | Type | Description |
|---|---|---|
| `id` | `text PK` | UUID |
| `clone_id` | `text FK → clone_configs.id` | Owner clone |
| `type` | `enum` | `youtube`, `pdf`, `video`, `text`, `web`, `interview` |
| `title` | `text NOT NULL` | Source title |
| `url` | `text` | URL (YouTube/web) |
| `status` | `enum` | `uploading`, `processing`, `ready`, `error` |
| `metadata` | `json` | Metadata (silo, etc.) |

#### `chunks`
| Column | Type | Description |
|---|---|---|
| `id` | `text PK` | UUID |
| `source_id` | `text FK → sources.id` | Parent source |
| `content` | `text NOT NULL` | Chunk content |
| `embedding` | `vector` | Embedding (pgvector) |
| `metadata` | `json` | Additional metadata |

### 3.4.3 pgvector

The **pgvector** extension stores and searches embeddings directly in PostgreSQL:

```sql
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE chunks (
    id TEXT PRIMARY KEY,
    content TEXT NOT NULL,
    embedding vector(1536),
    metadata JSONB
);

CREATE INDEX ON chunks USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
```

Cosine distance search:
```sql
SELECT c.id, c.content, 
       1 - (c.embedding <=> $1::vector) AS score
FROM chunks c
JOIN sources s ON s.id = c.source_id
WHERE s.clone_id = $2
  AND 1 - (c.embedding <=> $1::vector) > 0.75
ORDER BY c.embedding <=> $1::vector
LIMIT 5;
```

## 3.5 Authentication and Authorization

### 3.5.1 NextAuth v5

Configured in `src/lib/auth.ts`:

```tsx
export const { handlers, auth, signIn, signOut } = NextAuth({
  session: { strategy: "jwt" },
  adapter: DrizzleAdapter(db, { tables }),
  providers: [
    Credentials({ /* email + password */ }),
    Resend({ /* magic link */ }),
    Google({ /* OAuth */ }),
  ],
  callbacks: { /* jwt, session */ },
});
```

### 3.5.2 Auth Providers

| Provider | Method | Status |
|---|---|---|
| **Credentials** | Email + password (bcrypt) | ✅ Implemented |
| **Resend** | Magic link email | ✅ Implemented |
| **Google** | OAuth 2.0 | ✅ Implemented |

### 3.5.3 Roles and Permissions

| Role | Access | Assigned by |
|---|---|---|
| `owner` | Full tenant control | Tenant creator |
| `admin` | Tenant management | Owner |
| `member` | Basic clone usage | Owner/Admin |
| `platform_admin` | Global admin panel | Environment variables |

### 3.5.4 Platform Admin

Authenticated via environment variables:

```env
PLATFORM_ADMIN_EMAIL=admin@example.com
PLATFORM_ADMIN_PASSWORD_HASH=$2a$12$...
```

## 3.6 RAG Pipeline

### 3.6.1 Pipeline Flow

```
                    ┌─────────────┐
                    │   Question  │
                    └──────┬──────┘
                           ▼
┌──────────────────────────────────────────┐
│     1. Generate embedding                │
│  OpenAI text-embedding-3-small           │
└──────────────────┬───────────────────────┘
                   ▼
┌──────────────────────────────────────────┐
│   2. Semantic search in pgvector         │
│      Cosine similarity, top-5           │
│      Threshold: 0.75                     │
└──────────────────┬───────────────────────┘
                   ▼
┌──────────────────────────────────────────┐
│   3. Build system prompt                 │
│   - Clone personality                    │
│   - Mode prompt                          │
│   - Creator memories                     │
│   - Relevant chunks                      │
└──────────────────┬───────────────────────┘
                   ▼
┌──────────────────────────────────────────┐
│   4. Generate response (LLM)             │
│   Anthropic Claude (primary)             │
│   OpenAI GPT-4o-mini (fallback)          │
└──────────────────┬───────────────────────┘
                   ▼
┌──────────────────────────────────────────┐
│   5. Post-processing                     │
│   - Confidence scoring                   │
│   - Gap detection (confidence < 0.7)     │
│   - Conversation logging                 │
└──────────────────────────────────────────┘
```

### 3.6.2 Chunking

| Parameter | Value | Description |
|---|---|---|
| Chunk size | ~500 tokens | Embedding fragments |
| Overlap | ~50 tokens | Overlap between chunks |
| Strategy | Semantic | Split by paragraphs/sentences |

### 3.6.3 Embeddings

- **Model**: `text-embedding-3-small` (OpenAI)
- **Dimensions**: 1536
- **Index**: IVFFlat with cosine distance
- **Search threshold**: > 0.75 (cosine similarity)

### 3.6.4 LLM Configuration

| Parameter | Value | Description |
|---|---|---|
| Primary provider | Anthropic Claude | Chat, generation |
| Embeddings provider | OpenAI | text-embedding-3-small |
| STT | OpenAI Whisper | Speech-to-text |
| Chat model | `claude-sonnet-4-20250514` | Quality/speed balance |
| Temperature | 0.7 | Creativity control |
| Max tokens | 4096 | Max response length |

## 3.7 Middleware and Proxy

### 3.7.1 Purpose

The middleware (`src/middleware.ts`) acts as a **reverse proxy** between the Next.js frontend and Flask backend:

1. **API proxy**: redirects `/api/*` requests to Flask (`http://127.0.0.1:5001`)
2. **Tenant detection**: identifies tenant by subdomain
3. **Service-to-service auth**: injects API key to backend requests

### 3.7.2 Route Mapping

```typescript
const ROUTE_MAP = {
  "/api/admin/overview": "/console/api/myownclone/admin/overview",
  "/api/admin/tenants": "/console/api/myownclone/admin/tenants",
  "/api/clones": "/console/api/myownclone/clones",
  "/api/plans": "/console/api/myownclone/plans",
  "/api/stripe/checkout": "/console/api/myownclone/stripe/checkout",
  "/api/inbox": "/console/api/myownclone/inbox",
  "/api/auth/login": "/console/api/auth/login",
};
```

## 3.8 Integrations

| Service | Purpose | Integration point |
|---|---|---|
| **Stripe** | Subscriptions, checkout, billing portal | `src/lib/stripe.ts` |
| **Resend** | Transactional emails (verification, confirmations) | `src/lib/email.ts` |
| **SendGrid** | Inbound email parse webhook | Backend Flask endpoint |
| **Whereby** | Embedded video calls | `src/lib/video.ts` |
| **Supabase Storage** | File storage (PDFs, images) | `src/lib/storage.ts` |
| **Upstash Redis** | Rate limiting | `@upstash/ratelimit` |
| **Sentry** | Error tracking | `NEXT_PUBLIC_SENTRY_DSN` |
| **PostHog** | Product analytics | `NEXT_PUBLIC_POSTHOG_KEY` |

---

# 4. Deployment Guide

## 4.1 Production Requirements

| Resource | Minimum | Recommended |
|---|---|---|
| **Server** | 2 vCPU, 4 GB RAM | 4 vCPU, 8 GB RAM |
| **Disk** | 20 GB SSD | 50 GB SSD |
| **PostgreSQL** | 15+ with pgvector | 15+ with pgvector |
| **Redis** | 7+ | 7+ |
| **Node.js** | 20 LTS | 20 LTS |
| **Python** | 3.11+ | 3.11+ |
| **Nginx** | 1.24+ | 1.24+ |

## 4.2 Docker Deployment

### Backend

```dockerfile
FROM python:3.11-slim
WORKDIR /app/api
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5001
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "api.app_factory:create_app()"]
```

```yaml
# docker-compose.backend.prod.yml
version: '3.8'
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: myownclone
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - pgdata:/var/lib/postgresql/data
  redis:
    image: redis:7-alpine
    command: redis-server --requirepass ${REDIS_PASSWORD}
  api:
    build: .
    environment:
      DATABASE_URL: postgresql://postgres:${DB_PASSWORD}@db:5432/myownclone
      REDIS_URL: redis://:${REDIS_PASSWORD}@redis:6379/0
    depends_on: [db, redis]
    ports: ["5001:5001"]
volumes:
  pgdata:
```

### Frontend

```bash
cd MyOwnClone
npm ci
npm run build
npm run start  # Port 3000
```

## 4.3 Nginx Reverse Proxy

```nginx
server {
    listen 443 ssl;
    server_name myownclone.com;

    ssl_certificate /etc/letsencrypt/live/myownclone.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/myownclone.com/privkey.pem;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
    }

    location /api/ {
        proxy_pass http://localhost:5001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 4.4 SSL with Let's Encrypt

```bash
apt install certbot python3-certbot-nginx
certbot --nginx -d myownclone.com -d *.myownclone.com
certbot renew --dry-run
```

## 4.5 Backup and Restore

```bash
# Backup
pg_dump -U postgres myownclone | gzip > myownclone_$(date +%Y%m%d).sql.gz

# Restore
gunzip -c myownclone_20260101.sql.gz | psql -U postgres myownclone

# Automated (cron)
0 3 * * * pg_dump -U postgres myownclone | gzip > /backups/myownclone_$(date +\%Y\%m\%d).sql.gz
```

## 4.6 Migration Strategy

### Drizzle (Frontend)
```bash
npm run db:generate   # Generate SQL migration files
npm run db:migrate    # Apply migrations (production)
npm run db:push        # Direct schema push (development)
```

### Alembic (Backend)
```bash
flask --app app_factory db migrate -m "description"
flask --app app_factory db upgrade
flask --app app_factory db downgrade
```

## 4.7 Scaling

### Vertical
- Increase server RAM/CPU
- Optimize PostgreSQL queries with indexes
- Increase IVFFlat index `lists` for better precision

### Horizontal
- Frontend: multiple Next.js instances behind Nginx (round-robin)
- Backend: multiple Gunicorn workers (`--workers=4 --threads=2`)
- Database: read replicas
- Cache: Redis cluster for distributed rate limiting

---

# 5. API Reference

## 5.1 Frontend API Routes

### Authentication
| Endpoint | Method | Auth | Description |
|---|---|---|---|
| `/api/auth/[...nextauth]` | `*` | No | NextAuth handlers |
| `/api/auth/session` | `GET` | Cookie | Get current session |
| `/api/csrf` | `GET` | No | Get CSRF token |

### Sources
| Endpoint | Method | Auth | Description |
|---|---|---|---|
| `/api/clone/sources` | `GET` | Session | List clone sources |
| `/api/clone/sources` | `POST` | Session | Create source (multipart) |

### Chat
| Endpoint | Method | Auth | Description |
|---|---|---|---|
| `/api/clone/{slug}/chat` | `POST` | No (public) | Send message, receive SSE stream |

### Analytics
| Endpoint | Method | Auth | Description |
|---|---|---|---|
| `/api/clone/analytics/overview` | `GET` | Session | Metrics overview |
| `/api/clone/inbox/list` | `GET` | Session | List inbox |
| `/api/clone/inbox/{id}/generate-draft` | `POST` | Session | Generate AI draft |

### Other
| Endpoint | Method | Auth | Description |
|---|---|---|---|
| `/api/bookings` | `POST/GET` | Mixed | Create/list bookings |
| `/api/stt` | `POST` | Session | Speech-to-text (Whisper) |
| `/widget.js` | `GET` | No | Embeddable widget script |
| `/api/deploy` | `POST` | API Key | Trigger frontend deploy |

## 5.2 Backend Endpoints (via Middleware Proxy)

### Console API
| Frontend Path | Backend | Method | Description |
|---|---|---|---|
| `/api/clone/clones` | `/console/api/myownclone/clones` | `GET/POST` | Clone CRUD |
| `/api/clone/analytics/overview` | `/console/api/myownclone/clones/{id}/analytics/overview` | `GET` | Overview |
| `/api/clone/memories` | `/console/api/myownclone/clones/{id}/memories` | `GET/POST` | Memories |
| `/api/clone/plans` | `/console/api/myownclone/plans` | `GET` | Plans |
| `/api/clone/billing` | `/console/api/myownclone/stripe/billing` | `POST` | Billing portal |
| `/api/clone/stripe/checkout` | `/console/api/myownclone/stripe/checkout` | `POST` | Checkout |

### Admin API
| Frontend Path | Backend | Method | Description |
|---|---|---|---|
| `/api/admin/overview` | `/console/api/myownclone/admin/overview` | `GET` | Admin metrics |
| `/api/admin/tenants` | `/console/api/myownclone/admin/tenants` | `GET` | List tenants |

### Public API (No auth)
| Endpoint | Method | Description |
|---|---|---|
| `/api/public/{slug}/chat` | `POST` | Widget chat |
| `/api/public/{slug}/bookings/availability` | `GET` | Available slots |

---

# 6. Troubleshooting

## 6.1 Common Issues

### Error: "Backend unavailable" (HTTP 502)
**Cause**: Middleware cannot reach the Flask backend.
```bash
curl http://localhost:5001/health
systemctl status myownclone-api
```

### Error: "DEFAULT_CLONE_ID not configured"
**Cause**: Missing `DEFAULT_CLONE_ID` environment variable.
```bash
INSERT INTO clone_configs (id, tenant_id, name, slug, language, is_active)
VALUES ('your-uuid', 'tenant-id', 'My Clone', 'my-clone', 'en', true);
echo "DEFAULT_CLONE_ID=your-uuid" >> .env.local
```

### PostgreSQL connection error
```bash
psql -U postgres -h localhost -d myownclone
docker ps | grep postgres
```

### OpenAI embedding error
```bash
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

### Chat not responding
```bash
curl http://localhost:5001/console/api/myownclone/clones
docker logs myownclone_api --tail 50
```

## 6.2 Logs and Debugging

### Frontend
```bash
npm run dev              # Development logs
pm2 logs myownclone       # Production logs
```

### Backend
```bash
flask --app app_factory run --debug       # Development
journalctl -u myownclone-api -f           # Production
docker logs myownclone_api --tail 100     # Docker
```

### Database
```sql
SELECT * FROM pg_stat_activity WHERE datname = 'myownclone';
SELECT * FROM pg_extension WHERE extname = 'vector';
```

## 6.3 Common Development Errors

| Error | Cause | Solution |
|---|---|---|
| `Module not found: Can't resolve @/...` | Path alias not configured | Check `tsconfig.json` paths |
| `bcryptjs error` | Node.js version mismatch | Use Node.js 18+ |
| `Port 3000 already in use` | Another process on port | `npx kill-port 3000` |
| `pgvector: extension not found` | pgvector not installed | `CREATE EXTENSION vector;` |
| Missing `"use client"` error | Client hook in Server Component | Add `"use client"` directive |

---

# 7. FAQ

## 7.1 User FAQ

### How do I train my clone?
Upload content (PDFs, URLs, text) from the **Library** section. The clone uses that content to answer questions. More content = more accurate responses.

### How long does it take to process a source?
Depends on size: a small PDF (~10 pages) processes in seconds. A 1-hour YouTube video can take 2-3 minutes.

### Can I customize my clone's tone?
Yes. From the clone settings you can define personality ("empathetic, technical, fun..."), tone ("formal, casual, professional..."), and language.

### What happens if my clone can't answer?
The system automatically detects questions your clone couldn't answer with enough confidence (gaps). You can review them in Analytics and add content to cover them.

### Can I use my own domain?
Yes. Pro and higher plans allow configuring a custom domain for the widget and public clone page.

### Are there message limits?
Each plan has daily conversation and monthly email limits. Limits are shown on the pricing page and dashboard.

## 7.2 Developer FAQ

### How do I embed the clone on my website?
Use the embeddable widget:
```html
<script src="https://yourdomain.com/widget.js" data-clone="slug-of-clone"></script>
```

### Can I access the API directly?
Yes. From Settings you can generate API keys to access clone endpoints programmatically.

### What LLM models are used?
- **Primary chat**: Anthropic Claude (Sonnet)
- **Embeddings**: OpenAI text-embedding-3-small
- **Speech-to-text**: OpenAI Whisper

### How does multi-tenancy work?
Each client (tenant) has their own data isolated by `tenant_id` in all tables. Identification is by subdomain (tenant1.myownclone.com → Tenant 1).

### Where are files stored?
Files (PDFs, images) are stored in **Supabase Storage**. Public URLs are generated automatically after upload.

### Are there tests?
Yes:
- **Frontend**: Vitest + React Testing Library (`npm test`)
- **Backend**: pytest (`pytest tests/ -v`)

---

<p align="center">
  <strong>MyOwnClone</strong> — Multiply Yourself
  <br />
  <a href="../README.md">Back to README</a>
</p>
