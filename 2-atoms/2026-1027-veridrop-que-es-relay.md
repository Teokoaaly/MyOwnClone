---
id: 2026-1027-veridrop-que-es-relay
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-cinco-indicadores-duros-para-elegir-relay]]", "[[2026-1027-veridrop-tres-formas-de-dilucion-o-concubamiento]]"]
---

## Claim

Una **AI API 中转站** (relay, también llamado «镜像» o «代理») es un servicio de terceros que captura tu petición y la reenvía al API oficial de OpenAI / Anthropic / Google, devolviendo la respuesta original sin modificar. Las motivaciones principales son: (1) acceso desde regiones donde los dominios oficiales son inaccesibles, (2) precios minoristas hasta 70% más baratos al aglutinar múltiplos proveedores, y (3) una sola interfaz para múltiples proveedores de modelos. Veridrop define este concepto como la base para entender luego las diferencias de transparencia y fidelidad.

## Why It Matters

Este es el concepto fundamental que sustenta todo el resto de la FAQ: sin entender qué es un relay, no se pueden evaluar los riesgos de seguridad, los posibles fraudes de «bajada de calidad» ni las diferencias de protocolo. El vault aplica esta distinción para decidir cuándo es preferible conectar directamente al proveedor oficial y cuándo un relay es acceptable, balanceando costo versus confianza en la fidelidad de la respuesta.

## Nota de verificación

La definición es literal de la sección «中转站基础» de la FAQ. La captura no profundiza en las variantes técnicas de cada relay (ej. 1:1 pas-through vs. modificación de campos), que son materia de los detectores individuales de Veridrop.