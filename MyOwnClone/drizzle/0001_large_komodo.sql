CREATE TYPE "public"."subscription_status" AS ENUM('active', 'inactive', 'trialing', 'past_due', 'cancelled');--> statement-breakpoint
ALTER TABLE "nextauth_accounts" ALTER COLUMN "expires_at" SET DATA TYPE integer;--> statement-breakpoint
ALTER TABLE "tenants" ADD COLUMN "subscription_status" "subscription_status" DEFAULT 'inactive' NOT NULL;--> statement-breakpoint
ALTER TABLE "users" ADD COLUMN "status" text DEFAULT 'active' NOT NULL;--> statement-breakpoint
ALTER TABLE "users" ADD COLUMN "is_platform_admin" boolean DEFAULT false NOT NULL;--> statement-breakpoint
ALTER TABLE "users" ADD COLUMN "last_login_at" timestamp;