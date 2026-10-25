---
id: 2026-1024-flokinet-aup-prohibe-chia-netscan-y-origenes-de-ddos
type: atom
certainty: solid
sources: [sources/2026-10-24-flokinet-vps-pricing.md]
links: ["[[2026-1024-hostkey-casos-de-uso-cripto-vpn-y-nodos-blockchain]]", "[[2026-1024-flokinet-ddos-1tbps-incluido-en-los-siete-planes]]", "[[2026-1024-flokinet-ubicaciones-offshore-ripe-e-isnic]]"]
---

## Claim
La **Acceptable Usage Policy de FlokiNET** (enlaza a `knowledgebase/7/AUP---Acceptable-Use-Policy.html`) prohíbe, entre otros: **spam** (relays, sitios, enlaces, proxy), **netscan/portscan**, **orígenes de DDoS de cualquier tipo**, distribución de malware e intentos de hackeo, **botnets, doorway pages y carding**, **phishing, scam e impersonación** (incluidas plataformas falsas de exchange de criptomonedas), pornografía infantil, venta de farmacéuticos sin licencia, material relacionado con terrorismo y **doxxing**. En "Server Abuse" incluye expresamente **"Chia mining on shared hosted accounts, VPS or dedicated servers"**. En cambio, **no prohíbe VPN, proxy ni nodos de blockchain**.

## Why It Matters
Es el contrapunto exacto del catálogo de usos de HOSTKEY, que vende explícitamente "sitios anónimos, bots de trading cripto 24/7, VPN o proxy propios para eludir límites regionales, nodos de blockchain" como casos de uso de su línea de pago en cripto ([[2026-1024-hostkey-casos-de-uso-cripto-vpn-y-nodos-blockchain]]). La observación del thread —**el uso que el proveedor nombra es el uso que va a defender cuando algo falle**— tiene aquí su versión más dura: un proveedor *offshore* ([[2026-1024-flokinet-ubicaciones-offshore-ripe-e-isnic]]) que **sí** permite VPN/proxy y nodos blockchain pero **prohíbe el origen de DDoS y el mining de Chia en sus propios servidores**, mientras **incluye mitigación DDoS de 1 Tbps+ en todos los planes** ([[2026-1024-flokinet-ddos-1tbps-incluido-en-los-siete-planes]]). Es decir: el posture de "resistencia a la censura" del vendor **no se extiende al abuse que se define en red**. Para el vault, que usa un VPS autoalojado como relay expuesto ([[2026-1023-priceai-sponsors-vps-chinos-para-auto-hospedar-relay]]), la línea que separa "allowed" de "prohibido" es precisamente la del DDoS de salida.

## Nota de verificación
La captura reproduce **la lista resumida** de la AUP, no el documento completo enlazado (que es la fuente normativa real). No se publica el procedimiento de reclamación, las sanciones ni los plazos. La mención a "proxy" dentro de la categoría de spam se refiere a relays de spam, no a proxies de salida en general.
