---
id: 2026-1026-rebrowser-npm-install-sobrescribe-los-parches-y-hay-que-reaplicarlos
type: atom
certainty: solid
sources: [sources/2026-10-25-rebrowser-patches.md]
links: ["[[2026-1026-rebrowser-parchea-el-codigo-fuente-porque-no-hay-configuracion-que-lo-arregle]]", "[[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]", "[[2026-1024-github-search-diez-de-catorce-se-pushearon-en-las-veinticuatro-horas]]", "[[2026-1024-github-search-catorce-resultados-y-el-universo-indexado-de-la-consulta]]"]
---

## Claim
El flujo de uso documentado es parchar el paquete **ya instalado** en `node_modules`: `npx rebrowser-patches@latest patch --packageName puppeteer-core` (o `--packagePath /ruta/al/paquete`), y revertir con `unpatch`. El README advierte de un efecto colateral explícito: **"after running `npm install` or `yarn install` in your project folder, it might override all the changes from the patches. You'll need to run the patcher again to keep the patches in place."** Para actualizar a la última versión de los parches, el procedimiento es **borrar `node_modules/puppeteer-core`, reinstalar y volver a aplicar el parche**.

## Why It Matters
Esta es la operación que convierte el "parcheo" en **un coste recurrente de operación**, y es el dato que el vault no tenía para cerrar la aritmética de esta partida. El parche **no vive en el repositorio del proyecto**: vive en `node_modules`, que es un directorio regenerable. Cualquier `npm install` en CI lo borra silenciosamente. Es decir, la dependencia es **de una calidad que ningún `package.json` puede expresar**: no hay forma de declararla en el manifiesto, no hay lockfile que la fije y no hay un test que falle si falta.

El contraste con el corpus de registro masivo del thread es directo y corrige una lectura que el vault tenía. El bot de Go arrastra **cuatro commits, cero releases y cero tags** contra 338 estrellas, y la única forma de consumirlo es `git clone` + `go run` desde `main` ([[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]); el corpus público de 14 repositorios está **parado: ninguno hizo push en los últimos 88 días** ([[2026-1024-github-search-diez-de-catorce-se-pushearon-en-las-veinticuatro-horas]]), sobre un total de **810 estrellas y 308 forks** ([[2026-1024-github-search-catorce-resultados-y-el-universo-indexado-de-la-consulta]]). La lectura que el vault saco de ahí era "el código abierto que implementa esto, no". Pero esta fuente muestra un proyecto abierto **activo, con releases y tags, 1.441 estrellas y 83 forks** cuyo problema de mantenimiento no es la inactividad, sino un detalle de cadena de suministro: **los parches se pierden en cada instalación**.

Las dos lecciones no son la misma: la del corpus de registro es "nadie mantiene esto", la de rebrowser es "el mantenimiento existe pero **no es idempotente frente al gestor de dependencias**". Para un vault que construye un pipeline, la segunda es un problema **operable** (un paso de postinstall) y la primera no lo es.
