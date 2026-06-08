# Plan maestro: Rediseño premium del dashboard MyOwnClone

## Objetivo

Rediseñar el dashboard de administración de IA **MyOwnClone** como una interfaz React + Tailwind con estética profesional, moderna y premium: editorial tech-luxury, oscura, sofisticada, densa pero respirable. El resultado debe sentirse como una startup SaaS de alto nivel, con calidad visual cercana a Stripe/Linear en modo oscuro.

Este documento está escrito para que un modelo más simple pueda ejecutar el trabajo paso a paso sin perder requisitos.

## Alcance funcional

Implementar o adaptar la pantalla principal del dashboard con:

- Sidebar estrecho de navegación.
- Header con breadcrumb.
- Cards de métricas con estado vacío y animación count-up.
- Quick actions en grid responsive.
- CTA/banner inferior con progreso de onboarding.
- Avatar con interacción premium.
- Tooltips en navegación.
- Badge `New` en Analíticas.
- Google Fonts.
- Tailwind como sistema principal de estilos.

No crear una landing page. La primera pantalla debe ser el dashboard usable.

## Stack esperado

- React.
- Tailwind CSS.
- Google Fonts:
  - `Syne` para títulos.
  - `DM Sans` para cuerpo e interfaz.
  - `JetBrains Mono` para números, métricas, contadores y porcentajes.
- Iconos:
  - Preferir `lucide-react` si ya existe en el proyecto.
  - Si no existe, instalarlo solo si el proyecto ya usa npm/pnpm/yarn y es razonable hacerlo.
  - Si no se puede instalar, usar iconos existentes del proyecto o componentes SVG simples y consistentes.

## Principios de diseño

### Dirección visual

Crear una interfaz de **minimalismo denso**:

- Pocos elementos, pero cada uno con peso visual claro.
- Mucho aire entre bloques principales.
- Bordes finos, sombras sutiles y profundidad controlada.
- Nada de bloques planos chillones.
- Nada de aspecto genérico de template.
- Nada de cards dentro de cards.

La UI debe sentirse:

- Premium.
- Técnica.
- Editorial.
- Precisa.
- Oscura, pero no apagada.
- Rica en microdetalles, no recargada.

### Paleta

Usar estas variables base:

```css
:root {
  --bg-base: #0A0A0F;
  --surface-card: #111118;
  --border-soft: rgba(255, 255, 255, 0.06);
  --primary-violet: #7C3AED;
  --primary-violet-light: #A855F7;
  --secondary-cyan: #06B6D4;
  --text-primary: #F1F5F9;
  --text-secondary: #64748B;
}
```

Aplicacion visual:

- Fondo general: `#0A0A0F`.
- Superficies: `#111118` con `border: 1px solid rgba(255,255,255,0.06)`.
- Primario: gradiente violeta `#7C3AED -> #A855F7`.
- Secundario: cyan `#06B6D4` para highlights de datos.
- Texto principal: `#F1F5F9`.
- Texto secundario: `#64748B`.
- Quick actions: no usar fondos solidos de color; usar glassmorphism sutil.

### Tipografia

Configurar Google Fonts en el entry global de la app:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">
```

Si la app gestiona fuentes desde CSS:

```css
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600;700&family=Syne:wght@600;700;800&display=swap');
```

Uso:

- Titulos: `font-family: "Syne", sans-serif;`
- UI/cuerpo: `font-family: "DM Sans", sans-serif;`
- Metricas: `font-family: "JetBrains Mono", monospace;`

Tracking:

- No usar tracking negativo.
- Titulos pueden usar tracking amplio sutil, por ejemplo `tracking-[0.02em]`.

## Layout maestro

### Estructura general

Usar un layout de dashboard con:

- `min-h-screen`.
- Fondo base oscuro.
- Sidebar fija o sticky en desktop.
- Contenido principal flexible.
- Padding generoso, pero sin desperdicio.

Propuesta:

```tsx
<div className="min-h-screen bg-[#0A0A0F] text-slate-100">
  <div className="flex min-h-screen">
    <Sidebar />
    <main className="flex-1 px-5 py-5 md:px-8 md:py-7">
      <Header />
      <StatsGrid />
      <QuickActions />
      <OnboardingBanner />
    </main>
  </div>
