## Briefing: GitHub Search Antidetect Browser API (2026-10-27)

**Processed capture:** `2026-10-27-github-search-antidetect-browser-api.md` (0-raw)  
**Source:** `sources/2026-10-27-github-search-antidetect-browser-api.md` (full GitHub API search results, 21 items)  
**Atoms created:** 3  
**Thread updated:** `thread-2026-10-27-github-search-antidetect-browser-api.md`

### What was found

The GitHub search API query `antidetect browser api` returned 21 total repositories with `incomplete_results: false`, confirming the index was not truncated and all indexed results for this query are present in the result set.

Three distinct structural patterns emerged from the 21 items:

1. **Search result structure** — 21 items, no truncation. This is the baseline operational fact for all subsequent analysis on this query.

2. **MCP server pattern** — Two repositories (`foxprofile`, `undetectable-browser-MCP`) expose Model Context Protocol servers for profile and browser management, alongside `browser-proxies-sx` which also lists `mcp` as a topic. This indicates a emerging standardization pattern in the ecosystem.

3. **Functional categories** — The 21 repositories separate into two clear groups: (a) profile/management tools with integrated APIs/MCP (`foxprofile`, `vesper-antidetect-browser`, `undetectable-browser-MCP`), and (b) automation/frameworks focused on browser control with stealth capabilities (`invisible_selenium`, `invisible_puppeteer`, `antibrow`, plus Selenium-profile repos). These categories rarely co-occur in single repositories, suggesting typical workflows combine both types.

### Key tensions for the vault

- **Perfil vs. automatización**: Tooling splits cleanly between profile management (needs MCP/REST API) and automation (needs Selenium/Puppeteer/Playwright with stealth). Integration designs must account for this division.
- **Intención de búsqueda**: The query term is broad enough to capture both categories, meaning search intent must be explicitly scoped rather than assumed.
- **Estandarización de protocolo**: MCP appears across 3+ repositories as a shared integration pattern, contrasting with the variety of proprietary endpoints and stealth patches elsewhere.

### Follow-ups needed

- Monitor whether `incomplete_results: false` persists in future captures (affects validity of population-level analysis on 21 items).
- Track topic distribution changes over time for `antidetect browser api` — especially whether new categories emerge or the two-current categories shift in proportion.
- Evaluate [FRICTION] needs between the 3 new atoms and existing atoms on browser automation, proxy pools, and MCP workflows.