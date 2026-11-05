# Refinery Report — 2026-11-05

Run: 03:00 shift (scheduled cron). Fuentes capturadas por el Scout del 2026-11-04.

## Estado de partida

`0-raw/` contenía **15 punteros de captura** del 2026-11-04 (`Status: ready`), todos apuntando a `sources/2026-11-04-*.md`. Es la **quinta ronda consecutiva de los mismos 15 URLs** (capturados el 10-31, 11-01, 11-02, 11-03 y 11-04), lo que obliga a un tratamiento **incremental**: solo se atomiza lo que aporta información nueva, contradictoria o un delta de render identificable frente al corpus ya existente.

| Métrica | Valor |
|---|---|
| Capturas procesadas | **15** |
| Átomos nuevos | **76** (prefijo `2026-1104-`) |
| Átomos existentes extendidos | **40** (nota fechada al final, sin sobrescribir) |
| Átomos retirados a `2-atoms/archive/` | 0 |
| Bloques `## [FRICTION]` nuevos | **40** (en 40 de los 76 átomos nuevos) |
| Threads actualizados | **5** |
| Threads creados | 0 |
| Enlaces rotos introducidos | **0** (verificado: 0 de los wikilinks de los 76 átomos no resuelven) |
| Ficheros de `sources/` modificados | 0 |
| Capturas modificadas | 0 (movidas, no editadas) |
| Átomos eliminados | 0 |
| `0-raw/` al terminar | solo `reading-list.md` + `archive/` |

Todas las 15 capturas se movieron a `0-raw/archive/2026-11-05-2026-11-04-<nombre>.md`.

## Capturas procesadas

| # | Slug | Átomos nuevos | Atoms extendidos |
|---|---|---|---|
| 1 | `aiven-pricing` | 4 | 9 |
| 2 | `backblaze-b2-storage-pricing` | 4 | 3 |
| 3 | `cloudflare-r2-storage` | 4 | 1 |
| 4 | `digitalocean-droplets-pricing` | 3 (+1 `memphis`) | 2 |
| 5 | `hetzner-cloud` | 4 | 3 |
| 6 | `lambda-gpu-pricing` | 5 | 2 |
| 7 | `assemblyai-pricing` | 6 | 3 |
| 8 | `deepgram-pricing` | 5 | 2 |
| 9 | `twilio-sms-pricing` | 5 | 4 |
| 10 | `auth0-pricing` | 7 | 2 |
| 11 | `workos-pricing` | 7 | 3 |
| 12 | `clerk-pricing` | 7 | 0 |
| 13 | `tailscale-docs` | 6 | 4 |
| 14 | `azure-architecture-center` | 4 | 1 |
| 15 | `brightdata-pricing` | 4 | 1 |

## Threads actualizados

| Thread | Qué entró |
|---|---|
| `escala-de-hosting-barato-y-el-limite-de-4-euros` | §13 (13.1–13.7): Hetzner, DigitalOcean, Aiven, Backblaze B2, Lambda, Cloudflare R2 y el punto de método. `sources` 28→32, `links` 96→121 |
| `economia-de-la-verificacion-y-reventa-de-cuentas` | §15 (15.1–15.5): Auth0, WorkOS, Clerk, Twilio y la lectura para el producto. `sources` 29→33, `links` 142→168 |
| `voz-y-transcripcion-deepgram-assemblyai` | §8 (8.1 AssemblyAI, 8.2 Deepgram) + acotamiento de las preguntas abiertas 1 y 3. `sources` 6→8, `links` 38→49 |
| `myownclone-platform-architecture` | Sección nueva «La capa de red y de arquitectura de referencia» (Tailscale + Azure AC) antes de `## Fricciones abiertas`, **fricción 16** nueva, nota de método. `sources` 15→17, `links` 72→105 |
| `el-agregador-de-precios-como-producto` | §12 (12.1–12.4): Bright Data, la guía de cotización de Auth0, la comparativa Clerk↔Auth0 y el pipeline de captura. `sources` 12→15, `links` 82→101 |

