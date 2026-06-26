---
title: "MyClone.is - Deep Technical OSINT (API & Architecture)"
source: api.myclone.is OpenAPI spec + live API testing
date: 2026-06-24
tags: [osint, myclone-is, api, backend, voice-ai, rag]
entities: [myclone-is]
confidence: high
---

# MyClone.is — Deep Technical OSINT

## API Architecture

### Base URL
```
https://api.myclone.is
```
- **Backend**: Python + Uvicorn (ASGI)
- **Hosting**: AWS (IP range 54.208.x.x / 3.86.x.x, Amazon RSA 2048 M01 cert)
- **Total documented endpoints**: 227 (OpenAPI 1.0.0)
- **Auth method**: JWT Bearer tokens

### Authentication Flow
```bash
POST /api/v1/auth/login
Body: {"email": "...", "password": "..."}
Response: {"message":"Login successful","user_id":"...","token":"eyJhbG...","account_type":"creator"}
```

**Token JWT Payload (decoded)**:
```json
{
  "sub": "2021aa30-cdf1-465b-98d6-03896a252861",
  "email": "xoyigo3386@disiok.com",
  "fullname": "astalavista",
  "account_type": "creator",
  "exp": <epoch>
}
```

### User Account (test credentials used)
```json
{
  "id": "2021aa30-cdf1-465b-98d6-03896a252861",
  "email": "xoyigo3386@disiok.com",
  "username": "astalavista",
  "fullname": "astalavista",
  "email_confirmed": true,
  "onboarding_status": "FULLY_ONBOARDED",
  "account_type": "creator",
  "created_at": "2026-06-23T22:26:40.393184Z"
}
```

## Complete Endpoint Map (227 paths)

### Auth (`/api/v1/auth/`)
| Method | Path | Auth |
|--------|------|------|
| POST | /auth/login | No |
| POST | /auth/register | No |
| POST | /auth/logout | Yes |
| POST | /auth/forgot-password | No |
| POST | /auth/reset-password | No |
| POST | /auth/set-password | Yes |
| POST | /auth/verify-email | No |
| POST | /auth/request-otp | No |
| POST | /auth/resend-verification | No |
| POST | /auth/verify-otp | No |
| GET | /auth/google/login | No |
| GET | /auth/google/callback | No |
| GET | /auth/linkedin/login | No |
| GET | /auth/linkedin/callback | No |
| POST | /auth/linkedin/logout | Yes |
| GET | /auth/linkedin/verify | Yes |

### Users (`/api/v1/users/`)
| Method | Path | Auth |
|--------|------|------|
| GET | /users/me | Yes |
| PATCH | /users/me | Yes |
| POST | /users/me/avatar | Yes |
| DELETE | /users/me/avatar | Yes |
| GET | /users/check-username/{username} | No |
| POST | /users/expert/onboarding | Yes |
| POST | /users/linkedin/search | Yes |
| GET, POST | /users/me/email-domains | Yes |
| GET, PATCH, DELETE | /users/me/email-domains/{domain_id} | Yes |
| POST | /users/me/email-domains/{domain_id}/verify | Yes |
| GET, POST | /users/me/visitors | Yes |
| PATCH, DELETE | /users/me/visitors/{visitor_id} | Yes |
| GET, POST | /users/me/widget-tokens | Yes |
| DELETE | /users/me/widget-tokens/{token_id} | Yes |
| GET, PUT | /users/me/widget-config | Yes |
| GET | /users/{user_id}/conversations | Yes |
| POST | /users/{user_id}/regenerate-claim-code | Yes |

