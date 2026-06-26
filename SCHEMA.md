# Wiki Schema

## Domain
Ingeniería de software, startups, automatización empresarial, ciberseguridad y proyectos personales de Hacchi.

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `simgest-erp.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- **Provenance markers:** On pages that synthesize 3+ sources, append `^[raw/articles/source-file.md]`
  at the end of paragraphs whose claims come from a specific source.

## Frontmatter
  ```yaml
  ---
  title: Page Title
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  type: entity | concept | comparison | query | summary
  tags: [from taxonomy below]
  sources: [raw/articles/source-name.md]
  confidence: high | medium | low
  contested: true                        # set when unresolved contradictions exist
  contradictions: [other-page-slug]      # pages this one conflicts with
  ---
  ```

## Tag Taxonomy
- **Tech:** backend, frontend, devops, database, api, security, automation
- **Business:** startup, saas, erp, b2b, b2c, business-model, competitor
- **Projects:** simgest, myownclone, darkforest, picoclaw, hub-spoke
- **Tools:** tailscale, docker, llm, openai, python, linux
- **Meta:** comparison, timeline, controversy, prediction, reference
- **AI/ML:** model, training, inference, finetuning, rag, agent

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines
- **Archive a page** when its content is fully superseded — move to `_archive/`, remove from index

## Entity Pages
One page per notable entity (company, product, person, tool).
- Overview / what it is
- Key facts and dates
- Relationships to other entities ([[wikilinks]])
- Source references

## Concept Pages
One page per concept or topic.
- Definition / explanation
- Current state of knowledge
- Open questions or debates
- Related concepts ([[wikilinks]])

## Comparison Pages
Side-by-side analyses.
- What is being compared and why
- Dimensions of comparison (table format preferred)
- Verdict or synthesis
- Sources

## Update Policy
When new information conflicts with existing content:
1. Check dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for user review in the lint report
