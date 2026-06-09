CREATE TYPE "public"."source_type" AS ENUM('youtube', 'pdf', 'video', 'text', 'web', 'interview');
CREATE TYPE "public"."source_status" AS ENUM('uploading', 'processing', 'ready', 'error');
CREATE TYPE "public"."conversation_mode" AS ENUM('pedagogy', 'sales', 'support');

CREATE TABLE "sources" (
	"id" text PRIMARY KEY NOT NULL,
	"clone_id" text NOT NULL,
	"type" "source_type" NOT NULL,
	"title" text NOT NULL,
	"url" text,
	"status" "source_status" DEFAULT 'uploading' NOT NULL,
	"metadata" json,
	"created_at" timestamp DEFAULT now() NOT NULL,
	"updated_at" timestamp DEFAULT now() NOT NULL
);

CREATE TABLE "chunks" (
	"id" text PRIMARY KEY NOT NULL,
	"source_id" text NOT NULL,
	"content" text NOT NULL,
	"embedding" real[] NOT NULL,
	"token_count" integer,
	"metadata" json
);

CREATE TABLE "conversations" (
	"id" text PRIMARY KEY NOT NULL,
	"clone_id" text NOT NULL,
	"visitor_id" text,
	"mode" "conversation_mode" DEFAULT 'pedagogy' NOT NULL,
	"created_at" timestamp DEFAULT now() NOT NULL
);

CREATE TABLE "messages" (
	"id" text PRIMARY KEY NOT NULL,
	"conversation_id" text NOT NULL,
	"role" text NOT NULL,
	"content" text NOT NULL,
	"confidence" text,
	"sources" json,
	"feedback" text,
	"created_at" timestamp DEFAULT now() NOT NULL
);