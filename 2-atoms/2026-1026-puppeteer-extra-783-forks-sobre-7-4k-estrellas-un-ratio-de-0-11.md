---
id: 2026-1026-puppeteer-extra-783-forks-sobre-7-4k-estrellas-un-ratio-de-0-11
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-repo.md]
links: ["[[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos]]", "[[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]"]
---

## Claim
La cabecera da **7.4k estrellas y 783 forks**, un ratio forks/estrellas de **0,11** (783/7400 ≈ 0,106). Los ratios del corpus de fábricas de cuentas medidos en la búsqueda de GitHub eran de **0,51** en `gptGrok2api` (145/285), **0,50** en `wahdalo/chatgpt-account-creator` (69/139) y **0,27** en `verssache/chatgpt-creator` (90/338). Aquí el ratio es **2,6 a 4,8 veces menor**.

## Why It Matters
El vault interpretó un ratio alto (≈0,5) como la señal de "la gente copia y adapta en lugar de instalar y mantener", y un ratio bajo como el de "un proyecto que la gente consulta" ([[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos]]). Este caso consolida esa lectura desde el otro extremo: un framework de evasión con **604 commits, 559 tags y versionado por paquete** tiene un ratio de forks **muy bajo**, y la explicación que encaja es la de un proyecto **que se instala** (`npm install puppeteer-extra-plugin-stealth`) en lugar de uno que se clona.
La consecuencia práctica es de criterio de consumo: **el número de forks es un indicador del modelo de distribución**. Un ratio ≈0,5 sobre 4 commits (90 forks en `chatgpt-creator`) dice "código no publicable, se copia" ([[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]); un ratio 0,11 sobre 604 commits dice "hay un paquete, se instala y se fija por versión". Para un vault que documenta herramientas de evasión, distinguir **"se instala"** de **"se copia"** no es un detalle: lo primero se audita y se fija por versión, lo segundo se hereda sin control.
Nota de verificación: 7.4k es una **cifra redondeada por la propia GitHub** ("**7.4k** stars"), de modo que el ratio 0,11 es una aproximación; el cálculo es del vault sobre valores publicados. La captura no expone `stargazers_count` en entero ni el desglose de quién bifurca.