## Hallazgos de la tanda

### 1. Único cambio de precio real: Lambda anuncia precios con vigencia el 16 de noviembre de 2026

Primera vez en el corpus de Lambda que la página trae un **anuncio de cambio con fecha**: las cuatro tablas de Instances repiten *"New prices take effect November 16, 2026, at 00:00 UTC."* Ninguna captura anterior (10-31, 11-01, 11-02) la contenía. Las cifras de la tabla **son las futuras**, no las facturables el 4 de noviembre. La tabla de precios nuevos **muestra las mismas cifras** que las capturas anteriores, de modo que el anuncio es deprocedure, no de subida ([2026-1104-lambda-anuncia-precios-nuevos-con-vigencia-el-16-de-noviembre-de-2026], [2026-1104-lambda-la-tabla-de-precios-nuevos-muestra-las-mismas-cifras-que-las-capturas-anteriores]).

### 2. Auth0 zanja la contradicción de columnas B2C/B2B

El render completo (4.068 palabras) **confirma** que `$35`/`$240` son **B2C** y `$150`/`$800` son **B2B**, es decir, la contradicción abierta desde el 2026-11-03 está resuelta a favor de la lectura por encabezado ([2026-1104-auth0-el-render-completo-confirma-que-35-y-240-son-b2c-y-150-800-son-b2b]).

### 3. El patrón dominante de la tanda: el render degradado del 11-03 fue un artefacto del extractor, no una retirada de oferta

En **7 de 15** slugs el render del 11-04 vuelve a ser completo, y en varios casos **byte a byte idéntico** a una captura anterior: Tailscale (= 11-02), Azure AC (= 11-02), Clerk (= 11-01), Twilio (= 11-01), Bright Data (= 11-01), AssemblyAI (= 11-02), Deepgram (= 11-01), Backblaze B2, DigitalOcean, Aiven. La consecuencia metodológica es la que ya estaba escrita en el vault y ahora queda **confirmada con un contraejemplo por lado**: una captura nueva no puede usarse para desmentir un átomo anterior solo porque el detalle no aparece. Además se documenta que el metadato `word_count` del frontmatter **no es fiable** como métrica de cobertura (Tailscale, Deepgram) mientras que sí lo es en Azure AC — lo que convierte ese campo en un indicador de pipeline, no de contenido.

### 4. Contradicciones internas nuevas, todas dentro de una misma página

- **Auth0**: el add-on de tokens M2M en Essentials B2B **choca con su propio feature matrix** ([2026-1104-auth0-m2m-addon-en-essentials-b2b-choca-con-el-feature-matrix]); Enterprise MFA está **incluido** en B2C Essentials pero es **add-on** en B2B Essentials ($100/mes, $250/mes con más); el Self-Service SSO aparece incluido en B2B Essential y Professional, contradiciendo el átomo del 11-01 que lo situaba solo en Free.
- **Clerk**: la tabla dice **cuota por app** y la FAQ dice cuota **global** ([2026-1104-clerk-cuota-por-app-en-la-tabla-pero-global-en-la-faq]); la FAQ dice **una** conexión enterprise y la tabla **dos** ([2026-1104-clerk-la-faq-dice-una-conexion-enterprise-pero-la-tabla-dos]); y Clerk **compara sus precios con Auth0 usando las cifras B2C**, que el vault mide como B2B ([2026-1104-clerk-compara-con-auth0-con-cifras-b2c-que-el-vault-mide-como-b2b]).
- **WorkOS**: los Annual Credits se describen **de dos formas distintas** en la misma página; la etiqueta *"Available for all accounts"* aparece descolada de la fila a la que corresponde.
- **Twilio**: el titular sin contratos choca con la sección de compromiso anual; el titular lleva un ciclo de cuatro días (11-01 → 11-02 → 11-03 → 11-01).
- **Aiven**: el marketplace nombra a Oracle pero la FAQ solo cita tres; nueve regiones seleccionables frente al claim de "100+".
- **Hetzner**: el ahorro medio cambia con operandos idénticos, y el `max/mo` volvió a un valor negativo (el "cero" del 11-03 no se repite).

