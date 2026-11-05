---
id: 2026-1026-suno2openai-la-cookie-se-copia-a-mano-del-navegador
type: atom
certainty: solid
sources: [sources/2026-10-25-suno2openai.md]
links: ["[[2026-1024-gptgrok2api-registro-protocolo-sin-navegador-y-captcha-solver-integrado]]", "[[2026-1026-github-search-suno-api-plus-pool-de-cuentas-y-captcha-comprado]]"]
---

## Claim
El apartado *"How to get cookie"* del README es una **imagen de captura de pantalla con una sola instrucción: "copy all content about the cookie"**. Es decir, **el ingreso de credenciales al pool es manual**: el operador abre el navegador con su sesión de Suno, copia el valor de la cookie a mano y lo introduce por el endpoint `PUT /<prefijo>/cookies`. No hay registro de cuentas, ni correo, ni captcha, ni proxy, ni rotación de identidad: el pool se llena con **cookies de sesiones que ya existen**, y la única ayuda documentada es el prefijo `COOKIES_PREFIX` y el `AUTH_KEY`.

## Why It Matters
Este es el dato que separa definitivamente esta categoría del corpus de registro de cuentas. En `gptGrok2api` la credencial **se fabrica**: registro por protocolo, correo temporal, captcha resuelto en navegador real dentro de Docker y rotación de proxy ([[2026-1024-gptgrok2api-registro-protocolo-sin-navegador-y-captcha-solver-integrado]]). En `suno-api-plus` la credencial **se compra**: el repo nombra YesCaptcha y 2Captcha ([[2026-1026-github-search-suno-api-plus-pool-de-cuentas-y-captcha-comprado]]). Aquí la credencial **se recoge**: es trabajo manual de copiar y pegar.
Las tres son coste variable de capacidad, pero **con curvas y precios distintos**. El captcha es $/1000 y escala lineal; el registro automatizado escala con CPU y altas simultáneas; **la recolección manual escala con el tiempo humano del operador**, no con ningún catálogo. El vault no puede cotizar esta partida con lo que tiene, y esa ausencia es en sí misma el hallazgo: **hay una categoría de capacidad de IA cuyo insumo no tiene precio de lista, porque lo tiene el trabajo de una persona con una sesión abierta**.
Para el producto propio la lectura es incómoda y directa: un gateway de música autoalojado **no se escala con dinero, se escala con cookies ajenas**, y su rendimiento operativo está limitado por el cuello de botella humano del ingreso de credenciales.
