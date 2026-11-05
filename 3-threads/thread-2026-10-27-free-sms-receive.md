## 10sms-receive Atoms — 2026-10-27

Created 5 atomic notes from capture `2026-10-27-free-sms-receive.md` (sources/2026-10-27-free-sms-receive.md): free temporary SMS receiving service.

### Atoms created:

1. **2026-1027-free-sms-receive-no-registration** — Free temporary SMS service without requiring user registration. [FRICTION] with number-lifespan regarding brief vs. prolonged validation.

2. **2026-1027-free-sms-receive-privacy** — No personal data collected; messages retained for no more than 24 hours. [FRICTION] with email inbox models regarding persistent vs. ephemeral storage.

3. **2026-1027-free-sms-receive-countries** — Temporary phone numbers across multiple countries (Netherlands, France, Germany, Spain, Austria, UK, Hong Kong, China). [FRICTION] with number-availability-dynamics regarding real-time availability vs. claimed coverage.

4. **2026-1027-free-sms-receive-temporary** — Disposable numbers changed every month. [FRICTION] with masked-number-format regarding stability vs. brief-use design.

5. **2026-1027-free-sms-receive-services** — Supports SMS verification from Facebook, Telegram, WeChat, VK, PayPal, Alipay, and others. [FRICTION] with receive-smss coverage regarding platform breadth.

### Cross-atom tensions:

- **24h deletion vs. verification windows**: 24-hour message retention may expire before user completes verification. Both free-sms-receive and email services use similar retention but with different user expectations.

- **Privacy model divergence**: free-sms-receive offers anonymous ephemeral access (no account, auto-delete), while email services like Mail.tm may require passwords and imply persistence. Different privacy designs for different threat models.

- **Number rotation vs. stability**: Monthly number rotation (free-sms-receive) vs. 7-hour rotation or persistent mailboxes (other services). Different turnover assumptions affect usability for repeated verification.

- **Platform breadth**: free-sms-receive supports PayPal/Alipay financial platforms alongside social media, while other services may cover only social platforms. Different use-case coverage.

- **Country coverage discrepancy**: Claimed 8+ countries for free-sms-receive vs. 106 countries for 7sim. Different data sources or update cycles may explain the gap.

### Follow-up needed:

- Monitor number availability per country over time to verify claimed coverage.
- Track whether monthly rotation pattern holds or varies by region.
- Test whether numbers work for target verification services (Facebook, Telegram, etc.).
- Human judgment needed on whether the [FRICTION] contradictions are fundamental limitations or acceptable trade-offs.