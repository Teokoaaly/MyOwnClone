---
id: 2026-1027-incogniton-fingerprinting
type: atom
certainty: solid
sources: [sources/2026-10-27-incogniton-pricing.md]
links: ["[[2026-1027-incogniton-precios]]", "[[2026-1027-incogniton-cookies]]"]
---

## Claim

Incogniton's antidetect browser includes: **antidetect browser engine** that masks fingerprinting, **real device fingerprints** for authentic device representation, **paste as human typing** to simulate natural keyboard input, **Widevine DRM support** for streaming content, and pass compatibility with **Pixelscan / BrowserLeaks / BrowserScan** for evading detection scripts.

## Why It Matters

The antidetect browser engine is available across all pricing tiers, but advanced features like **Selenium/Puppeteer integration**, **API Access**, and **Cookie Collector** are tier-gated. This means that while the core fingerprint-masking technology is universally accessible, the programmatic automation layers that rely on consistent fingerprint presentation are restricted to higher-priced plans. Users on Starter Plus can run browsers with fingerprint masking but cannot access the API endpoints that automate profile creation at scale.

## [FRICTION]

> [[2026-1027-incogniton-cookies]] clasifica los cookies en Funcional, Estadísticas y Marketing con diferentes niveles de activación. Esta nota presiona esto porque el motor de antidetect browser y los fingerprints reales pueden depender de cookies de funcionalidad y preferencias para mantener consistencia de fingerprint entre sesiones. Si un usuario bloquea cookies de marketing, la capacidad del sistema para mantener perfiles coherentes a través de sesiones podría verse afectada, lo que contradice la afirmación de que el motor está disponible en todos los planes por igual. Ambas no pueden ser completamente correctas sin testing de fingerprint persistence bajo bloqueo de cookies. Marcado para juicio humano, no auto-resuelto.