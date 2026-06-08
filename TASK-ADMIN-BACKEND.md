Quiero aplicar a toda la aplicación un rediseño visual basado en las imágenes de referencia adjuntas.

OBJETIVO
Transformar todos los dashboards, paneles de administración, vistas internas y backend para que sigan un estilo SaaS moderno, limpio, claro y profesional, similar a las referencias visuales aportadas.

IMPORTANTE
No quiero un simple cambio de colores. Quiero que se convierta en una línea visual consistente para todo el producto. Antes de tocar código, revisa la aplicación completa paso a paso y crea un plan de implementación claro.

REFERENCIAS VISUALES
Usa las imágenes adjuntas como referencia principal de estilo.

El estilo debe seguir estas características:

- Interfaz tipo dashboard SaaS B2B.
- Fondo general claro, blanco roto o gris muy suave.
- Tarjetas blancas con bordes suaves.
- Bordes redondeados amplios.
- Sombras muy sutiles, sin efecto pesado.
- Mucho espacio en blanco.
- Tipografía limpia, moderna y legible.
- Jerarquía visual clara: títulos, subtítulos, métricas, acciones y estados.
- Sidebar lateral compacta, limpia y bien estructurada.
- Menús con iconos sencillos.
- Cards modulares para métricas, acciones rápidas, integraciones, estados y flujos.
- Uso de colores suaves y controlados: naranja, violeta, verde, azul y gris, siempre como acentos, nunca saturando.
- Gradientes suaves solo en bloques destacados o banners.
- Inputs grandes tipo command/search bar cuando tenga sentido.
- Botones limpios, con estados hover/focus correctos.
- Badges y etiquetas pequeñas para estados.
- Diseño responsive para escritorio, tablet y móvil.
- Backend/admin con el mismo lenguaje visual, no como una zona separada o descuidada.

PLAN DE IMPLEMENTACIÓN OBLIGATORIO
Antes de implementar, crea o actualiza un documento llamado:

IMPLEMENTATION_PLAN.md

Debe incluir:

1. Auditoría visual actual
   - Listar todas las páginas, dashboards, layouts, componentes y vistas backend existentes.
   - Indicar qué partes ya cumplen parcialmente con el nuevo estilo.
   - Indicar qué partes no cumplen.
   - Indicar riesgos técnicos antes de modificar.

2. Sistema de diseño
   - Definir paleta de colores.
   - Definir tipografías.
   - Definir espaciados.
   - Definir radios de borde.
   - Definir sombras.
   - Definir estilos de cards.
   - Definir estilos de botones.
   - Definir estilos de inputs.
   - Definir estilos de sidebar.
   - Definir estilos de tablas.
   - Definir estilos de estados: success, warning, error, info, disabled.

3. Componentes base
   Crear o revisar los componentes reutilizables:
   - AppShell
   - Sidebar
   - Header
   - DashboardCard
   - MetricCard
   - ActionCard
   - IntegrationCard
   - StatusBadge
   - SearchCommandBar
   - DataTable
   - EmptyState
   - LoadingState
   - ErrorState
   - PageSection
   - FormPanel
   - Modal/Dialog
   - Toast/Notification

4. Implementación por fases
   Dividir el trabajo en fases:
   - Fase 1: auditoría y documentación.
   - Fase 2: sistema de diseño y tokens visuales.
   - Fase 3: componentes base.
   - Fase 4: dashboards principales.
   - Fase 5: backend/admin.
   - Fase 6: vistas secundarias.
   - Fase 7: responsive y accesibilidad.
   - Fase 8: QA visual y revisión final.

5. Checklist por pantalla
   Para cada pantalla indicar:
   - Estado inicial.
   - Cambios necesarios.
   - Archivos afectados.
   - Estado: No iniciado / En progreso / Implementado / Revisado.
   - Observaciones.

USO DE AGENTES
Trabaja como un equipo de agentes especializados. Aunque estés ejecutando en una sola sesión, organiza el trabajo como si intervinieran estos agentes:

AGENTE 1 — Auditor visual
Revisa todas las pantallas, layouts y componentes actuales.
Detecta inconsistencias visuales.
Documenta qué hay que cambiar antes de implementar.

AGENTE 2 — Arquitecto UI
Define el sistema de diseño reutilizable.
Evita soluciones sueltas por pantalla.
Prioriza componentes globales antes que cambios aislados.

AGENTE 3 — Frontend implementador
Aplica el diseño en código.
Reutiliza componentes existentes cuando sea posible.
No dupliques estilos innecesariamente.
No rompas lógica, rutas, permisos, autenticación ni llamadas API.

AGENTE 4 — Backend/Admin reviewer
Revisa específicamente las zonas internas, paneles administrativos, gestión de usuarios, configuración, tablas, formularios y vistas privadas.
Debe aplicar el mismo estilo visual que el frontend principal.

AGENTE 5 — QA visual y funcional
Comprueba pantalla por pantalla:
- Que no haya errores visuales.
- Que todo sea responsive.
- Que los botones sigan funcionando.
- Que los formularios sigan enviando datos.
- Que las tablas sigan mostrando información.
- Que no haya errores de consola.
- Que no se hayan roto permisos, roles o navegación.

MÉTODO DE TRABAJO
No implementes todo de golpe.

Primero:
1. Analiza la estructura del proyecto.
2. Detecta framework, librerías UI, rutas y componentes.
3. Crea el plan de implementación.
4. Crea la checklist.
5. Después empieza la implementación por fases.

Cada cambio debe quedar documentado.

Después de cada fase, actualiza IMPLEMENTATION_PLAN.md indicando:
- Qué se ha hecho.
- Qué archivos se han tocado.
- Qué falta.
- Qué está bloqueado.
- Qué debe revisarse manualmente.

CRITERIO DE CALIDAD
El resultado debe parecer un producto SaaS moderno, elegante y profesional, no una plantilla genérica.

Debe tener una estética similar a:
- Dashboard limpio.
- Panel administrativo premium.
- Backend moderno.
- Producto B2B de IA o gestión empresarial.
- Interfaz clara, ligera, ordenada y escalable.

NO HACER
- No cambiar lógica de negocio sin necesidad.
- No eliminar funcionalidades.
- No romper autenticación.
- No tocar base de datos salvo que sea imprescindible.
- No duplicar componentes si ya existe una base reutilizable.
- No aplicar estilos inline masivos.
- No dejar pantallas antiguas mezcladas con pantallas nuevas.
- No usar colores chillones.
- No saturar con sombras.
- No convertir todo en una landing; esto debe seguir siendo una herramienta de trabajo.

ENTREGABLE FINAL
Al terminar, entrega:

