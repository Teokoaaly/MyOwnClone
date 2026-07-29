import { renderPublicLanding } from "@/lib/public-landing";

export function GET(): Promise<Response> {
  return renderPublicLanding();
}
