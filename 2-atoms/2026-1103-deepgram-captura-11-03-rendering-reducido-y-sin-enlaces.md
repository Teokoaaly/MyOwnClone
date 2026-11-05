---
id: 2026-1103-deepgram-captura-11-03-rendering-reducido-y-sin-enlaces
type: atom
certainty: solid
sources: [sources/2026-11-02-deepgram-pricing.md, sources/2026-11-03-deepgram-pricing.md]
links: ["[[2026-1103-deepgram-precios-estables-en-cuatro-capturas-consecutivas]]", "[[2026-1101-deepgram-enterprise-selfhost-nvidia-y-endpoint-eu]]", "[[2026-1031-deepgram-precios-por-minuto-por-modelo]]"]
---

## Claim
La captura de `deepgram.com/pricing` del **2026-11-03 es un rendering reducido** frente a las del 10-31 y 11-01/11-02 (8.060 bytes y ~950 palabras frente a 8.143 y 10.315-10.316 bytes): **pierde todos los enlaces markdown** ("Contact sales" deja de apuntar a `deepgram.com/contact-us`, "Log in" y "Sign up" dejan de apuntar a la Console), **elimina el bloque de compliance** ("Sweating compliance, so you don't have to", con las tarjetas SOC 2 Type 1 & 2, HIPAA, GDPR Ready & EU Data Residency, CCPA, PCI y la sección "How we protect voice data") y **colapsa la estructura de listas y encabezados** (los planes pasan de `## Pay as you go` a `- Pay as you go`, las preguntas de la FAQ de `###` a texto plano). Los precios, las tablas y el texto de la FAQ **sí se conservan íntegros**.

## Why It Matters
Es un aviso de método para el pipeline del vault: la diferencia de 8060 frente a 10315 bytes **no es una versión más corta de la página, es la misma página con menos instrumentación**, y confundirlas lleva a dos errores opuestos — dar por ausente un dato que sí está (los precios) o dar por ausente una sección que sí existe en la web (compliance, enlaces a la Console). Concreta: el hostname explícito del endpoint europeo (`api.eu.deepgram.com`) aparece en las capturas del 11-01 y 11-02 y **desaparece en esta**, aunque la FAQ siga listando "GDPR with an EU endpoint"; el átomo [[2026-1101-deepgram-enterprise-selfhost-nvidia-y-endpoint-eu]] conserva la cifra correcta y esta nota explica por qué no se pudo re-verificar el dominio exacto el 11-03. Regla operativa derivada: **el word_count de una captura es un indicador de extracción, no de cobertura de contenido**, y hay que comprobar contra el material una sección concreta antes de darla por perdida. La lectura transversal de la estabilidad de cifras está en [[2026-1103-deepgram-precios-estables-en-cuatro-capturas-consecutivas]].

## [FRICTION]
> [[2026-1101-deepgram-enterprise-selfhost-nvidia-y-endpoint-eu]] (escrita hace 2 días) afirma el endpoint europeo como `api.eu.deepgram.com` con "GDPR Ready & EU Data Residency" y cita como fuentes las capturas del 11-01 y 11-02.
> Esta nota presiona esa creencia porque **la captura del 11-03 no contiene ni el hostname ni el bloque de compliance**: solo la frase de la FAQ "GDPR with an EU endpoint". El dato del átomo no está refutado —está mejor documentado por las fuentes que ya cita—, pero queda demostrado que un mismo URL puede entregar material en dos niveles de detalle distintos según el día, y que el hostname exacto **no es re-verificable** con esta cuarta captura.
> Ambas no pueden ser la misma descripción de una página única: o el bloque de compliance se retiró de la web entre el 11-02 y el 11-03, o el extractor del 11-03 lo perdió. Marcado para juicio humano, no auto-resuelto.
