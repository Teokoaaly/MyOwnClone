---
id: 2026-1026-veridrop-cero-gpt-puede-ser-permiso-key
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-openai-detection.md]
links: ["[[2026-1026-veridrop-profundidades-deteccion]]", "[[2026-1026-veridrop-firma-usage-field]]"]
---

## Claim
Cuando Veridrop muestra "0 modelos GPT disponibles", por lo general significa que la key no tiene permisos para los modelos GPT, no que el relay esté roto. Muchos middleboxes integran modelos de diferentes fabricantes (Claude, Gemini, etc.) y el usuario debe comprar el acceso correspondiente al modelo deseado. El sistema detecta esto al inicio y sugiere probar con los modelos disponibles para ese key.

## Why It Matters
Los usuarios a menudo asumen que "0 GPT models" significa que el relay dejó de funcionar o tiene un error. Este átomo aclara que es un estado esperado cuando la key no tiene ese permiso concreto. Evita que los usuarios pierdan tiempo buscando fallos en el relay cuando la causa es simplemente la configuración de permisos de su key. El sistema ofrece un mensaje directo: "estas key solo pueden usar X modelos Claude, ¿ir a probar allí?".

## [FRICTION]
> Ninguna fricción directa con átomos existentes, ya que esta aclaración operativa no existía previamente en el vault y no contradice ninguna creencia almacenada. Es conocimiento nuevo derivado de la captura, sin conflicto con átomos previos.