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
      const duration = Math.min(1200, Math.max(680, Math.abs(distance) * 0.5));
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

    const revealElements = [...root.querySelectorAll<HTMLElement>(".reveal")];
    const processSection = root.querySelector<HTMLElement>(".process-section");

    const syncVisibleState = () => {
      revealElements.forEach((element) => {
        if (element.classList.contains("is-visible")) return;
        const rect = element.getBoundingClientRect();
        if (rect.top < window.innerHeight * 0.88 && rect.bottom > 0) {
          element.classList.add("is-visible");
        }
      });

      if (processSection) {
        const rect = processSection.getBoundingClientRect();
        const inView = rect.top < window.innerHeight * 0.9 && rect.bottom > window.innerHeight * 0.18;
        processSection.classList.toggle("is-active", inView);
      }
    };

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

    syncVisibleState();
    window.addEventListener("scroll", syncVisibleState, { passive: true });
    window.addEventListener("resize", syncVisibleState, { passive: true });

    if (window.location.hash) {
      window.setTimeout(() => {
        animateToHash(window.location.hash);
        window.setTimeout(syncVisibleState, 140);
      }, 80);
    }

    return () => {
      root.removeEventListener("click", handleAnchorClick);
      window.removeEventListener("scroll", syncVisibleState);
      window.removeEventListener("resize", syncVisibleState);
      revealObserver.disconnect();
      processObserver?.disconnect();
    };
  }, []);

  return null;
}
