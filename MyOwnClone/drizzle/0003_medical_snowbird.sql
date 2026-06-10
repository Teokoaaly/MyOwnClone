CREATE TYPE "public"."clone_feedback_rating" AS ENUM('up', 'down');--> statement-breakpoint
CREATE TYPE "public"."cost_category" AS ENUM('clone_response', 'content_ingestion', 'platform_ops');--> statement-breakpoint
CREATE TYPE "public"."inbound_email_status" AS ENUM('pending', 'sent', 'discarded', 'spam');--> statement-breakpoint
CREATE TABLE "clone_feedback" (
	"id" text PRIMARY KEY NOT NULL,
	"clone_id" text NOT NULL,
	"conversation_id" text,
	"message_id" text,
	"rating" "clone_feedback_rating" NOT NULL,
	"comment" text
);
--> statement-breakpoint
CREATE TABLE "cost_tracking" (
	"id" text PRIMARY KEY NOT NULL,
	"tenant_id" text NOT NULL,
	"category" "cost_category" NOT NULL,
	"operation" text,
	"model" text,
	"tokens_in" integer DEFAULT 0 NOT NULL,
	"tokens_out" integer DEFAULT 0 NOT NULL,
	"cost_cents" integer DEFAULT 0 NOT NULL,
	"created_at" timestamp DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "email_inbound" (
	"id" text PRIMARY KEY NOT NULL,
	"clone_id" text NOT NULL,
	"from_email" text,
	"from_name" text,
	"subject" text,
	"body_text" text,
	"body_html" text,
	"draft_reply" text,
	"status" "inbound_email_status" DEFAULT 'pending' NOT NULL,
	"labels" text[],
	"classification" text,
	"thread_id" text,
	"received_at" timestamp DEFAULT now() NOT NULL,
	"responded_at" timestamp
);
--> statement-breakpoint
CREATE TABLE "email_templates" (
	"id" text PRIMARY KEY NOT NULL,
	"clone_id" text NOT NULL,
	"name" text NOT NULL,
	"subject" text,
	"body" text,
	"trigger_keywords" text[],
	"created_at" timestamp DEFAULT now() NOT NULL,
	"updated_at" timestamp DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "impersonation_tokens" (
	"id" text PRIMARY KEY NOT NULL,
	"token" text NOT NULL,
	"admin_id" text NOT NULL,
	"tenant_id" text NOT NULL,
	"expires_at" timestamp NOT NULL,
	"created_at" timestamp DEFAULT now() NOT NULL,
	CONSTRAINT "impersonation_tokens_token_unique" UNIQUE("token")
);
--> statement-breakpoint
CREATE TABLE "myownclone_plans" (
	"id" text PRIMARY KEY NOT NULL,
	"name" text NOT NULL,
	"price_cents" integer NOT NULL,
	"stripe_price_id" text,
	"words_training_limit" bigint DEFAULT 500000 NOT NULL,
	"responses_month_limit" integer DEFAULT 2000 NOT NULL,
	"modes_active" integer DEFAULT 1 NOT NULL,
	"email_triage" boolean DEFAULT false NOT NULL,
	"booking" boolean DEFAULT false NOT NULL,
	"api_access" boolean DEFAULT false NOT NULL,
	"multi_clone" boolean DEFAULT false NOT NULL,
	"whitelabel" boolean DEFAULT false NOT NULL
);
--> statement-breakpoint
ALTER TABLE "clone_feedback" ADD CONSTRAINT "clone_feedback_clone_id_clone_configs_id_fk" FOREIGN KEY ("clone_id") REFERENCES "public"."clone_configs"("id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "cost_tracking" ADD CONSTRAINT "cost_tracking_tenant_id_tenants_id_fk" FOREIGN KEY ("tenant_id") REFERENCES "public"."tenants"("id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "email_inbound" ADD CONSTRAINT "email_inbound_clone_id_clone_configs_id_fk" FOREIGN KEY ("clone_id") REFERENCES "public"."clone_configs"("id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "email_templates" ADD CONSTRAINT "email_templates_clone_id_clone_configs_id_fk" FOREIGN KEY ("clone_id") REFERENCES "public"."clone_configs"("id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "impersonation_tokens" ADD CONSTRAINT "impersonation_tokens_admin_id_users_id_fk" FOREIGN KEY ("admin_id") REFERENCES "public"."users"("id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "impersonation_tokens" ADD CONSTRAINT "impersonation_tokens_tenant_id_tenants_id_fk" FOREIGN KEY ("tenant_id") REFERENCES "public"."tenants"("id") ON DELETE cascade ON UPDATE no action;--> statement-breakpoint
CREATE INDEX "clone_feedback_clone_id_idx" ON "clone_feedback" USING btree ("clone_id");--> statement-breakpoint
CREATE INDEX "cost_tracking_tenant_category_ts_idx" ON "cost_tracking" USING btree ("tenant_id","category","created_at");--> statement-breakpoint
CREATE INDEX "email_inbound_clone_status_idx" ON "email_inbound" USING btree ("clone_id","status");--> statement-breakpoint
CREATE INDEX "email_templates_clone_id_idx" ON "email_templates" USING btree ("clone_id");--> statement-breakpoint
CREATE INDEX "impersonation_tokens_admin_id_idx" ON "impersonation_tokens" USING btree ("admin_id");--> statement-breakpoint
CREATE INDEX "impersonation_tokens_tenant_id_idx" ON "impersonation_tokens" USING btree ("tenant_id");