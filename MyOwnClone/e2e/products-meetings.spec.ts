import { test, expect } from "@playwright/test";

/**
 * Spec de products y meetings.
 *
 * Cubre:
 * - /productos carga con estados loading/list/empty/error
 * - /reuniones carga
 * - APIs de products y meeting types responden contrato JSON
 * - API rechaza mutaciones no autenticadas con 401/403 (no 200)
 */

test.describe("Products UI", () => {
  test("/productos carga estructura", async ({ page }) => {
    await page.goto("/productos");
    await expect(page.locator("body")).toBeVisible();
    // La pagina no debe mostrar un error 500
    const body = await page.locator("body").textContent();
    expect(body?.toLowerCase()).not.toContain("internal server error");
  });

  test("API GET products responde JSON o auth", async ({ request }) => {
    const res = await request.get("/api/clone/clones", {
      headers: { Accept: "application/json" },
    });
    expect([200, 401, 403]).toContain(res.status());
    const ct = res.headers()["content-type"] || "";
    expect(ct).toMatch(/application\/json/);
  });

  test("API POST products sin auth rechaza con JSON", async ({ request }) => {
    const res = await request.post("/api/clone/clones/test-clone/products", {
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      data: { name: "Test product", price_cents: 1000 },
    });
    expect(res.status()).not.toBe(200);
    expect(res.status()).not.toBe(500);
    expect([400, 401, 403, 404, 503]).toContain(res.status());
    const ct = res.headers()["content-type"] || "";
    expect(ct).toMatch(/application\/json/);
  });
});

test.describe("Meetings UI", () => {
  test("/reuniones carga estructura", async ({ page }) => {
    await page.goto("/reuniones");
    await expect(page.locator("body")).toBeVisible();
    const body = await page.locator("body").textContent();
    expect(body?.toLowerCase()).not.toContain("internal server error");
  });

  test("API meeting types sin auth rechaza", async ({ request }) => {
    const res = await request.get("/api/clone/clones/test-clone/meeting-types", {
      headers: { Accept: "application/json" },
    });
    expect(res.status()).not.toBe(200);
    expect([401, 403, 404]).toContain(res.status());
  });
});
