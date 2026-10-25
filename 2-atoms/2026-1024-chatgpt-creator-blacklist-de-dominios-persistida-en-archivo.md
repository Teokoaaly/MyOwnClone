---
id: 2026-1024-chatgpt-creator-blacklist-de-dominios-persistida-en-archivo
type: atom
certainty: tentative
sources: [sources/2026-10-24-chatgpt-creator-verssache.md]
links: ["[[2026-1024-chatgpt-creator-correo-temporal-y-otp-automatico-con-generator-email]]", "[[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]", "[[2026-1024-chatgpt-creator-worker-pool-y-retry-hasta-alcanzar-la-meta]]"]
---

## Claim
Uno de los tres commits visibles del repositorio es **"feat: Persist domain blacklist to blacklist.json"**, y el cambio está asociado a la fila de **`.gitignore`**, no a un archivo de código versionado. Es decir: el bot **mantiene una lista de dominios de correo bloqueados y la persiste en `blacklist.json`, un archivo deliberadamente fuera del control de versiones** (con la regla de la contraseña por defecto, el directorio `internal/` y los archivos de código, lo versionado es el conjunto mínimo). El README **no menciona la blacklist en ninguna de sus secciones** —ni en Features, ni en Configuration, ni en Output Format—.

## Why It Matters
Es un **mecanismo de memoria operativa** del bot, y solo se ve por el mensaje del commit y por el `.gitignore`. Lo que hace es **recordar qué dominios fallan**: cuando el flujo de alta con un dominio de correo no llega a completarse, ese dominio se marca para no volver a intentarlo. Con el patrón de reintento del bot ([[2026-1024-chatgpt-creator-worker-pool-y-retry-hasta-alcanzar-la-meta]]) y con el generador de correo aleatorio ([[2026-1024-chatgpt-creator-correo-temporal-y-otp-automatico-con-generator-email]]), esa memoria es lo que convierte un bucle de reintentos en algo que converge.
La observación que importa para el vault es el patrón, no el archivo: **en un flujo automatizado de altas, la calidad de una partida de insumo —en este caso el dominio de correo— no es estable y hay que registrar sus fallos para no repetir el gasto**. Es el mismo tipo de aprendizaje que el thread documenta para el proxy, donde "los datos que no se consumen no se facturan" pero el tráfico que sí se consume lo decide el volumen por sesión, y donde la sesión sticky debe durar lo que la tarea: aquí el equivalente es un archivo local que recuerda el fallo. Un flujo de alta a escala necesita **memoria de fallos por insumo**, y el repositorio de referencia la implementa en doce líneas de JSON.
La lectura secundaria es de higiene: el `.gitignore` es lo que impide versionar la lista, lo que confirma que la blacklist es **estado local de la máquina que corre el bot**, no una configuración compartida. Dos operadores con el mismo repositorio empiezan con listas distintas.

## Nota de verificación
El átomo queda en `tentative` a propósito: **lo único que hay es el mensaje del commit y su asociación a la fila de `.gitignore` en la tabla de archivos de GitHub**. La captura no contiene el archivo `blacklist.json`, ni el código que lo escribe, ni el criterio por el que un dominio entra en la lista. El vault no puede afirmar que la blacklist se use para excluir dominios del generador de correo, ni que el formato sea el que dice el nombre del commit.
