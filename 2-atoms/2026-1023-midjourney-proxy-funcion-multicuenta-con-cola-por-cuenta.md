---
id: 2026-1023-midjourney-proxy-funcion-multicuenta-con-cola-por-cuenta
type: atom
certainty: solid
sources: [sources/2026-10-22-midjourney-proxy-github.md]
links: ["[[2026-1023-midjourney-proxy-arquitectura-token-discord-y-wss]]", "[[2026-1023-midjourney-proxy-riesgo-de-cuenta-por-frecuencia-de-dibujo]]", "[[2026-1023-midjourney-proxy-edicion-plus-ampliada]]"]
---

## Claim
La última casilla de la lista de **"主要功能"** (funciones principales) del README es: **"支持多账号配置，每个账号可设置对应的任务队列"** — soporte de configuración de **múltiples cuentas**, con **una cola de tareas asignable a cada cuenta**, es decir, cada identidad de sesión ([[2026-1023-midjourney-proxy-arquitectura-token-discord-y-wss]]) lleva su propia cola. La edición ampliada añade además **"账号池持久化，动态维护"**: pool de cuentas persistente y mantenido dinámicamente.

## Why It Matters
El multi-cuenta con cola por cuenta es la respuesta operativa a la fragilidad de [[2026-1023-midjourney-proxy-arquitectura-token-discord-y-wss]]: si una sola identidad es un punto único de fallo (bloqueo, aviso, caída de sesión), el pool la convierte en un recurso que se degrada de forma parcial en lugar de caerse entera.
Pero tiene un coste de diseño que el vault debe ver con claridad: **una cola por cuenta significa que la latencia de una tarea depende de la carga de una identidad concreta**, y el reparto de trabajo entre cuentas es una decisión operativa manual o heurística, no una abstracción limpia de capacidad.
Además, esta función es exactamente la que hace que el proyecto separe versiones: la edición "plus" ([[2026-1023-midjourney-proxy-edicion-plus-ampliada]]) la eleva a pool persistente con mantenimiento dinámico, es decir, **la gestión del pool de cuentas es la línea de producto premium** de este tipo de proxy, no un detalle interno. Y es también la que más tensiona con la advertencia de baneo de cuenta ([[2026-1023-midjourney-proxy-riesgo-de-cuenta-por-frecuencia-de-dibujo]]): multiplicar identidades multiplica identidades señalables.

## Nota de verificación
El README no documenta cómo se asigna una tarea a una cuenta concreta (estrategia de reparto, prioridades, límites por cuenta) ni ningún límite numérico de cuentas o de cola.