1. Resumen de cambios aplicados.
2. Lista de archivos modificados.
3. Checklist de pantallas revisadas.
4. Estado de cada pantalla:
   - Implementado
   - Parcial
   - Pendiente
5. Problemas detectados.
6. Recomendaciones de siguiente fase.
7. Confirmación de que dashboard, backend y vistas internas siguen una línea visual coherente.

CONDICIÓN FINAL
No marques una pantalla como implementada si no has revisado visualmente y funcionalmente que cumple el nuevo estilo.

Crítica clara: no lo plantees como “ponme este estilo”. Eso suele acabar en un lavado superficial. Lo correcto es obligar al agente a crear sistema de diseño, checklist y revisión por fases. Así evitas que toque cuatro cards y deje el backend viejo.

He hecho: he convertido las dos imágenes en un prompt operativo para aplicar ese estilo a dashboards y backend, incluyendo plan de implementación, agentes, auditoría paso a paso y criterios de validación.

Se ha pegado el markdown.md
Archivo
Se ha pegado el markdown (2).md
Archivo
Se ha pegado el markdown (3).md
Archivo
añade todo y has un mega plan maestro. inclueyndo l oque acaba de pponer y un task mucho mas completo se muy detallado 
Pensó durante 21s

Correcto. Hay una contradicción importante en lo que has juntado: un documento pide Institutional Console claro por defecto, otro pide dashboard oscuro premium tipo Linear/Stripe. Si lo mandas así sin resolverlo, el agente puede mezclar estilos y dejar una app incoherente. Lo he resuelto así: estilo global Institutional Console en light mode por defecto, y dark mode premium como variante completa por tokens, no como rediseño separado. Esto encaja con tu guía global, con el plan backend admin y con el rediseño premium del dashboard.

Pega este prompt/task completo:

# MEGA PLAN MAESTRO DE IMPLEMENTACIÓN — MYOWNCLONE
# Backend Admin + Rediseño Global + Dashboard Premium + QA por Agentes

## 0. OBJETIVO GENERAL

Quiero que ejecutes una implementación integral de MyOwnClone, no un cambio superficial.

El objetivo es convertir MyOwnClone en una plataforma SaaS profesional, segura, escalable y visualmente coherente, con:

1. Backend Admin estable, seguro y verificable.
2. API admin canónica en Flask.
3. Proxy Next correctamente autenticado.
4. Contratos frontend-backend estables.
5. Rediseño visual global basado en las imágenes de referencia.
6. Estilo Institutional Console aplicado a toda la aplicación.
7. Light mode como experiencia por defecto.
8. Dark mode premium como variante completa por tokens.
9. Dashboard, backend, admin, inbox, biblioteca, memoria/cerebro, analíticas, billing, configuración, onboarding, login/register y páginas públicas con la misma línea visual.
10. Auditoría paso a paso de lo que está implementado, lo que está parcial y lo que está pendiente.
11. Uso de agentes especializados para revisar, implementar y validar.
12. QA visual, funcional, responsive, seguridad y build final.

No quiero una landing.
No quiero un lavado de cara.
No quiero tocar cuatro cards y dejar el backend o el admin antiguo.
No quiero romper autenticación, multi-tenancy, rutas, permisos, contratos, modelos ni lógica de negocio.

El trabajo se considera terminado solo cuando exista documentación, checklist, backend funcional, frontend adaptado, diseño consistente, build correcto y revisión final pantalla por pantalla.

---

## 1. DECISIÓN DE DISEÑO OBLIGATORIA

Hay dos líneas visuales a integrar:

1. Institutional Console:
   - Claro por defecto.
   - Inspirado en dashboards financieros premium.
   - Shell institucional.
   - Sidebar sobria.
   - Topbar clara.
   - Cards con bordes finos.
   - Tablas/graficas protagonistas.
   - Responsive real.

2. Dashboard premium dark:
   - Oscuro, sofisticado, editorial tech-luxury.
   - Glassmorphism controlado.
   - Gradientes violet/cyan.
   - Microinteracciones premium.
   - Avatar ring.
   - Logo shimmer.
   - Count-up.
   - Quick actions con hover glow.

La decisión final es esta:

- Light mode será el modo principal de producto.
- Dark mode será variante completa por tokens.
- No habrá dos diseños distintos.
- El dashboard oscuro premium debe traducirse a tokens globales para que funcione como variante `.dark`.
- El admin/backend no puede quedar en estilo antiguo.
- Las pantallas internas deben sentirse como software ejecutivo real, no marketing.

---

## 2. REFERENCIAS VISUALES

Usa las imágenes de referencia como dirección visual:

- Dashboard SaaS B2B limpio.
- Shell ancho con marco redondeado.
- Sidebar lateral clara y compacta.
- Topbar con búsqueda, acciones y breadcrumb.
- Cards blancas con bordes suaves.
- Superficies limpias.
- Mucho espacio en blanco.
- Datos y acciones bien jerarquizados.
- Banners con gradientes suaves.
- Inputs tipo command/search bar.
- Integraciones, quick actions y estados en cards modulares.
- Estilo premium, técnico, claro y usable.

No copies logos, marcas ni contenido literal.
Recrea el sistema visual.

---

## 3. DOCUMENTOS QUE DEBES CREAR O ACTUALIZAR

Antes de tocar código, crea o actualiza estos documentos:

```text
MASTER_IMPLEMENTATION_PLAN.md
DESIGN_SYSTEM.md
BACKEND_ADMIN_CONTRACTS.md
BACKEND_SECURITY_AUDIT.md
FRONTEND_UI_AUDIT.md
ROUTE_AND_COMPONENT_MAP.md
QA_CHECKLIST.md
IMPLEMENTATION_LOG.md
3.1 MASTER_IMPLEMENTATION_PLAN.md

Debe contener:

Objetivo general.
Alcance.
Stack detectado.
Estructura real del proyecto.
Riesgos.
Orden de implementación.
Fases.
Checklist por fase.
Checklist por pantalla.
Checklist backend.
Checklist frontend.
Checklist responsive.
Checklist accesibilidad.
Checklist build/test.
Estado de cada área:
No iniciado.
En progreso.
Parcial.
Implementado.
Revisado.
Bloqueado.
3.2 DESIGN_SYSTEM.md

Debe contener:

Nombre del estilo: Institutional Console.
Light mode default.
Dark mode premium variant.
Tokens CSS.
Paleta.
Tipografías.
Espaciados.
Radios.
Sombras.
Bordes.
Cards.
Botones.
Inputs.
Badges.
Estados.
Tablas.
Charts.
Sidebar.
Topbar.
Layout responsive.
Componentes reutilizables.
Reglas de uso.
Reglas de lo que no se debe hacer.
3.3 BACKEND_ADMIN_CONTRACTS.md

Debe contener todos los contratos admin:

Overview.
Tenants.
Tenant detail.
Tenant patch.
Feedback.
Impersonation.
Stop impersonation.
Audit log.
Errores estándar.
Paginación estándar.
Fechas estándar.
Planes y estados canónicos.
3.4 BACKEND_SECURITY_AUDIT.md

Debe contener:

Estado actual de auth.
Estado actual de roles.
Estado actual de multi-tenancy.
Riesgos detectados.
Cambios aplicados.
Cambios pendientes.
Pruebas 401/403/200.
Confirmación de que no se filtran secretos.
Confirmación de que las acciones sensibles quedan auditadas.
3.5 FRONTEND_UI_AUDIT.md

Debe contener:

Lista de pantallas.
Lista de layouts.
Lista de componentes.
Qué ya cumple el nuevo estilo.
Qué no cumple.
Qué se ha rediseñado.
Qué falta.
Capturas o descripción visual si no puedes adjuntar imágenes.
3.6 ROUTE_AND_COMPONENT_MAP.md

Debe contener:

Rutas frontend.
Componentes principales.
Componentes compartidos.
APIs consumidas.
Archivos afectados.
Dependencias visuales.
Dependencias de auth.
Dependencias de datos.
3.7 QA_CHECKLIST.md

Debe contener:

Checklist de backend.
Checklist de frontend.
Checklist visual.
Checklist responsive.
Checklist accesibilidad.
Checklist seguridad.
Checklist build.
Checklist manual.
3.8 IMPLEMENTATION_LOG.md

Debe actualizarse después de cada fase con:

Fecha/hora.
Fase ejecutada.
Archivos modificados.
Cambios realizados.
Problemas detectados.
Decisiones tomadas.
Pendientes.
Comandos ejecutados.
Resultado de comandos.
4. AGENTES OBLIGATORIOS

Trabaja como si fueras un equipo de agentes especializados. Aunque ejecutes en una sola sesión, organiza el trabajo con estos roles.

AGENTE 0 — Orquestador

Responsabilidades:

Leer el repositorio.
Crear el plan.
Dividir el trabajo en fases.
Evitar cambios desordenados.
Mantener MASTER_IMPLEMENTATION_PLAN.md.
No permitir que se implemente UI antes de resolver riesgos críticos de backend/auth si afectan al admin.
Confirmar que cada fase tenga criterio de aceptación.

Entregables:

Plan maestro.
Orden de ejecución.
Estado general.
AGENTE 1 — Auditor de repositorio

Responsabilidades:

Ejecutar inspección inicial.
Detectar stack real.
Detectar estructura real.
Detectar archivos duplicados.
Detectar rutas activas.
Detectar componentes compartidos.
Detectar CSS global.
Detectar Tailwind config.
Detectar sistema de auth.
Detectar modelos backend reales.

Comandos sugeridos:

rg --files
git status --short
rg "Dashboard|dashboard|Sidebar|Admin|admin|Tenant|tenant|Feedback|feedback|impersonate|auth|platform_admin" .

Debe confirmar especialmente:

Si el backend real está en api/api/*.
Si existen duplicados en api/*.
Qué árbol registra Flask realmente.
Qué rutas consume Next.
Qué endpoints existen y cuáles faltan.
Qué pantallas están usando mocks.
AGENTE 2 — Arquitecto Backend Admin

Responsabilidades:

Endurecer API admin Flask.
Corregir modelos/imports.
Normalizar contratos.
Crear endpoints faltantes.
Evitar mezcla de Drizzle/Flask sin justificación.
Garantizar paginación.
Garantizar errores estándar.
Garantizar fechas ISO 8601.
Garantizar planes y estados canónicos.

Debe trabajar sobre:

api/api/app_factory.py
api/api/controllers/console/myownclone/admin_platform.py
api/api/controllers/console/auth.py
api/api/libs/login.py
api/api/models/*
api/api/migrations/versions/*

No debe editar duplicados en:

api/controllers/*
api/models/*

salvo que confirme que el runtime los usa.

AGENTE 3 — Seguridad/Auth/Multi-tenancy

Responsabilidades:

Revisar auth Next -> Flask.
Revisar platform_admin.
Revisar impersonation.
Revisar tokens.
Revisar cookies.
Revisar JWT.
Revisar tenant scope.
Revisar auditoría.
Evitar bypass de admin.
Evitar token muerto en env.
Evitar filtrar secretos.

Debe comprobar:

Usuario sin sesión: 401.
Usuario sin rol admin: 403.
Usuario platform_admin: 200.
Backend caído: error claro.
Tenant normal no puede acceder a rutas de plataforma.
Impersonation exige reason.
Impersonation expira.
Impersonation queda auditada.
Stop impersonation cierra el log correcto.
AGENTE 4 — Arquitecto UI / Design System

Responsabilidades:

Crear sistema visual global.
Traducir las imágenes a tokens y componentes.
Resolver la contradicción light/dark.
Evitar estilos sueltos por pantalla.
Crear componentes reutilizables.
Asegurar coherencia entre frontend público, dashboard, admin y backend.

Debe crear o revisar:

AppShell
Sidebar
MobileNavigation
Topbar
SectionHeader
Breadcrumb
Tabs
DashboardCard
MetricCard
ActionCard
IntegrationCard
StatusBadge
SearchCommandBar
DataTable
MobileListRow
EmptyState
LoadingState
ErrorState
PageSection
FormPanel
Modal/Dialog
Toast/Notification
ChartCard
AuditTimeline
TenantHealthCard
AGENTE 5 — Frontend Implementador

Responsabilidades:

Aplicar el diseño en React/Next/Tailwind.
Reutilizar componentes.
No duplicar estilos.
No romper rutas.
No romper estado.
No romper llamadas API.
No romper permisos.
No convertir pantallas internas en landing.

Debe trabajar sobre:

replica/src/app/admin/layout.tsx
replica/src/app/admin/resumen/page.tsx
replica/src/app/admin/tenants/page.tsx
replica/src/app/admin/feedback/page.tsx
replica/src/app/api/admin/[...path]/route.ts
replica/src/app/api/admin/route.ts
replica/src/lib/db/schema/*
replica/src/components/*
replica/src/app/*
replica/src/styles/*
AGENTE 6 — QA Visual y Funcional

Responsabilidades:

Revisar pantalla por pantalla.
Revisar responsive.
Revisar accesibilidad.
Revisar errores de consola.
Revisar botones.
Revisar formularios.
Revisar tablas.
Revisar estados vacíos.
Revisar loading/error.
Revisar build/lint/typecheck/test.

Debe validar anchuras:

375px
768px
1024px
1440px
AGENTE 7 — Documentador

Responsabilidades:

Mantener todos los documentos actualizados.
Registrar qué se ha hecho.
Registrar qué queda.
Registrar errores.
Registrar comandos.
Registrar decisiones.
No marcar nada como terminado sin evidencia.
5. STACK ESPERADO Y DETECCIÓN

Antes de asumir nada, confirma el stack.

Stack esperado por documentación:

Frontend/Admin:

Next 16.2.6
React 19.2.4
Tailwind 4
TypeScript
Vitest

Backend:

Flask
Flask-RESTX
SQLAlchemy
Alembic
JWT propio en /console/api/auth
PostgreSQL

Base de datos:

PostgreSQL
SQLAlchemy en Flask
Drizzle en Next

Riesgo:

Hay esquemas duplicados/paralelos entre SQLAlchemy y Drizzle.
Hay posible doble árbol api/ y api/api/.
No edites a ciegas.
6. RIESGOS CRÍTICOS DETECTADOS

Antes de implementar UI, revisa estos puntos.

6.1 Import sospechoso

En admin_platform.py puede existir:

from models.account import Account

Debe revisarse. El patrón correcto probablemente sea:

from api.models.account import Account, Tenant

No lo cambies sin comprobar estructura real, pero no dejes imports inconsistentes.

6.2 Modelos stub

api/api/models/account.py puede contener clases stub como:

class Tenant:
    id: str
    name: str
    status: str

Si luego se hacen queries SQLAlchemy sobre Tenant.id, puede fallar en runtime.

Debes convertir esos modelos en SQLAlchemy reales o importar los modelos correctos.

6.3 Doble árbol backend

Puede existir:

api/controllers/*
api/api/controllers/*
api/models/*
api/api/models/*

Fuente principal probable:

api/api/*

porque api/api/app_factory.py registra controladores.

No edites duplicados si no confirmas que se usan.

6.4 Auth Next -> Flask inconsistente

El backend Flask espera:

Authorization: Bearer <jwt>

Pero el proxy Next puede estar reenviando solo cookies:

Cookie: request.headers.get("cookie") || ""

También puede existir:

const ADMIN_TOKEN = process.env.PLATFORM_ADMIN_TOKEN || ""

sin usar.

Esto debe resolverse.

6.5 Fuente de verdad mezclada

Puede existir:

replica/src/app/api/admin/route.ts

leyendo tenants directamente con Drizzle, mientras:

replica/src/app/api/admin/[...path]/route.ts

proxya Flask.

Decisión obligatoria:

Flask debe ser API admin canónica.
Next debe actuar como BFF/proxy con auth.
Si queda lectura Drizzle local, debe documentarse y no duplicar lógica crítica admin.
6.6 Feedback incompleto

La pantalla:

replica/src/app/admin/feedback/page.tsx

puede llamar:

/api/admin/feedback

Pero Flask puede no tener:

GET /console/api/myownclone/admin/feedback

Debes crearlo si falta.

6.7 Planes y estados inconsistentes

Backend puede usar:

"básico", "pro", "escala", "enterprise"

Drizzle puede usar:

"basic", "pro", "scale", "enterprise", "trial"

Backend puede usar:

Tenant.status == "normal"

Drizzle puede usar:

"active", "suspended", "cancelled", "trial"

Debes normalizar a:

Plans: trial, basic, pro, scale, enterprise
Statuses: active, trial, suspended, cancelled

La traducción a español se hace en frontend, no en backend.

7. PRINCIPIOS DE ARQUITECTURA
7.1 Fuente de verdad

Para administración de plataforma:

Flask = API canónica
Next = BFF/proxy + validación de sesión
Drizzle = solo auth/web si aplica, no lógica admin crítica duplicada
7.2 Seguridad

Cada ruta admin debe cumplir:

Usuario autenticado.
Rol platform_admin.
Validación estricta de payload.
Auditoría en acciones sensibles.
No devolver secretos.
No loguear tokens completos.
No permitir acceso de tenant normal a endpoints de plataforma.
No modificar tenants sin registrar auditoría.
7.3 Multi-tenancy

Toda query debe ser explícita:

Global de plataforma.
Scoped por tenant.

No mezclar.

7.4 Contratos estables

Listas:

{
  "items": [],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 0,
    "pages": 0
  }
}

Errores:

{
  "error": "error_code",
  "message": "Human readable message"
}

Fechas:

ISO 8601 UTC
8. CONTRATOS BACKEND ADMIN
8.1 GET /console/api/myownclone/admin/overview

Debe devolver:

{
  "total_tenants": 0,
  "active_tenants": 0,
  "total_clones": 0,
  "mrr_cents": 0,
  "mrr_display": "0.00€",
  "total_costs_cents": 0,
  "total_costs_display": "0.00€",
  "margin_cents": 0,
  "margin_display": "0.00€",
  "plan_breakdown": {
    "trial": 0,
    "basic": 0,
    "pro": 0,
    "scale": 0,
    "enterprise": 0
  },
  "generated_at": "2026-06-04T00:00:00Z"
}

Reglas:

Usar planes canónicos en inglés.
No contar suspendidos/cancelados en MRR.
Costes en ventana 30 días si existe CostTracking.
Valores nulos a 0.
Añadir generated_at.
8.2 GET /console/api/myownclone/admin/tenants

Parámetros:

page=1
limit=20
search=
status=
plan=
sort=created_at
direction=desc

Respuesta:

{
  "items": [
    {
      "id": "tenant_id",
      "slug": "tenant-slug",
      "name": "Tenant name",
      "plan": "pro",
      "status": "active",
      "subscription_status": "active",
      "clone_count": 1,
      "monthly_cost_cents": 0,
      "created_at": "2026-06-04T00:00:00Z",
      "updated_at": "2026-06-04T00:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 0,
    "pages": 0
  }
}

Reglas:

limit <= 50.
Search por name, slug y owner email si existe.
No devolver datos sensibles.
Respuesta siempre paginada.
8.3 GET /console/api/myownclone/admin/tenants/<tenant_id>

Debe devolver:

{
  "tenant": {
    "id": "tenant_id",
    "slug": "tenant-slug",
    "name": "Tenant name",
    "plan": "pro",
    "status": "active",
    "subscription_status": "active",
    "created_at": "2026-06-04T00:00:00Z"
  },
  "usage": {
    "clone_count": 0,
    "cost_cents_30d": 0,
    "tokens_in_30d": 0,
    "tokens_out_30d": 0,
    "questions_30d": 0,
    "gaps_open": 0
  },
  "clones": []
}

Si no existe tenant:

{
  "error": "tenant_not_found",
  "message": "Tenant not found"
}

con status 404.

8.4 PATCH /console/api/myownclone/admin/tenants/<tenant_id>

Payload permitido:

{
  "plan": "pro",
  "status": "active"
}

Reglas:

Solo campos allowlist.
Registrar auditoría.
No modificar billing externo sin endpoint dedicado.
Validar plan/status.
8.5 GET /console/api/myownclone/admin/feedback

Parámetros:

page=1
limit=20
search=
rating=
clone_id=
tenant_id=

Respuesta:

{
  "items": [
    {
      "id": "feedback_id",
      "clone_id": "clone_id",
      "tenant_id": "tenant_id",
      "tenant_name": "Tenant name",
      "rating": "up",
      "comment": "Texto",
      "created_at": "2026-06-04T00:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 0,
    "pages": 0
  }
}
8.6 POST /console/api/myownclone/admin/impersonate

Payload:

{
  "tenant_id": "tenant_id",
  "reason": "Necesario para soporte"
}

Reglas:

reason obligatorio.
Mínimo 10 caracteres.
Máximo 1000 caracteres.
Confirmar que tenant existe.
Expiración máxima 30 minutos.
Token no debe loguearse completo.
Si se persiste, guardar hash.
Registrar started_at.
Registrar auditoría.

Respuesta:

{
  "impersonation_id": "id",
  "token": "one_time_token",
  "tenant_id": "tenant_id",
  "tenant_name": "Tenant name",
  "expires_at": "2026-06-04T00:30:00Z"
}
8.7 POST /console/api/myownclone/admin/impersonate/stop

Reglas:

Cerrar el log correcto.
No cerrar “el último” por accidente.
Revocar token.
Registrar auditoría.
Si no hay token activo, devolver 404 o 400 claro.
8.8 GET /console/api/myownclone/admin/audit-log

Respuesta:

{
  "items": [
    {
      "id": "log_id",
      "actor_id": "admin_id",
      "action": "impersonation_started",
      "tenant_id": "tenant_id",
      "reason": "Texto",
      "created_at": "2026-06-04T00:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 0,
    "pages": 0
  }
}

Debe listar:

Impersonaciones.
Cambios de plan.
Cambios de status.
Acciones admin sensibles.
9. SISTEMA VISUAL GLOBAL — INSTITUTIONAL CONSOLE
9.1 Nombre del estilo
Institutional Console

Descripción:

Consola SaaS institucional, clara por defecto y oscura como variante, con información operativa presentada como software ejecutivo: superficies suaves, bordes finos, acentos luminosos controlados, tipografía precisa y jerarquía muy ordenada.
9.2 Principios
Light mode por defecto.
Dark mode por tokens.
UI responsive real.
Información operativa protagonista.
Gráficas, tablas, listas y métricas protagonistas.
Nada de landing dentro de app.
Nada de cards dentro de cards.
Nada de gradientes enormes tapando datos.
Nada de textos largos explicando la interfaz.
Nada de colores chillones.
Nada de sombras pesadas.
Nada de estética template.
9.3 Paleta light default
:root {
  --bg-page: #D6D0CD;
  --bg-shell: #F8FAFC;
  --bg-sidebar: #FFFFFF;
  --bg-topbar: #FFFFFF;
  --surface-1: #F8FAFC;
  --surface-2: #F1F5F9;
  --surface-3: #E9EEF4;

  --border-soft: rgba(15, 23, 42, 0.08);
  --border-medium: rgba(15, 23, 42, 0.12);
  --border-strong: rgba(15, 23, 42, 0.18);

  --text-primary: #334155;
  --text-secondary: #64748B;
  --text-muted: #94A3B8;
  --text-faint: #CBD5E1;

  --accent-warm: #F97316;
  --accent-amber: #F59E0B;
  --accent-pink: #EC4899;
  --accent-blue: #2563EB;
  --accent-cyan: #06B6D4;
  --accent-violet: #8B5CF6;
  --accent-green: #10B981;
}
9.4 Paleta dark variant
.dark {
  --bg-page: #070708;
  --bg-shell: #0B0B0C;
  --bg-sidebar: #101011;
  --bg-topbar: #111112;
  --surface-1: #121213;
  --surface-2: #171718;
  --surface-3: #1D1D1F;

  --border-soft: rgba(255, 255, 255, 0.07);
  --border-medium: rgba(255, 255, 255, 0.11);
  --border-strong: rgba(255, 255, 255, 0.16);

  --text-primary: #F4F4F5;
  --text-secondary: #A1A1AA;
  --text-muted: #71717A;
  --text-faint: #52525B;
}
9.5 Acentos dark premium

Usar estos acentos dentro de .dark sin crear otro sistema separado:

--primary-violet: #7C3AED;
--primary-violet-light: #A855F7;
--secondary-cyan: #06B6D4;

Regla:

El violeta/cyan no debe invadir toda la app.
Usarlo en highlights, quick actions, avatar ring, logo shimmer, charts y CTAs controlados.
No saturar toda la UI con morado.
9.6 Tipografías

Preferencia:

UI/cuerpo: DM Sans, Inter o Geist Sans
Números: JetBrains Mono o Geist Mono
Títulos: DM Sans/Inter 600-700
Opcional editorial: Syne solo en dashboard premium o títulos especiales

Reglas:

Títulos de página: 24-32px.
Títulos de card: 16-20px.
Labels: 12-14px.
Números grandes: 24-36px.
Números y porcentajes en mono.
No usar tracking negativo.
Labels en gris.
Valores en color principal.

Si usas Google Fonts:

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">

O en CSS:

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600;700&family=Syne:wght@600;700;800&display=swap');
10. LAYOUT GLOBAL
10.1 Desktop
Fondo ambiental claro
  Shell app redondeada
    Sidebar 220-260px
    Content
      Topbar 72px
      Main 24px
10.2 Tablet
Shell con radius menor
Sidebar colapsada o rail 72px
Topbar 64-72px
Cards en 2 columnas cuando quepa
Tabs con scroll horizontal
10.3 Mobile
Sin sidebar fija
Topbar compacta
Drawer o bottom nav
Main 16px
Cards en 1 columna
Tabs con scroll horizontal
Tablas convertidas en list rows/cards
Gráficas con altura fija 260-320px
11. SHELL EXTERIOR
Light
background:
  radial-gradient(circle at 8% 8%, rgba(249, 115, 22, 0.22), transparent 34%),
  radial-gradient(circle at 90% 85%, rgba(236, 72, 153, 0.16), transparent 34%),
  linear-gradient(135deg, #E7E1DE 0%, #D6D0CD 100%);
Dark
background:
  radial-gradient(circle at 8% 8%, rgba(249, 115, 22, 0.55), transparent 34%),
  radial-gradient(circle at 90% 85%, rgba(236, 72, 153, 0.42), transparent 34%),
  linear-gradient(135deg, #160F0D 0%, #070708 100%);
12. COMPONENTES BASE OBLIGATORIOS

Crea o adapta componentes reutilizables:

AppShell
Sidebar
SidebarItem
MobileNavigation
Topbar
Breadcrumb
SectionHeader
Tabs
DashboardCard
MetricCard
ActionCard
IntegrationCard
StatusBadge
SearchCommandBar
DataTable
MobileListRow
EmptyState
LoadingState
ErrorState
PageSection
FormPanel
Modal/Dialog
Toast/Notification
ChartCard
AuditTimeline
TenantHealthCard
UserAvatar
Tooltip
OnboardingBanner
QuickActions
QuickActionCard

Reglas:

Reutilizar componentes existentes si son buenos.
No duplicar variantes por pantalla.
No meter estilos inline masivos.
No crear abstracciones absurdas si el proyecto ya tiene sistema.
Pero sí crear base común para que el estilo no quede roto.
13. SIDEBAR

Desktop:

Ancho 220-260px para Institutional Console.
Si se aplica dashboard dark premium específico, puede usar 200px en esa pantalla, pero no romper consistencia global.
Fondo light: #FFFFFF.
Fondo dark: #101011.
Border derecho fino.
Search arriba si aplica.
Nav central.
Links auxiliares abajo.
Iconos sencillos.
Item activo con borde, fondo suave y acento.
Tooltip en hover/focus.
Badge New en Analíticas si existe.

Mobile:

No usar sidebar persistente.
Drawer o bottom nav.
Mantener mismo orden de navegación.
14. TOPBAR
Altura desktop: 72px.
Altura mobile: 56-64px.
Fondo light: #FFFFFF.
Fondo dark: #111112.
Border bottom fino.
Breadcrumb en desktop.
Título corto en mobile.
Acciones a la derecha.

Acciones por contexto:

Admin: Run Audit, Export
Dashboard: Create Clone, Sync Data
Inbox: Generate Draft, Archive
Biblioteca: New Source, Upload
Analíticas: Export, Refresh
Configuración: Save
15. CARDS

Reglas:

Radius: 14-18px.
Padding: 16px mobile, 20-24px desktop.
Border siempre visible pero suave.
Hovers máximo translateY(-1px) o translateY(-2px) en Institutional.
Quick actions dark premium pueden usar translateY(-4px) si no rompe layout.
No meter card grande dentro de otra card.
No sombras pesadas.
No fondos sólidos chillones.
16. GRÁFICAS

La gráfica debe parecer producto financiero:

Grid lines sutiles.
Labels pequeños.
Leyendas compactas con dots.
Tooltips con border.
Colores brillantes pero controlados.
Fondo integrado con la card.

Series:

--series-orange: #FB923C;
--series-amber: #FBBF24;
--series-pink: #EC4899;
--series-blue: #2563EB;
--series-cyan: #06B6D4;
--series-violet: #8B5CF6;

Gráficas sugeridas por área:

Admin: MRR, Costs, Tenants, Audit events
Dashboard: Clone activity, Sessions, Automation rate
Inbox: Pending, Drafted, Resolved
Biblioteca: Sources, Chunks, Coverage
Analíticas: Questions, Gaps, Conversion
Facturación: Usage, Limits, Cost
17. TABLAS Y LISTAS

Desktop:

Tablas compactas.
Header gris suave.
Filas con border bottom.
Números alineados a la derecha.
Hover muy sutil.

Mobile:

Convertir tablas en cards/list rows.
Mostrar 3-5 campos clave.
Acciones en menú o botón icono.
No usar overflow horizontal salvo tablas técnicas inevitables.
18. BADGES

Estados:

Active: emerald
Trial/New: cyan
Warning/Suspended: amber
Error/Cancelled: red muted
Enterprise/Admin: violet

Reglas:

Bordes translúcidos.
Fondo translúcido.
Texto legible.
No depender solo del color: usar texto claro.
19. ESTADOS VACÍOS

Todo estado vacío debe tener:

Icono.
Título corto.
Microcopy de una línea.
Acción principal si aplica.

Ejemplo:

No clones yet
Create your first AI clone to start capturing conversations.
[Create Clone]

No mostrar solo 0.
No dejar tablas vacías sin explicación.

20. DASHBOARD PRINCIPAL

Debe incluir:

Header:
  Workspace Overview
  CTA: Create Clone

Grid:
  Stats row:
    Clones
    Sessions
    Automation
    Feedback

Main:
  Clone Activity chart
  Inbox preview
  Knowledge coverage
  Quick actions
  Onboarding banner
Stats cards
Desktop: 3 o 4 columnas según datos reales.
Mobile: 1 columna.
Números en mono.
Count-up si hay datos.
Empty state si valor 0.
Iconos sobrios.
Quick actions

Desktop:

4 columnas

Mobile:

2x2

Acciones sugeridas:

Create Clone
Train Memory
Connect Sources
Review Insights

Reglas:

Glassmorphism sutil en dark.
No usar fondos sólidos de color.
Hover glow controlado.
No romper layout.
Onboarding banner

Debe incluir:

Finish your AI workspace setup
Connect your first source, create a clone, train memory, and publish.
0/4 steps
[Complete setup]
[View guide]

Fondo:

background:
  radial-gradient(circle at 20% 20%, rgba(124, 58, 237, 0.32), transparent 34%),
  radial-gradient(circle at 80% 0%, rgba(6, 182, 212, 0.18), transparent 32%),
  rgba(17, 17, 24, 0.78);
21. ADMIN OVERVIEW

Desktop:

Sidebar 220-260px
Topbar 72px
Main 24px

Header:
  MyOwnClone Admin
  Tabs:
    Overview
    Tenants
    Clones
    Usage
    Feedback
    Audit

Grid:
  Row 1:
    Platform Performance chart 2/3
    Operational Overview 1/3

  Row 2:
    Admin Actions 1/3
    Tenant Health table 2/3

  Row 3:
    Audit / Cost History full width

Mobile:

Topbar compacta
Título + acción primaria
Tabs scroll horizontal
Platform Performance full width
Operational Overview full width
Admin Actions list
Tenant Health como list rows
Audit History como timeline/list
22. INBOX
Header:
  Inbox
  CTA: Generate Draft

Desktop:
  Left list of messages
  Right detail/draft panel

Mobile:
  Message list first
  Detail as route/modal/drawer

Debe tener:

Empty state.
Loading state.
Error state.
Filtros si existen.
Diseño coherente con cards/list rows.
23. BIBLIOTECA / KNOWLEDGE LIBRARY
Header:
  Knowledge Library
  CTA: New Source

Content:
  Source cards/list
  Ingestion status badges
  Coverage chart
  Empty state if no sources

Debe mostrar:

Estado de fuentes.
Progreso de ingesta.
Coverage.
Errores de sincronización.
Acciones claras.
24. MEMORY CORE / CEREBRO

Debe incluir:

Resumen de memoria.
Fuentes activas.
Gaps detectados.
Última actualización.
Acciones:
Train Memory.
Review Gaps.
Sync Sources.
Charts o indicadores si hay datos.
Empty state si no hay memoria entrenada.
25. ANALÍTICAS

Debe incluir:

Questions.
Gaps.
Conversion.
Sessions.
Automation rate.
Feedback.
Export.
Refresh.
Charts con estilo financiero.
Tablas compactas.
Filtros temporales.
26. FACTURACIÓN / BILLING

Debe incluir:

Plan actual.
Usage.
Limits.
Cost.
MRR si admin.
Invoices si existen.
Estado subscription.
Badges:
active.
trial.
suspended.
cancelled.
No mostrar datos sensibles innecesarios.
27. CONFIGURACIÓN

Debe incluir:

Perfil.
Workspace.
Integraciones.
API keys si existen.
Seguridad.
Preferencias.
Tema light/dark.
Save button contextual.

Reglas:

Formularios en FormPanel.
Validación clara.
Estados loading/saving/error/success.
No botones gigantes.
28. LOGIN / REGISTER / ONBOARDING

Debe seguir la misma línea visual:

No parecer una landing ajena.
Shell limpio.
Cards suaves.
Copy corto.
Inputs claros.
Estados de error visibles.
Responsive.
Accesibilidad correcta.
29. PLAN DE IMPLEMENTACIÓN POR FASES
FASE -1 — Inspección real del repositorio

Antes de editar:

rg --files
git status --short
rg "Dashboard|dashboard|Sidebar|Quick|Analytics|Analiticas|Admin|Tenant|Feedback|impersonate|platform_admin" .

Documentar en:

ROUTE_AND_COMPONENT_MAP.md
FRONTEND_UI_AUDIT.md
BACKEND_SECURITY_AUDIT.md

Criterios de aceptación:

Stack confirmado.
Rutas confirmadas.
Archivos activos confirmados.
Duplicados detectados.
Riesgos listados.
No se ha tocado código aún.
FASE 0 — Plan maestro y checklist

Crear:

MASTER_IMPLEMENTATION_PLAN.md
DESIGN_SYSTEM.md
BACKEND_ADMIN_CONTRACTS.md
QA_CHECKLIST.md
IMPLEMENTATION_LOG.md

Criterios:

Plan por fases creado.
Checklist por pantalla creado.
Checklist backend creado.
Checklist frontend creado.
Checklist responsive creado.
Checklist seguridad creado.
FASE 1 — Modelos e imports backend

Objetivo:

Que rutas admin puedan consultar accounts y tenants con SQLAlchemy real.

Tareas:

Revisar tablas reales.
Revisar migraciones.
Revisar modelos.
Corregir imports.
Convertir stubs en modelos reales si aplica.
Confirmar _is_platform_admin.

Implementación recomendada:

def _is_platform_admin(account_id: str) -> bool:
    account = db.session.execute(
        select(Account).where(Account.id == account_id)
    ).scalar_one_or_none()

    return bool(
        account
        and (
            getattr(account, "is_platform_admin", False)
            or getattr(account, "role", None) == "platform_admin"
        )
    )

Criterios:

No falla overview por modelo stub.
Imports correctos.
Rol admin real confirmado.
No se editan duplicados equivocados.
FASE 2 — Auth Next -> Flask

Objetivo:

Que /admin web consuma Flask de forma segura.

Tareas:

Decidir mecanismo:
JWT Flask reenviado.
O token de servicio con auditoría.
Validar sesión Next.
Validar usuario platform_admin.
Reenviar credencial correcta.
Eliminar o usar ADMIN_TOKEN.
Manejar 401/403/502/504.

Criterios:

No autenticado: 401.
No admin: 403.
Platform admin: 200.
Backend caído: error claro.
No hay env muerta.
FASE 3 — Overview admin

Tareas:

Normalizar planes.
Normalizar estados.
Calcular MRR.
Calcular costes.
Añadir generated_at.
Devolver contrato estable.

Criterios:

trial/basic/pro/scale/enterprise.
active/trial/suspended/cancelled.
MRR no cuenta cancelados.
DB vacía no rompe.
Frontend consume contrato.
FASE 4 — Tenants paginado

Tareas:

Respuesta { items, pagination }.
Filtros search/status/plan.
Sort.
Limit máximo 50.
Clone count.
Monthly cost.
Actualizar frontend.

Criterios:

Lista vacía funciona.
Paginación funciona.
Search no rompe.
Frontend no espera array plano.
FASE 5 — Tenant detail

Crear:

GET /console/api/myownclone/admin/tenants/<tenant_id>

Y opcionalmente pantalla:

replica/src/app/admin/tenants/[id]/page.tsx

Criterios:

Detalle sin impersonar.
404 si no existe.
Usage 30d si hay datos.
Clones listados sin secretos.
FASE 6 — Tenant patch

Crear:

PATCH /console/api/myownclone/admin/tenants/<tenant_id>

Criterios:

Allowlist.
Validación.
Auditoría.
No billing externo accidental.
FASE 7 — Feedback admin

Crear:

GET /console/api/myownclone/admin/feedback

Criterios:

Paginado.
Filtros.
Join con tenant si posible.
Frontend adaptado.
Empty state.
FASE 8 — Impersonation segura

Tareas:

reason obligatorio.
Confirmar tenant.
Expiración máxima 30 min.
Token no logueado.
Hash si se persiste.
Stop cierra log correcto.
Auditoría.

Criterios:

Tenant inexistente: 404.
Reason corta: 400.
Stop correcto.
Logs correctos.
FASE 9 — Audit log

Crear tabla si falta:

admin_audit_log

Campos:

id
actor_id
action
tenant_id
target_type
target_id
reason
metadata_json
ip_address
user_agent
created_at

Registrar:

impersonation_started
impersonation_stopped
tenant_plan_updated
tenant_status_updated

Crear:

GET /console/api/myownclone/admin/audit-log

Criterios:

Cada acción sensible deja rastro.
El panel muestra auditoría.
No hace falta consultar DB manualmente.
FASE 10 — Design tokens

Tareas:

Crear tokens CSS.
Configurar light default.
Configurar dark variant.
Configurar fuentes.
Configurar Tailwind si aplica.
Evitar hardcode masivo.

Criterios:

Light completo.
Dark completo.
No hay pantallas solo dark.
No hay colores sueltos incoherentes.
FASE 11 — AppShell global

Tareas:

Crear AppShell.
Crear Sidebar.
Crear Topbar.
Crear SectionHeader.
Crear mobile nav/drawer.
Aplicar en admin y dashboard.

Criterios:

Desktop con shell redondeado.
Mobile sin sidebar fija.
Navegación coherente.
No rompe rutas.
FASE 12 — Componentes base

Crear/adaptar:

DashboardCard
MetricCard
ActionCard
IntegrationCard
StatusBadge
SearchCommandBar
DataTable
MobileListRow
EmptyState
LoadingState
ErrorState
FormPanel
Modal/Dialog
Toast/Notification
ChartCard

Criterios:

Reutilizables.
Light/dark.
Responsive.
Accesibles.
Sin estilos duplicados innecesarios.
FASE 13 — Admin UI

Rediseñar:

replica/src/app/admin/layout.tsx
replica/src/app/admin/resumen/page.tsx
replica/src/app/admin/tenants/page.tsx
replica/src/app/admin/feedback/page.tsx

Criterios:

Overview con charts/cards.
Tenants con tabla desktop/list rows mobile.
Feedback con tabla/lista.
Audit preparado.
Loading/error/empty.
Contratos actualizados.
FASE 14 — Dashboard usuario

Implementar:

Workspace Overview.
Stats.
Clone Activity.
Inbox preview.
Knowledge coverage.
Quick actions.
Onboarding banner.
Avatar ring.
Tooltips.
Badge New en Analíticas.

Criterios:

No landing.
Dashboard usable.
Mobile 2x2 quick actions.
Count-up.
Empty states.
FASE 15 — Resto de pantallas

Aplicar sistema a:

Inbox
Library
Memory Core
Analytics
Billing
Settings
Onboarding
Login
Register
Public clone pages

Criterios:

Misma línea visual.
No quedan pantallas antiguas.
Responsive.
Estados completos.
FASE 16 — Responsive

Validar:

375px
768px
1024px
1440px

Revisar:

Overflows.
Textos cortados.
Cards rotas.
Tabs.
Tablas.
Gráficas.
Sidebar.
Topbar.
Modales.
Formularios.
FASE 17 — Accesibilidad

Checklist:

Botones con texto o aria-label.
Tooltips con hover/focus.
Focus-visible.
Contraste.
Navegación teclado.
No depender solo del color.
Reduced motion.
Labels en formularios.
Estados de error visibles.
FASE 18 — Tests y build

Backend:

cd api
python -m pytest

Frontend:

cd replica
npm run lint
npm run typecheck
npm run test
npm run build

Si algún comando no existe:

Revisar package.json.
Usar equivalente.
Documentar bloqueo exacto.

Criterios:

Lint pasa.
Typecheck pasa.
Build pasa.
Tests pasan o deuda preexistente documentada.
No hay errores de consola.
Rutas admin críticas probadas.
30. QA FINAL OBLIGATORIO

No marques nada como terminado sin revisar.

Backend
 Modelos reales o imports correctos.
 Auth admin unificada.
 overview funciona.
 tenants paginado.
 tenant detail funciona.
 tenant patch auditado.
 feedback funciona.
 impersonate seguro.
 stop impersonate correcto.
 audit-log funciona.
 401 probado.
 403 probado.
 200 probado.
 Backend caído probado.
 No secretos expuestos.
Frontend
 Proxy admin valida platform_admin.
 Proxy reenvía credencial correcta.
 Overview consume contrato.
 Tenants consume paginación.
 Feedback consume paginación.
 Error states reales.
 Loading states.
 Empty states.
 No mocks donde ya hay API real.
UI
 Light mode default.
 Dark mode completo.
 Shell institucional.
 Sidebar desktop.
 Mobile nav.
 Topbar.
 Breadcrumb.
 Section headers.
 Tabs responsive.
 Cards.
 Charts.
 Tables.
 List rows mobile.
 Badges.
 Buttons.
 Inputs.
 Modals.
 Toasts.
 Avatar.
 Quick actions.
 Onboarding banner.
 No cards dentro de cards.
 No landing dentro de app.
Responsive
 375px.
 768px.
 1024px.
 1440px.
 Sin overflow horizontal.
 Sin textos cortados.
 Tablas adaptadas.
 Gráficas legibles.
 Sidebar no rompe mobile.
Accesibilidad
 Aria labels.
 Focus visible.
 Keyboard nav.
 Contraste.
 Reduced motion.
 Estados no solo por color.
31. REGLAS DE NO HACER

No hagas esto:

No implementar todo de golpe.
No tocar UI antes de auditar backend si afecta admin.
No cambiar lógica de negocio sin necesidad.
No eliminar funcionalidades.
No romper autenticación.
No romper multi-tenancy.
No romper permisos.
No tocar base de datos salvo migración necesaria.
No modificar migraciones antiguas aplicadas.
No duplicar componentes.
No hardcodear colores por pantalla.
No dejar dark mode como único modo.
No mezclar planes españoles e ingleses en backend.
No devolver arrays planos si el contrato exige paginación.
No confiar en cookies si Flask espera Bearer.
No loguear tokens.
No exponer secretos.
No meter cards dentro de cards.
No usar fondos chillones.
No usar sombras pesadas.
No dejar pantallas antiguas mezcladas.
No marcar implementado sin revisión visual y funcional.
32. FORMATO DE ENTREGA FINAL

Al terminar, entrega un resumen con:

1. Fases completadas.
2. Archivos modificados.
3. Endpoints creados/modificados.
4. Componentes creados/modificados.
5. Pantallas revisadas.
6. Estado de cada pantalla:
   - Implementado
   - Parcial
   - Pendiente
   - Bloqueado
7. Comandos ejecutados.
8. Resultado de lint/typecheck/test/build.
9. Errores detectados.
10. Riesgos pendientes.
11. Recomendaciones de siguiente fase.
12. Confirmación de coherencia visual entre dashboard, admin, backend y vistas internas.
33. CONDICIÓN FINAL

El trabajo no está terminado hasta que:

Backend admin funcione.
Auth admin esté clara.
API admin tenga contratos estables.
Frontend consuma esos contratos.
Diseño global esté aplicado.
Light mode sea default.
Dark mode sea variante completa.
Todas las pantallas internas tengan la misma línea visual.
Responsive esté revisado.
Accesibilidad básica esté cubierta.
Build pase.
Tests pasen o bloqueo quede documentado.
IMPLEMENTATION_LOG.md esté actualizado.
Ninguna pantalla esté marcada como implementada sin revisión visual y funcional.