### Personas (`/api/v1/personas/`)
| Method | Path | Auth |
|--------|------|------|
| GET | /personas/users/{user_id}/personas | Yes |
| GET | /personas/{persona_id} | Yes |
| DELETE | /personas/{persona_id} | Yes |
| GET | /personas/check-persona-name?name= | No |
| GET | /personas/generate_communication_style | Yes |
| GET | /personas/generate_persona_expertise | Yes |
| GET | /personas/generate_persona_intro | Yes |
| GET | /personas/username/{username}/check-access | Yes |
| POST | /personas/username/{username}/init-session | Yes |
| POST | /personas/username/{username}/request-access | Yes |
| POST | /personas/username/{username}/verify-access | Yes |
| POST | /personas/username/{username}/save-voice-transcript | Yes |
| POST | /personas/username/{username}/stream-chat | Yes |
| POST | /personas/username/{username}/special-stream-chat | Yes |
| GET | /personas/username/{username}/voice-conversations/{session_token} | Yes |
| POST | /personas/with-knowledge | Yes |
| GET, PATCH | /personas/{persona_id}/with-knowledge | Yes |
| GET | /personas/{persona_id}/knowledge-sources | Yes |
| GET | /personas/{persona_id}/knowledge-sources/available | Yes |
| POST | /personas/{persona_id}/knowledge-sources | Yes |
| DELETE | /personas/{persona_id}/knowledge-sources/{source_record_id} | Yes |
| PATCH | /personas/{persona_id}/knowledge-sources/{source_record_id}/toggle | Yes |
| GET | /personas/{persona_id}/conversations | Yes |
| GET, POST | /personas/{persona_id}/visitors | Yes |
| DELETE | /personas/{persona_id}/visitors/{visitor_id} | Yes |
| PATCH | /personas/{persona_id}/access-control | Yes |
| GET, PATCH | /personas/{persona_id}/summary-email | Yes |
| POST, DELETE | /personas/{persona_id}/avatar | Yes |
| PATCH | /personas/{persona_id}/voice | Yes |

### Chat/Conversations (`/api/v1/`)
| Method | Path | Auth |
|--------|------|------|
| GET | /conversations/{conversation_id} | Yes |
| GET | /conversations/{conversation_id}/attachments | Yes |
| GET | /conversations/{conversation_id}/summary | Yes |
| GET | /sessions/{session_token}/status | Yes |
| POST | /sessions/{session_token}/capture-lead | Yes |
| POST | /sessions/{session_token}/provide-email | Yes |
| POST | /sessions/{session_token}/refresh-index | Yes |
| POST | /sessions/{session_token}/upload-attachment | Yes |
| POST | /sessions/{session_token}/upload-pdf | Yes |
| GET | /sessions/{session_token}/attachments | Yes |

### Knowledge / RAG (`/api/v1/`)
| Method | Path | Auth |
|--------|------|------|
| GET | /knowledge-library/users/{user_id} | Yes |
| GET, DELETE | /knowledge-library/{source_type}/{source_id} | Yes |
| POST | /documents/add | Yes |
| POST | /documents/add-text | Yes |
| GET | /documents/{user_id} | Yes |
| DELETE | /documents/{document_id} | Yes |
| POST | /documents/refresh | Yes |
| POST | /documents/process-pdf-data | Yes |
| GET | /documents/check-embeddings/{user_id}/{document_id} | Yes |

### Embeddings (`/api/v1/embeddings/`)
| Method | Path | Auth |
|--------|------|------|
| GET | /embeddings/stats | Yes |
| POST | /embeddings/migrate | Yes |
| POST | /embeddings/fix-voyage-metadata | Yes |

**Embeddings stats (platform-wide)**:
```json
{"voyage_embeddings": 96891, "total_embeddings": 96891}
```

### Voice (`/api/v1/voice-clones/`, `/cartesia/`, `/eleven_labs/`)
| Method | Path | Auth |
|--------|------|------|
| GET | /voice-clones/health | Yes |
| GET | /voice-clones/users/{user_id} | Yes |
| GET | /voice-clones/users/{user_id}/platform/{platform} | Yes |
| DELETE | /voice-clones/{voice_id} | Yes |
| POST | /cartesia/create_voice_clone | Yes |
| POST | /cartesia/create_voice_clone_from_paths | Yes |
| POST | /cartesia/create_voice_clone_from_s3 | Yes |
| GET | /cartesia/users/{user_id}/voice-clones | Yes |
| DELETE | /cartesia/voice-clones/{voice_id} | Yes |
| POST | /eleven_labs/create_voice_clone | Yes |
| POST | /eleven_labs/create_voice_clone_from_paths | Yes |
| POST | /eleven_labs/create_voice_clone_from_s3 | Yes |
| GET | /eleven_labs/users/{user_id}/voice-clones | Yes |
| DELETE | /eleven_labs/voice/{voice_id} | Yes |
| DELETE | /eleven_labs/voice/by-username/{username} | Yes |
| PATCH | /persona/{persona_id}/voice | Yes |
| PATCH | /expert/{username}/voice | Yes |

### Real-time Voice (`/api/v1/livekit/`)
| Method | Path | Auth |
|--------|------|------|
| POST | /livekit/connection-details | Yes |
| POST | /livekit/session/{session_id}/heartbeat | Yes |

