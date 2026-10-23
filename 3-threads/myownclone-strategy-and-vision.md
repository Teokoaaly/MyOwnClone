---
id: thread-myownclone-strategy-and-vision
type: thread
updated: 2026-10-22
sources: [raw/articles/myownclone-founder-transcript.md, raw/articles/myownclone-new-findings-may-2026.md]
links: ["[[eugenio-oller]]", "[[myownclone]]", "[[delphi]]", "[[emprenda-aprendiendo]]"]
---

# Thread — Estrategia, visión y modelo de negocio de MyOwnClone

Síntesis del transcript del founder y del material de negocio. Este thread no trata de lo que el código hace sino de **lo que el producto se propone ser** — y ahí es donde el material más rico y más expuesto vive: 18 átomos que describen la visión, los errores reconocidos y la lógica comercial, casi todos de certeza `tentative` porque su fuente es una transcripción, no una observación.

## El error reconocido: "fase 3"

El dato más honesto del lote no es un hallazgo técnico. [[2026-1022-error-fase-3-sobreconstruir]]: el founder empezó a construir la visión completa y "se me hizo un monstruo". El consejo de Hai fue "céntrate" (¿cuál es el ataque al mercado?); el de Javi, "magnificar 10 veces menos… esto es un monstruo". El diagnóstico del propio founder: "muchas cosas, pero con poca profundidad".

[[2026-1022-vision-fase-3-clon-opera-el-negocio]] define qué es la fase 3: el clon lleva el proyecto entero —construir productos, páginas de ventas, embudos por sí solo—, con recetas de cada sector. La visión sigue siendo esa; el founder justifica que "tarde o temprano" llegará porque la IA se vuelve más fácil. El límite explícito: "no puedo empezar por ahí".

Y [[2026-1022-mvp-salir-al-mercado-pronto]] da el temperamento de fondo: "necesito salir al mercado lo antes posible porque mi trauma fue… un año en esta fase, donde cada día fantaseas más". MVP que "funciona muy bien porque ya lo hemos testeado".

Estos tres átomos no son contradictorios entre sí — son un mapa de la tensión viva entre visión y ejecución. La fricción real aparece cuando se cruza con el plan interno ([[2026-1022-plan-orden-implementacion-myownclone]]): el Step 1 del handoff es versionado de prompts, una feature interna de gobernanza, no de lanzamiento.

## El ataque al mercado: no la tecnología

[[2026-1022-diferenciacion-negocios-online-vs-famosos]] es la tesis de posicionamiento más limpia del lote: "es la misma la que tiene Delfi". La diferencia no es el stack sino el mercado. Delfi (San Francisco) clona a Tony Robbins, un inversor famoso, un escritor. MyOwnClone se dirige a "gente de negocios online, infoproductos y marcas personales".

[[2026-1022-arquitectura-rac-tres-modos-por-clon]] concreta el grano de esa diferencia: la arquitectura "RAC" (retrieval sobre base vectorizada) con **tres modelos por clon** —aprendizaje, soporte al cliente y ventas— y el founder призна que la granularidad de los modos es la diferencia, no la base tecnológica.

El modelo de negocio completo cabe en cuatro átomos:

- [[2026-1022-low-ticket-a-high-ticket-con-clon]] — la primera idea: convertir cursos pregrabados low-ticket (pirateables, propensos a pasar de moda) en high-ticket, porque "Eug está al lado para ayudarte con tu caso específico".
- [[2026-1022-impacto-del-clon-en-ventas]] — en [[emprenda-aprendiendo]] el clon pasó a ser parte de la oferta en la landing ("acceso a tu clon"), lo que aumentó conversión, y llegó a vender la oferta temporal del día con fecha límite y enlace.
- [[2026-1022-instancia-como-captador-de-leads]] — cada instancia puede exigir email antes de hablar: captador de leads con base exportable a CRM.
- [[2026-1022-instancias-contexto-por-enlace]] — cada enlace compartido puede llevar contexto (un vídeo de YouTube de fitness): quien llega desde ese enlace recibe "sigamos hablando de fitness" y conserva el conocimiento completo para vender mentoría.

