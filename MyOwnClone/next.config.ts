import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "standalone",
  typescript: { ignoreBuildErrors: true },
  serverExternalPackages: ["pg"],
};

export default nextConfig;
