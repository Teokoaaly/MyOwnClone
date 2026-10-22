---
id: 2026-1022-arquitectura-rac-tres-modos-por-clon
type: atom
certainty: tentative
sources: [raw/articles/myownclone-founder-transcript.md, raw/articles/myownclone-frontend-recon.md]
links: ["[[retrieval-augmented-cognition]]", "[[myownclone]]", "[[ai-clones]]", "[[2026-1022-admin-rutas-bilingues-sin-subdominio]]", "[[2026-1022-soporte-al-cliente-separado-y-escalado]]"]
---

## Claim
La arquitectura de [[myownclone]] es "RAC" (retrieval sobre base de datos vectorizada) con tres modelos por clon —aprendizaje, soporte al cliente y ventas— y el founder reconoce que la diferencia con [[delphi]] no está en la tecnología base sino en ser "mucho más granular" en esos modos.
> "creas un RAC. un RAC es un retrival, o sea, en vez de una base de datos normal y corriente, es una base de datos vectorizada que el clon lo que hace es antes de responder… el clon tiene un modelo de lenguaje que lo que hace es yo le inyecto eh proms por encima antes de que hable la persona y lo que hace eso es el retribal de tu información por detrás… Yo lo que he hecho es ser mucho más granular y cada clon tiene como tres modelos. Uno es el de aprendizaje, otro es el de soporte al cliente y otro es el de ventas."

## Why It Matters
[[retrieval-augmented-cognition]] ya describe el mecanismo RAC; este átomo lo aterriza al modelo de producto y lo enlaza con la comparación de [[delphi]]: la granularidad de los tres modos es la respuesta directa a un clon único que no sabe si debe enseñar, vender o dar soporte. Vincula con [[ai-clones]], donde la tabla de modos y retrieval paths separados recoge esta misma estructura. El recon de bundles confirma que los tres modos no son un concepto abstracto sino secciones reales del panel: `/admin/brain` separa el corpus en cuatro subespacios (`/knowledge`, `/products`, `/support`, `/terms`, con alias ES `/conocimiento`, `/productos`, `/soporte`, `/terminos`) y `/admin/identity` tiene subsecciones para purpose, style y voice-call — cada silo del RAC tiene su corpus y su configuración — ver [[2026-1022-admin-rutas-bilingues-sin-subdominio]] y el routing de soporte de [[2026-1022-soporte-al-cliente-separado-y-escalado]].
