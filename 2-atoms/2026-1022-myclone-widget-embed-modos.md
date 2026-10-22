---
id: 2026-1022-myclone-widget-embed-modos
type: atom
certainty: solid
sources: [raw/articles/myownclone-technical-deep-dive-2026-06-23.md, raw/articles/myclone-deep-api-osint-2026-06-24.md]
links: ["[[2026-1022-myclone-widget-personalizacion]]", "[[2026-1022-myclone-widget-comunicacion-websocket]]", "[[myownclone]]", "[[2026-1022-myclone-custom-domains-whitelabel]]"]
---
## Claim
El widget de MyClone.is se distribuye como script externo `https://app.myclone.is/embed/myclone-embed.js` con una config objeto (mode, expertUsername, personaName, widgetToken, position, primaryColor, bubbleText, enableVoice, welcomeMessage, layout) e idempotencia de carga (comprueba `window.MyClone` antes de inyectar el script). Soporta 3 modos de embed: `bubble` (default, botón flotante que abre modal), `inline` (se inserta en el flujo HTML) y `fullpage` (ocupa toda la página). En el plan Free solo está disponible el modo `bubble`; `inline` y `fullpage` exigen Pro+, igual que el `widgetToken`. Frameworks declarados como soportados: HTML, Next.js, React (TS/JS), Vue, Astro, WordPress, Wix, Hostinger.

## Why It Matters
El embed es la superficie de integración que [[myownclone]] no documenta en su panel de admin (`entities/myownclone.md` lista `/admin/library`, `/admin/brain`, `/admin/learning`… pero ningún widget). El modo `fullpage` con landing dedicada y los tokens separados por plan son el tipo de decisión que [[myownclone-competitors]] señala como territorio de Personify ("embed en Kajabi, Thinkific…"), así que MyClone.is entra en el mismo terreno de integración.

## Extensión (API OSINT 2026-06-24)
La API confirma la existencia de la configuración de widget **en el backend del creator**, no solo en el embed: `GET,PUT /users/me/widget-config` (objeto completo, ver [[2026-1022-myclone-widget-personalizacion]]) y `GET,POST /users/me/widget-tokens` + `DELETE /users/me/widget-tokens/{token_id}` para tokens `wgt_` rotables. El token es lo que une el widget en una web externa con el clon del creator, y puede servirse bajo **dominio propio del creator** gracias a `/custom-domains` (ver [[2026-1022-myclone-custom-domains-whitelabel]]). Además, la conversación se direcciona por **username** (`/personas/username/{username}/init-session`), no por UUID, lo que confirma que el embed solo necesita el username y el token.
