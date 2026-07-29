import { renderPublicLanding } from "@/lib/public-landing";

export async function GET(): Promise<Response> {
  return renderPublicLanding();
}
