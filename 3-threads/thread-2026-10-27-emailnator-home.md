## Emailnator Atoms — 2026-10-27

Created 5 atomic notes from capture `2026-10-27-emailnator-home.md` (sources/2026-10-27-emailnator-home.md): temporary Gmail address service.

### Atoms created:

1. **2026-1027-emailnator-real-gmail-avoids-blocklists** — Real @gmail.com addresses avoid disposable-domain blocklists that reject fake-domain temp mail. [FRICTION] with guardarrail-no-alucinar regarding blanket avoidance of temp mail.

2. **2026-1027-emailnator-24h-auto-deletes** — Every temp Gmail auto-deletes after 24h with no account needed. [FRICTION] with herosms-reembolso-si-no-llega-sms-en-20-minutos regarding SMS verification time windows.

3. **2026-1027-emailnator-bulk-generation** — Supports generating up to 100 addresses at once for QA, testing, bulk signups. Tentative certainty; real-world validation needed.

4. **2026-1027-emailnator-customizable-formats** — Pre-generation format selection: Domain, +Gmail, or Gmail dot. Dots ignored before @, +everything ignored. All route to same inbox.

5. **2026-1027-emailnator-public-inbox-risk** — Free inbox is public: anyone with address can read messages. Never use for banking, password resets, or anything private. Premium offers private inboxes.

### Cross-atom tensions:

- **Public inbox vs. real Gmail delivery**: A real @gmail.com that bypasses blocklists also inherits Gmail's public-inbox model by default. The blocklist advantage and public-risk trade-off are inseparable.

- **24h auto-deletion vs. SMS verification windows**: Codes arriving after hours are lost when the inbox self-deletes. Users needing extended retention must use Premium or alternative services.

- **Bulk generation (100 addresses) vs. public inbox risk**: Scaling disposable usage amplifies exposure of public inboxes. Batch operations increase the probability someone captures a short-lived address.

### Follow-up needed:

- Test whether bulk-generated addresses all maintain the "real Gmail" blocklist-bypassing property.
- Verify if Premium private inboxes actually restrict access as claimed, or if the underlying Gmail public-model persists.
- Track whether the 24h auto-delete is exact or has variance that affects verification code receipt.