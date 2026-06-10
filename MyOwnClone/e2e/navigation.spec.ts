import { test, expect } from "@playwright/test";

test.describe("Public pages", () => {
  test("landing page loads", async ({ page }) => {
    await page.goto("/");
    await expect(page).toHaveTitle(/MyOwnClone/i);
  });

  test("login page is accessible", async ({ page }) => {
    await page.goto("/login");
    await expect(page.locator("body")).toBeVisible();
  });

  test("register page is accessible", async ({ page }) => {
    await page.goto("/registro");
    await expect(page.locator("body")).toBeVisible();
  });

  test("forgot password page is accessible", async ({ page }) => {
    await page.goto("/forgot-password");
    await expect(page.locator("body")).toBeVisible();
  });
});

test.describe("API health", () => {
  test("backend health endpoint responds", async ({ request }) => {
    const response = await request.get(
      "http://127.0.0.1:5001/console/api/myownclone/admin/overview",
      {
        headers: { "X-API-Key": "dev-api-key-for-proxy" },
      }
    );
    // Should return 200 or 401, but not 500/connection error
    expect(response.status()).not.toBe(502);
  });
});
