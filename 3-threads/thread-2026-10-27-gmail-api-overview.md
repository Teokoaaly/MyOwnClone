## Gmail API Atoms — 2026-10-27

Created 17 atomic notes from capture `2026-10-27-gmail-api-overview.md` (sources/2026-10-27-gmail-api-overview.md): Google's Gmail API reference documentation.

### Atoms created:

1. **2026-10-27-gmail-api-restful** — The Gmail API is a RESTful API for accessing mailboxes and sending mail. Solid certainty.

2. **2026-10-27-gmail-api-uses** — Suitable for read-only extraction/index/backup, programmatic sending, migration, organization/filtering/sorting, and signature standardization. Solid certainty.

3. **2026-10-27-gmail-api-migration** — Suitable for email account migration between services or systems. Solid certainty.

4. **2026-10-27-gmail-api-labels** — Two types: system labels (INBOX, TRASH, SPAM, internally created, not deletable/modifiable but applicable/removable) and user labels (created by user, deletable/modifiable). Solid certainty.

5. **2026-10-27-gmail-api-threads** — A thread is a collection of related messages forming a conversation via recipient replies. Solid certainty.

6. **2026-10-27-gmail-api-messages** — An email message with sender, recipients, subject, body; immutable after creation. Solid certainty.

7. **2026-10-27-gmail-api-drafts** — An unsent message that can be replaced; sending a draft automatically deletes the draft and creates a SENT message. Solid certainty.

8. **2026-10-27-gmail-api-filters** — Advanced rules evaluating incoming messages against criteria (sender, subject, size); trigger label actions or forwarding on match. Solid certainty.

9. **2026-10-27-gmail-api-forwarding** — Verified email addresses configured to receive auto-forwarded messages; must be registered/verified before use. Solid certainty.

10. **2026-10-27-gmail-api-aliases** — Send-as aliases representing authorized email addresses; every account has at least one (primary), corresponds to "Send mail as" feature, basis for per-address signatures. Solid certainty.

11. **2026-10-27-gmail-api-certificates** — S/MIME digital certificates uploaded to send-as aliases for encrypted and signed email, ensuring security and sender authenticity. Solid certainty.

12. **2026-10-27-gmail-api-push** — Server-side notification via Google Cloud Pub/Sub; applications "watch" a mailbox and receive webhooks/alerts on changes (new email), eliminating polling need. Solid certainty.

13. **2026-10-27-gmail-api-delegation** — Delegator grants mailbox access to another user within same Google Workspace; delegate can read, send, delete messages and view/add contacts on delegator's account. Solid certainty.

### Cross-atom tensions:

- **RESTful vs. delegation access**: The RESTful architecture doesn't automatically grant delegated access; OAuth configuration and explicit permissions are required. ([[2026-10-27-gmail-api-restful]] ↔ [[2026-10-27-gmail-api-delegation]])

- **Message immutability vs. draft replaceability**: Messages cannot be changed after creation, but drafts can be replaced, creating tension between immutable message model and mutable draft workflow. ([[2026-10-27-gmail-api-messages]] ↔ [[2026-10-27-gmail-api-drafts]])

- **System labels vs. thread grouping**: System labels (INBOX/TRASH/SPAM) are automatically applied and fundamental to thread architecture, while user labels enable custom categorization. Both can coexist in thread management. ([[2026-10-27-gmail-api-labels]] ↔ [[2026-10-27-gmail-api-threads]])

- **Aliases vs. forwarding addresses**: Both involve verified email addresses but serve different purposes: aliases for "send as" identity while forwarding addresses direct copies to another destination. ([[2026-10-27-gmail-api-aliases]] ↔ [[2026-10-27-gmail-api-forwarding]])

### Follow-up needed:

- Test whether the draft/model distinction (immutable message vs. replaceable draft) holds across different Gmail API client libraries.
- Verify whether push notification watch() applies to delegated mailboxes or only to owner accounts, given OAuth permission variations.
- Explore whether S/MIME certificate requirements differ between primary address and send-as aliases in practice.
- Validate filter+forwarding interaction: does a filter that forwards also apply labels to the original message?