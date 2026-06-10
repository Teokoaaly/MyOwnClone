import NextAuth from "next-auth";
import Google from "next-auth/providers/google";
import Resend from "next-auth/providers/resend";
import Credentials from "next-auth/providers/credentials";
import { DrizzleAdapter } from "@auth/drizzle-adapter";
import { db, schema } from "@/lib/db";
import { sql } from "drizzle-orm";
import bcrypt from "bcryptjs";
import {
  getPlatformAdminEmail,
  getPlatformAdminPasswordHash,
  hasPlatformAdminEnvCredentials,
  normalizeEmail,
} from "@/lib/platform-admin";

export const { handlers, auth, signIn, signOut } = NextAuth({
  session: { strategy: "jwt" },
  adapter: DrizzleAdapter(db, {
    usersTable: schema.users,
    accountsTable: schema.accounts,
    verificationTokensTable: schema.verificationTokens,
  }),
  providers: [
    Credentials({
      name: "credentials",
      credentials: {
        email: { label: "Email", type: "email" },
        password: { label: "Password", type: "password" },
      },
      async authorize(credentials) {
        if (!credentials?.email || !credentials?.password) return null;
        const email = normalizeEmail(credentials.email as string);
        const password = credentials.password as string;

        if (
          hasPlatformAdminEnvCredentials() &&
          email === getPlatformAdminEmail()
        ) {
          const valid = await bcrypt.compare(
            password,
            getPlatformAdminPasswordHash(),
          );

          if (!valid) return null;

          return {
            id: `platform-admin:${email}`,
            email,
            name: "Platform Admin",
            role: "platform_admin",
          };
        }

        try {
          // Use raw SQL to avoid Drizzle schema enum issues
          const result = await db.execute(
            sql`SELECT id, email, name, password_hash, role FROM ${schema.users} WHERE email = ${email} LIMIT 1`
          );
          const rows = result.rows as Array<{ id: string; email: string; name: string | null; password_hash: string | null; role: string }>;
          const user = rows?.[0];
          if (!user) return null;
          if (!user.password_hash) return null;

          const valid = await bcrypt.compare(password, user.password_hash);
          if (!valid) return null;

          return {
            id: user.id,
            email: user.email,
            name: user.name ?? undefined,
            role: user.role,
          };
        } catch {
          return null;
        }
      },
    }),
    Resend({
      from: process.env.RESEND_FROM_EMAIL,
    }),
    Google({
      clientId: process.env.AUTH_GOOGLE_ID!,
      clientSecret: process.env.AUTH_GOOGLE_SECRET!,
    }),
  ],
  pages: {
    signIn: "/login",
    verifyRequest: "/verificar",
  },
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        token.role = (user as any).role;
        token.id = user.id;
      }
      return token;
    },
    async session({ session, token }) {
      if (session.user) {
        session.user.id = token.id as string;
        (session.user as any).role = token.role as string;
      }
      return session;
    },
  },
});
