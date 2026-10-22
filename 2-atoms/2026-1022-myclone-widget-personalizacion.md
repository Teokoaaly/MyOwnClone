---
id: 2026-1022-myclone-widget-personalizacion
type: atom
certainty: solid
sources: [raw/articles/myownclone-technical-deep-dive-2026-06-23.md, raw/articles/myclone-deep-api-osint-2026-06-24.md]
links: ["[[2026-1022-myclone-widget-embed-modos]]", "[[myownclone]]", "[[myownclone-competitors]]"]
---
## Claim
El widget de MyClone.is expone una superficie de personalización verificada con valores por defecto explícitos: theme (primary `#f59e0b`, background `#fff4eb`, text `#4c6eb8`, secondary text `#374151`, user message bg `#3b82f6`, bot message bg `#ffffff`), tamaños (modal 420×700, overlay centrado 900×820, border radius 16px, botón burbuja 60px, offsets 20px), layout (posición burbuja en 4 esquinas, modal bottom-right o centrado, estilos `guide`/`minimal`/`classic` con `guide` recomendado) y branding (título/subtítulo, avatar custom, icono de burbuja, texto de burbuja, mensaje de bienvenida, toggles de avatar, AI branding, voice chat y modo simple sin animaciones).

## Why It Matters
El informe califica esto como uno de los 7 puntos fuertes de MyClone.is ("Widget Altamente Customizable — 5 pestañas con vista previa en vivo → reduce fricción de integración"). El nivel de detalle (hex defaults, píxeles exactos, estilos de chat nombrados) es exactamente el tipo de guía de marca que un embed necesita para no romper la web del cliente — una gap que [[myownclone]] no cubre hoy. El toggle "Modo Simple" (desactivar animaciones) aparece también como palanca de rendimiento/accesibilidad.

## Extensión (API OSINT 2026-06-24)
`GET/PUT /api/v1/users/me/widget-config` expone el **objeto de configuración completo del widget tal y como se persiste**, no solo lo que muestra el panel. Confirma los mismos defaults (`primaryColor #f59e0b`, `backgroundColor #fff4eb`, `textColor #4c6eb8`, `userMessageBg #3b82f6`, `botMessageBg #ffffff`, `borderRadius 16px`, `bubbleSize 60px`, `chatbotWidth 420px`, `chatbotHeight 700px`, `offsetX/offsetY 20px`, `position bottom-right`, `chatbotStyle guide`, `showBranding true`, `enableVoice true`, `showAvatar true`, `simpleBubble false`) y añade campos no mencionados antes: `modalPosition`, `headerTitle`, `headerBackground` (`rgba(255,255,255,0.8)`), `textSecondaryColor #374151`, `botMessageTextColor #1f2937`, `userMessageTextColor #ffffff`, `bubbleBackgroundColor #f59e0b`, `bubbleTextColor #ffffff`, `personaName "default"` y `welcomeMessage`. El sistema de tokens (`GET,POST /users/me/widget-tokens`, `DELETE .../{token_id}`) usa el prefijo **`wgt_`** y guarda `name`, `description`, `is_active` y `last_used_at` — es decir, los tokens son **rotables y rastreables por uso**, no credenciales opacas de un solo uso.