Y [[2026-1022-precio-99-mensual]] ancla el precio al uso real del cliente cero: 99 €/mes con un millón de palabras y 4.000 respuestas, frente a 3.000+ conversaciones/mes y 100+ alumnos de Emprenda Aprendiendo — "vais bastante sobrados".

## Las capacidades de producto que solo existen en el discurso

Aquí está la zona más frágil del vault, y conviene ser explícito: **varias capacidades que el founder describe como existentes no están en el código**. Los átomos existen y son ciertos —lo que el founder dijo es lo que dijo— pero la fricción está entre discurso e implementación.

- [[2026-1022-clon-avisar-al-creador-de-gaps]] — el clon avisa a su creador de que le preguntan algo que no sabe, para que lo "rellene". El código tiene `analytics_gaps` pero el mecanismo de aviso al creador no está confirmado.
- [[2026-1022-soporte-al-cliente-separado-y-escalado]] — base de conocimiento de soporte con retrieval por separado, y si no sabe resolver, ofrecer escalar a humano con email automático del ticket. Coherente con el modo `support` y el silo `support`, pero el auto-escalado no está verificado.
- [[2026-1022-dashboard-de-insights]] — cuatro salidas del panel de aprendizajes: feedback, preguntas frecuentes, avatar de la audiencia (con memoria de interlocutores) y gaps de conocimiento.
- [[2026-1022-separacion-de-hablantes-en-entrevistas]] — al subir una entrevista se separa hablante de entrevistador para que el retrieval use solo la voz del entrevistado; el founder admite que le costó "muchas horas" para que no sea "un chatbot random".
- [[2026-1022-guardarrail-no-alucinar]] — el clon declara que no tiene conocimiento en lugar de inventar. Este átomo lleva fricción explícita con la nota legacy [[myownclone-vs-delfi]], que atribuye alucinación a Delfi: el transcript no sostiene esa lectura, y la distinción entre "Delfi alucina" y "Delfi no tiene guardarrail de umbral de similitud" no se resuelve con la fuente disponible.

El eje [[2026-1022-delfi-elimino-instancias-y-contexto]] añade una lesson learned con historia: Delfi tenía "instancias" (versiones del clon) para que un cliente del curso Silex no accediera al conocimiento de otro curso; el founder pidió esa funcionalidad explícitamente y **Delfi la eliminó a los 6 meses**, junto con la opción de contextualizar por clase "ni aún pagando más". Esto choca frontalmente con el eje de instancias de MyOwnClone ([[2026-1022-instancia-como-captador-de-leads]], [[2026-1022-instancias-contexto-por-enlace]]): la funcionalidad que MyOwnClone plantea como ventaja central ya fue retirada por el competidor en el que se inspiró.

## Certezas y límites

De los 18 átomos de este thread, los que proceden de código propio (el precio, la arquitectura de tres modos, la separación de hablantes en el pipeline) son `solid`; los que proceden del transcript son `tentative` — no porque sean dudosos, sino porque una transcripción es una fuente de intención, no de comportamiento. Cuando un átomo del transcript y uno del código chocan, el código describe lo que existe; el transcript describe lo que existe en la cabeza del founder. Los dos son ciertos y la distancia entre ellos es el trabajo pendiente.

## Fricciones abiertas

1. **Visión vs. MVP** — [[2026-1022-vision-fase-3-clon-opera-el-negocio]] vs [[2026-1022-mvp-salir-al-mercado-pronto]]: el propio founder dice que no se puede empezar por ahí y a la vez describe la fase 3 con detalle. La fase 3 es el norte, no el plan.
2. **Instancias: ventaja o lesson learned** — [[2026-1022-instancia-como-captador-de-leads]] vs [[2026-1022-delfi-elimino-instancias-y-contexto]].
3. **Capacidades del discurso sin código** — el eje de gaps/soporte/escalado arriba vs [[2026-1022-gap-lead-capture-visitors]] y [[2026-1022-pipeline-chat-actual-myownclone]].
4. **Delfi y el guardarrail** — [[2026-1022-guardarrail-no-alucinar]] vs la nota legacy [[myownclone-vs-delfi]].

Ver también: [[myownclone-vs-myclone-is]] para el estado competitivo y [[myownclone-platform-architecture]] para lo que el código realmente hace.
