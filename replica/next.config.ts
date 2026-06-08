import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  typescript: { ignoreBuildErrors: true },
  serverExternalPackages: ["pg", "@phosphor-icons/react"],
};

export default nextConfig;
