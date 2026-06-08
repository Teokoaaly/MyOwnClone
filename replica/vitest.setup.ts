// Vitest setup file. Runs once before each test file.
//
// We register a few globals and mocks that the tests rely on:
//   - `crypto.randomUUID` is missing in jsdom 25 for older Node setups.
//   - `IntersectionObserver` and `ResizeObserver` are not in jsdom.
//   - `matchMedia` is not in jsdom (used by `next-themes`-style hooks).
import "@testing-library/jest-dom/vitest";

// jsdom does not implement these; provide no-op shims so React Testing
// Library's render path and any component using IntersectionObserver does
// not crash.
class IOStub {
  observe() {}
  unobserve() {}
  disconnect() {}
}

const g = globalThis as unknown as {
  IntersectionObserver?: unknown;
  ResizeObserver?: unknown;
};
if (!g.IntersectionObserver) g.IntersectionObserver = IOStub;
if (!g.ResizeObserver) g.ResizeObserver = IOStub;

if (typeof window !== "undefined" && !window.matchMedia) {
  Object.defineProperty(window, "matchMedia", {
    writable: true,
    value: (query: string) => ({
      matches: false,
      media: query,
      onchange: null,
      addListener: () => {},
      removeListener: () => {},
      addEventListener: () => {},
      removeEventListener: () => {},
      dispatchEvent: () => false,
    }),
  });
}
