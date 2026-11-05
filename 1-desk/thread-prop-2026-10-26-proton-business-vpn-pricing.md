# Propuesta de inserción en thread — Proton Business VPN (capturas 2026-10-26)

THREAD: economia-de-la-verificacion-y-reventa-de-cuentas
Fuente: `sources/2026-10-26-proton-business-vpn-pricing.md` (captura `0-raw/2026-10-26-proton-business-vpn-pricing.md`) y `sources/2026-10-26-proton-business-vpn-overview.md` (captura `0-raw/2026-10-26-proton-business-vpn-overview.md`).
Átomos: 18 nuevos (`2026-1027-proton-business-vpn-*` y `2026-1027-proton-business-workspace-standard-*`) + 9 extendidos (8 en `extend-2026-10-26-proton-business-vpn-pricing.md` + 1 nuevo en `extend-2026-10-26-proton-business-vpn-overview.md`; 2 bloques del segundo repiten átomos del primero).

Instrucciones de inserción:
(1) Insertar en la §8.10 (la subsection "El bundle de Proton, cuantificado"), **al final**, una subsección nueva "§8.11" con la tabla de la línea B2B y la corrección de la fricción 37.
(2) **Actualizar la fricción 37** de la §9: está redactada sobre la premisa de que la línea de empresa de Proton no tiene precio, y la captura lo desmiente. El texto de la fricción 37 **no se borra**: se le añade una coletilla con la corrección, o se marca como reescrita por el integrador.
(3) **Actualizar la §7** (tabla de coste por insumo): la fila de VPN no tenía precio de equipo; añadir la nota de que el VPN B2B es la primera partida de red cotizada por asiento.
(4) El integrador numera la subsección y las fricciones nuevas; no se han asignado números aquí.

---

## [INSERTAR EN economia-de-la-verificacion-y-reventa-de-cuentas, §8.10 — después del cierre actual de la subsection]

### §8.11 La línea de empresa de Proton: por fin una partida de red cotizada, por asiento

La §8.8 y la §8.9 escalera del thread trataron el VPN como **partida plana**: precio único por mes, sin escala de consumo, con un tope de dispositivos por cuenta (Mullvad €5/mes con 5 dispositivos, Proton $3,49/mes con 10). La §8.10 cerró diciendo que «**la línea de empresa es donde el coste del VPN se vuelve material para un producto multi-tenant**» y que su precio no era público. **Esa frase ya no es cierta**, y el motivo es concreto: `proton.me/business/vpn/pricing` publica la línea B2B completa, con precio unitario, mínimo de licencias y tabla de capacidad ([[2026-1027-proton-business-vpn-precios-publicados-por-usuario-en-cuatro-planes]]).

| Plan | Precio | Mínimo | Lo que añade sobre el anterior | Total declarado |
|---|---|---|---|---|
| **VPN Essentials** | **$6,99/usuario/mes** | **2 usuarios** | NetShield, gestión centralizada, **2FA obligatoria en toda la organización**, kill switch, always-on VPN, split tunneling, MDM | "Billed at **$167.76** for 2 users" |
| **VPN Professional** | **$9,99/usuario/mes** | **2 usuarios** | **SSO + SCIM**, IP fija y gateways privados en 20+ países, segmentación de red, monitorización y audit trails, Proton Sentinel, **cuenta de soporte dedicada** | "Billed at **$719.64** for 2 users" |
| **VPN and Pass Professional** | **$10,99/usuario/mes** | **3 usuarios** | Pass integrado, alias Hide-my-email ilimitados, 2FA authenticator, **integración SIEM y CLI** | "Billed at **$875.52** for 3 users" |
| **Workspace Standard** | **$12,99/usuario/mes** | **ninguno** | Los **8 productos** del ecosistema, **1 TB por usuario**, **15 dominios de correo propios**, VPN para **10 dispositivos por usuario** | "Billed at **$155.88** every 12 months" |
| **Enterprise** | **sin precio** | — | "Customizable solution", "Dedicated account manager", "All Proton services" → CTA "Let's talk" | — |

([[2026-1027-proton-business-vpn-precios-publicados-por-usuario-en-cuatro-planes]], [[2026-1027-proton-business-vpn-pass-professional-anade-pass-integrado-alias-y-un-cli]], [[2026-1027-proton-business-workspace-standard-1-tb-15-dominios-y-todos-los-productos]], [[2026-1027-proton-business-vpn-enterprise-sin-precio-con-cta-de-contacto-comercial]])

