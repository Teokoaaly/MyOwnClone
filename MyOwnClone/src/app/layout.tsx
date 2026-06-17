import type { Metadata } from "next";
import { DM_Sans, JetBrains_Mono } from "next/font/google";
import { headers } from "next/headers";
import { Providers } from "./providers";
import "./globals.css";
import { resolveLocale } from "@/i18n/routing";

const dmSans = DM_Sans({
  variable: "--font-dm-sans",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
});

const jetbrainsMono = JetBrains_Mono({
  variable: "--font-jetbrains-mono",
  subsets: ["latin"],
  weight: ["500", "600", "700"],
});

export const metadata: Metadata = {
  title: "MyOwnClone - Multiply Yourself",
  description:
    "Create an AI clone trained on your knowledge. Support, teach, and sell around the clock from one workspace.",
  icons: {
    icon: [
      { url: "/favicon-32.png", type: "image/png", sizes: "32x32" },
      { url: "/icon-192.png", type: "image/png", sizes: "192x192" },
      { url: "/icon.svg", type: "image/svg+xml" },
    ],
    shortcut: "/favicon-32.png",
    apple: "/icon-192.png",
  },
};

export default async function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const headerStore = await headers();
  const locale = resolveLocale(headerStore.get("x-locale"));
  const messages = (await import(`../i18n/${locale}.json`)).default;

  return (
    <html
      lang={locale}
      className={`${dmSans.variable} ${jetbrainsMono.variable}`}
      suppressHydrationWarning
    >
      <head />
      <body className="min-h-full flex flex-col antialiased">
        <Providers locale={locale} messages={messages}>
          {children}
        </Providers>
      </body>
    </html>
  );
}
