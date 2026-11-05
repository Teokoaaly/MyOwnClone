---
id: 2026-1026-rebrowser-descargo-legal-que-niega-el-proposito-del-repo
type: atom
certainty: solid
sources: [sources/2026-10-25-rebrowser-patches.md]
links: ["[[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]", "[[2026-1026-patchright-declara-pasar-catorce-detectores-publicados]]", "[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]"]
---

## Claim
El README incluye un **"Disclaimer"** explícito y extenso: *"No responsibility is accepted for the use of this software. This software is intended for educational and informational purposes only... This software is not intended to bypass any security measures, including but not limited to CAPTCHAs, anti-bot systems, or other protective mechanisms employed by websites. The software must not be used for malicious purposes."* Y sin embargo, **la página 1 del mismo README** se titula *"Patches for undetectable browser automation"*, el párrafo de apertura afirma que sin el parche *"you're just a big red flag for any major website"*, y el parche se describe como neutralizar una técnica *"used by all major anti-bot software such as Cloudflare, DataDome"*.

## Why It Matters
El vault ya tenía un precedente de contraste directo: el bot de Go incluye un descargo que **reconoce el hecho** —*"Use of this tool to create accounts in violation of OpenAI's Terms of Service is solely at your own risk"* ([[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]). Aquí el descargo hace algo distinto y más fuerte: **niega el propósito** en vez de advertir sobre él, mientras el propio README describe la función del software en términos de eludir exactamente los sistemas que el descargo dice no eludir.

La diferencia importa para la lectura que el vault viene haciendo del sector. El bot de Go es un **producto con función declarada** (registro masivo de cuentas) y un descargo que asume la responsabilidad legal del uso. rebrowser-patches es un **producto cuya función declarada contradice su propio descargo**, lo que lo convierte en un caso de **descargo como mecanismo de protección jurídica**: si el descargo dice que no es para eludir anti-bot, entonces el uso para eludir anti-bot queda fuera del alcance que el autor acepta. Es la diferencia entre "esto viola los ToS, úsalo bajo tu responsabilidad" y "esto no es para eso, úsalo bajo tu responsabilidad".

Y hay una comparación que el vault puede hacer gracias a las fuentes hermanas: Patchright **no** incluye un descargo comparable, sino una **declaración de cobertura** —catorce detectores nombrados con marca ✅ y la frase *"currently is considered undetectable"* ([[2026-1026-patchright-declara-pasar-catorce-detectores-publicados]]). Es decir, el sector tiene **dos registros declarativos distintos** para herramientas casi idénticas: uno dice "esto funciona contra estos catorce detectores" y el otro dice "esto no es para evadir detectores". La diferencia no es de alcance técnico, es de **postura jurídica**, y el vault no la había registrado.

Para la economía del thread, la observación relevante es que el descargo **no cambia el precio ni la disponibilidad de la capacidad**: el parche es gratis, público, con detector público y con paquetes drop-in. El descargo es una cláusula, no un mecanismo de acceso. Es un recordatorio de que en este sector **la capa legal es decorativa y la capa de código es funcional** —y de que el vault debe seguir registrando la capacidad sin blurring su carga de riesgo legal ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]).
