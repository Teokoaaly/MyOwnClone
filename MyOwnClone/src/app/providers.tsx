"use client";

import { SessionProvider } from "next-auth/react";
import { NextIntlClientProvider } from "next-intl";
import { ThemeProvider } from "next-themes";
import enMessages from "../i18n/en.json";
import esMessages from "../i18n/es.json";

type ProvidersProps = {
  children: React.ReactNode;
  locale: string;
  messages: Record<string, unknown>;
};

const ALL: Record<string, Record<string, unknown>> = {
  en: enMessages as unknown as Record<string, unknown>,
  es: esMessages as unknown as Record<string, unknown>,
};

export function Providers({ children, locale, messages }: ProvidersProps) {
  const fullMessages = ALL[locale] || messages;

  return (
    <NextIntlClientProvider locale={locale} messages={fullMessages}>
      <SessionProvider>
        <ThemeProvider attribute="class" defaultTheme="light" enableSystem={false}>
          {children}
        </ThemeProvider>
      </SessionProvider>
    </NextIntlClientProvider>
  );
}
