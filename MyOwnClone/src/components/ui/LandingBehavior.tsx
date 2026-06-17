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

    const handleAnchorClick = (event: Event) => {
      const target = event.target;
      if (!(target instanceof Element)) return;

      const anchor = target.closest('a[href^="#"]');
      if (!(anchor instanceof HTMLAnchorElement)) return;

      const hash = anchor.getAttribute("href");
      if (!hash || hash === "#") return;

      const section = document.querySelector(hash);
      if (!(section instanceof HTMLElement)) return;

      event.preventDefault();

      const navHeight = 96;
      const startY = window.scrollY;
      const targetY = Math.max(0, section.getBoundingClientRect().top + window.scrollY - navHeight);
      const distance = targetY - startY;
      const duration = Math.min(1200, Math.max(680, Math.abs(distance) * 0.5));
      const started = performance.now();

      const step = (now: number) => {
        const progress = Math.min((now - started) / duration, 1);
        const eased = easeInOutCubic(progress);
        window.scrollTo(0, startY + distance * eased);
        if (progress < 1) {
          window.requestAnimationFrame(step);
        } else {
          window.history.replaceState(null, "", hash);
        }
      };

      window.requestAnimationFrame(step);
    };

    root.addEventListener("click", handleAnchorClick);

    const revealObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;

          const element = entry.target as HTMLElement;
          const parent = element.parentElement;
          const siblings = parent ? [...parent.querySelectorAll(":scope > .reveal")] : [];
          const delay = Math.max(0, siblings.indexOf(element)) * 90;

          window.setTimeout(() => {
            element.classList.add("is-visible");
          }, delay);

          revealObserver.unobserve(element);
        });
      },
      { threshold: 0.15, rootMargin: "0px 0px -40px 0px" },
    );

    root.querySelectorAll(".reveal").forEach((element) => {
      revealObserver.observe(element);
    });

    const processSection = root.querySelector(".process-section");
    const processObserver = processSection
      ? new IntersectionObserver(
          ([entry]) => {
            processSection.classList.toggle("is-active", entry.isIntersecting);
          },
          { threshold: 0.2 },
        )
      : null;

    if (processSection && processObserver) {
      processObserver.observe(processSection);
    }

    return () => {
      root.removeEventListener("click", handleAnchorClick);
      revealObserver.disconnect();
      processObserver?.disconnect();
    };
  }, []);

  return null;
}
