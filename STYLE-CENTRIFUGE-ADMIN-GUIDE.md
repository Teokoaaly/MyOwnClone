# Guia de estilo global: MyOwnClone Institutional Console

## Objetivo

Aplicar a **todo MyOwnClone** un lenguaje visual inspirado en dashboards financieros premium: claro por defecto, responsive, elegante, denso y muy legible. El estilo debe servir para Admin, dashboard principal, inbox, biblioteca, cerebro/memoria, analiticas, facturacion, configuracion, onboarding, login/register y paginas publicas del clon.

No copiar logos, marca ni contenido de la referencia. Recrear su sistema visual: shell institucional, jerarquia compacta, bordes finos, cards precisas, tablas/graficas protagonistas y microinteracciones sobrias.

## Nombre del estilo

**Institutional Console**

Descripcion:

> Una consola SaaS institucional, clara por defecto y oscura como variante, con informacion operativa presentada como software ejecutivo: superficies suaves, bordes finos, acentos luminosos controlados, tipografia precisa y jerarquia muy ordenada.

## Principios

- Light mode es el default.
- Dark mode existe como variante por tokens, no como rediseño separado.
- La UI debe ser responsive de verdad: desktop denso, tablet compacto, mobile apilado y navegable.
- La informacion debe parecer importante, no decorativa.
- Las graficas, tablas, listas y metricas son protagonistas.
- Nada de landing page dentro de pantallas internas.
- Nada de cards dentro de cards.
- Nada de textos largos explicando la interfaz.
- Nada de gradientes enormes que tapen la informacion.

## Sensacion visual

Debe sentirse:

- Premium.
- Financiera.
- Tecnica.
- Clara.
- Confiable.
- Compacta pero respirable.
- Moderna sin parecer juguete.

Evitar:

- Fondos chillones.
- Botones excesivamente grandes.
- Cards con radius exagerado.
- Iconos de marketing.
- Sombras blandas tipo template.
- Paletas de un solo color.
- Dark mode como unica experiencia.

## Paleta

### Light default

```css
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
```

### Dark variant

```css
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
```

Reglas:

- No hardcodear solo dark classes.
- Todos los componentes deben verse terminados en light.
- Dark se activa con `.dark` o preferencia de usuario.
- Los acentos se mantienen iguales en ambos modos, bajando opacidad cuando haga falta.

## Tipografia

Recomendacion:

- UI/cuerpo: `DM Sans`, `Inter` o `Geist Sans`.
- Numeros: `JetBrains Mono` o `Geist Mono`.
- Titulos: `DM Sans`/`Inter` peso 600-700, o `Syne` solo si se quiere un toque editorial.

Reglas:

- Titulos de pagina: 24-32px.
- Titulos de card: 16-20px.
- Labels: 12-14px.
- Numeros grandes: 24-36px.
- Numeros y porcentajes siempre en mono.
- No usar tracking negativo.
- Labels en gris; valores en color principal.

## Layout global

### Desktop

```text
Fondo ambiental claro
  Shell app redondeada
    Sidebar 220-260px
    Content
      Topbar 72px
      Main 24px
```

### Tablet

```text
Shell con radius menor
Sidebar colapsada o rail 72px
Topbar 64-72px
Cards en 2 columnas cuando quepa
Tabs con scroll horizontal
```

### Mobile

```text
Sin sidebar fija
Topbar compacta
Drawer o bottom nav
Main 16px
Cards en 1 columna
Tabs con scroll horizontal
Tablas convertidas en list rows/cards
Graficas con altura fija 260-320px
```

## Shell exterior

Light default:

```css
background:
  radial-gradient(circle at 8% 8%, rgba(249, 115, 22, 0.22), transparent 34%),
  radial-gradient(circle at 90% 85%, rgba(236, 72, 153, 0.16), transparent 34%),
  linear-gradient(135deg, #E7E1DE 0%, #D6D0CD 100%);
```

Dark variant:

```css
background:
  radial-gradient(circle at 8% 8%, rgba(249, 115, 22, 0.55), transparent 34%),
  radial-gradient(circle at 90% 85%, rgba(236, 72, 153, 0.42), transparent 34%),
  linear-gradient(135deg, #160F0D 0%, #070708 100%);
```

## Sidebar

Desktop:

- Ancho: `220px` a `260px`.
- Fondo light: `#FFFFFF`.
- Fondo dark: `#101011`.
- Border derecho fino.
- Search arriba.
- Nav central.
- Links auxiliares abajo.

Mobile:

- No usar sidebar persistente.
- Usar drawer o bottom nav.
- Mantener el mismo orden de navegacion.

Nav item activo light:

