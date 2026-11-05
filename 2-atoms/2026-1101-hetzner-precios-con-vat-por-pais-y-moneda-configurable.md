---
id: 2026-1101-hetzner-precios-con-vat-por-pais-y-moneda-configurable
type: atom
certainty: solid
sources: [sources/2026-11-01-hetzner-cloud.md, sources/2026-11-03-hetzner-cloud.md]
links: ["[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1023-hetzner-cpx02-1-vcpu-5-99-al-mes]]", "[[2026-1023-hetzner-escalera-de-precios-y-salto-a-dedicados]]"]
---

## Claim
La captura del 2026-11-01 es la primera del corpus de Hetzner que incluye el panel de **"Choose your location settings"**, que permite fijar **idioma** (Deutsch / English / Français / Español), **moneda** (**€ EUR** o **$ USD**) y **país (VAT)**, con un botón "Save settings". Todos los precios que publica la página están marcados **"excl. VAT"** y la web advierte además de que su traducción automática ("Automatically translated by AI") puede introducir discrepancias.

## Why It Matters
Dos consecuencias concretas para el modelo de coste del vault. Primera: **el precio del suelo de Hetzner (€ 5,99/mes sin IVA) es una cifra ex-VAT dependiente del país del cliente**, de modo que el desvío real frente al presupuesto duro de ≤ €4/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]) se calcula sobre el precio con IVA del país de facturación, no sobre el 5,99 de lista — el 50 % de desvío que documenta ese átomo es el mínimo, no el valor final. Segunda: la existencia de un conmutador EUR/USD significa que **el "coste en euros" de cualquier referencia de precio del vault es una convención de presentación, no una característica del proveedor**, igual que la sección de idioma implica que las cifras en las páginas de Hetzner pueden no ser las que el lector ve por defecto. Es la misma caution sobre el coste marginal que aplica a las demás partidas del modelo de coste por asiento: cada partida del TCO hay que leerla en la convención de presentación que impone el proveedor, no en la que hereda el vault por inercia. Y tiene un segundo efecto: el bloque de cumplimiento que el vault usa para justificar pagar más a Hetzner ([[2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001]]) se publica en la misma página ex-VAT, de modo que la comparación "cumplimiento auditable frente a el más barato" del vault también depende del país de facturación que se configure.

## Nota de verificación
La captura **no publica ninguna tabla de precios en USD ni en EUR con IVA**, ni tipos de cambio, ni los tipos de IVA por país: solo el selector. La advertencia de traducción automática aparece también en la captura del 2026-11-01.

## 2026-11-03 — re-verificación
Fuente: `sources/2026-11-03-hetzner-cloud.md`. Esta captura **no renderiza el panel "Choose your location settings"**, de modo que no aporta datos nuevos sobre idioma, moneda o país (VAT) — pero sí confirma el efecto que este átomo documenta: **todos los precios publicados vienen marcados "excl. VAT"** ("€ 5.99 per month, excl. VAT", "€ 6.49 per month, excl. VAT", "€ 43.49 per month, excl. VAT", y el bloque de la calculadora "excl. VAT."). Aparece además el aviso de geolocalización ("We noticed you're browsing from a different part of the world. Switch to settings tailored to your location?"), presente también en las capturas del 10-22, 10-31, 11-01 y 11-02, lo que confirma que la página se sirve con una configuración regional por defecto que el lector no controla desde la propia URL. La consecuencia del átomo se mantiene: el precio de € 5,99 con el que el vault compara contra el presupuesto de ≤ €4/mes es **ex-VAT y dependiente del país de facturación** ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]), y esta captura sigue sin publicar tipos de IVA ni tabla en USD.
