# Auditoria — Frontend, App Router y UX (TASK-360-03)

## Resumen
- **Estado:** Amarillo — Funcional pero con carencias significativas en i18n, estados de carga/error y metadata SEO
- **Riesgo principal:** Cero uso de next-intl (strings hardcodeadas en todas las paginas), sin `loading.tsx`/`error.tsx` en ninguna ruta, sin metadata por pagina
- **Veredicto prod:** Apto para MVP pero requiere Fase i18n + estados de UI antes de escalar

## Mapa de estado actual

| Componente | Existe | Completo | Evidencia |
|---|---|---|---|
| App Router estructura | ✅ | ~85% | 44 paginas en dashboard, admin, public, auth |
| Layouts (root, dashboard, admin, public) | ✅ | 4/4 | `layout.tsx` en cada grupo de ruta |
| loading.tsx | ❌ | 0/44 | Ningun grupo de ruta tiene loading state |
| error.tsx | ❌ | 0/44 | Ningun grupo de ruta tiene error boundary |
| metadata por pagina | ❌ | 0/44 | Solo root layout tiene `<title>` y `<meta>` |
| API Routes | ✅ | ~75% | 10 endpoints, auth variado, sin validacion Zod |
| i18n (useTranslations) | ❌ | 0/44 | next-intl instalado pero no usado |
| Componentes UI genericos | ✅ | ~90% | EmptyState, ErrorState, LoadingState, Modal, Sheet, etc. |
| Server Components | ⚠️ | ~30% | 22/22 dashboard pages son `"use client"` — todas son CSR |
| Tests frontend | ✅ | ~60% | 71 tests vitest segun coordinacion |

## Hallazgos priorizados

| ID | Prioridad | Hallazgo | Impacto | Evidencia | Recomendacion |
|---|---|---|---|---|---|
| F03-001 | P1 | Cero uso de next-intl en componentes | Toda la UI tiene strings hardcodeadas en ingles/espanol mezclados | `grep -r "useTranslations" src/` = 0 resultados; `en.json` existe pero no se importa en ningun componente | Adoptar `useTranslations()` en todos los componentes; empezar por los mas visibles (sidebar, landing, login) |
| F03-002 | P1 | Sin loading.tsx ni error.tsx en ninguna ruta | Usuarios ven pantalla en blanco durante carga o errores no controlados | `find src/app -name "loading.tsx"` = vacio; `find src/app -name "error.tsx"` = vacio | Añadir `loading.tsx` y `error.tsx` a dashboard, admin, y grupos publicos |
| F03-003 | P1 | Ninguna pagina exporta metadata | SEO nulo, Open Graph ausente, sin compartir en redes | `grep -r "export.*metadata" src/app/` — solo root layout tiene | Añadir `generateMetadata()` en landing, login, registro, dashboard pages |
| F03-004 | P2 | 22/22 dashboard pages son Client Components | Perdida de beneficios SSR, JS bundle mas grande, peor LCP | `grep '"use client"' src/app/\(dashboard\)/*/page.tsx` = todas | Migrar a Server Components donde no haya interactividad; solo usar `"use client"` cuando se necesite useState/useEffect |
| F03-005 | P2 | Textos del Command Center desalineados | "build or query / endpoints / schema design" no refleja el producto | `resumen/page.tsx:190-207` | Aplicar `.docs_md/DASHBOARD_MESSAGING_PLAN.md` Fase 1 |
| F03-006 | P2 | Sidebar labels confusas | Search/Crawl/Extract/Research no describen la funcionalidad real | `dashboard/layout.tsx:21-29` | Renombrar: Search→Knowledge, Crawl→Memories, Extract→Inbox, Research→Products |
| F03-007 | P2 | API Routes sin validacion de input | Riesgo de inyeccion y errores 500 no controlados | `api/clone/sources/route.ts`, `api/bookings/route.ts` — sin Zod ni parse | Añadir validacion con Zod en todas las API Routes |
| F03-008 | P3 | SignOutButton con texto hardcodeado en español | Inconsistente con el resto de la UI en ingles | `components/auth/SignOutButton.tsx:37-48` — "Cerrar sesion", "Saliendo…" | Traducir a ingles o hacer i18n-ready |
| F03-009 | P3 | Onboarding no redirige automaticamente | Usuarios nuevos van a /resumen sin clone creado | `register-form.tsx` redirige a `/resumen`, no a `/onboarding` | Considerar redirect a `/onboarding` si usuario tiene 0 clones |
| F03-010 | P3 | Sin tests E2E de flujos criticos | No se puede validar login, creacion de fuente o chat automaticamente | `e2e/` existe con setup pero sin tests de flujos completos segun coordinacion | Priorizar E2E: login → dashboard → crear fuente → chat |

## Matriz de interconexion

### Paginas del Dashboard

| Ruta | Pagina | Layout | loading.tsx | error.tsx | Metadata | i18n | Auth | Backend dependency |
|---|---|---|---|---|---|---|---|---|
| `/resumen` | dashboard | ✅ | ❌ | ❌ | ❌ | ❌ | Session | Flask analytics + inbox |
| `/biblioteca` | dashboard | ✅ | ❌ | ❌ | ❌ | ❌ | Session | Flask sources |
| `/biblioteca/nuevo` | dashboard | ✅ | ❌ | ❌ | ❌ | ❌ | Session | Flask sources |
| `/cerebro` | dashboard | ✅ | ❌ | ❌ | ❌ | ❌ | Session | Flask memories |
| `/inbox` | dashboard | ✅ | ❌ | ❌ | ❌ | ❌ | Session | Flask inbox |
| `/productos` | dashboard | ✅ | ❌ | ❌ | ❌ | ❌ | Session | Flask products |
| `/analiticas` | dashboard | ✅ | ❌ | ❌ | ❌ | ❌ | Session | Flask analytics |
| `/facturacion` | dashboard | ✅ | ❌ | ❌ | ❌ | ❌ | Session | Stripe (stripe.ts eliminado) |
| `/configuracion` | dashboard | ✅ | ❌ | ❌ | ❌ | ❌ | Session | — |
| `/reuniones` | dashboard | ✅ | ❌ | ❌ | ❌ | ❌ | Session | Flask booking + Whereby |
| `/registro` | dashboard | ✅ | ❌ | ❌ | ❌ | ❌ | No | NextAuth |