</div>
```

### Sidebar

Requisitos:

- Ancho desktop: `200px`.
- En movil: colapsar, ocultar o convertir en top/bottom navigation segun patron existente del proyecto.
- Logo arriba con gradiente animado tipo shimmer.
- Nav items con icono, texto y dot indicator de color.
- Tooltip descriptivo en cada item.
- Hover: background entra desde la izquierda.
- Item activo: borde/indicator violeta o cyan.
- `Analiticas` debe tener badge `New`.

Comportamiento visual:

- Sidebar background: ligeramente distinto del fondo base, por ejemplo `rgba(17,17,24,0.72)`.
- Border derecho: `1px solid rgba(255,255,255,0.06)`.
- Backdrop blur si encaja con el layout.

Micro-interaccion hover del item:

- Usar pseudo-elemento `before`.
- `before` empieza con `scale-x-0`.
- En hover pasa a `scale-x-100`.
- Origen de transformacion: izquierda.
- Duracion: 180-220ms.

Tooltip:

- Debe aparecer en hover/focus.
- Texto corto y util:
  - Dashboard: `Vista general`
  - Clones: `Gestiona tus agentes`
  - Analiticas: `Rendimiento e insights`
  - Ajustes: `Configura tu workspace`

### Header

Debe incluir:

- Titulo principal: `Dashboard`.
- Subtitulo corto y sofisticado, por ejemplo: `Control center for your AI workspace`.
- Breadcrumb sutil debajo o encima del titulo:
  - `MyOwnClone / Admin / Dashboard`
- Avatar de usuario a la derecha.

Avatar:

- Circular.
- En hover mostrar ring animado con gradiente violeta/cyan.
- Si no hay imagen real, usar iniciales.

No poner textos largos explicativos.

### Stats cards

Requisitos:

- 3 stats cards en una fila en desktop.
- En movil: una columna.
- Con separadores de borde.
- Sin background solido pesado.
- Glassmorphism:
  - fondo semitransparente.
  - blur.
  - border suave.
- Numeros con `JetBrains Mono`.
- Count-up animation al cargar.
- Estado vacio con iconografia, no solo `0`.

Metricas sugeridas:

1. `AI Clones`
   - Valor inicial: `0`
   - Icono: Bot/Brain/Sparkles.
   - Estado vacio: mostrar icono y texto breve `No clones yet`.
2. `Active Sessions`
   - Valor inicial: `0`
   - Icono: Activity/MessageCircle.
   - Estado vacio: `No active sessions`.
3. `Automation Rate`
   - Valor inicial: `0%`
   - Icono: Gauge/Zap.
   - Estado vacio: `Awaiting data`.

Implementacion count-up:

- Para datos reales: animar desde 0 hasta el valor.
- Para valores 0: no dejar la card muerta; mostrar icono vacio y microcopy.
- Evitar librerias nuevas si se puede implementar con `requestAnimationFrame`.

Pseudocodigo:

```tsx
function useCountUp(target: number, duration = 900) {
  const [value, setValue] = useState(0);

  useEffect(() => {
    let frame = 0;
    const totalFrames = Math.max(1, Math.round(duration / 16));

    function tick() {
      frame += 1;
      const progress = Math.min(frame / totalFrames, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      setValue(Math.round(target * eased));
      if (progress < 1) requestAnimationFrame(tick);
    }

    tick();
  }, [target, duration]);

  return value;
}
```

### Quick actions

Requisitos:

- Grid 2x2 en movil.
- Grid de 4 columnas en desktop.
- Cada card:
  - Icono grande estilizado.
  - Titulo corto.
  - Descripcion de una linea maximo.
  - Border glass.
  - Hover con `translateY(-4px)`.
  - Hover con glow del color del icono.
- No usar fondos solidos de color en las cards.
- Usar glassmorphism sutil.

Acciones sugeridas:

1. `Create Clone`
   - Icono: Plus/Bot.
   - Color: violeta.
2. `Train Memory`
   - Icono: Brain.
   - Color: cyan.
3. `Connect Sources`
   - Icono: Plug/Database.
   - Color: emerald o cyan controlado.
4. `Review Insights`
   - Icono: BarChart/Sparkles.
   - Color: amber suave o violeta claro.

Importante:

- El hover no debe romper layout.
- Definir dimensiones estables.
- En movil, asegurar que los textos no se pisen.

### CTA/banner inferior

Requisitos:

- Banner inferior con gradiente radial de fondo, no color flat.
- Debe incluir indicador de progreso de onboarding `0/4 pasos`.
- Debe sentirse como una pieza premium, no anuncio generico.
- CTA principal, por ejemplo `Complete setup`.
- CTA secundaria opcional, por ejemplo `View guide`.

Contenido sugerido:

- Titulo: `Finish your AI workspace setup`
- Texto: `Connect your first source, create a clone, train memory, and publish.`
- Progreso: `0/4 steps`
- Barra de progreso visual en 0%.

Fondo:

```css
background:
  radial-gradient(circle at 20% 20%, rgba(124, 58, 237, 0.32), transparent 34%),
  radial-gradient(circle at 80% 0%, rgba(6, 182, 212, 0.18), transparent 32%),
  rgba(17, 17, 24, 0.78);
```

## Componentes recomendados

Crear o adaptar componentes pequenos y claros:

- `DashboardLayout`
- `Sidebar`
- `SidebarItem`
- `Header`
- `Breadcrumb`
- `StatsGrid`
- `StatCard`
- `QuickActions`
- `QuickActionCard`
- `OnboardingBanner`
- `UserAvatar`
- `Tooltip`

No crear abstracciones si el proyecto ya tiene un sistema propio. Seguir siempre el patron local.

## Clases Tailwind sugeridas

### Superficie glass

```tsx
"border border-white/[0.06] bg-white/[0.035] backdrop-blur-xl shadow-[0_20px_80px_rgba(0,0,0,0.28)]"
```

### Texto

```tsx
"text-[#F1F5F9]"
"text-[#64748B]"
"font-['Syne']"
"font-['DM_Sans']"
"font-['JetBrains_Mono']"
```

Si Tailwind no acepta nombres con espacios en clases arbitrarias, configurar `tailwind.config.js`:

```js
theme: {
  extend: {
    fontFamily: {
      display: ['Syne', 'sans-serif'],
      sans: ['DM Sans', 'sans-serif'],
      mono: ['JetBrains Mono', 'monospace'],
    },
  },
}
```

Y usar:

```tsx
"font-display"
"font-sans"
"font-mono"
```

### Gradiente primario

```tsx
"bg-gradient-to-r from-[#7C3AED] to-[#A855F7]"
```

### Glow hover

```tsx
"hover:shadow-[0_18px_60px_rgba(124,58,237,0.22)]"
```

Para cyan:

```tsx
"hover:shadow-[0_18px_60px_rgba(6,182,212,0.18)]"
```

## Animaciones CSS

Agregar al CSS global o al archivo de estilos principal:

```css
@keyframes logo-shimmer {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

@keyframes avatar-ring {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.logo-shimmer {
  background-size: 220% 220%;
  animation: logo-shimmer 5s ease infinite;
}
```

Avatar ring:

- Crear contenedor relativo.
- Ring como pseudo-elemento o div absoluto.
- Animar solo en hover.
- Respetar `prefers-reduced-motion`.

Accesibilidad:

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    scroll-behavior: auto !important;
  }
}
```

## UX y accesibilidad

Checklist obligatorio:

- Todos los botones deben tener label visible o `aria-label`.
- Tooltips deben funcionar con hover y focus.
- Contraste suficiente entre texto y fondo.
- Navegacion usable con teclado.
- Estados `hover`, `focus-visible`, `active` consistentes.
- No depender solo del color para estado activo: usar dot, borde o forma.
- Textos cortos y escaneables.
- Nada de texto que se salga de botones/cards en movil.
- Respetar `prefers-reduced-motion`.

## Plan de implementacion paso a paso

### Paso 1: Inspeccion del proyecto

Antes de editar:

- Revisar estructura de archivos.
- Identificar framework exacto:
  - Vite React.
  - Next.js.
  - CRA.
  - Otro.
- Localizar:
  - Componente actual del dashboard.
  - CSS global.
  - Configuracion de Tailwind.
  - Sistema de iconos existente.
  - Datos/mock data de metricas.

Comandos sugeridos:

```bash
rg --files
rg "Dashboard|dashboard|Sidebar|Quick|Analytics|Analiticas" .
```

### Paso 2: Configurar fuentes y tokens

Hacer:

- Agregar Google Fonts.
- Configurar `tailwind.config.js` con familias:
  - `display`
  - `sans`
  - `mono`
- Agregar variables CSS si el proyecto usa CSS global.
- Mantener cambios pequenos y localizados.

Criterio de aceptacion:

- La app carga `Syne`, `DM Sans` y `JetBrains Mono`.
- Titulos, UI y metricas usan la fuente correcta.

### Paso 3: Reconstruir layout base

Hacer:

- Crear o adaptar `DashboardLayout`.
- Sidebar de 200px en desktop.
- Main area con padding responsive.
- Fondo base oscuro.
- Evitar hero/landing.

Criterio de aceptacion:

- Primera pantalla muestra dashboard real.
- No hay bloques visuales fuera de estilo.

### Paso 4: Implementar sidebar premium

Hacer:

- Logo con gradiente animado.
- Items con iconos.
- Dot indicators.
- Tooltip por item.
- Hover slide-in.
- Badge `New` en Analiticas.
- Estado activo claro.

Criterio de aceptacion:

- Sidebar ocupa 200px en desktop.
- Hover se siente fluido.
- Analiticas muestra `New`.
- Tooltips aparecen en hover/focus.

### Paso 5: Implementar header y breadcrumb

Hacer:

- Titulo `Dashboard`.
- Breadcrumb `MyOwnClone / Admin / Dashboard`.
- Avatar con ring animado en hover.

Criterio de aceptacion:

- Header queda alineado y no compite visualmente con stats.
- Breadcrumb es visible pero sutil.
- Avatar tiene interaccion premium.

### Paso 6: Implementar stats cards

Hacer:

- 3 cards responsive.
- Glassmorphism.
- Separadores de borde.
- Count-up.
- Empty states con iconografia.
- Numeros en JetBrains Mono.

Criterio de aceptacion:

- Desktop: 3 columnas.
- Movil: 1 columna.
- Valores 0 no se ven como fallo.
- Animacion no molesta.

### Paso 7: Implementar quick actions

Hacer:

- 4 acciones.
- Desktop: 4 columnas.
- Movil: 2x2.
- Icono grande.
- Hover lift + glow.
- No fondos solidos de color.

Criterio de aceptacion:

- Cards tienen dimensiones estables.
- No hay overflow de texto.
- Hover no desplaza otros elementos.

### Paso 8: Implementar onboarding banner

Hacer:

- Banner inferior con gradientes radiales.
- Progreso `0/4 steps`.
- Barra en 0%.
- CTA principal.
- CTA secundaria opcional.

Criterio de aceptacion:

- Banner no parece plano.
- El progreso se entiende inmediatamente.
- En movil no se rompe.

### Paso 9: Pulido responsive

Verificar:

- 375px ancho.
- 768px ancho.
- 1024px ancho.
- 1440px ancho.

Corregir:

- Overflows.
- Textos partidos mal.
- Cards demasiado altas/bajas.
- Sidebar inutil en movil.
- Contraste insuficiente.

### Paso 10: Verificacion final

Ejecutar:

```bash
npm run lint
npm run build
```

Si el proyecto usa otros comandos, revisar `package.json` y usar los equivalentes.

Si hay tests:

```bash
npm test
```

Solo dejar el trabajo como terminado cuando:

- Build pasa.
- Lint pasa o se documentan errores preexistentes.
- La UI se ve correcta en desktop y movil.
- No hay errores en consola del navegador.

## Criterios de aceptacion globales

El rediseño se considera completo si:

- Usa React + Tailwind.
- Usa Google Fonts solicitadas.
- Respeta la paleta exacta.
- Sidebar mide 200px en desktop.
- Logo tiene shimmer sutil.
- Hay breadcrumb bajo o junto al header.
- Hay badge `New` en Analiticas.
- Las 3 stats cards estan en una fila en desktop.
- Stats usan glassmorphism y separadores, no fondos solidos pesados.
- Stats tienen count-up y empty state con iconografia.
- Quick actions son 2x2 en movil y 4 columnas en desktop.
- Quick actions usan glassmorphism, iconos grandes y hover glow.
- Banner inferior usa gradiente radial.
- Banner muestra progreso de onboarding `0/4`.
- Avatar tiene ring animado en hover.
- Tooltips existen en nav items.
- No hay landing page.
- No hay fondos solidos de color en quick actions.
- No hay elementos superpuestos o texto cortado.
- La app compila.

## Riesgos comunes y como evitarlos

- **Demasiado morado**: usar cyan solo para highlights y variar neutrales; no saturar todo con violeta.
- **Glassmorphism ilegible**: subir contraste del texto y mantener bordes suaves.
- **Hover exagerado**: animaciones entre 160ms y 240ms, sin rebotes.
- **Fonts mal aplicadas**: comprobar que metricas usan mono y titulos usan Syne.
- **Mobile roto**: quick actions deben ser 2x2, stats una columna, sidebar adaptada.
- **Cards anidadas**: evitar meter secciones enteras dentro de cards.
- **Texto explicativo excesivo**: UI premium usa copy corto y especifico.
- **Instalar dependencias innecesarias**: preferir patrones y dependencias existentes.

## Entregables esperados

- Componentes React actualizados o creados.
- Estilos Tailwind/CSS global actualizados.
- Fuentes Google configuradas.
- Dashboard responsive terminado.
- Verificacion con build/lint.
- Breve resumen final indicando:
  - Archivos modificados.
  - Comandos ejecutados.
  - Cualquier limitacion o error preexistente.

