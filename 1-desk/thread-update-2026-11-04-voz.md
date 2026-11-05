# Thread update — voz-y-transcripcion-deepgram-assemblyai (2026-11-04)

Archivo tocado: `3-threads/voz-y-transcripcion-deepgram-assemblyai.md` (único archivo modificado).
Fuentes leídas antes de escribir: `sources/2026-11-03-deepgram-pricing.md`, `sources/2026-11-03-assemblyai-pricing.md`.
Atomos leídos: los 8 nuevos del 2026-1103 + `2026-1102-assemblyai-tier-gratuito-185-horas-y-333-streaming`, `2026-1102-assemblyai-facturacion-mensual-sin-minimos-ni-contratos`, `2026-1031-deepgram-growth-4000-anuales-y-sobreconsumo-10`.

## Secciones añadidas

1. **§7 — "La captura del 2026-11-03: los precios no se mueven, el contrato comercial sí se desescrita"** (nueva subsección `###` dentro de "Key Ideas", justo antes de "## Open Questions"). Siete párrafos:
   - Estabilidad de Deepgram en cuatro capturas (10-31, 11-01, 11-02, 11-03): cifras idénticas; solo cambia la superficie textual.
   - Estabilidad de AssemblyAI medida **solo para Pre-recorded** (mismos importes que 11-01 y 11-02).
   - Tercer escalón de AssemblyAI: columna "Custom" sin tarifa; suelo público $0,15/hr vs techo negociado.
   - Deepgram Enterprise: escalera no publicada + "custom model training" + "named account team" + umbral "millions of minutes a month".
   - Dos salidas de caja del prepago: reembolso de créditos no usados en 30 días (vía `consolebilling@deepgram.com`) y renovación anticipada que resetea el crédito y evita el +10 %.
   - Capabilities de modelo Nova (60+ idiomas, diarización, Smart Formatting, Keyterm Prompting) frente a líneas de precio de add-ons.
   - Los dos renderizados degradados (Deepgram: pierde enlaces y bloque de compliance, conserva precios/tablas/FAQ; AssemblyAI: solo Pre-recorded, resto como "..."), con la regla de que `word_count` es indicador de extracción y no de cobertura.

2. **"Nota de método (capturas del 2026-11-03)"** — párrafo nuevo colocado justo antes de la nota de método preexistente (que se conserva intacta). Nombra las dos fuentes, declara que toda cifra es transcripción de página pública de precios, que **ninguna cifra se verificó contra contrato, factura ni panel de cliente**, mantiene explícita la distinción **medición vs claim** (claims entre comillas: "Save up to 20 %", "millions of minutes a month", "ladders down with committed volume", "enhanced concurrency") y advierte que **el rendering reducido del 11-03 no debe leerse como retirada de precios** (ausencia de dato en la captura ≠ precio retirado; la fuente vigente del catálogo no renderizado de AssemblyAI sigue siendo `sources/2026-11-02-assemblyai-pricing.md`).

## Links añadidos (frontmatter `links:`)

Los 8 átomos nuevos, como cadenas entrecomilladas:
`[[2026-1103-deepgram-captura-11-03-rendering-reducido-y-sin-enlaces]]`, `[[2026-1103-deepgram-enterprise-descuentos-por-volumen-model-training-y-account-team]]`, `[[2026-1103-deepgram-nova-3-soporta-60-idiomas-con-diarizacion-smart-formatting-y-keyterms]]`, `[[2026-1103-deepgram-precios-estables-en-cuatro-capturas-consecutivas]]`, `[[2026-1103-deepgram-reembolso-de-creditos-no-usados-en-30-dias]]`, `[[2026-1103-deepgram-renovacion-anticipada-growth-resetea-creditos]]`, `[[2026-1103-assemblyai-captura-reducida-solo-pre-recorded-expandido]]`, `[[2026-1103-assemblyai-columna-custom-tercer-escalon-de-precios]]`.
Los links y sources previos se conservan íntegros.

## Fuentes añadidas (frontmatter `sources:`)

`sources/2026-11-03-deepgram-pricing.md`, `sources/2026-11-03-assemblyai-pricing.md` (las 4 anteriores se conservan).

## Frontmatter

`updated: 2026-11-03` → `updated: 2026-11-04`.

## Preguntas abiertas actualizadas in place

- **P1 (pre-recorded de Deepgram sin cifra)**: acotada, no cerrada. La cuarta captura reproduce las mismas pestañas Streaming/Pre-recorded con una sola columna y la misma frase "Pre-recorded runs lower"; dada la estabilidad de las cuatro capturas, la ausencia del dato es **omisión editorial estable de la página, no pérdida de extracción**.
- **P3 (coherencia interna de los catálogos)**: ampliada a Deepgram. La descripción de producto presenta Speaker Diarization y Keyterm Prompting como *capabilities* del modelo Nova y a la vez como líneas de precio; Smart Formatting queda "Included" sin contradicción. La incoherencia afecta a los dos catálogos, no solo a AssemblyAI.

Sin duplicar: no se creó ninguna pregunta nueva. P2, P4 y P5 no cambian con las capturas del 11-03.

## No colocado / pendientes

- **FRICTION de concurrencia de AssemblyAI** (`2026-1103-assemblyai-columna-custom-tercer-escalon-de-precios` vs `2026-1102-assemblyai-concurrencia-streaming-100-sesiones-por-minuto`): "enhanced concurrency" en la columna Custom vs "at no additional cost" en la FAQ. Es una fricción **entre átomos**, no entre thread y átomo, y no encaja en ninguna pregunta abierta existente (P4 trata el silencio en Voice Agent de Deepgram, tema distinto). Se ha resumido dentro de §7 (el escalón Custom ofrece "enhanced concurrency" como concesión comercial frente a la concurrencia de lista) sin abrir una pregunta nueva, para no duplicar ni falsear una pregunta ajena. Queda como candidata a pregunta abierta en una pasada posterior.
- **Hostname `api.eu.deepgram.com`**: el dato no se re-verifica con la captura del 11-03; no se ha modificado el átomo `2026-1101-deepgram-enterprise-selfhost-nvidia-y-endpoint-eu` (fuera del alcance de esta tarea). Consta en §7 y en la fricción del propio átomo nuevo.
- **Cifra del pre-recorded de Deepgram**: sigue sin existir en las fuentes; no se ha estimado ni rellenado.

## Errores

Ninguno.
