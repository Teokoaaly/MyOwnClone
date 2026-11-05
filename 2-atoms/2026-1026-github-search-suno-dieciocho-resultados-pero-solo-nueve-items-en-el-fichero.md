---
id: 2026-1026-github-search-suno-dieciocho-resultados-pero-solo-nueve-items-en-el-fichero
type: atom
certainty: solid
sources: [sources/2026-10-25-github-search-suno-openai.md]
links: ["[[2026-1024-github-search-catorce-resultados-y-el-universo-indexado-de-la-consulta]]", "[[2026-1026-github-search-cero-resultados-como-medicion-del-indice-y-no-de-la-realidad]]"]
---

## Claim
La consulta `GET /search/repositories?q=suno+openai+api` (captura del 2026-10-25) devuelve **`total_count: 18`** con `incomplete_results: false`, pero el fichero de fuente **solo contiene 9 objetos `item`**: 8 completos y un noveno (`mmmbankton/sunog-telegram-bot`) cortado a mitad de objeto, porque el fichero termina con la marca `..._This content has been truncated to stay below 50000 characters_...`. El noveno objeto conserva `name`, `full_name`, `description`, `created_at`, `updated_at`, `pushed_at` y `fork`, pero **no conserva `stargazers_count`, `forks_count`, `language`, `license`, `topics`, `size` ni `open_issues_count`**. Por tanto **18 es el tamaño del índice** y **9 es el tamaño de lo medible**: la mitad de los repositorios indexados no es medible con esta captura.

## Why It Matters
El vault ya tiene la regla de que toda cifra de repositorios es citable solo junto a su cadena de consulta exacta ([[2026-1026-github-search-cero-resultados-como-medicion-del-indice-y-no-de-la-realidad]]). Esta captura añade una segunda capa de caution: **la cadena de consulta tampoco basta**, porque el fichero puede llegar truncado al vault y el `total_count` no describe lo que hay en el JSON. Cualquier porcentaje de estrellas calculado sobre este corpus es un porcentaje **sobre los 8 items legibles**, no sobre los 18 indexados, y esa diferencia hay que declararla en el texto del átomo y no esconderla en una nota.
El caso del noveno objeto es el más instructivo: es un repositorio real, con descripción completa ("Telegram Mini App + Bot for AI song generation with FastAPI, React, OpenAI GPT-4, and Suno API") y con fechas verificables, pero **sin un solo contador de comunidad**. El vault puede afirmar qué dice y cuándo se movió; no puede afirmar cuánta gente lo mira.

## [FRICTION]
> [[2026-1024-github-search-catorce-resultados-y-el-universo-indexado-de-la-consulta]] (escrita el 2026-10-24) afirma que la consulta de registro de cuentas de ChatGPT devuelve "**el conjunto indexado por GitHub para esa frase es entero y cerrado en 14 repositorios**, no una muestra ni una cola truncada: no hay paginación pendiente", y de ello deduce que el corpus **puede** tratarse como población completa.
> Este átomo presiona esa afirmación desde el lado del fichero: en esta consulta el índice es de 18 repositorios y **el JSON entregado al vault contiene 9**. El corte no está en la API —`incomplete_results` es `false` y `total_count` es 18— sino en el guardado del fichero, que se detuvo en 50.000 caracteres. "Entero y cerrado" era una propiedad de *aquella* captura concreta, no una propiedad general del método.
> Ambas no pueden ser la misma regla: o `total_count` describe lo que el vault tiene delante, o no. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Recuento hecho con un script sobre `sources/2026-10-25-github-search-suno-openai.md`: se localizaron 9 inicios de objeto `{"id":`, de los cuales 8 se parsean con `json.JSONDecoder().raw_decode` y el noveno lanza `JSONDecodeError` en el carácter 49.999. La ausencia de los campos de contadores en el noveno se verificó por búsqueda de clave sobre el fragmento restante. Ningún dato fue estimado a ojo.
