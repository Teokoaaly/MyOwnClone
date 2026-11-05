# Propuesta de hilo — captura `2026-10-25-suno2openai.md`

Fuente: `sources/2026-10-25-suno2openai.md` (README completo de `wlhtea/Suno2openai` + página del repositorio en GitHub, capturada 2026-10-25).
Átomos nuevos de esta captura: 11 (todos en `2-atoms/`, prefijo `2026-1026-suno2openai-`).
Extensiones propuestas: 4 (en `1-desk/extend-suno2openai.md`).

---

## Propuesta A — `myownclone-platform-architecture`

```markdown
### Una quinta edición del arquetipo: el gateway que expone una etiqueta de modelo falsa y no publica ni coste ni capacidad

La sección de este thread que describe el arquetipo del puente no oficial tiene ahora **una quinta edición medida**, y es la que más se parece al producto propio porque su valor está entero en la **capa de gestión de credenciales**, no en la llamada.

`wlhtea/Suno2openai` (275 estrellas, 49 forks, Python, MIT, 464 commits, último commit el 19 de enero de 2025) **no es una implementación musical original**: es una **capa wrapper/orquestadora** construida sobre `SunoSongsCreator` (yihong0618) y `Suno-API` (SunoAI-API), que expone el resultado en **interfaz compatible con OpenAI** ([[2026-1026-suno2openai-integrado-sobre-sunosongscreator-y-suno-api]]). Es decir: **la categoría no reimplementa el backend, lo envuelve y lo vende con el formato de otro**. La observación que el thread ya tenía sobre el arquetipo —"el puente es un envoltorio, el valor está en las credenciales"— queda aquí con su forma exacta: el envoltorio **gestiona cookies en base de datos y las rota** ([[2026-1026-suno2openai-el-pool-de-cookies-exige-mysql-como-requisito]]).

**El detalle de contrato que más importa a un producto que sirve inferencia a tenants es este: el campo `model` vale `gpt-3.5-turbo`.** El único ejemplo documentado del endpoint `POST /v1/chat/completions` usa `model: gpt-3.5-turbo`, `messages` y `stream` opcional, y **no hay catálogo de modelos de Suno ni mapeo entre modelos y capacidades** ([[2026-1026-suno2openai-el-campo-model-es-gpt-3-5-turbo-sobre-un-backend-de-musica]]). Es decir: **el backend es musical y el contrato dice OpenAI**, lo que significa que **un relay que reenvía este gateway no puede ofrecer una columna de "modelo" honesta**: cualquier cliente que pregunte qué modelo está usando recibe una etiqueta de compatibilidad, y el orden de prioridad entre relays y modelos se vuelve **indistinguible desde la petición**. Para un producto de agregación, esto es el problema operativo central: **la ausencia de un modelo real no es una inconvenience estética, es la razón por la que un gateway no puede enrutar por calidad ni cotizar por modelo**.

**La segunda lectura de arquitectura es la de la madurez del artefacto, y es desfavorable.** El proyecto **no publica releases, ni changelog, ni SLA, ni hoja de ruta fechada**; el soporte es un **correo QQ** y la página ofrece **prácticas a estudiantes** — es un proyecto unipersonal, con la estructura de operación de un trabajo de fin de carrera, no de una infraestructura ([[2026-1026-suno2openai-proyecto-unipersonal-con-practicas-y-email-qq]]). Y la distribución es **una imagen `wlhtea/suno2openai:latest` sin versión fijable**, con la guía de `docker-compose` fechada el **7 de abril de 2024**, dos meses antes del último commit ([[2026-1026-suno2openai-imagen-docker-sin-versionar-y-documentacion-fija]]).

**Y hay una pieza de capacidad que el thread debe leer como advertencia de diseño.** La rotación de cookies está **implementada** —cuatro endpoints REST de administración del pool— pero la **cola de peticiones figura en "Future Plans"**: se rotan las credenciales y no se serializan las peticiones ([[2026-1026-suno2openai-rotacion-de-cookies-declarada-sin-cola-de-peticiones]]). Es el **contorno exacto del límite**: un pool sin cola no es una capacidad, es un **conjunto de cookies con presupuesto de API**. La lección de arquitectura que el thread debería extraer es que **la concurrencia no viene del pool de credenciales sino de la cola**, y que un proyecto que confunde ambas cosas está vendiendo un límite que no ha medido.
```

THREAD: myownclone-platform-architecture

---

## Propuesta B — `economia-de-la-verificacion-y-reventa-de-cuentas`

