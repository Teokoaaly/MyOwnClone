---
id: 2026-1022-live-verify-identidad-legal-y-diseno-reconstruidos
type: atom
certainty: solid
sources: [0-raw/archive/2026-10-23-2026-10-22-myownclone-live-reverification.md]
links: ["[[myownclone]]", "[[2026-1022-superficie-legal-publica-dpa-clon-terms]]", "[[2026-1022-i18n-es-first-jurisdiccion-es]]", "[[2026-1022-euge-oller-clon-personal-en-delphi]]", "[[2026-1022-tema-oscuro-css-variables]]"]
---

## Claim
La capa legal y de marca de [[myownclone]] ha sido reconstruida. El Aviso Legal es ahora **una sola página** en `/legal` (49.723 bytes, "Última actualización: 11 de mayo de 2026", diez secciones: datos identificativos, objeto, hosting, aceptación, propiedad intelectual, responsabilidad del usuario, naturaleza generativa, limitación de responsabilidad, modificaciones, legislación aplicable) y no seis documentos separados. La entidad es **Myownclone llc**, LLC de Wyoming, domicilio **30 N Gould St, Ste R, Sheridan, WY 82801**, y los **representantes legales son Jacinto Guzman II** — no Marea Kiss LLC ni Eugenio Oller. `contacto@myownclone.com` y `privacy@myownclone.com` son los contacts. `/en/legal` devuelve el mismo texto español, byte a byte. El namespace i18n `legal` en inglés sigue siendo un *placeholder* explícito: "This page is a production placeholder for the legal documents that should be reviewed with counsel before a public launch." El diseño cambia: la tipografía pasa de Poppins a **DM Sans** (JetBrains Mono se mantiene), la clave de tema pasa de `myownclone-theme` a `localStorage["theme"]` con valores `light`/`dark`/`system`, y el set de variables CSS es nuevo (`--bg-page`, `--text-primary`, `--text-muted`, `--text-secondary`, `--border-soft`, `--border-medium`, `--surface-2`, `--color-accent-violet`). El locale ya no es español-primero: `/`, `/es` y `/en` devuelven todos `lang="en"` y cuerpos byte-idénticos (49.386 bytes).

## Why It Matters
Tres cosas se rompen a la vez. La **identidad legal**: el vault atribuía la operación a Marea Kiss LLC y a Eugenio Oller; el Aviso Legal publicado nombra a Myownclone llc y a Jacinto Guzman II. El **idioma**: el producto ya no es español-primero, sino inglés con una ruta `/es` que no cambia nada. Y el **diseño**: el sistema de tokens es otro, así que cualquier átomo de tema (Poppins, `myownclone-theme`, `--brand-lime`) describe una versión anterior.

## [FRICTION]
> [[2026-1022-superficie-legal-publica-dpa-clon-terms]] afirma que "el footer público expone seis documentos legales" (Aviso Legal, Privacidad, Cookies, Términos, DPA y "Clone Terms") con versión inglesa en `/en/legal/*`; [[2026-1022-i18n-es-first-jurisdiccion-es]] afirma que "el sitemap duplica cada ruta bilingüe" y que el español es el idioma por defecto con `og:locale: es_ES`; [[2026-1022-euge-oller-clon-personal-en-delphi]] sitúa la operación en "la empresa Marea Kiss LLC (Wyoming)"; [[2026-1022-tema-oscuro-css-variables]] fija Poppins, la clave `myownclone-theme` y el set `--bg/--fg/--brand-lime/--radius`.
> Este átomo presiona las cuatro creencias: hay una sola página legal, `/en/legal` duplica el español en vez de traducirlo, la entidad publicada es Myownclone llc con representante Jacinto Guzman II, y el sistema de diseño usa DM Sans con `localStorage["theme"]` y otro set de variables.
> Todas pueden ser ciertas en su momento: el Aviso Legal se fecha el 11 de mayo de 2026, así que su contenido puede ser anterior a la migración a VPS de octubre. Lo que no cuadra es el idioma: `og:locale: es_ES` y `og:locale: en_US` ya no aparecen en la landing viva.
> Marcado para juicio humano, no auto-resuelto.
