Briefing: Gmail API Overview — 2026-10-27

17 atomic notes created from the Gmail API overview source (sources/2026-10-27-gmail-api-overview.md, 784 words). The source document provides a comprehensive reference for the Gmail RESTful API, covering common terms, use cases, and infrastructure concepts.

ATOMS CREATED (17 total):
- Foundational infrastructure: RESTful API access (restful), label taxonomy (labels), thread model (threads), message immutability (messages), draft workflow (drafts)
- Core functionality: mail use cases (uses), migration support (migration), filter system (filters), forwarding (forwarding), send-as aliases (aliases), S/MIME certificates (certificates), push notifications (push), account delegation (delegation)

CROSS-ATOM TENSIONS IDENTIFIED (7 key frictions):
1. RESTful architecture vs. delegated access — REST alone doesn't imply delegated OAuth permissions
2. Message immutability vs. draft replaceability — fundamental unit cannot change, but drafts are meant to be replaced
3. System labels vs. thread grouping — system labels are automatic and foundational; user labels are customizable
4. Aliases vs. forwarding addresses — both use verified addresses but serve opposite purposes (identity vs. duplication)
5. Push notification scope — whether watch() applies to delegated mailboxes or only owner accounts
6. Filter+forwarding interaction — whether forwarding filters also label the original message
7. S/MIME placement — whether certificates are recommended for primary address or only send-as aliases

FOLLOW-UP ACTION ITEMS (3 priority):
1. Verify push notification behavior with delegated mailbox OAuth scopes
2. Test draft replacement vs. message immutability across API client libraries
3. Explore S/MIME certificate usage patterns in organizational deployments

THREAD: 3-threads/thread-2026-10-27-gmail-api-overview.md
NEXT STEP: Continue processing remaining captures or begin synthesis in 3-threads.