```markdown
### 7.5.8 Una categoría donde la credencial se recoge a mano y no se fabrica ni se compra

La §7 desglosa el coste del alta en cuatro partidas —correo, captcha, proxy e identidad— y su §7.5 añade el corpus público de herramientas de registro. Una cuarta captura de esa misma línea, ahora con el **README íntegro** de un gateway de Suno (`wlhtea/Suno2openai`, 2026-10-25), documenta **una categoría neighbour donde ninguna de las cuatro partidas se paga** ([[2026-1026-suno2openai-la-cookie-se-copia-a-mano-del-navegador]]).

El apartado *"How to get cookie"* del README es **una captura de pantalla con la instrucción "copy all content about the cookie"**: la credencial **se transcribe a mano desde el navegador**. No hay registro, ni correo temporal, ni captcha, ni proxy, ni rotación de identidad — y el pool de cookies que sostiene todo el servicio **se alimenta de material preexistente** ([[2026-1026-suno2openai-cuatro-endpoints-de-gestion-de-cookies]]).

**El efecto sobre la tabla de coste por insumo es de una partida nueva, y esa es la aportación.** En la §7 toda capacidad de una plataforma sin API oficial se costea con correo, captcha, proxy, identidad y, en el alto de ChatGPT, tiempo de espera de OTP. Aquí **las cuatro partidas son cero** y queda una quinta: **la cookie**, cuyo coste unitario es **tiempo humano de copia y disponibilidad de una sesión viva** — una partida que **no se compra en ningún catálogo** y que el vault, con lo que tiene, **no puede cotizar**. Es la misma forma de partida que el thread ya identificó en `gptGrok2api` (ingeniería de imitación como capa dominante), pero aquí **invertida**: en `gptGrok2api` el captcha se internaliza para no comprarlo ([[2026-1024-gptgrok2api-registro-protocolo-sin-navegador-y-captcha-solver-integrado]]); aquí la capa dominante **no existe**, y lo que hay es **acumulación manual de sesiones**.

**La consecuencia estructural es que la capacidad de esta categoría es de crecimiento lento y de degradación silenciosa.** Una cookie de sesión **caduca** y el pool hay que reponerlo a mano; la rotación entre cookies está implementada, pero **la cola de peticiones que repartiría esa rotación está en "Future Plans"** ([[2026-1026-suno2openai-rotacion-de-cookies-declarada-sin-cola-de-peticiones]]). Es decir: **rotar sin encolar no aumenta la capacidad, solo reparte el mismo dwindling entre más solicitudes** — y el propio repositorio lo reconoce con una línea de *Future Plans* que el vault puede leer como **la confirmación de su propio techo**.

**La última pieza cierra el modo de fallo con una advertencia operativa concreta.** El `AUTH_KEY` que protege las rutas de generación **tiene como valor por defecto el timestamp del momento del arranque**, es decir, **un secreto que cualquiera que lea el README adivina** ([[2026-1026-suno2openai-auth-key-por-defecto-es-el-timestamp-actual]]). En una economía donde la credencial es el activo, **un activo protegido por un valor por defecto público es un activo que no está protegido**; y el readout de cookies (`POST /<prefijo>/cookies`) está **en el mismo canal que la generación**, con la misma clave.
```

THREAD: economia-de-la-verificacion-y-reventa-de-cuentas

---

## Propuesta C — `el-agregador-de-precios-como-producto`

```markdown
### 7.5 Un gateway que expone la compatibilidad OpenAI y no expone ni el coste, ni el límite, ni la capacidad

La §7.1 de este thread es el hallazgo estructural: PriceAI y VeriDrop son **dos inventarios del mismo mercado que no se fusionan**, y la §7.2 añade 48 dominios foráneos de baja fricción. El vault acaba de leer el **README íntegro de un gateway de Suno de la categoría que estos inventarios miden** (`wlhtea/Suno2openai`, 2026-10-25), y la lectura tiene un valor distinto de los anteriores: **no aporta ni un precio, y eso es exactamente el dato**.

**Lo que el gateway publica sobre sí mismo es deliberadamente mínimo.** El único endpoint de generación documentado es `POST /v1/chat/completions`; **no hay API de tareas, ni de progreso, ni de descarga de audio, ni consulta de consumo, ni historial de peticiones** ([[2026-1026-suno2openai-el-contrato-publico-es-el-formato-de-chat-con-streaming]]). El campo `model` del ejemplo es `gpt-3.5-turbo`, y **no hay catálogo de modelos** ([[2026-1026-suno2openai-el-campo-model-es-gpt-3-5-turbo-sobre-un-backend-de-musica]]). Es decir: **el proveedor de capacidad no puede ser comparado por lo que expone su API**, porque su API expone **compatibilidad, no capacidad**.

**El resultado para el agregador es una regla de arquitectura de inventario, y es nueva.** Un inventario de relays cotiza **modelo, multiplicador, disponibilidad y SLA**. Este gateway **no puede entrar en esa tabla en ninguna de las cuatro columnas**: no publica qué modelos hay detrás de la etiqueta `gpt-3.5-turbo`, ni cuánto cuesta, ni qué disponibilidad tiene, ni qué compromiso de servicio ofrece — y su sección de `Releases` está **vacía**, de modo que tampoco hay un canal de changelog donde aparece un cambio de precio o de modelo ([[2026-1026-suno2openai-metricas-de-la-pagina-464-commits-y-dos-watchers]]). **Lo único que publica es un contador de estrellas y un contacto de correo QQ** ([[2026-1026-suno2openai-proyecto-unipersonal-con-practicas-y-email-qq]]). Es el caso límite del thread: **un proveedor cuya única superficie pública comparable es lakxestrellas**, y 275 estrellas frente a **2 watchers** reales en la página web — es decir, **la única métrica comparable que ofrece es la del propio repositorio, no la de su servicio** ([[2026-1026-suno2openai-metricas-de-la-pagina-464-commits-y-dos-watchers]]).

**La consecuencia de negocio para el producto agregador es concreta.** La §7.1 mostró que el hueco de un inventario unificado está en la **fricción de la comparación**; esta captura muestra el otro extremo del problema, que es **la opacidad del proveedor en la capa de servicio**: **un gateway que solo expone compatibilidad obliga al agregador a cotizar a ciegas, y a vender un rango en lugar de un precio**. La única palanca de comparación disponible sin acceso al upstream es **la latencia y el éxito observado desde fuera** — el mismo criterio empírico que la §7.2 ya aplicaba a los dominios foráneos, y que aquí queda mejor justificado por la ausencia de cualquier campo de estado. Un agregador que no puede preguntar "¿qué modelo es esto?" al proveedor tiene que **preguntárselo al cliente mediante mediciones propias**, y esa es una partida de coste de medición que hasta ahora este thread no tenía.
```

THREAD: el-agregador-de-precios-como-producto