### 5. Dos proveedores que el corpus no había visto

**DigitalOcean** publica ahora **Memphis** como décimo tercer datacenter en su FAQ de regiones. Y **Bright Data** es el caso límite: de las **ocho subpáginas de precio** que publica su hub, el vault solo ha capturado **una**, mientras el hub se recaptura todas las noches — argumento directo a favor de pausar los slugs sin cifras.

### 6. Auth0 vende la estructura de su propio precio

La página de Auth0 incorpora ahora una **guía de cotización en 7 pasos** con la fórmula literal *"Total = Base Price + sum of all applicable add-on prices"*. Y **Clerk publica una comparativa de precios contra Auth0** en su propia página. Los proveedores están empaquetando la estructura y la comparativa de precios como producto — el tema de fondo del thread del agregador.

## Fricciones para juicio humano

**40 bloques `## [FRICTION]`** en átomos nuevos. Las más relevantes:

| Átomo | Contradicción |
|---|---|
| `2026-1104-lambda-anuncia-precios-nuevos-...` | Las cifras publicadas son futuras (vigencia 16-11-2026); no son el precio facturable hoy |
| `2026-1104-auth0-m2m-addon-en-essentials-b2b-choca-con-el-feature-matrix` | Add-on de M2M contradice el feature matrix de la misma página |
| `2026-1104-auth0-self-service-sso-incluido-en-b2b-essential-y-professional` | Contradice [[2026-1101-auth0-sso-scim-en-free-pero-no-en-essentials-b2c]] |
| `2026-1104-clerk-cuota-por-app-en-la-tabla-pero-global-en-la-faq` | Tabla y FAQ del mismo proveedor, dos unidades de cuota |
| `2026-1104-clerk-la-faq-dice-una-conexion-enterprise-pero-la-tabla-dos` | 1 vs 2 conexiones |
| `2026-1104-clerk-compara-con-auth0-con-cifras-b2c-que-el-vault-mide-como-b2b` | La comparativa del proveedor usa cifras de otro segmento |
| `2026-1104-workos-annual-credits-se-describe-de-dos-formas-distintas` | Dos definiciones en la misma página |
| `2026-1104-workos-el-render-de-soporte-confirma-que-scale-no-incluye-revision-trimestral` | Resuelve a favor del 11-02 la fricción del plan Scale |
| `2026-1104-workos-la-etiqueta-available-for-all-accounts-se-descoloca` | Etiqueta desalineada respecto a su fila |
| `2026-1104-twilio-el-titular-sin-contratos-choca-con-la-seccion-de-compromiso-anual` | Titular ≠ sección de compromiso |
| `2026-1104-twilio-panhandle-telecom-aparece-en-los-dos-grupos-a-y-b` | $0,0108 o $0,0125 sin poder decidir |
| `2026-1104-aiven-nueve-regiones-seleccionables-frente-al-claim-de-100-mas` | El claim excede lo verificable |
| `2026-1104-aiven-el-marketplace-de-oracle-aparece-pero-la-faq-solo-nombra-tres` | Inconsistencia interna del catálogo |
| `2026-1104-hetzner-ahorro-medio-cambia-con-operandos-identicos-al-11-03` | El widget de ahorro no es reproducible |
| `2026-1104-hetzner-max-mo-vuelve-a-negativo-el-cero-del-11-03-no-se-repite` | El "cero" anterior fue un artefacto |
| `2026-1104-deepgram-el-conmutador-por-hora-nunca-publica-una-columna-por-hora` | Conmutador sin columna: el conmutador es decorativo |
| `2026-1104-deepgram-quinta-captura-sin-cambio-de-precio-y-faq-que-vuelve-a-la-formulacion-anterior` | La FAQ oscila entre dos redacciones |
| `2026-1104-assemblyai-universal-streaming-multilingual-sin-columna-de-add-ons` | Hueco de precio: el multilingüe no tiene columna de add-ons. Además el bloque señala que la pista del Scout ($0,12/hr, $0,04/hr) confundía precios de modelo con precios de add-on |
| `2026-1104-r2-testimonio-character-ai-multicloud-sin-egreso` | Testimonio sin escenario declarado |
| `2026-1104-brightdata-el-render-de-imagenes-alterna-y-la-captura-pierde-los-doce-logos` | El SVG inline vacío borra los logos: el render degradado es el estado mayoritario |
| `2026-1104-brightdata-dos-rutas-de-captura-producen-distinto-texto-de-la-misma-pagina` | Errata "requets" solo en la ruta markdown |
| `2026-1104-tailscale-la-frase-zero-trust-vuelve-a-renderizarse` | Desclasifica el átomo del 11-03 |
| `2026-1104-tailscale-ask-ai-solo-aparece-en-la-captura-del-11-03` | 1 de 5 capturas: artefacto, no función |
| `2026-1104-azure-architecture-center-el-word-count-si-cuadra-con-el-cuerpo-capturado` | Corrige la nota metodológica del 11-02 |
| `2026-1104-memphis-aparece-como-decimo-tercer-datacenter-en-la-faq-de-regiones` | Datacenter nuevo, sin ficha de precio |

