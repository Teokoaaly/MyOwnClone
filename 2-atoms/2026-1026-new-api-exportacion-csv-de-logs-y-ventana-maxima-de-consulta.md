---
id: 2026-1026-new-api-exportacion-csv-de-logs-y-ventana-maxima-de-consulta
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-aviso-legal-para-reventa-publica]]", "[[2026-1022-superficie-legal-publica-dpa-clon-terms]]", "[[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]"]
---

## Claim
**v1.0.0-rc.44** añade **exportación de logs de uso a CSV** desde la página de logs, con los filtros y el rango de fechas de la vista, en el idioma del visor. Cada usuario hace **una exportación a la vez**, **a través de pestañas** y, con Redis, **a través de nodos**. En **Log Maintenance** hay dos ajustes nuevos: **"Allow users to export logs"** (**activado por defecto**) y **"Longest log time range (days)"** (**365 días por defecto**); antes **las consultas de logs de los usuarios regulares no tenían límite**, y ahora búsquedas, exportaciones y gráficos del dashboard comparten ese rango.

## Why It Matters
Es una **decisión de retención y de acceso a datos de consumo**, y el vault la necesita por dos razones.
La primera es de cumplimiento: el README del propio proyecto condiciona la reventa pública a **retención de logs** como obligación ([[2026-1023-new-api-aviso-legal-para-reventa-publica]]). El software permite **recortar la ventana de consulta a 365 días por defecto** — pero la obligación legal de retención y la ventana de visibilidad para el usuario **no son la misma cosa**, y el release note no dice si la exportación cubre lo que ya está fuera de la ventana.
La segunda es de superficie: la exportación CSV de **los logs de todos los usuarios** en la vista de administrador es una **vía de salida de datos de consumo** del gateway. Es exactamente el tipo de salida que un producto con clientes finales tiene que Poder justificar ante un auditor o un cliente corporativo ([[2026-1022-superficie-legal-publica-dpa-clon-terms]]), y por eso el switch "Allow users to export logs" (activado por defecto) es una decisión de política, no un detalle de UI.
Y hay un detalle de escalabilidad que conecta con la topología: la exportación se serializa **por usuario, también entre nodos con Redis**, lo que confirma que el log vive en una base separada (ClickHouse) y que el coste de una exportación es real ([[2026-1023-new-api-despliegue-postgres-redis-y-clickhouse]]).

## [FRICTION]
> [[2026-1023-new-api-aviso-legal-para-reventa-publica]] afirma que el README del proyecto **condiciona la reventa pública** al cumplimiento previo de **retención de logs** entre otras obligaciones, y que esa retención es **obligación explícita**, no buena práctica.
> Este átomo presiona esa creencia en un punto: rc.44 **acota por defecto la ventana de logs a 365 días** para usuarios regulares (búsquedas, exportaciones y gráficos), y el administrador dispone de un interruptor para **recortarla**. Una ventana de consulta de 365 días **no es una política de retención**: es un límite de *visibilidad*. El software que dice "retén logs" y a la vez recorta por defecto lo que el usuario puede ver deja un hueco entre las dos cosas — o los logs se conservan más allá de 365 días y el límite es solo de interfaz, o se podan y entonces **la obligación de retención no la cumple el software**, sino una configuración que el release note no describe.
> Ambas no pueden ser completamente correctas en su lectura general: o "Longest log time range" es solo un filtro de consulta y la retención real es otra cosa (indeterminada en la fuente), o la ventana **es** la retención y entonces los 365 días por defecto son una **política de retención** — y entonces hay que leerla como tal, con su impacto en las obligaciones del operador. Marcado para juicio humano, no auto-resuelto: **el release note no dice si los logs más antiguos de 365 días se borran o solo se ocultan**, ni menciona ninguna tarea de purga automática (aunque existe una sección de "history log cleanup" en el panel).

