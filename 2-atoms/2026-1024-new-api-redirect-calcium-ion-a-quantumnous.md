---
id: 2026-1024-new-api-redirect-calcium-ion-a-quantumnous
type: atom
certainty: solid
sources: [sources/2026-10-23-new-api-calcium-ion-redirect.md]
links: ["[[2026-1023-new-api-escala-adopcion-y-traduccion]]", "[[2026-1023-new-api-licencia-agplv3-y-atribucion-en-ui]]", "[[2026-1023-new-api-una-sola-api-multiproto]]", "[[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]]", "[[2026-1023-new-api-aviso-legal-para-reventa-publica]]", "[[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]]"]
---

## Claim
La URL `https://github.com/Calcium-Ion/new-api` **no sirve un repositorio propio**: GitHub la redirige a **`QuantumNous/new-api`**, que es el mismo proyecto con el **propietario renombrado**, no un repositorio separado. La captura del 2026-10-23 lo confirma en el propio HTML: los **enlaces internos apuntan a `github.com/QuantumNous/new-api`**, mientras el *badge* de **Star History sigue apuntando a `github.com/Calcium-Ion/new-api`** — la mezcla de ambas URLs es la firma de un cambio de propietario **reciente** a nivel de cuenta/organización.

El README completo del proyecto ya estaba capturado el 2026-10-22 en `sources/2026-10-22-new-api-github.md` y la nota de verificación del 2026-10-23 **no lo duplica**: solo registra lo que su propio HTML permite afirmar.

## Why It Matters
Para MyOwnClone esto es una **decisión de identificadores, no de producto**: la URL canónica del gateway que se quiere usar como relay (y cuyo motor de precios/routing se analiza en [[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]]) es hoy `QuantumNous/new-api`. Cualquier `OPENAI_API_BASE`, docker-compose, pin de versión o enlace de documentación del vault que se guarde con la ruta `Calcium-Ion/...` depende hoy de que GitHub **mantenga la redirección** — una redirección de repo, no un alias estable.

El riesgo operativo es de **trazabilidad de la contraparte**: el cambio de propietario es reciente, así que el historial del proyecto (issues, releases, debates) que el vault cite en [[2026-1023-new-api-escala-adopcion-y-traduccion]] se está moviendo de cuenta. Para quien dependa de un relay open-source de un tercero (DeepSeek como proveedor por defecto vía `OPENAI_API_BASE`), el nombre de la cuenta no es cosmético: es **la identidad contra la que se resuelve la confianza, los acuerdos y las incidencias** ([[2026-1023-new-api-aviso-legal-para-reventa-publica]]).

También fija un criterio de lectura para todo lo que el vault capturó con la URL antigua: las cifras y la licencia ([[2026-1023-new-api-licencia-agplv3-y-atribucion-en-ui]]) son las de `QuantumNous/new-api`, y el nombre "Calcium-Ion/new-api" debe tratarse como **alias histórico**.

## [FRICTION]
Contradicción con la captura del 2026-10-22 (`sources/2026-10-22-new-api-github.md`): aquel README contenía enlaces internos al owner antiguo — `LICENSE` raw en `raw.githubusercontent.com/Calcium-Ion/new-api/main/LICENSE`, `github.com/Calcium-Ion/new-api/issues`, `/releases` y el Star History — mientras la captura del 2026-10-23 dice que ya **todos los enlaces internos del repo apuntan a `QuantumNous/new-api`**. Es decir, **el README se editó para actualizar el owner entre el 22 y el 23 de octubre de 2026** y solo el badge de Star History quedó atrás. Consecuencia: las rutas `Calcium-Ion/...` que el vault tiene registradas (incluido el `research/MASTER-DEFINITIVO-2026-07.md`, que aún cita `https://github.com/Calcium-Ion/new-api` como repo de referencia) son **obsoletas por alias** — funcionan hoy solo mientras GitHub mantenga la redirección, y no son la referencia canónica.
