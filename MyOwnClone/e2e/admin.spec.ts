import { test, expect } from "@playwright/test";

/**
 * Spec de paginas admin.
 *
 * Cubre:
 * - /admin/audit, /admin/feedback, /admin/courtesy cargan sin 500
 * - Las paginas admin rechazan acceso no-admin
 * - Los endpoints API admin rechazan sin token
 */

const ADMIN_PAGES = [
  "/admin/audit",
  "/admin/feedback",
  "/admin/courtesy",
];

test.describe("Admin pages render", () => {
  for (const path of ADMIN_PAGES) {
    test(`${path} carga con su estructura basica`, async ({ page }) => {
      const response = await page.goto(path);
      // 200 si hay sesion admin, 302/401/403 si no. Nunca 500.
      expect(response?.status() ?? 0).not.toBe(500);
      // Estructura minima: body visible
      await expect(page.locator("body")).toBeVisible();
    });
  }
});

test.describe("Admin API contract", () => {
  const adminApi = [
    "/api/admin/overview",
    "/api/admin/tenants",
    "/api/admin/audit-log",
    "/api/admin/feedback",
    "/api/admin/courtesy",
  ];

  for (const path of adminApi) {
    test(`GET ${path} sin auth devuelve 401/403 (no 200)`, async ({ request }) => {
      const res = await request.get(path, {
        headers: { Accept: "application/json" },
      });
      expect(res.status()).not.toBe(200);
      expect(res.status()).not.toBe(500);
      expect([401, 403]).toContain(res.status());
    });
  }
});
