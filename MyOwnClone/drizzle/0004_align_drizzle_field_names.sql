DO $$
BEGIN
  IF EXISTS (
    SELECT 1
    FROM information_schema.columns
    WHERE table_schema = 'public'
      AND table_name = 'clone_configs'
      AND column_name = 'personality'
  ) THEN
    ALTER TABLE "clone_configs" ADD COLUMN IF NOT EXISTS "personality_tone" text;
    UPDATE "clone_configs"
    SET "personality_tone" = COALESCE(
      "personality_tone",
      NULLIF(trim(concat_ws(' ', "personality", "tone")), '')
    );
    ALTER TABLE "clone_configs" DROP COLUMN IF EXISTS "personality";
    ALTER TABLE "clone_configs" DROP COLUMN IF EXISTS "tone";
  END IF;
END $$;
--> statement-breakpoint

DO $$
BEGIN
  IF EXISTS (
    SELECT 1
    FROM information_schema.columns
    WHERE table_schema = 'public'
      AND table_name = 'meeting_types'
      AND column_name = 'duration'
  ) THEN
    ALTER TABLE "meeting_types" RENAME COLUMN "duration" TO "duration_minutes";
  END IF;

  IF EXISTS (
    SELECT 1
    FROM information_schema.columns
    WHERE table_schema = 'public'
      AND table_name = 'meeting_types'
      AND column_name = 'price'
  ) THEN
    ALTER TABLE "meeting_types" RENAME COLUMN "price" TO "price_cents";
  END IF;
END $$;
--> statement-breakpoint

DO $$
BEGIN
  IF EXISTS (
    SELECT 1
    FROM information_schema.columns
    WHERE table_schema = 'public'
      AND table_name = 'bookings'
      AND column_name = 'time'
  ) THEN
    ALTER TABLE "bookings" RENAME COLUMN "time" TO "start_time";
  END IF;

  ALTER TABLE "bookings" ADD COLUMN IF NOT EXISTS "end_time" text;
END $$;
--> statement-breakpoint

DO $$
BEGIN
  IF EXISTS (
    SELECT 1
    FROM information_schema.columns
    WHERE table_schema = 'public'
      AND table_name = 'products'
      AND column_name = 'price'
  ) THEN
    ALTER TABLE "products" RENAME COLUMN "price" TO "price_cents";
  END IF;
END $$;
