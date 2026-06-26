---
title: "Nuevos Hallazgos de la Investigación myownclone (Mayo 2026)"
created: 2026-05-25
updated: 2026-05-25
type: research-update
tags: [myownclone, investigation, js-bundles, onboarding, competitors]
sources: [myownclone_chunks/, myownclone_login.html, myownclone_contacto.html, myownclone_registro.html]
confidence: high
---

# Nuevos Hallazgos — Mayo 2026

## 1. Módulos Internos Confirmados (de bundles JS)

Del análisis de 15 bundles JS (~1.2 MB) de myownclone.com se extrajo la estructura completa de módulos:

### Admin Platform (backoffice multi-tenant de myownclone)

| Módulo | Descripción |
|--------|-------------|
| `AdminPlatformResumen` | Dashboard con MRR, costes Anthropic+OpenAI+email, gráficos, métricas |
| `AdminPlatformTenants` | CRUD tenants, invitaciones, cortesías, trials Stripe, impersonación (30 min) |
| `AdminPlatformInbox` | Bandeja global (*@myownclone.com), etiquetas, estados |
| `AdminPlatformSpam` | Lista negra de dominios spam |
| `AdminPlatformFeedback` | Gestión de feedback y screenshots de usuarios |
| `AdminPlatformFaqs` | FAQs de la plataforma |
| `AdminImpersonationBanner` | Banner de suplantación de tenant en modo soporte |

### Tenant App (lo que ve cada creador)

| Módulo | Descripción |
|--------|-------------|
| `Onboarding` | Flujo completo: subdominio → contenido → voz → publicar |
| `Brain` | CRUD memorias, firma email, plantillas, dominios spam, dominio inbound |
| `Triage` | IA lee inbox, propone drafts en voz del creador, voice-to-text, one-click send |
| `PublicBooking` | Calendario público, videollamada integrada, ICS/Google/Outlook/Apple |
| `MyBooking` | Vista de reserva con videollamada en myownclone, cancelación |
| `PublicRecording` | Grabación con transcripción + chat con clon IA contextual |
| `FeedbackWidget` | Widget de feedback con screenshots (Ctrl+V) |
| `PublicFooter` | Footer legal multi-idioma |
| `CookieBanner` | Banner cookies (solo necesarias) |

---

## 2. Flujo de Registro y Onboarding

**Estado actual**: BETA CERRADA. `/registro` redirige a `/contacto`. Incorporación manual caso por caso.

### Flujo completo cuando está abierto:

```
/registro → Stripe Checkout → /registro/exito → /registro/onboarding
```

**Paso 1 - Registro (2 pasos)**:
- Email, nombre, subdominio (`tunombre.myownclone.com`, validación en tiempo real)
- Aceptación de términos + privacidad
- Opción Google OAuth
- Planes visibles: Pro, Scale, Enterprise (precios dinámicos `€{price}`)
- Badge "Acceso Beta" con precio bloqueado de por vida

**Paso 2 - Stripe Checkout**: Tarjeta obligatoria, facturación mensual, sin permanencia.

**Paso 3 - Éxito**: Código mágico de 6 dígitos por email para verificar.

**Paso 4 - Onboarding**:
- Nombre del clon + subdominio
- Encuesta: ¿dónde nos conociste? (X, YouTube, Instagram, LinkedIn, Podcast, Newsletter, Recomendación, Google, Anuncio, Otro)
- Encuesta: ¿para qué usarás myownclone? (Atender alumnos, Capturar leads, Recomendar productos, Soporte automático, Q&A, Otro)

### Auth
- **Magic link** (código 6 dígitos) — método principal
- **Google OAuth** — alternativa
- Manejo de errores: email inválido, código incorrecto, código caducado, Google cancelado, email no verificado, cuenta sin tenant, pago requerido

---

## 3. Stack Confirmado (Actualizado)

| Componente | Tecnología | Confirmación |
|-----------|-----------|-------------|
| **Framework** | Next.js 16.2.4 (App Router) | RSC payload + `__next_f` |
| **Hosting** | Vercel (cdg1::iad1) | `x-vercel-id` headers |
| **Auth** | Magic link propio + Google OAuth | RSC payload auth strings |
| **DB** | Neon (PostgreSQL serverless) | Aviso legal |
| **Vector DB** | PGvector | Inferido (extensión Neon) |
| **LLMs** | Anthropic Claude + OpenAI | Cost tracking strings |
| **Embeddings** | OpenAI (text-embedding-3) | Inferido |
| **Pagos** | Stripe (Checkout + Subscriptions + Portal) | Strings i18n |
| **Error tracking** | Sentry (org: 4511315838173184) | JS bundles |
| **Analytics** | PostHog (eu.i.posthog.com) | JS bundles |
| **i18n** | next-intl (ES + EN) | Routing por locale |
| **Fuentes** | Poppins + JetBrains Mono (woff2) | next/font |

---

## 4. Competidores (Ver detalle completo)

Ver [[comparisons/myownclone-competitors]]

- **Personify** (⭐⭐⭐⭐ 80% similitud) — El competidor más directo. Coaches + cursos.
- **Coachvox AI** (⭐⭐⭐ 60%) — WordPress, más simple, lead gen.
- **Cpycat** (⭐⭐ 40%) — Digital twin B2C, no B2B.

**Conclusión**: mercado poco competido. Solo Personify compite de verdad.

---

## 5. Euge Oller — Perfiles Encontrados

- **LinkedIn**: es.linkedin.com/in/eugeniooller
- **LinkedIn (alt)**: es.linkedin.com/in/eugenio-josé-oller-valencia-a4a23581
- **Delphi original**: delphi.ai/euge-oller (su clon pre-myownclone)
- **Empresa**: Marea Kiss LLC, Wyoming
- **Proyecto anterior**: Emprenda Aprendiendo (infoproductos)

---

## Archivos generados en esta ronda

- `/home/haxth3/myownclone_chunks/` — 15 bundles JS (~1.2 MB)
- `/home/haxth3/myownclone_main.html` — HTML de la home
- `/home/haxth3/myownclone_login.html` — HTML del login
- `/home/haxth3/myownclone_contacto.html` — HTML del contacto
- `/home/haxth3/myownclone_registro.html` — HTML del registro (redirige a /contacto)
- `/home/haxth3/myownclone_onboarding.html` — HTML del onboarding (skeleton vacío)
- `/home/haxth3/wiki/comparisons/myownclone-competitors.md` — Análisis de competidores
