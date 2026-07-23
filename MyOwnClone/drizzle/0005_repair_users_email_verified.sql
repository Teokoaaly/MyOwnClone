DO $$
BEGIN
  IF EXISTS (
    SELECT 1
    FROM information_schema.tables
    WHERE table_schema = 'public'
      AND table_name = 'users'
  ) THEN
    ALTER TABLE "users" ADD COLUMN IF NOT EXISTS "email_verified" timestamp;
  END IF;
END $$;