Tres consecuencias que cambian cómo el thread debe tratar la partida de red.

**La primera: la unidad de venta cambia de cuenta a asiento, y eso es lo que hace el VPN B2B incompatible con el resto de la tabla de coste.** El VPN de consumo se paga **por cuenta** con 10 dispositivos; el B2B se paga **por usuario**, con un mínimo de 2 o 3 licencias, y Workspace Standard lleva **10 dispositivos por usuario** ([[2026-1027-proton-business-workspace-standard-1-tb-15-dominios-y-todos-los-productos]]). Es decir: la capacidad de red **escala linealmente con el número de licencias** en vez de repartirse. Para un producto multi-tenant con un tenant por persona, el suelo de la partida pasa de "una suscripción plana" a **N × $6,99/mes con un mínimo de 2 licencias** ($13,98/mes) — y en el escalón de soporte presencial, desde **$59,94/mes** (6 usuarios en Professional), porque el phone and screen sharing support arranca en "6+ users" y el onboarding telefónico en "20+ users" ([[2026-1027-proton-business-vpn-onboarding-telefonico-solo-desde-20-usuarios]]). Estos suelos superan de largo el techo de ≤ €4/mes con el que el vault construyó su ancla de hosting: **la partida de red B2B es de otro orden de magnitud que el resto del corpus de insumos del §7**.

**La segunda: la red de empresa no es una red premium, y el precio se paga por control, no por capacidad.** "20,000+ servers in 140+ countries" es **literalmente la misma cifra** en la home B2B, en la página de precios B2B y en la página de consumo ([[2026-1027-proton-business-vpn-100000-empresas-y-4-6-en-sourceforge]]). Lo que los $3,00 de diferencia entre Essentials y Professional compran no es más ancho de banda: es **SSO, SCIM, IP fija, gateways privados y audit trails** — un plano de control, no más red. Es la misma tesis del bundle de consumo aplicada al B2B, y por eso la comparación "VPN barato de consumo" frente a "VPN de empresa" no es una comparación de velocidad ni de cobertura.

**La tercera: dos de los cuatro totales facturados no cuadran con su propio precio unitario, y la lectura correcta es usar el precio unitario.** "Billed at $719.64 for 2 users" **no** es $9,99 × 2 × 12 = $239,76, y "Billed at $875.52 for 3 users" **no** es $10,99 × 3 × 12 = $395,64; en cambio $167,76 y $155,88 sí cuadran con sus planes ([[2026-1027-proton-business-vpn-los-totales-facturados-no-cuadran-con-el-precio-por-usuario]]). Los dos importes irreproducibles son exactamente $19,99 × 3 × 12 y $24,32 × 3 × 12, **cifras que no aparecen en ninguna parte de la página**, lo que apunta a una mezcla de los estados `Monthly`/`Yearly` del conmutador durante la captura — pero la captura no permite demostrarlo. La regla operativa para el vault: **en la línea B2B el total impreso no es dato; el precio unitario sí, declarando el supuesto de conmutador.**

Y un cuarto apunte, el que más duele al corpus: **la página de precios es un marketing de gestión, no de red**. Enumera SSO/SCIM, SIEM, CLI, "15 custom email domains", "1 TB storage per user" y compliance "including GDPR and HIPAA" como "Included" en las cuatro columnas, **sin publicar ni una auditoría, ni un SLA con créditos, ni un uptime** — frente a Hetzner, que sí publica ISO/IEC 27001, BSI C5 y SLA del 99,9 % ([[2026-1027-proton-business-vpn-netshield-filtra-en-dns-y-declara-hipaa-ccpa-y-gdpr]]). Los contadores de escala ("Trusted by over 100,000 businesses", "+30 locations with dedicated IPs" frente a los "20+ countries" de la ficha de precios) son claims de página, y el único activo verificable sin confiar en el proveedor sigue siendo el **código abierto** y la **enumeración de algoritmos** (WireGuard, OpenVPN, ChaCha20, Poly1305, AES-256) ([[2026-1027-proton-business-vpn-cifrado-wireguard-openvpn-chacha20-y-aes-256]]).

### La parte que sigue sin cotizar: el servidor dedicado