### Prompt Engineering (`/api/v1/prompt/`, `/prompt-templates/`)
| Method | Path | Auth |
|--------|------|------|
| POST | /prompt/create-advanced-prompt | Yes |
| POST | /prompt/create-prompt-for-persona | Yes |
| POST | /prompt/update-prompt-for-persona | Yes |
| GET | /prompt/list-active-prompts | Yes |
| GET | /prompt/persona-prompts/{persona_id} | Yes |
| PUT | /prompt/persona-prompts/{persona_id} | Yes |
| GET | /prompt/persona-prompts/{persona_id}/compare | Yes |
| GET | /prompt/persona-prompts/{persona_id}/history | Yes |
| GET | /prompt/persona-prompts/{persona_id}/history/{version} | Yes |
| POST | /prompt/persona-prompts/{persona_id}/restore/{version} | Yes |
| GET | /prompt/persona-prompts/{persona_id}/timeline | Yes |
| GET | /prompt/persona-prompts/{persona_id}/versions | Yes |
| GET | GET | /prompt/persona-prompts-all | Yes |
| GET, POST | /prompt-templates/ | Yes |
| GET | /prompt-templates/{template_id} | Yes |
| PATCH | /prompt-templates/update-parameter | Yes |
| PATCH | /prompt-templates/{template_id}/deactivate | Yes |
| POST | /langfuse/prompts/compile | Yes |
| POST | /langfuse/prompts/create | Yes |
| GET | /langfuse/prompts/get/{prompt_name} | Yes |
| GET | /langfuse/prompts/list | Yes |
| PUT | /langfuse/prompts/update/{prompt_name} | Yes |

### Workflows BETA (`/api/v1/workflows/`, `/workflow-templates/`)
| Method | Path | Auth |
|--------|------|------|
| GET | /workflow-templates | No |
| GET | /workflow-templates/{template_id} | Yes |
| POST | /workflow-templates/enable | Yes |
| PUT | /workflow-templates/workflows/{workflow_id}/customize | Yes |
| POST | /workflow-templates/workflows/{workflow_id}/sync | Yes |
| GET | /workflow-templates/workflows/{workflow_id}/sync-status | Yes |
| POST, GET | /workflows | Yes |
| POST, GET | /workflows/sessions | Yes |
| GET | /workflows/sessions/{session_id} | Yes |
| POST | /workflows/sessions/{session_id}/abandon | Yes |
| POST | /workflows/sessions/{session_id}/answer | Yes |
| GET, PATCH, DELETE | /workflows/{workflow_id} | Yes |
| GET | /workflows/{workflow_id}/analytics | Yes |
| POST | /workflows/{workflow_id}/publish | Yes |
| POST | /workflows/{workflow_id}/regenerate-objective | Yes |

### Scraping / Data Ingestion (`/api/v1/scraping/`)
| Method | Path | Auth |
|--------|------|------|
| POST | /scraping/linkedin | Yes |
| POST | /scraping/twitter | Yes |
| POST | /scraping/website | Yes |
| POST | /scraping/auto-onboard | Yes |
| POST | /scraping/bulk-onboard | Yes |
| GET | /scraping/status/{user_id} | Yes |
| GET | /scraping/audit/{job_id} | Yes |
| GET | /ingestion/expert-status/{username} | Yes |
| GET | /ingestion/expert-status-stream/{username} | Yes |
| GET | /ingestion/persona/{persona_id}/data-sources | Yes |

### Voice Processing (`/api/v1/voice-processing/`)
| Method | Path | Auth |
|--------|------|------|
| GET | /voice-processing/health | Yes |
| POST | /voice-processing/upload | Yes |
| POST, GET | /voice-processing/jobs | Yes |
| GET, DELETE | /voice-processing/jobs/{job_id} | Yes |
| GET | /voice-processing/jobs/{job_id}/progress | Yes |
| POST | /voice-processing/jobs/{job_id}/retry | Yes |
| GET | /voice-processing/stats | Yes |
| POST | /voice-processing/ingest-youtube | Yes |
| GET | /voice-processing/youtube/{user_id} | Yes |
| DELETE | /voice-processing/youtube/{youtube_video_id} | Yes |
| GET | /voice-processing/youtube/check-embeddings/{user_id}/{youtube_video_id} | Yes |
| POST | /voice-processing/youtube/refresh | Yes |

