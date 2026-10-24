---
id: 2026-1024-skhron-ipv6-enrutado-64-y-56-gratis-e-ipv4-addon-0-65
type: atom
certainty: solid
sources: [sources/2026-10-23-skhron-bitcoin-vps.md]
links: ["[[2026-1023-hetzner-ipv4-primario-incluido-o-costo-cero]]", "[[2026-1024-skhron-nat64-saliente-pero-no-inverso]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
Skhron: **"Every VPS includes a routed /64 IPv6 prefix at no extra cost. A routed /56 prefix is available free of charge upon request."** La página añade la ventaja técnica frente a la competencia: "Unlike many providers, we offer routed prefixes to help you avoid quirks required for 'on link' prefixes". En el lado IPv4, **la dirección dedicada no está incluida**: "A dedicated IPv4 address is not included, but it is available as an add-on at **€0.65 per month per address**. Each IPv4 address you add is dedicated to your server."

## Why It Matters
Es una partida de coste recurrente que el vault debe modelar por separado del precio del VPS: **€0.65/mes por IPv4 dedicada** se suma a cualquier plan, incluidos los de €2,34. Choca de frente con la lectura del átomo de Hetzner, donde el IPv4 primario aparecía a €0,00 en la configuración por defecto ([[2026-1023-hetzner-ipv4-primario-incluido-o-costo-cero]]): para el despliegue vivo, que hoy expone una IP IPv4 (`212.227.169.99`) en dos hosts ([[2026-1022-live-verify-superficie-dns-reducida-a-dos-hosts]]), Skhron exige pagar el IPv4 aparte. El prefijo /64 enrutado y gratuito es en cambio un argumento sólido para un producto de clones que quiera servir por IPv6 sin penalización de precio.

## [FRICTION]
> [[2026-1023-hetzner-ipv4-primario-incluido-o-costo-cero]] (escrita hace ~1 semana) lee el conmutador "IPv6 only / Primary IPv4" de Hetzner con un **€ 0.00** asociado, es decir, **IPv4 a coste cero** en la configuración por defecto (con la lectura tentativa que el propio átomo ya declara).
> Skhron afirma lo contrario en la misma variable de coste: **la IPv4 dedicada no está incluida y cuesta €0.65/mes por dirección** ("not included, but it is available as an add-on at €0.65 per month per address").
> Ambas no pueden ser simultáneamente verdaderas en su lectura completa, o la lectura del € 0.00 de Hetzner no corresponde al IPv4 primario, o Skhron cobra un extra donde Hetzner no. Marcado para juicio humano, no auto-resuelto.
