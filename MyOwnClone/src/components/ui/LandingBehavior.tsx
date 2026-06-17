"use client";

import { useEffect } from "react";

function easeInOutCubic(value: number) {
  return value < 0.5
    ? 4 * value * value * value
    : 1 - Math.pow(-2 * value + 2, 3) / 2;
}

export default function LandingBehavior() {
  useEffect(() => {
    const root = document.querySelector(".moc-local-landing");
    if (!root) return;

    const animateToHash = (hash: string, replaceUrl = false) => {
      if (!hash || hash === "#") return;

      const section = document.querySelector(hash);
      if (!(section instanceof HTMLElement)) return;

      const navHeight = 96;
      const startY = window.scrollY;
      const targetY = Math.max(0, section.getBoundingClientRect().top + window.scrollY - navHeight);
      const distance = targetY - startY;
      const duration = Math.min(800, Math.max(300, Math.abs(distance) * 0.3));
      const started = performance.now();

      const step = (now: number) => {
        const progress = Math.min((now - started) / duration, 1);
        const eased = easeInOutCubic(progress);
        window.scrollTo(0, startY + distance * eased);
        if (progress < 1) {
          window.requestAnimationFrame(step);
        } else if (replaceUrl) {
          window.history.replaceState(null, "", hash);
        }
      };

      window.requestAnimationFrame(step);
    };

    const handleAnchorClick = (event: Event) => {
      const target = event.target;
      if (!(target instanceof Element)) return;

      const anchor = target.closest('a[href^="#"]');
      if (!(anchor instanceof HTMLAnchorElement)) return;

      const hash = anchor.getAttribute("href");
      if (!hash || hash === "#") return;

      event.preventDefault();
      animateToHash(hash, true);
    };

    root.addEventListener("click", handleAnchorClick);

    if (window.location.hash) {
      window.setTimeout(() => {
        animateToHash(window.location.hash);
      }, 80);
    }

    return () => {
      root.removeEventListener("click", handleAnchorClick);
    };
  }, []);

  return null;
}
