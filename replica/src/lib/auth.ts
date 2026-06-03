import NextAuth from "next-auth";
import Google from "next-auth/providers/google";
import Resend from "next-auth/providers/resend";
import Credentials from "next-auth/providers/credentials";
import { DrizzleAdapter } from "@auth/drizzle-adapter";
import { db, schema } from "@/lib/db";

export const { handlers, auth, signIn, signOut } = NextAuth({
  session: { strategy: "jwt" },
adapter: DrizzleAdapter(db, {
    usersTable: schema.users,
    // @ts-expect-error — schema column names differ from adapter's expected postgres defaults
    accountsTable: schema.accounts,
    verificationTokensTable: schema.verificationTokens,
  }),
  providers: [
    Credentials({
      name: "Dev Login",
      credentials: {
        email: { label: "Email", type: "email" },
      },
      async authorize(credentials) {
        if (!credentials?.email) return null;

        // Development only: auto-create or find user
        const email = credentials.email as string;

        let user = await db.query.users.findFirst({
          where: (users, { eq }) => eq(users.email, email),
        });

        if (!user) {
          // Development only: auto-create or find user
          let tenant = await db.query.tenants.findFirst();
          
          // Auto-create tenant if none exists (dev mode)
          if (!tenant) {
            const [newTenant] = await db
              .insert(schema.tenants)
              .values({
                id: "dev-tenant-001",
                slug: "dev",
                name: "Developer Tenant",
                plan: "pro",
                status: "active",
              })
              .returning();
            tenant = newTenant;
          }

          const [newUser] = await db
            .insert(schema.users)
            .values({
              id: `dev-${Date.now()}`,
              tenantId: tenant.id,
              email,
              name: email.split("@")[0],
              role: "platform_admin",
            })
            .returning();
          user = newUser;
        }

        return {
          id: user.id,
          email: user.email,
          name: user.name,
          role: user.role,
        };
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
        token.role = user.role;
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
