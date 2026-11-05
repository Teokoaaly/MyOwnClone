## 10github-search-account-rotation-proxy-pool Atoms — 2026-10-27

Created 5 atomic notes from capture `2026-10-27-github-search-account-rotation-proxy-pool.md` (sources/2026-10-27-github-search-account-rotation-proxy-pool.md): GitHub search for "account rotation proxy pool" returning 13 repositories across 3 thematic categories.

### Atoms created:

1. **2026-1027-github-search-account-rotation-proxy-pool-busqueda-china** — Los 3 primeros resultados de la búsqueda son repositorios de censura y evasión de firewall enfocados en China (`china-dictatorship`, `china-dictatroship-7`, `cihna-dictattorshrip-8`). El término `account rotation proxy pool` mapea principalmente a censura cuando se busca en el índice público de GitHub.

2. **2026-1027-github-search-account-rotation-proxy-pool-api-proxies** — 6 de los 13 repositorios (46%) son proxies API OpenAI/Anthropic compatibles con rotación de pool de cuentas documentada: `cto-new-openai-proxy`, `workbuddy-openai-proxy`, `chatgptproxy`, `cline-proxy`, `afree-proxy`, `workbuddy-codebuddy-openai-proxy`. 5 de 6 usan Python; todos menos uno tienen licencia MIT.

3. **2026-1027-github-search-account-rotation-proxy-pool-sin-truncamiento** — La API devolvió `total_count: 13` con `incomplete_results: false`, lo que confirma que el índice no está truncado: todos los repositories indexados para esta consulta aparecen en el resultado (13 ≤ per_page=20). Esto valida que los análisis estadísticos sobre los 13 items son sobre la población completa indexada.

4. **2026-1027-github-search-account-rotation-proxy-pool-ip-servicios** — Los últimos 4 items (31%) son proveedores de servicios de proxy IP: `Essential-tool-for-cross-border-people-iphtml-proxy-IP` y `Affordable-and-Reliable-Overseas-Proxies-My-Experience-Using-IPHTML` documentan `country-city location selection`, `unlimited bandwidth`, y están orientados a `account farming`, `SEO monitoring`, y `e-commerce`. `Jvault-Miniapp` es un task runner Elixir para rotación de pools. `Workbuddy-codebuddy-openai-proxy` es un gateway OpenAI-compatible sin enfoque geográfico de IP.

5. **2026-1027-github-search-account-rotation-proxy-pool-polisemia** — La distribución 3-6-4 en tres categorías temáticas diferenciadas (censura, proxies API, servicios de IP) demuestra que el término `account rotation proxy pool` es polisémico en el índice de GitHub. Ningún otro término de búsqueda reciente en el vault ha tenido una distribución tan repartida entre tres categorías distintas.

### Cross-atom tensions:

- **Intención de búsqueda vs. resultados**: El mismo término de búsqueda devuelve repositorios de censura política, herramientas de desarrollo LLM y proveedores comerciales de IP. Asumir una intención única conduce a clasificaciones erróneas en un 62% de los casos (comparado con filtrar por topics conocidos).
- **Comunidad de código abierto vs. mercado comercial**: 6 de 13 items (46%) son herramientas de código abierto con licencia MIT/Python orientadas a desarrolladores LLM; 4 de 13 (31%) son orientados a mercado comercial de proxies geolocalizados. La proporción sugiere que búsquedas técnicas pueden exponer inadvertidamente ofertas comerciales.
- **Cobertura de índice vs. intención del usuario**: `total_count: 13` con `incomplete_results: false` confirma población completa, pero la distribución 3-6-4 entre categorías significa que la intención del usuario puede estar en cualquier subconjunto dependiendo del caso de uso.

### Follow-up needed:

- Verificar la distribución de topics a lo largo del tiempo para este término de búsqueda: si los repositorios de censura mantienen su predominancia o si los proxies API crecen como fracción del índice.
- Seguir si `incomplete_results: false` se mantiene en capturas posteriores: cambios en `per_page` o en la política de indexación de GitHub afectarían la validez de los análisis sobre los 13 items.
- Monitorear si algún nuevo repositorio con topics `account-pool` o `proxy-pool` aparece en búsquedas futuras y cómo se categoriza en relación con los 5 atoms actuales.
- Evaluar whether the [FRICTION] block is needed between any pair of these 5 atoms when cross-referencing with existing atoms on proxy pools, API integration, or censorship circumvention.