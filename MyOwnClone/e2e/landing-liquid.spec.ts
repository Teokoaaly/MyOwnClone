import AxeBuilder from "@axe-core/playwright";
import { expect, test } from "@playwright/test";

const forbiddenClaims = [/4\.9\/5/i, /2700/i, /trusted by/i, /customers/i];

test.describe("landing liquid", () => {
  for (const viewport of [
    { name: "375", width: 375, height: 812 },
    { name: "768", width: 768, height: 1024 },
    { name: "1280", width: 1280, height: 900 },
  ]) {
    test(`${viewport.name}px is responsive and accessible`, async ({ page }) => {
      await page.setViewportSize(viewport);
      await page.goto("/landing-liquid");

      await expect(page).toHaveTitle(/MyOwnClone.*clon digital/i);
      await expect(page.locator("main[lang='es']")).toBeVisible();
      await expect(
        page.getByRole("heading", { level: 1, name: /Trabaja con más inteligencia/i }),
      ).toBeVisible();
      await expect(page.getByTestId("capability-card")).toHaveCount(3);
      await expect(page.getByTestId("process-step")).toHaveCount(4);
      await expect(page.getByTestId("technology-wordmark")).toHaveCount(5);
      await expect(page.locator("video, canvas")).toHaveCount(0);

      for (const claim of forbiddenClaims) {
        await expect(page.getByText(claim)).toHaveCount(0);
      }

      const overflow = await page.evaluate(
        () => document.documentElement.scrollWidth > window.innerWidth,
      );
      expect(overflow).toBe(false);

      const accessibility = await new AxeBuilder({ page })
        .exclude(".shared-pricing")
        .analyze();
      expect(accessibility.violations).toEqual([]);

      await page.screenshot({
        path: `../.omo/evidence/landing-liquid-${viewport.name}.png`,
        fullPage: true,
      });
    });
  }

  test("uses owned visual assets and capability cards without prices", async ({ page }) => {
    const externalOrbRequests: string[] = [];
    page.on("request", (request) => {
      if (/future\.co|\.webm(?:$|\?)/i.test(request.url())) {
        externalOrbRequests.push(request.url());
      }
    });

    await page.goto("/landing-liquid");
    await expect(page.getByRole("heading", { name: "Conecta conocimiento, acción y contexto" })).toBeVisible();
    await expect(page.getByTestId("capability-detail-card")).toHaveCount(3);
    await expect(page.getByText(/\$\d/)).toHaveCount(0);
    await expect(page.getByTestId("liquid-orb")).toHaveAttribute("aria-hidden", "true");
    expect(externalOrbRequests).toEqual([]);
  });

  test("preserves keyboard focus and reduced motion", async ({ page }) => {
    await page.emulateMedia({ reducedMotion: "reduce" });
    await page.goto("/landing-liquid");

    await page.keyboard.press("Tab");
    await expect(page.getByRole("link", { name: "Inicio de MyOwnClone" })).toBeFocused();

    const reducedMotionName = await page.locator("[data-testid='liquid-orb']").evaluate(
      (orb) => getComputedStyle(orb).animationName,
    );
    expect(reducedMotionName).toBe("none");
  });
});