La FAQ define el servidor dedicado como **alquiler, no venta** —"reserved exclusively for your team **as long as you rent them**", con IP fija y acceso restringido a los miembros de la organización— y el alta de servidores dedicados y gateways queda reservada a **"VPN Professional and Proton Workspace customers only"**, **sin publicar precio, número máximo de gateways ni coste por gateway** ([[2026-1027-proton-business-vpn-servidores-dedicados-alquilados-con-ip-fija]]). Para un producto multi-tenant, esto es **la salida dedicada por tenant** —la garantía de que la IP de un tenant no cambia ni se comparte— y sigue siendo **dato faltante explícito**, no hipótesis. La frontera de cotizabilidad del sector queda así: **asiento × capacidad estándar sí se cotiza; infraestructura dedicada, no.**

### Una incoherencia interna que conviene no pasar por alto

En la tabla "Compare plans", las filas **SSO** y **SCIM** tienen **celdas vacías en Workspace Standard**, el plan más caro, que sin embargo se anuncia como "All Proton products for business" ([[2026-1027-proton-business-workspace-standard-no-incluye-sso-ni-scim-en-la-tabla]]). Y en la página de producto, **SSO admite cualquier SAML 2.0 pero SCIM solo funciona con Okta y Microsoft Entra ID** (Google Workspace aparece en SSO y en MDM pero no en SCIM) ([[2026-1027-proton-business-vpn-sso-con-cualquier-saml-2-0-pero-scim-solo-okta-y-entra]]). La consecuencia para el vault: **el ciclo completo de identidad no viene genérico** — el login sí se delega a cualquier IdP, pero la provisión y la revocación automática de licencias solo con dos, y esa revocación es exactamente la operación que en un producto con tenants que se van evita pagar licencias muertas.

## [FRICCIONES A AÑADIR]

<!--friccion:NUEVA-->
- **La fricción 37 del thread queda desmentida para Proton.** Decía: «la línea de empresa es la única partida del vault cuyo precio no existe en ninguna captura». La captura de `proton.me/business/vpn/pricing` **publica cuatro planes con precio unitario, mínimo de licencias y tabla de capacidad** ($6,99 / $9,99 / $10,99 / $12,99 por usuario y mes), de modo que la ausencia registrada era una **ausencia de la captura de consumo**, no un rasgo del proveedor. La fricción se reduce a **un solo caso (IVPN, "VPN-only" sin precio)**, lo que **deja de ser una característica del sector** y pasa a ser una característica de IVPN. Contradicción directa entre [[2026-1027-proton-business-vpn-precios-publicados-por-usuario-en-cuatro-planes]] y [[2026-1024-proton-ofrece-vpn-para-empresas-sin-precio-publicado]].

<!--friccion:NUEVA-->
- **Los totales facturados de dos de los cuatro planes B2B no son reproducibles con su propio precio unitario**, y la página no publica precio de lista, precio de renovación ni fecha de fin del descuento (solo porcentajes por plan: 22 % / 19 % / 18 % / 13 %). O la página tiene un error de renderizado —y entonces sus totales no son datos— o los precios unitarios están recalculados sobre otra base y no son comparables con los totales. Contradicción entre [[2026-1027-proton-business-vpn-los-totales-facturados-no-cuadran-con-el-precio-por-usuario]] y la regla de lectura del precio de Proton en [[2026-1024-protonvpn-el-descuento-caduza-y-la-renovacion-sube-a-6-99]].

<!--friccion:NUEVA-->
- **La capacidad de la escalera B2B no es monótona.** Workspace Standard, el plan más caro y descrito como "All Proton products for business", tiene las celdas de **SSO y SCIM vacías** en la tabla de precios, mientras que planes más baratos los incluyen. Contradicción interna entre [[2026-1027-proton-business-workspace-standard-no-incluye-sso-ni-scim-en-la-tabla]] y [[2026-1027-proton-business-vpn-professional-anade-sso-scim-ips-dedicadas-y-sentinel]].

<!--friccion:NUEVA-->
- **Dos unidades distintas para las IP dedicadas en dos páginas del mismo producto el mismo día**: "+30 locations with dedicated IPs" en la home frente a "Dedicated IPs in 20+ countries" en la ficha de precios. "Ubicación" y "país" no son la misma magnitud, así que los dos números **pueden ser ciertos a la vez**; lo que no puede es citarse "20+ países" como "30 ubicaciones" ni al revés. Contradicción entre [[2026-1027-proton-business-vpn-30-ubicaciones-de-ip-dedicada-frente-a-20-paises]] y [[2026-1027-proton-business-vpn-professional-anade-sso-scim-ips-dedicadas-y-sentinel]].