```tsx
className="
  flex h-11 items-center gap-3 rounded-lg border border-slate-900/[0.08]
  bg-[linear-gradient(90deg,rgba(249,115,22,0.14),rgba(255,255,255,0.88))]
  px-3 text-sm font-medium text-slate-900 shadow-sm
"
```

Nav item activo dark:

```tsx
className="
  flex h-11 items-center gap-3 rounded-lg border border-white/[0.08]
  bg-[linear-gradient(90deg,rgba(249,115,22,0.34),rgba(255,255,255,0.04))]
  px-3 text-sm font-medium text-white
"
```

Nav item normal:

```tsx
className="
  flex h-11 items-center gap-3 rounded-lg px-3 text-sm text-slate-500
  transition hover:bg-slate-900/[0.04] hover:text-slate-900
  dark:text-zinc-400 dark:hover:bg-white/[0.04] dark:hover:text-white
"
```

## Topbar

- Altura desktop: `72px`.
- Altura mobile: `56px` a `64px`.
- Fondo light: `#FFFFFF`.
- Fondo dark: `#111112`.
- Border bottom fino.
- Breadcrumb en desktop.
- En mobile, breadcrumb puede comprimirse a titulo corto.
- Acciones a la derecha.

Acciones por contexto:

- Admin: `Run Audit`, `Export`.
- Dashboard: `Create Clone`, `Sync Data`.
- Inbox: `Generate Draft`, `Archive`.
- Biblioteca: `New Source`, `Upload`.
- Analiticas: `Export`, `Refresh`.
- Configuracion: `Save`.

## Header de seccion

Usar patron comun:

```text
[icono gradiente] Titulo de seccion
Subtitulo breve opcional
Tabs/context actions debajo o al lado
```

Ejemplos:

- Admin: `MyOwnClone Admin`
- Dashboard: `Workspace Overview`
- Inbox: `Inbox`
- Cerebro: `Memory Core`
- Biblioteca: `Knowledge Library`
- Analiticas: `Analytics`
- Facturacion: `Billing`
- Configuracion: `Settings`

Tabs:

- Desktop: barra compacta.
- Mobile: scroll horizontal.

Tab activo light:

```tsx
className="
  rounded-md border border-slate-900/[0.08] bg-white px-4 py-2
  text-sm font-medium text-slate-900 shadow-sm
"
```

Tab activo dark:

```tsx
className="
  rounded-md border border-white/[0.08]
  bg-[linear-gradient(135deg,rgba(249,115,22,0.28),rgba(255,255,255,0.06))]
  px-4 py-2 text-sm font-medium text-white
"
```

## Cards

Light:

```tsx
className="
  rounded-2xl border border-slate-900/[0.08] bg-[#F8FAFC]
  p-5 shadow-[inset_0_1px_0_rgba(255,255,255,0.85)]
"
```

Dark:

```tsx
className="
  rounded-2xl border border-white/[0.08] bg-[#121213]
  p-5 shadow-[inset_0_1px_0_rgba(255,255,255,0.04)]
"
```

Reglas:

- Radius: `14px` a `18px`.
- Padding: `16px` mobile, `20-24px` desktop.
- Border siempre visible pero suave.
- Hovers maximo `translateY(-1px)` o `translateY(-2px)`.
- No meter una card grande dentro de otra card.

## Graficas

La grafica debe parecer producto financiero:

- Grid lines sutiles.
- Labels pequenos.
- Leyendas compactas con dots.
- Tooltips con border.
- Colores brillantes pero controlados.
- Fondo integrado con la card.

Series:

```css
--series-orange: #FB923C;
--series-amber: #FBBF24;
--series-pink: #EC4899;
--series-blue: #2563EB;
--series-cyan: #06B6D4;
--series-violet: #8B5CF6;
```

Graficas sugeridas por area:

- Admin: `MRR`, `Costs`, `Tenants`, `Audit events`.
- Dashboard: `Clone activity`, `Sessions`, `Automation rate`.
- Inbox: `Pending`, `Drafted`, `Resolved`.
- Biblioteca: `Sources`, `Chunks`, `Coverage`.
- Analiticas: `Questions`, `Gaps`, `Conversion`.
- Facturacion: `Usage`, `Limits`, `Cost`.

## Tablas y listas

Desktop:

- Tablas compactas.
- Header gris suave.
- Filas con border bottom.
- Numeros alineados a la derecha.
- Hover muy sutil.

Mobile:

- Convertir tablas en cards/list rows.
- Mostrar 3-5 campos clave.
- Acciones en menu o boton icono.
- No usar overflow horizontal salvo para tablas tecnicas inevitables.

Tabla light:

```tsx
<table className="w-full text-sm">
  <thead className="bg-slate-900/[0.035] text-xs uppercase text-slate-500">
    ...
  </thead>
  <tbody className="divide-y divide-slate-900/[0.07]">
    ...
  </tbody>
</table>
```