### Stripe Payments (`/api/v1/stripe/`)
| Method | Path | Auth |
|--------|------|------|
| POST | /stripe/checkout/persona-access | Yes |
| POST | /stripe/checkout/platform-subscription | Yes |
| GET | /stripe/personas/{persona_id}/access | Yes |
| GET | /stripe/personas/{persona_id}/connect/dashboard | Yes |
| POST | /stripe/personas/{persona_id}/connect/onboard | Yes |
| POST, PUT, DELETE, GET | /stripe/personas/{persona_id}/monetization | Yes |
| PATCH | /stripe/personas/{persona_id}/monetization/status | Yes |

### Tier / Plans (`/api/v1/tier/`)
| Method | Path | Auth |
|--------|------|------|
| GET | /tier/plans | No |
| GET, POST | /tier/plans | Yes |
| PUT, DELETE | /tier/plans/{tier_id} | Yes |
| GET | /tier/subscription | Yes |
| GET | /tier/usage | Yes |
| GET | /tier/usage/{user_id} | Yes |
| POST | /tier/usage/{user_id}/refresh | Yes |

### Custom Domains / Whitelabel (`/api/v1/custom-domains/`)
| Method | Path | Auth |
|--------|------|------|
| GET, POST | /custom-domains | Yes |
| GET | /custom-domains/lookup/{domain} | No |
| GET, DELETE | /custom-domains/{domain_id} | Yes |
| POST | /custom-domains/{domain_id}/verify | Yes |

### Webhooks (`/api/v1/account/webhook/`, `/webhooks/`)
| Method | Path | Auth |
|--------|------|------|
| POST, GET, PATCH, DELETE | /account/webhook | Yes |
| GET | /account/webhook/health | Yes |
| POST | /webhooks/stripe | No |

### Integrations
| Method | Path | Auth |
|--------|------|------|
| POST | /claim/submit | No |
| POST | /claim/verify-code | No |
| POST | /claim/check-username | No |
| POST | /claim/get-link | No |
| POST | /waitlist | No |
| POST | /appsumo/activate-license | No |
| GET | /appsumo/health | No |
| GET | /appsumo/tier-mappings | No |
| POST | /appsumo/webhook | No |

## Internal Services (Discovered from API)

### Voyage AI Embeddings
- **Total platform embeddings**: 96,891
- **Provider**: Voyage AI (voyage-embeddings)
- Used for RAG knowledge vectorization

### Langfuse (Prompt Engineering & Observability)
Endpoints suggest heavy use of Langfuse for:
- Prompt versioning and history
- A/B testing prompts
- LLM evaluation (custom eval llama-rag, llm-judge, etc.)
- Dataset creation from traces
- Prompt compilation

### Voice Providers
1. **Cartesia AI** — `api.myclone.is/api/v1/cartesia/*`
   - Voice clone creation from audio/paths
2. **ElevenLabs** — `api.myclone.is/api/v1/eleven_labs/*`
   - Voice clone creation and management
3. **LiveKit** — real-time voice sessions

### Vercel AI SDK
- Streaming endpoint (`text/event-stream` for `stream-chat`)
- Confirmed by the SSE (Server-Sent Events) response format

### Stripe Connect
- Platform subscription (SaaS)
- Per-persona monetization (creators can charge for access)
- Connect onboarding for creators

## Prompt Template System (Critical for MyOwnClone)

The platform has a sophisticated prompt engineering system:

### Default Prompt Template Structure
```
# Expert Digital Persona System Instructions

You are {name}, {role} at {company}, {description}...

## Core Identity & Expertise
**Professional Background:** {introduction}
**Primary Expertise Areas:** {area_of_expertise}
**Communication Objective:** {chat_objective}

## Behavioral Framework
- Stateful Interaction (uses full conversation history)
- Progressive Disclosure (starts with assessment questions)
- Solution Reasoning (gathers data before recommending)
- Evidence-Based Responses (references past context)

## Expertise Boundaries
{trigger topics, out-of-scope handling}

## Communication Style
{practical + authentic | systems thinking | story-driven | signature patterns}

## Response Structure
1. Assessment Phase: targeted questions
2. Information Gathering: progressive disclosure
3. Solution Reasoning: analysis
4. Recommendation Delivery: actionable advice
5. Experience Integration: analogies

## Conversation Guidelines
- Tone: expert directness + casual/natural
- Start with single discovery question
- Ask follow-up questions building on previous answers
- Reference specific methodologies/frameworks
- Conclude with next steps
- NO markdown formatting in responses
- Human-like, friendly, casual tone
```

### Prompt Versioning
- Every prompt change creates a versioned history
- Can restore any previous version
- Timeline view of prompt evolution
- Compare prompt versions side-by-side

