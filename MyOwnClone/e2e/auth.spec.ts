import { test, expect } from "@playwright/test";

/**
 * Authentication pages — valida estructura y comportamiento, no solo
 * presencia de elementos. Cada test verifica que el flujo ES el
 * contrato esperado, no que el HTML contiene strings genericos.
 */

test.describe("Login page", () => {
  test("carga con h1, form, y los campos requeridos", async ({ page }) => {
    await page.goto("/login");
    await expect(page.locator("h1").first()).toBeVisible();
    await expect(page.locator('input[type="email"]')).toBeVisible();
    await expect(page.locator('input[type="password"]')).toBeVisible();
    await expect(page.locator('button[type="submit"]')).toBeVisible();
  });

  test("submit vacio activa validacion HTML5 (no se envia el form)", async ({ page }) => {
    await page.goto("/login");
    const url = page.url();
    await page.click('button[type="submit"]');
    // La URL no debe haber cambiado: el browser bloqueo el submit
    expect(page.url()).toBe(url);
    // El input email es required y queda focused
    const emailInput = page.locator('input[type="email"]');
    const isInvalid = await emailInput.evaluate(
      (el) => !(el as HTMLInputElement).validity.valid
    );
    expect(isInvalid).toBeTruthy();
  });

  test("email invalido activa validacion HTML5", async ({ page }) => {
    await page.goto("/login");
    await page.fill('input[type="email"]', "no-es-un-email");
    await page.fill('input[type="password"]', "x");
    await page.click('button[type="submit"]');
    const emailInput = page.locator('input[type="email"]');
    const isInvalid = await emailInput.evaluate(
      (el) => !(el as HTMLInputElement).validity.valid
    );
    expect(isInvalid).toBeTruthy();
  });

  test("olvido de contrasena visible como link", async ({ page }) => {
    await page.goto("/login");
    await expect(
      page.locator("a", { hasText: /forgot|olvid/i })
    ).toBeVisible();
  });
});

test.describe("Register page", () => {
  test("carga con form magic link y boton Google", async ({ page }) => {
    await page.goto("/registro");
    await expect(page.locator("h1").first()).toBeVisible();
    await expect(page.locator('input[type="text"]')).toBeVisible();
    await expect(page.locator('input[type="email"]')).toBeVisible();
    await expect(page.locator('button[type="submit"]')).toBeVisible();
    await expect(
      page.locator("button", { hasText: /google/i })
    ).toBeVisible();
  });
});

test.describe("Auth API contract", () => {
  test("POST /api/auth/login con body vacio devuelve 400, no 500", async ({ request }) => {
    const res = await request.post("/api/auth/login", {
      headers: { "Content-Type": "application/json" },
      data: {},
    });
    expect(res.status()).toBe(400);
    const body = await res.json();
    expect(body.error).toBeTruthy();
  });

  test("POST /api/auth/login con credenciales malas devuelve 401 (no 200)", async ({ request }) => {
    const res = await request.post("/api/auth/login", {
      headers: { "Content-Type": "application/json" },
      data: { email: "no-existe@example.com", password: "wrong" },
    });
    expect(res.status()).toBe(401);
    const body = await res.json();
    expect(body.error).toBeTruthy();
    // Nunca devolver el user/token en fallo
    expect(body.token).toBeUndefined();
  });
});