## Badges

Light:

```tsx
className="
  rounded-full border border-emerald-500/20
  bg-emerald-500/10 px-2.5 py-1 text-xs font-medium text-emerald-700
"
```

Dark:

```tsx
className="
  rounded-full border border-emerald-400/20
  bg-emerald-400/10 px-2.5 py-1 text-xs font-medium text-emerald-300
"
```

Estados:

- Active: emerald.
- Trial/New: cyan.
- Warning/Suspended: amber.
- Error/Cancelled: red muted.
- Enterprise/Admin: violet.

## Botones

Primario light:

```tsx
className="
  rounded-lg border border-orange-500/20
  bg-[linear-gradient(135deg,rgba(249,115,22,0.16),rgba(255,255,255,0.90))]
  px-4 py-2 text-sm font-medium text-slate-900 shadow-sm
  hover:border-orange-500/40 hover:shadow-[0_0_28px_rgba(249,115,22,0.16)]
"
```

Primario dark:

```tsx
className="
  rounded-lg border border-orange-300/20
  bg-[linear-gradient(135deg,rgba(249,115,22,0.34),rgba(120,53,15,0.35))]
  px-4 py-2 text-sm font-medium text-white
  hover:border-orange-300/40 hover:shadow-[0_0_28px_rgba(249,115,22,0.18)]
"
```

Secundario:

```tsx
className="
  rounded-lg border border-slate-900/[0.08] bg-white/70 px-4 py-2
  text-sm text-slate-700 hover:bg-white
  dark:border-white/[0.08] dark:bg-white/[0.05] dark:text-zinc-100 dark:hover:bg-white/[0.08]
"
```

## Estados vacios

Todo estado vacio debe tener:

- Icono.
- Titulo corto.
- Microcopy de una linea.
- Accion principal si aplica.

Ejemplo:

```text
No clones yet
Create your first AI clone to start capturing conversations.
[Create Clone]
```

No mostrar solo `0` o una tabla vacia.

## Muestra aplicada a MyOwnClone

### Admin Overview

Desktop:

```text
Sidebar 220-260px
Topbar 72px
Main 24px

Header:
  MyOwnClone Admin
  Tabs: Overview | Tenants | Clones | Usage | Feedback | Audit

Grid:
  Row 1:
    Platform Performance chart 2/3
    Operational Overview 1/3

  Row 2:
    Admin Actions 1/3
    Tenant Health table 2/3

  Row 3:
    Audit / Cost History full width
```

Mobile:

```text
Topbar compacta
Titulo + accion primaria
Tabs scroll horizontal
Platform Performance full width
Operational Overview full width
Admin Actions list
Tenant Health como list rows
Audit History como timeline/list
```

### Dashboard usuario

```text
Header:
  Workspace Overview
  CTA: Create Clone

Grid:
  Stats row: Clones | Sessions | Automation | Feedback
  Main chart: Clone Activity
  Inbox preview
  Knowledge coverage
  Quick actions
```

### Inbox

```text
Header:
  Inbox
  CTA: Generate Draft

Desktop:
  Left list of messages
  Right detail/draft panel

Mobile:
  Message list first
  Detail as route/modal/drawer
```

### Biblioteca

```text
Header:
  Knowledge Library
  CTA: New Source

Content:
  Source cards/list
  Ingestion status badges
  Coverage chart
  Empty state if no sources
```

## Prompt para otro modelo

