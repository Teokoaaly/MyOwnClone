import { expect, test } from "@playwright/test";

test.describe("public landing routes", () => {
  test.describe.configure({ timeout: 120_000 });

  test("serves the approved landing at root and preserves the previous landing", async ({
    page,
  }) => {
    await page.goto("/", { waitUntil: "domcontentloaded" });

    await expect(
      page.getByRole("heading", {
        level: 1,
        name: /Create an AI clone that works for you/i,
      }),
    ).toBeVisible();
    await expect(page.locator(".primary-liquid-cta").first()).toBeVisible();
    await expect(page.locator(".moc-local-landing")).toHaveCount(0);

    await page.goto("/landing-original", { waitUntil: "domcontentloaded" });

    await expect(
      page.getByRole("heading", {
        level: 1,
        name: /Create an AI clone that works for you/i,
      }),
    ).toBeVisible();
    await expect(page.locator(".moc-local-landing")).toHaveCount(1);
  });

  test("keeps every visible internal destination available", async ({ page, request }) => {
    await page.goto("/", { waitUntil: "domcontentloaded" });

    for (const href of ["/login", "/registro", "/legal", "/contacto"] as const) {
      await expect(page.locator(`a[href="${href}"]`).first()).toBeVisible();
      const response = await request.get(href, { maxRedirects: 0 });
      expect(response.status(), `${href} must remain available`).toBeLessThan(400);
    }

    await page.goto("/legal", { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("heading", { level: 1, name: "Aviso Legal" })).toBeVisible();

    await page.goto("/contacto", { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("link", { name: "info@myownclone.com" })).toHaveAttribute(
      "href",
      "mailto:info@myownclone.com",
    );
  });
});
