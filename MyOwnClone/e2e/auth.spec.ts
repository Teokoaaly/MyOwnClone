import { test, expect } from "@playwright/test";

test.describe("Authentication flows", () => {
  test("login page loads with form elements", async ({ page }) => {
    await page.goto("/login");
    await expect(page.locator("h1")).toBeVisible();
    await expect(page.locator('input[type="email"]')).toBeVisible();
    await expect(page.locator('input[type="password"]')).toBeVisible();
    await expect(page.locator('button[type="submit"]')).toBeVisible();
  });

  test("register page loads with form elements", async ({ page }) => {
    await page.goto("/registro");
    await expect(page.locator("h1")).toBeVisible();
    await expect(page.locator('input[type="email"]')).toBeVisible();
    await expect(page.locator('input[type="password"]')).toBeVisible();
    await expect(page.locator('button[type="submit"]')).toBeVisible();
  });

  test("login form shows validation on empty submit", async ({ page }) => {
    await page.goto("/login");
    await page.click('button[type="submit"]');
    // HTML5 validation should prevent submission
    const emailInput = page.locator('input[type="email"]');
    await expect(emailInput).toBeFocused();
  });

  test("forgot password link is visible on login page", async ({ page }) => {
    await page.goto("/login");
    await expect(
      page.locator("a", { hasText: /forgot|olvid/i })
    ).toBeVisible();
  });

  test("register page has Google sign-in button", async ({ page }) => {
    await page.goto("/registro");
    await expect(
      page.locator("button", { hasText: /google/i })
    ).toBeVisible();
  });
});
