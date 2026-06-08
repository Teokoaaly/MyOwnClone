import NextAuth from "next-auth";
import Google from "next-auth/providers/google";
import Resend from "next-auth/providers/resend";
import Credentials from "next-auth/providers/credentials";
import { DrizzleAdapter } from "@auth/drizzle-adapter";
import { db, schema } from "@/lib/db";
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
          const user = await db.query.users.findFirst({
            where: (users, { eq }) => eq(users.email, email),
          });
          if (!user) return null;
          if (!user.passwordHash) return null;

          const valid = await bcrypt.compare(password, user.passwordHash);
          if (!valid) return null;

          return {
            id: user.id,
            email: user.email,
            name: user.name,
            // eslint-disable-next-line @typescript-eslint/no-explicit-any
            role: (user as any).role,
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
    newUser: "/onboarding",
  },
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        token.role = (user as any).role;
        token.id = user.id;
      }
      return token;
    },
    async session({ session, token }) {
      if (session.user) {
        session.user.id = token.id as string;
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        (session.user as any).role = token.role as string;
      }
      return session;
    },
  },
});
