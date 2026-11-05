---
id: 2026-1028-cliproxyapi-sdk-go-embedding
type: atom
certainty: solid
sources: [sources/2026-10-28-cliproxyapi-github.md]
links: ["[[2026-1023-new-api-una-sola-api-multiproto]]", "[[2026-1026-new-api-stack-go-gin-react19-y-electron]]"]
---

## Claim

CLIProxyAPI ships a reusable Go SDK (`sdk/`) that can be embedded into other Go projects, allowing downstream applications to integrate proxy functionality without running a separate binary — the SDK provides provider initialization, request wrapping, and response normalization embedded directly in-process.

## Why It Matters

Most LLM gateway deployments require running a separate proxy binary or Docker container, with HTTP communication overhead and an additional moving part for scaling, monitoring, and security hardening. The Go SDK lowers this barrier: a Go service can import the SDK, initialize registered providers once, and call model endpoints as regular Go function calls. This is especially valuable for CPU-constrained or air-gapped environments where a separate containerized proxy is impractical, and it enables tighter integration with telemetry, caching, and custom middleware that would be difficult to express through HTTP-only boundaries.

## [FRICTION]

> [[2026-1023-new-api-una-sola-api-multiproto]] describe una superficie de API unificada que el vault usa como referencia de contraste, pero el atom no aborda cómo esa superficie se expande ocontrae según el proveedor activado. El atom de SDK de Go asume que la normalización ocurre en proceso, mientras que el atom de Nueva API asume un modelo cliente-servidor HTTP. Ambas pueden convivir: el SDK es una optimización de implementación, no un cambio en el contrato de la API. Sin embargo, el vault no tiene un atom que documente explícitamente el acoplamiento entre el SDK y la superficie de API unificada, lo que deja abierta la pregunta de si el SDK expone el mismo modelo de conversión que el gateway HTTP o un subconjunto reducido. Marcado para juicio humano, no auto-resuelto.