## Chat Streaming Architecture

### Init Session
```bash
POST /api/v1/personas/username/{username}/init-session
Response: {
  "session_token": "uuid",
  "persona_id": "uuid",
  "persona_name": "default",
  "is_anonymous": true
}
```

### Stream Chat (SSE)
```bash
POST /api/v1/personas/username/{username}/stream-chat
Accept: text/event-stream
Body: {"message": "...", "session_token": "uuid"}

Response (SSE):
data: {"type": "content", "chunk": "response text..."}
data: {"type": "complete", "session_token": "uuid"}
```

### Lead Capture
After conversation, can capture email:
```bash
POST /api/v1/sessions/{session_token}/capture-lead
Body: {"email": "...", "full_name": "..."}
```

## Free Plan Limits (Verified via API)
```json
{
  "tier": "free",
  "raw_text": {"files": {"used": 0, "limit": 5}, "storage": {"used_mb": 0, "limit_mb": 50}},
  "documents": {"files": {"used": 0, "limit": 3}, "storage": {"used_mb": 0, "limit_mb": 150}},
  "multimedia": {"files": {"used": 0, "limit": 3}, "storage": {"used_mb": 0, "limit_mb": 500}, "duration": {"used_hours": 0, "limit_hours": 1}},
  "youtube": {"videos": {"used": 0, "limit": 5}, "duration": {"used_hours": 0, "limit_hours": 2}},
  "voice": {"minutes_used": 0, "minutes_limit": 10, "reset_date": "2026-07-01T00:00:00+00:00"},
  "text": {"messages_used": 0, "messages_limit": 500, "reset_date": "2026-07-01T00:00:00+00:00"},
  "personas": {"used": 1, "limit": 2}
}
```

## Widget System

### Widget Token Structure
```json
{
  "id": "uuid",
  "token": "wgt_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "name": "Token Name",
  "description": "...",
  "created_at": "ISO8601",
  "last_used_at": null,
  "is_active": true
}
```

### Widget Config (Full)
```json
{
  "width": "900px",
  "height": "820px",
  "offsetX": "20px",
  "offsetY": "20px",
  "position": "bottom-right",
  "textColor": "#4c6eb8",
  "bubbleSize": "60px",
  "bubbleText": "Chat with me",
  "showAvatar": true,
  "enableVoice": true,
  "headerTitle": "",
  "personaName": "default",
  "borderRadius": "16px",
  "botMessageBg": "#ffffff",
  "chatbotStyle": "guide",
  "chatbotWidth": "420px",
  "primaryColor": "#f59e0b",
  "showBranding": true,
  "simpleBubble": false,
  "chatbotHeight": "700px",
  "modalPosition": "bottom-right",
  "userMessageBg": "#3b82f6",
  "welcomeMessage": "Hello! How can I help you?",
  "backgroundColor": "#fff4eb",
  "bubbleTextColor": "#ffffff",
  "headerBackground": "rgba(255, 255, 255, 0.8)",
  "textSecondaryColor": "#374151",
  "botMessageTextColor": "#1f2937",
  "userMessageTextColor": "#ffffff",
  "bubbleBackgroundColor": "#f59e0b"
}
```

## MyOwnClone Comparative Analysis

### What MyClone does better:
1. **Workflows BETA** — industry-specific conversation flows (CPA, Tax, Insurance)
2. **Per-persona monetization** via Stripe Connect
3. **LiveKit real-time voice** — video/audio calls
4. **Langfuse integration** — full prompt observability and A/B testing
5. **Visitor management** — track leads per persona
6. **Custom domains** — full whitelabel
7. **Prompt versioning** — timeline + restore

### What MyOwnClone can replicate:
1. Complete auth system (credentials + OAuth)
2. Knowledge library with multi-source scraping
3. Voice cloning (Cartesia + ElevenLabs)
4. RAG pipeline with Voyage embeddings
5. Widget embed system
6. Session-based chat with SSE streaming
7. Lead capture and email collection
8. Prompt template system

### Key API Gaps (MyOwnClone missing):
1. `/workflows/*` — conversation flows with objectives
2. `/langfuse/*` — prompt engineering and evaluation
3. `/livekit/*` — real-time voice
4. `/stripe/personas/*/monetization` — creator payments
5. `/custom-domains/*` — whitelabel
6. `/visitors/*` — lead management
7. `/voice-processing/*` with YouTube ingestion
8. Prompt version history and comparison
