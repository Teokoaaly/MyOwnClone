import { beforeEach, describe, expect, it, vi } from "vitest";
import DashboardAliasPage from "@/app/dashboard/page";

const mockAuth = vi.hoisted(() => vi.fn());
const mockRedirect = vi.hoisted(() => vi.fn());
const mockIsPlatformAdminSession = vi.hoisted(() => vi.fn());

vi.mock("@/lib/auth", () => ({
  auth: mockAuth,
}));

vi.mock("next/navigation", () => ({
  redirect: mockRedirect,
}));

vi.mock("@/lib/platform-admin", () => ({
  isPlatformAdminSession: mockIsPlatformAdminSession,
}));

describe("DashboardAliasPage", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it("redirects unauthenticated users to login", async () => {
    mockAuth.mockResolvedValue(null);

    await DashboardAliasPage();

    expect(mockRedirect).toHaveBeenCalledWith("/login");
  });

  it("redirects platform admins to admin summary", async () => {
    mockAuth.mockResolvedValue({
      user: { email: "admin@myownclone.com", role: "platform_admin" },
    });
    mockIsPlatformAdminSession.mockReturnValue(true);

    await DashboardAliasPage();

    expect(mockRedirect).toHaveBeenCalledWith("/admin/resumen");
  });

  it("redirects signed-in users to workspace summary", async () => {
    mockAuth.mockResolvedValue({
      user: { email: "owner@myownclone.com", role: "owner" },
    });
    mockIsPlatformAdminSession.mockReturnValue(false);

    await DashboardAliasPage();

    expect(mockRedirect).toHaveBeenCalledWith("/resumen");
  });
});
