import { Fustat, Inter } from "next/font/google";
import type { ReactNode } from "react";

const fustat = Fustat({
  variable: "--font-liquid-display",
  subsets: ["latin"],
});

const inter = Inter({
  variable: "--font-liquid-body",
  subsets: ["latin"],
});

export default function LiquidLandingLayout({ children }: Readonly<{ children: ReactNode }>) {
  return (
    <div lang="en" className={`${fustat.variable} ${inter.variable}`}>
      {children}
    </div>
  );
}
