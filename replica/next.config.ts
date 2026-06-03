import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  serverExternalPackages: ["pg"],
  headers: async () => [
    {
      source: "/(.*)",
      headers: [
        { key: "X-Content-Type-Options", value: "nosniff" },
        { key: "X-Frame-Options", value: "DENY" },
        { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
        { key: "Strict-Transport-Security", value: "max-age=63072000; includeSubDomains; preload" },
        { key: "Content-Security-Policy", value: "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://js.stripe.com; frame-src 'self' https://js.stripe.com https://hooks.stripe.com https://*.whereby.com; connect-src 'self' https://api.anthropic.com https://api.openai.com https://api.stripe.com https://api.resend.com; img-src 'self' data: https:; style-src 'self' 'unsafe-inline'; font-src 'self';" },
      ],
    },
    {
      source: "/api/:path*",
      headers: [
        { key: "Access-Control-Allow-Origin", value: "http://localhost:3000" },
        { key: "Access-Control-Allow-Methods", value: "GET, POST, PUT, DELETE, OPTIONS" },
        { key: "Access-Control-Allow-Headers", value: "Content-Type, Authorization, Cookie" },
        { key: "Access-Control-Allow-Credentials", value: "true" },
      ],
    },
  ],
};

export default nextConfig;