### Paginas del Admin

| Ruta | Pagina | Layout | loading.tsx | error.tsx | Metadata | i18n | Auth | Backend dependency |
|---|---|---|---|---|---|---|---|---|
| `/admin/resumen` | admin | ✅ | ❌ | ❌ | ❌ | ❌ | platform_admin | Flask admin overview |
| `/admin/tenants` | admin | ✅ | ❌ | ❌ | ❌ | ❌ | platform_admin | Flask admin tenants |
| `/admin/tenants/[id]` | admin | ✅ | ❌ | ❌ | ❌ | ❌ | platform_admin | Flask admin tenant |
| `/admin/audit` | admin | ✅ | ❌ | ❌ | ❌ | ❌ | platform_admin | Flask admin audit |
| `/admin/impersonation` | admin | ✅ | ❌ | ❌ | ❌ | ❌ | platform_admin | Flask admin impersonate |
| `/admin/courtesy` | admin | ✅ | ❌ | ❌ | ❌ | ❌ | platform_admin | Flask admin courtesy |
| `/admin/feedback` | admin | ✅ | ❌ | ❌ | ❌ | ❌ | platform_admin | Flask admin feedback |

### Paginas Publicas y Auth

| Ruta | Pagina | Layout | loading.tsx | error.tsx | Metadata | i18n | Auth |
|---|---|---|---|---|---|---|---|
| `/` | landing | root | ❌ | ❌ | Solo root | ❌ | No |
| `/login` | auth | root | ❌ | ❌ | ❌ | ❌ | No |
| `/registro` | auth | root | ❌ | ❌ | ❌ | ❌ | No |
| `/forgot-password` | auth | root | ❌ | ❌ | ❌ | ❌ | No |
| `/reset-password` | auth | root | ❌ | ❌ | ❌ | ❌ | No |
| `/[slug]` | public | public | ❌ | ❌ | ❌ | ❌ | No |

### Componentes UI compartidos

| Componente | Tipo | Estados | i18n | Accesible | Evidencia |
|---|---|---|---|---|---|
| EmptyState | Cliente | Sin datos | ❌ | ⚠️ Sin aria | `components/ui/EmptyState.tsx` |
| ErrorState | Cliente | Error + retry | ❌ | ⚠️ Sin aria | `components/ui/ErrorState.tsx` |
| LoadingState | Cliente | Cargando | ❌ | ⚠️ Sin aria | `components/ui/LoadingState.tsx` |
| Modal | Cliente | Abierto/cerrado | N/A | ✅ Radix Dialog | `components/ui/Modal.tsx` |
| Sheet | Cliente | Abierto/cerrado | N/A | ✅ Radix Dialog | `components/ui/Sheet.tsx` |
| Sidebar | Cliente | Nav activa | ❌ | ✅ aria-labels | `components/dashboard/Sidebar.tsx` |
| ChatOrb | Cliente | Animacion | N/A | ❌ Sin aria | `components/dashboard/ChatOrb.tsx` |
| ThemeToggle | Cliente | Dark/light | N/A | ✅ | `components/ui/ThemeToggle.tsx` |

## Tareas propuestas

| ID | Prioridad | Tarea | Owner sugerido | Estimacion | Depende de |
|---|---|---|---|---|---|
| F03-A | P1 | Implementar `useTranslations()` en componentes core (Sidebar, Landing, Login) | Agent i18n/Frontend | 2-3d | — |
| F03-B | P1 | Añadir `loading.tsx` y `error.tsx` a dashboard, admin, public | Agent Frontend | 1d | — |
| F03-C | P1 | Añadir `generateMetadata()` en landing, login, registro | Agent Frontend | 0.5d | — |
| F03-D | P2 | Migrar paginas dashboard a Server Components donde sea posible | Agent Frontend | 2d | — |
| F03-E | P2 | Renombrar sidebar labels (Search→Knowledge, etc.) | Agent Frontend | 0.5d | F03-A (i18n) |
| F03-F | P2 | Añadir Zod validation en API Routes | Agent Frontend | 1d | — |
| F03-G | P2 | Traducir SignOutButton y textos residuales en espanol | Agent Frontend | 0.5d | F03-A |
| F03-H | P3 | Añadir aria-labels a EmptyState, ErrorState, LoadingState | Agent Frontend | 0.5d | — |
| F03-I | P3 | Redirigir a /onboarding si usuario tiene 0 clones | Agent Frontend | 0.5d | — |

## Open Questions

1. **Decision sobre i18n**: Se quiere `localePrefix: "never"` (cookie, facil, sin SEO) o `prefix` (URL /en/..., mejor SEO, mas trabajo)?
2. **Server Components vs Client Components**: Estrategia para migrar gradualmente o se prefiere mantener todo cliente por ahora?
3. **stripe.ts eliminado**: La pagina de facturacion depende de el. Se restaura o se reimplementa?
4. **Onboarding**: El wizard de onboarding existe en `(dashboard)/onboarding/` pero no se redirige automaticamente. Es intencional?
