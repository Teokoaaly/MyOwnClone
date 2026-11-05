---
id: 2026-1026-rebrowser-repo-con-1441-estrellas-y-83-forks-un-ratio-de-0-06
type: atom
certainty: solid
sources: [sources/2026-10-25-rebrowser-patches.md]
links: ["[[2026-1026-puppeteer-extra-783-forks-sobre-7-4k-estrellas-un-ratio-de-0-11]]", "[[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos]]", "[[2026-1024-github-search-catorce-resultados-y-el-universo-indexado-de-la-consulta]]"]
---

## Claim
La cabecera del repositorio da **1.441 estrellas, 83 forks y 27 watchers**, con **6 releases y 6 tags**, rama por defecto `main`, y **creado el 2024-08-06**. El ratio forks/estrellas es **83/1.441 ≈ 0,058**, el más bajo que el vault ha registrado en esta familia: por debajo del **0,11** de `puppeteer-extra` (783 forks sobre 7,4k estrellas) y del **0,27** de `verssache/chatgpt-creator`, y entre 6 y 9 veces por debajo de los **0,50–0,51** de `gptGrok2api` y `wahdalo/chatgpt-account-creator` ([[2026-1026-puppeteer-extra-783-forks-sobre-7-4k-estrellas-un-ratio-de-0-11]], [[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos]]). Y un dato de escala que el vault no tenía: **1.441 estrellas es más que las 810 del corpus completo de 14 repositorios de registro de cuentas** ([[2026-1024-github-search-catorce-resultados-y-el-universo-indexado-de-la-consulta]]).

## Why It Matters
El ratio de forks/estrellas se había leído en el thread como **indicador del modelo de distribución**: 0,5 significa "la gente copia y adapta", 0,11 significa "la gente instala y fija por versión". Con 0,058 y **6 releases y 6 tags**, rebrowser-patches refuerza la lectura y la lleva al extremo: es un proyecto **que se instala y se versiona**, y encima **no se parchea a mano** —para eso están los paquetes drop-in y el alias de npm. Es decir, **el ratio más bajo de la familia corresponde al proyecto cuya vía de consumo es la más limpia**: dependencia declarada, versión fijada, `npm install`.

El dato de escala es el que reorganiza el thread. El corpus de registro masivo sumaba **810 estrellas en 14 repositorios**; rebrowser-patches, **un solo repo de una capa que no es la de registro**, tiene **1.441**. La lectura que eso fuerza es de **dónde está la atención pública**: la capa de elusión de navegador tiene **más atención pública que la capa de producción de cuentas**, y en el corpus de registro el 94,1 % de las estrellas estaba en tres repositorios. Es decir, **la parte del stack que nadie está dispuesto a publicar en abierto es la fábrica; la parte que sí se publica es la elusión**. La elusión es el componente con comunidad y releases; la fábrica es el componente con forks y sin mantenimiento.

Eso tiene una consecuencia operativa para el vault: **construir la fábrica es más difícil de publicar que construir la elusión**, porque la fábrica es el componente que viola los términos del proveedor y la elusión es solo "no detectado". Y explica por qué el bot de Go arrastra cuatro commits: no es falta de interés, es que el corpus de fábricas está inactivo por razones que no tienen que ver con la demanda ([[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos]]).
