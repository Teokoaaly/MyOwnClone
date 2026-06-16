import createNextIntlPlugin from "next-intl/plugin";
import type { NextConfig } from "next";

const isProduction = process.env.NODE_ENV === "production";

const nextConfig: NextConfig = {
  serverExternalPackages: [
    "pg",
    "drizzle-orm",
    "@auth/drizzle-adapter",
    "@auth/core",
  ],
  allowedDevOrigins: ["127.0.0.1", "localhost"],
  experimental: {
    useNonce: true,
  },
  turbopack: {
    root: process.cwd(),
  },
  async headers() {
    const nonce = process.env.__NEXT_CSP_NONCE || "";
    return [
      {
        source: "/:path*",
        headers: [
          {
            key: "Content-Security-Policy",
            value: [
              "default-src 'self'",
              `script-src 'self'${isProduction ? "" : " 'unsafe-eval'"} https: 'nonce-${nonce}'`,
              `style-src 'self' https: 'nonce-${nonce}'`,
              "img-src 'self' data: blob: https:",
              "font-src 'self' data: https:",
              "connect-src 'self' https: ws: wss:",
              "media-src 'self' blob: data: https:",
              "object-src 'none'",
              "base-uri 'self'",
              "form-action 'self'",
              "frame-ancestors 'none'",
            ].join("; "),
          },
          { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
          { key: "X-Content-Type-Options", value: "nosniff" },
          { key: "X-Frame-Options", value: "DENY" },
          { key: "Permissions-Policy", value: "camera=(), microphone=(), geolocation=()" },
          {
            key: "Strict-Transport-Security",
            value: "max-age=31536000; includeSubDomains; preload",
          },
        ],
      },
    ];
  },
};

const withNextIntl = createNextIntlPlugin("./src/i18n/request.ts");

export default withNextIntl(nextConfig);