```text
Rediseña todo MyOwnClone con el estilo "Institutional Console".

Debe ser claro por defecto, responsive y premium. La referencia es una consola financiera institucional: shell con marco redondeado en desktop, sidebar sobria, topbar con breadcrumb, header de seccion con tabs, cards con bordes finos, tablas/listas compactas y graficas como protagonistas.

Aplica el estilo a todas las areas: Admin, dashboard, inbox, biblioteca, cerebro/memoria, analiticas, facturacion, configuracion, onboarding, login/register y paginas publicas del clon. No hagas landing page dentro de pantallas internas.

Light mode default:
- Fondo exterior gris calido #D6D0CD con gradientes ambientales suaves.
- App shell #F8FAFC.
- Sidebar #FFFFFF.
- Topbar #FFFFFF.
- Cards #F8FAFC o #F1F5F9.
- Border rgba(15,23,42,0.08).
- Texto primario #334155.
- Texto secundario #64748B.
- Texto muted #94A3B8.

Dark mode opcional:
- App #070708/#0B0B0C.
- Sidebar #101011.
- Cards #121213.
- Border rgba(255,255,255,0.08).
- Texto primario #F4F4F5.

Acentos:
- Warm #F97316.
- Pink #EC4899.
- Blue #2563EB.
- Cyan #06B6D4.
- Violet #8B5CF6.
- Green #10B981.

Tipografia:
- DM Sans, Inter o Geist Sans para UI.
- JetBrains Mono o Geist Mono para numeros.
- Pesos 500/600; evita bold excesivo.

Responsive:
- Desktop: sidebar 220-260px, topbar 72px, main 24px.
- Tablet: sidebar colapsada o rail.
- Mobile: sin sidebar fija; usar drawer o bottom nav, topbar compacta, cards en 1 columna, tabs con scroll horizontal, tablas convertidas en list rows/cards.

Componentes:
- Shell global.
- Sidebar/Bottom nav.
- Topbar.
- Header de seccion.
- Tabs.
- Cards.
- Data cards.
- Charts.
- Tables desktop.
- List rows mobile.
- Badges translucidos.
- Estados vacios con icono + accion.

Interacciones:
- Hover sutil.
- Cards elevan maximo 1-2px.
- Botones con border glow controlado.
- Tooltips en icon buttons.
- Animaciones 160-220ms.
- Respetar prefers-reduced-motion.

No uses fondos solidos chillones, no uses cards dentro de cards, no uses textos largos explicativos ni elementos marketing dentro de la app. Todo debe sentirse como software ejecutivo real.
```

## Snippet base React + Tailwind light-first

```tsx
export function AppShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-[radial-gradient(circle_at_8%_8%,rgba(249,115,22,0.22),transparent_34%),radial-gradient(circle_at_92%_86%,rgba(236,72,153,0.16),transparent_32%),#D6D0CD] p-3 text-slate-700 md:p-8">
      <div className="mx-auto flex min-h-[calc(100vh-24px)] max-w-[1680px] overflow-hidden rounded-[18px] border border-slate-900/[0.10] bg-[#F8FAFC] shadow-[0_40px_120px_rgba(15,23,42,0.20)] md:min-h-[calc(100vh-64px)] md:rounded-[22px]">
        <aside className="hidden w-[220px] shrink-0 border-r border-slate-900/[0.08] bg-white p-5 md:flex md:flex-col">
          <div className="text-lg font-semibold tracking-wide text-slate-900">MyOwnClone</div>
          <div className="mt-8 rounded-lg border border-slate-900/[0.08] bg-slate-900/[0.025] px-3 py-2 text-sm text-slate-400">
            Search...
          </div>

          <nav className="mt-8 space-y-1">
            {["Overview", "Inbox", "Library", "Analytics", "Settings"].map((item, index) => (
              <a
                key={item}
                className={[
                  "flex h-11 items-center rounded-lg px-3 text-sm transition",
                  index === 0
                    ? "border border-slate-900/[0.08] bg-[linear-gradient(90deg,rgba(249,115,22,0.14),rgba(255,255,255,0.88))] text-slate-900 shadow-sm"
                    : "text-slate-500 hover:bg-slate-900/[0.04] hover:text-slate-900",
                ].join(" ")}
              >
                {item}
              </a>
            ))}
          </nav>
        </aside>

        <div className="flex min-w-0 flex-1 flex-col">
          <header className="flex h-[64px] items-center justify-between border-b border-slate-900/[0.08] bg-white px-4 md:h-[72px] md:px-6">
            <div className="text-sm text-slate-500">
              MyOwnClone / <span className="text-slate-900">Overview</span>
            </div>
            <button className="rounded-lg border border-orange-500/20 bg-[linear-gradient(135deg,rgba(249,115,22,0.16),rgba(255,255,255,0.90))] px-4 py-2 text-sm font-medium text-slate-900 shadow-sm">
              Create Clone
            </button>
          </header>

          <main className="min-w-0 flex-1 p-4 md:p-6">{children}</main>
        </div>
      </div>
    </div>
  );
}
```

## Checklist final

- [ ] El estilo se aplica globalmente, no solo Admin.
- [ ] Light mode es default.
- [ ] Dark mode existe como variante consistente.
- [ ] Shell exterior con gradiente ambiental suave.
- [ ] App clara dentro de marco redondeado en desktop.
- [ ] Sidebar desktop y navegacion mobile alternativa.
- [ ] Topbar responsive.
- [ ] Header de seccion reusable.
- [ ] Tabs con scroll horizontal en mobile.
- [ ] Cards con bordes finos.
- [ ] Graficas protagonistas.
- [ ] Tablas desktop compactas.
- [ ] List rows/cards en mobile.
- [ ] Numeros con fuente mono.
- [ ] Badges translucidos.
- [ ] Estados vacios con icono y accion.
- [ ] Hovers sutiles.
- [ ] Sin texto cortado ni solapado en 375px.

