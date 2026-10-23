---
id: 2026-1023-new-api-relaykit-conversion-perdida-de-campos
type: atom
certainty: solid
sources: [sources/2026-10-22-new-api-github.md]
links: ["[[2026-1023-new-api-una-sola-api-multiproto]]", "[[2026-1023-new-api-gateway-unificado-de-modelos]]", "[[2026-1023-new-api-stack-go-gin-react19-y-electron]]"]
---

## Claim
La conversión entre protocolos no la hace el núcleo sino un módulo aparte, **RelayKit**, described así en el README: *"provides request, response, and streaming conversion between the four text protocols"*. Es además un **módulo Go construible de forma independiente** (tabla de responsabilidades del repositorio: `relaykit/` = "Independently buildable Go module for protocol DTOs and conversions"), y el README advierte explícitamente de sus límites:

> "Available features depend on the channel, upstream model, and conversion path; **protocol-specific tools and fields may not map exactly**. WebSocket support also requires a compatible upstream and channel configuration."

## Why It Matters
Este es el **límite honesto** del producto y lo separa de la promesa de marketing: "compatible con OpenAI" no significa "idéntico a OpenAI". Campos y tools específicos de un protocolo **se pierden o se deforman** al cruzar, y el WebSocket (Realtime) solo funciona si el upstream y el canal lo soportan.
Para el vault que decide dónde poner su capa de inferencia, la lección es de arquitectura: si el producto expone una sola API multi-protocolo, el coste no está en el endpoint sino en la **conversión** — y ese coste es real y está declarado por el propio proyecto.
El dato estructural adicional es que RelayKit (y su gemelo **tokenkit**) son **independientes y reutilizables por otros gateways**, lo que significa que la capa de conversión es commodity: no es una ventaja diferencial de New API sino un componente que cualquiera puede extraer y usar ([[2026-1023-new-api-stack-go-gin-react19-y-electron]]).
