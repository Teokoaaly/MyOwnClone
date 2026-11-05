PROPUESTA DE INSERCIÓN EN THREAD — sin editar 3-threads/

THREAD: economia-de-la-verificacion-y-reventa-de-cuentas

=== INSERTAR (markdown exacto) ===
**7.5.6 Una segunda consulta de la misma API devuelve cero, y eso redefine el "14".** La captura del 2026-10-25 lanza la misma búsqueda con otra formulación —`GET /search/repositories?q=chatgpt+signup+api+birthday+age+verification`— y la respuesta es **`total_count: 0`**, con `incomplete_results: false` y `items: []`: ninguna coincidencia para esa conjunción de seis términos ([[2026-1026-github-search-cero-resultados-para-la-consulta-de-edad-y-cumpleanos]]).

El dato obliga a acotar la §7.5.1 en un punto que el thread ya enunciaba como advertencia y que esta captura convierte en medición: **14 es el tamaño del índice para *esa* consulta, no el tamaño del corpus**. Formulada por función —signup por API, verificación de edad— la misma API no devuelve ni un repositorio; la tooling pública de registro de cuentas de ChatGPT está indexada por **nombre de producto** ("account creator"), no por sus funciones internas. Toda cifra de "N repositorios" de esta API es citable **solo junto a su cadena de consulta exacta** ([[2026-1026-github-search-cero-resultados-como-medicion-del-indice-y-no-de-la-realidad]]).

La segunda consecuencia es una laguna del thread. La §7 cierra el coste de las cuatro patas del alta —correo, captcha, proxy, SMS/KYC— y el vault no tiene **quinta pata**: la **verificación de edad**. Esta es la primera captura que la interroga y devuelve cero; el único punto del vault donde la edad legal aparece documentada es el L1 de NoOnes —"We ask for your date of birth to confirm your legal age"—, un peldaño de KYC de un exchange cripto ([[2026-1024-noones-escalera-de-verificacion-l1-l1plus-l2-l3]]), no el del alta de cuentas de IA; y el flujo de nueve pasos que el thread sí tiene medido (CSRF → signup → OTP → callback) **no contiene ningún paso de edad** ([[2026-1024-chatgpt-creator-flujo-de-registro-en-nueve-pasos]]). Tres lecturas posibles —que la edad no se pida en esa vía, que exista pero solo en el circuito cerrado, o que no exista como fricción operativa— y **la fuente no permite elegir entre ellas**. Queda como captura pendiente, no como hueco rellenable por inferencia ([[2026-1026-github-search-ningun-repo-publico-indexa-la-verificacion-de-edad-en-el-alta]]).

=== FIN ===
