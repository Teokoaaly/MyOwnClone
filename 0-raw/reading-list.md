# Reading List
# Add URLs below, one per line. Lines starting with # are ignored.
# The Scout (23:00) will fetch these and save them to sources/.
# Format: URL  # optional comment

# Example (uncomment to activate):
# https://example.com/article-about-something  # interesting take on X

# Your actual reading list — add URLs here:

# --- Lote 2026-10-29 · infraestructura self-hosted para MyOwnClone (VPS ≤€4/mes) ---
https://www.hetzner.com/cloud/  # CX: coste real de VPS UE vs el presupuesto 4 EUR/mes del vault
https://www.digitalocean.com/pricing/droplets  # droplets + managed Postgres/Redis/Mongo, alternativa Hetzner
https://www.aiven.io/pricing  #托管 Postgres/Redis/Kafka/S3 con precio por GB y por GB-hora
https://www.backblaze.com/cloud-storage/pricing  # B2: almacenamiento barato para backups de Postgres
https://www.cloudflare.com/developer-platform/products/r2/  # R2: S3-compatible sin fees de egreso
https://deepgram.com/pricing  # transcripción de audio: posible módulo de voicemail/llamada en los clones
https://www.assemblyai.com/pricing  # alternativa de ASR, comparación de coste por hora de audio
https://www.twilio.com/en-us/sms/pricing  # SMS: costes reales de verificación de teléfono en el flujo de cuentas
https://brightdata.com/pricing  # proxies de pago: coste por GB para el eje de cuentas verificadas

# --- Lote 2026-10-29 · auth, SSO y seguridad multi-tenant ---
https://clerk.com/pricing  # SSO/identidad para el dashboard de clones, coste por MAU
https://workos.com/pricing  # alternativa SSO/SAML (nivel enterprise del vault)
https://auth0.com/pricing  # benchmark de precio por MAU contra Clerk y WorkOS

# --- Lote 2026-10-29 · operaciones y red ---
https://tailscale.com/kb  # red private para(api, worker, db) sin exponer puertos públicos
https://www.lambda.ai/pricing  # GPU bajo demanda: alternativa a Weaviate Cloud si el self-hosting no escala
https://learn.microsoft.com/en-us/azure/architecture/  # patrones de referencia multi-tier para el backend Flask
