---
id: 2026-1027-veridrop-los-tres-modos-de-deteccion-y-sus-conteos-no-coinciden-entre-paginas
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md, sources/2026-10-26-veridrop-openai-detection.md]
links: ["[[2026-1027-veridrop-pesos-de-los-11-detectores-y-el-contexto-largo-de-pago]]", "[[2026-1027-veridrop-la-sonda-de-contexto-largo-y-la-maxima-por-modelo]]", "[[2026-1024-veridrop-ventana-de-actividad-y-frescura-de-deteccion]]"]
---

## Claim
Las tres modalidades de profundidad existen y se nombran igual en las dos capturas, pero **sus recuentos de comprobaciones no coinciden entre páginas**. La FAQ (genérica, "standard / quick / full 三档模式") da: **quick (~15 s, 3-5 项)**, **standard (~40 s, 7-8 项)** y **full (~70 s, 全 10 项)**, y añade que **"所有模式都会跑 thinking signature 这种核心项"**. La sección de cobertura de Claude de esa misma FAQ da otra cosa: **"standard 模式跑 9 项常规检测 ~45 秒,full 模式跑完整 11 项常规检测 ~75 秒"**. Y la página OpenAI da una tercera: **"快速 (~15 秒,3 项)标准 (~40 秒,6 项)完整 (~70 秒,全 6 项)"**, con **"8 项 Chat Completions 协议检测"** en el subtítulo. Es decir, el mismo producto declara **3-5, 7-8, 9, 10, 11 y 6 comprobaciones** según la página que se mire.

## Why It Matters
Es una **inconsistencia interna del competidor** y importa por dos razones. La primera, de método: **el número de comprobaciones de un producto de verificación no es una constante** —depende del protocolo y de la página—, así que cualquier comparación entre detectores ("VeriDrop tiene 11 detectores, CCTest tiene 2") es **una comparación de marketing, no de cobertura**. La segunda, de producto: si el vault construye o consume un servicio de verificación, **necesita un identificador de versión del detector**, porque dos detecciones de "standard" hechas con dos semanas de diferencia pueden no ser comparables. Es la misma lección que el vault ya aplicó a la **ventana de actividad sin duracion publicada** ([[2026-1024-veridrop-ventana-de-actividad-y-frescura-de-deteccion]]): un número sin unidad ni versión es un número que caduca.
Y hay un dato útil dentro del ruido: **el modo rápido incluye igualmente el detector de firma criptográfica**. Es decir, el coste de la prueba concluyente **no está detrás del muro de pago** — la profundidad cara es la del contexto largo, no la de la identidad criptográfica ([[2026-1027-veridrop-pesos-de-los-11-detectores-y-el-contexto-largo-de-pago]]). Eso separa dos cosas que el mercadeo suele mezclar: **cuanto más cara la prueba, más se paga por el contexto, no por la certeza**.

## Nota de verificación
Conteos, tiempos y nombres transcritos literalmente de cada captura. La explicación (protocolos con detectors distintos por página) es **inferencia del vault**: las capturas no la formulan. Ninguno de los recuentos se ha verificado ejecutando una detección real.
