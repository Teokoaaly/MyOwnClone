# Notas de extensión — captura `2026-10-25-noones-developer-api.md`

Fuente: `sources/2026-10-25-noones-developer-api.md` (`https://dev.noones.com/`, capturada 2026-10-25).
No se ha modificado ningún fichero de `2-atoms/`.

=== EXTEND 2-atoms/2026-1024-noones-superficie-publica-productos-y-dominios-espejo
## Nota de extensión 2026-10-26
El átomo afirma que la superficie pública de NoOnes expone un enlace **"API documentation"** que apunta a `dev.noones.com`, y lo lee como señal de "un modelo de integradores serio y no a un intermediario opaco" frente a HeroSMS. La captura del 2026-10-25 permite precisar **qué es exactamente `dev.noones.com`**: son **547 palabras de landing de marketing** —cuatro bullets ("Automate your trading", "Receive trade activity notifications", "Trade on behalf of your clients", "Automatically update offer margins"), cuatro bloques de caso de uso con su "Read more" y un selector "Choose Your Format" con dos CTA a `dev.noones.com/dashboard/direct-access` y `dev.noones.com/dashboard/delegated-access`. **No hay ni un endpoint, ni un esquema de autenticación, ni un rate limit, ni un precio, ni un SLA.** El botón "Get Started" apunta a `#chooseYourFormat`, un ancla de la misma página, no a un panel de referencia.

El matiz que la extensión añade sin contradecir el átomo: el enlace no está roto ni es decorado —el subdominio **funciona y responde con contenido**—, pero lo que se enlaza desde el pie no es "documentación", sino **el escaparate de dos formatos de acceso**, y lo técnico vive detrás del login. La distinción que conviene conservar es, por tanto, entre "hay un sitio propio para desarrolladores" (cierto, y sigue siendo una diferencia real con HeroSMS, que no publica ni el suyo) y "hay documentación técnica accesible" (no verificable con esta captura).

Ver también: [[2026-1026-noones-dev-noones-sin-precios-ni-limites-ni-documentacion-publica]] y [[2026-1026-noones-api-dos-formatos-directo-y-delegado]].
=== END

=== EXTEND 2-atoms/2026-1024-noones-publicar-ofertas-y-visa-virtual-exigen-id
## Nota de extensión 2026-10-26
La captura de la API de desarrollador añade un dato que este átomo no podía tener: entre los cuatro bullets de cabecera de `dev.noones.com` está **"Automatically update offer margins"**, y otro es **"Trade on behalf of your clients"**. Es decir, el proveedor **invita explícitamente a un tercero a automatizar el lado vendedor** del marketplace —el lado que este átomo describe como atado a identidad documentada por usuario (Publish Offers = No en L1, Yes desde L1+; Visa virtual = ID completo).

Lo que la extensión deja **sin resolver**, y que conviene tener presente al releer este átomo: la captura **no publica los scopes delegables**, ni dice si la capacidad de publicar ofertas y la de emitir Visa virtual **heredan el nivel de verificación del usuario delegante** o si se concede a la app instalada, ni si esos permisos pueden compartirse entre usuarios de una misma app. La escalera L1→L3 ([[2026-1024-noones-escalera-de-verificacion-l1-l1plus-l2-l3]]) sigue siendo la descripción válida de lo que la plataforma **publica**; lo que la API añade es la figura de un actor que opera **en nombre de** varios usuarios verificados, y cuyo alcance no está documentado.

Ver también: [[2026-1026-noones-trade-en-nombre-de-tus-clientes-como-modelo-de-negocio]] y [[2026-1026-noones-acceso-delegado-app-instalada-por-el-usuario]].
=== END
