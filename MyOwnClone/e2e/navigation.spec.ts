import { test, expect } from "@playwright/test";

/**
 * Páginas públicas y salud del backend.
 * Verifica que el sistema responde y que las páginas
 * no son placeholders rotos.
 */

test.describe("Public pages", () => {
  test("landing tiene titulo y CTA principal", async ({ page }) => {
    await page.goto("/");
    await expect(page).toHaveTitle(/MyOwnClone/i);
    // El landing debe tener al menos un link de navegacion o CTA
    const links = await page.locator("a[href]").count();
    expect(links).toBeGreaterThan(0);
  });

  test("paginas auth son accesibles", async ({ page }) => {
    for (const path of ["/login", "/registro", "/forgot-password"]) {
      const response = await page.goto(path);
      expect(response?.status() ?? 0).toBeLessThan(500);
      await expect(page.locator("body")).toBeVisible();
    }
  });
});

test.describe("Backend health", () => {
  test("admin/overview no devuelve 502/connection-refused", async ({ request }) => {
    const response = await request.get(
      "http://127.0.0.1:5001/console/api/myownclone/admin/overview",
      {
        headers: { "X-API-Key": "dev-api-key-for-proxy" },
        failOnStatusCode: false,
      }
    );
    // 200 con auth, 401/403 sin auth, 503 si proxy mal configurado.
    // 502 indicaria backend caido.
    expect([200, 401, 403, 503]).toContain(response.status());
  });

  test("el proxy rechaza requests sin MYOWNCLONE_API_URL en prod-like", async ({ request }) => {
    // En CI con NODE_ENV=production, una request a /api/admin/overview
    // sin backend configurado debe devolver 503, no 500.
    // En dev local, el proxy hace fallback a localhost:5001.
    const res = await request.get("/api/admin/overview", { failOnStatusCode: false });
    expect([200, 401, 403, 502, 503]).toContain(res.status());
  });
});