Además, una fricción de nivel **thread** en `myownclone-platform-architecture` (nº 16): la capa de red es la única del stack sin ninguna base de coste, y se cierra con la regla de que la ausencia en una captura no es una retirada.

## Errores y cosas que requieren atención humana

1. **El pipeline de captura es la fuente dominante de ruido.** El 11-03 produjo renders degradados en al menos 7 slugs y el 11-04 los restauró. La recomendación operativa es **no leer ninguna captura como estado actual sin compararla byte a byte con la anterior**, y **no atomizar un "precio que ha desaparecido"**. Los átomos de esta tanda se han escrito con esa distinción explícita.
2. **Slugs que no aportan nada y se recapturan cada noche**: `brightdata-pricing` (hub sin cifras), `tailscale-docs` (KB sin cifras), `azure-architecture-center` (catálogo sin precios). Deberían pausarse o pasar a captura semanal, y en caso de Bright Data deberían capturarse las **siete subpáginas de precio** que nunca se han visitado, no el hub por quinta vez.
3. **`word_count` del frontmatter no es fiable** como métrica de cobertura (Tailscale declara 420 con 301 palabras reales; Deepgram, idem). No debe usarse para decidir si una captura está completa.
4. **Las cifras de Lambda en el corpus pasan a estar fechadas.** Cualquier referencia a "el precio de Lambda" anterior al 2026-11-16 debe marcarse como precio anterior.
5. **Nueve enlaces preexistentes sin resolver** en `myownclone-platform-architecture` (incluido `[[myownclone]]`), no introducidos por esta tanda.
6. **Ninguna cifra de esta tanda está verificada contra contrato, panel de cliente ni checkout.** Todas son transcripciones literales de páginas públicas de precios.

## Verificación

- 76 átomos nuevos: frontmatter YAML válido en los 76, con `id`, `type`, `certainty`, `sources` y `links`; `## Claim` y `## Why It Matters` presentes en los 76; `certainty` = `solid` en 69 y `tentative` en 7.
- 0 claims duplicados entre los 76 átomos.
- 0 wikilinks rotos en los 76 átomos (todos resuelven contra ficheros existentes de `2-atoms/`).
- 5 threads: frontmatter YAML válido, secciones nuevas en la posición correcta.
- 0 claves, tokens, passwords ni connection strings en átomos o threads (barrido por regex: los únicos aciertos son las palabras "token" en el sentido de *token de LLM* y nombres de variable como `WEAVIATE_API_KEY` en texto preexistente).

## Ficheros del run

- `1-desk/refinery-report-2026-11-05.md` — este informe.
- `1-desk/refinery-2026-11-05-contexto.md` — contexto compartido de la tanda (leído por los 15 subagentes), conservado como registro de las reglas de deduplicación aplicadas.
