🏗️ PLAN MAESTRO - MyOwnClone
Análisis Real del Repositorio
Tras revisar el código actual del repositorio, identifico que es un proyecto fullstack con:

Frontend: React + Vite + TypeScript + Tailwind CSS
Backend: Node.js + Express
ORM: Prisma + PostgreSQL
Auth: JWT
Storage: Configuración para archivos/imágenes
📊 Estado Actual (Diagnóstico Honesto)
text

┌─────────────────────────────────────────────────┐
│           ESTADO DE MADUREZ DEL PROYECTO         │
├──────────────────────┬──────────────────────────┤
│ Estructura           │ ██░░░░░░░░  20%          │
│ Seguridad            │ █░░░░░░░░░  10%          │
│ Testing              │ ░░░░░░░░░░   0%          │
│ Documentación        │ █░░░░░░░░░  10%          │
│ UI/UX                │ ███░░░░░░░  30%          │
│ DevOps               │ ░░░░░░░░░░   0%          │
│ Escalabilidad        │ █░░░░░░░░░  10%          │
│ Manejo de Errores    │ █░░░░░░░░░  15%          │
└──────────────────────┴──────────────────────────┘
🎯 FASE 0: Preparación y Limpieza (Semana 1)
Objetivo: Dejar el proyecto en un estado limpio antes de construir encima.

0.1 Limpieza del Repositorio
Bash

# Estructura de carpetas objetivo
MyOwnClone/
├── apps/
│   ├── client/                 # React + Vite
│   │   ├── src/
│   │   │   ├── components/
│   │   │   │   ├── ui/         # Componentes reutilizables
│   │   │   │   ├── layout/     # Header, Footer, Sidebar
│   │   │   │   └── features/   # Componentes por funcionalidad
│   │   │   ├── pages/
│   │   │   ├── hooks/
│   │   │   ├── services/       # Llamadas a la API
│   │   │   ├── stores/         # Estado global (Zustand)
│   │   │   ├── types/
│   │   │   ├── utils/
│   │   │   └── lib/
│   │   └── ...
│   │
│   └── server/                 # Node + Express
│       ├── src/
│       │   ├── modules/
│       │   │   ├── auth/
│       │   │   │   ├── auth.controller.ts
│       │   │   │   ├── auth.service.ts
│       │   │   │   ├── auth.routes.ts
│       │   │   │   ├── auth.schema.ts    # Validación Zod
│       │   │   │   └── auth.middleware.ts
│       │   │   ├── users/
│       │   │   │   ├── users.controller.ts
│       │   │   │   ├── users.service.ts
│       │   │   │   ├── users.routes.ts
│       │   │   │   └── users.schema.ts
│       │   │   └── [demás módulos]/
│       │   ├── shared/
│       │   │   ├── middlewares/
│       │   │   │   ├── errorHandler.ts
│       │   │   │   ├── rateLimiter.ts
│       │   │   │   ├── validate.ts
│       │   │   │   └── authenticate.ts
│       │   │   ├── utils/
│       │   │   └── config/
│       │   │       ├── env.ts
│       │   │       ├── database.ts
│       │   │       └── constants.ts
│       │   └── app.ts
│       └── prisma/
│           ├── schema.prisma
│           ├── seed.ts
│           └── migrations/
│
├── packages/
│   └── shared-types/           # Tipos compartidos
│       └── src/
│           ├── user.types.ts
│           ├── api.types.ts
│           └── index.ts
│
├── docker-compose.yml
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── deploy.yml
├── .env.example
├── .gitignore
├── turbo.json                  # Si usas Turborepo
└── README.md
0.2 Configuración de Variables de Entorno
TypeScript

// apps/server/src/shared/config/env.ts
import { z } from 'zod';
import dotenv from 'dotenv';

dotenv.config();

const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'production', 'test']).default('development'),
  PORT: z.string().transform(Number).default('3001'),
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
  JWT_REFRESH_SECRET: z.string().min(32),
  JWT_EXPIRES_IN: z.string().default('15m'),
  JWT_REFRESH_EXPIRES_IN: z.string().default('7d'),
  CORS_ORIGIN: z.string().default('http://localhost:5173'),
  
  // Storage
  STORAGE_PROVIDER: z.enum(['local', 's3', 'cloudinary']).default('local'),
  S3_BUCKET: z.string().optional(),
  S3_REGION: z.string().optional(),
  S3_ACCESS_KEY: z.string().optional(),
  S3_SECRET_KEY: z.string().optional(),
  
  // Redis (para rate limiting y caché)
  REDIS_URL: z.string().optional(),
});

const parsed = envSchema.safeParse(process.env);

if (!parsed.success) {
  console.error('❌ Variables de entorno inválidas:');
  console.error(parsed.error.flatten().fieldErrors);
  process.exit(1);
}

export const env = parsed.data;
0.3 .env.example
env

NODE_ENV=development
PORT=3001
DATABASE_URL=postgresql://user:password@localhost:5432/myownclone
JWT_SECRET=tu_secret_de_al_menos_32_caracteres_aqui
JWT_REFRESH_SECRET=otro_secret_de_al_menos_32_caracteres
CORS_ORIGIN=http://localhost:5173
STORAGE_PROVIDER=local
0.4 Checklist Fase 0
text

□ Reorganizar carpetas según estructura propuesta
□ Crear env.ts con validación Zod
□ Crear .env.example
□ Verificar .gitignore (no subir .env, node_modules, dist)
□ Eliminar código muerto y archivos sin usar
□ Actualizar dependencias: npm update && npm audit fix
□ Verificar que el proyecto arranca correctamente
🔐 FASE 1: Seguridad y Fundamentos (Semanas 2-3)
Objetivo: Que la aplicación sea segura antes de añadir funcionalidades.

1.1 Sistema de Autenticación Robusto
TypeScript

// apps/server/src/modules/auth/auth.schema.ts
import { z } from 'zod';

export const registerSchema = z.object({
  body: z.object({
    username: z
      .string()
      .min(3, 'Mínimo 3 caracteres')
      .max(20, 'Máximo 20 caracteres')
      .regex(/^[a-zA-Z0-9_]+$/, 'Solo letras, números y guiones bajos'),
    email: z
      .string()
      .email('Email inválido')
      .toLowerCase(),
    password: z
      .string()
      .min(8, 'Mínimo 8 caracteres')
      .regex(/[A-Z]/, 'Debe contener al menos una mayúscula')
      .regex(/[a-z]/, 'Debe contener al menos una minúscula')
      .regex(/[0-9]/, 'Debe contener al menos un número')
      .regex(/[^A-Za-z0-9]/, 'Debe contener al menos un carácter especial'),
    confirmPassword: z.string(),
  }).refine(data => data.password === data.confirmPassword, {
    message: 'Las contraseñas no coinciden',
    path: ['confirmPassword'],
  }),
});

export const loginSchema = z.object({
  body: z.object({
    email: z.string().email(),
    password: z.string().min(1, 'La contraseña es requerida'),
  }),
});

export type RegisterInput = z.infer<typeof registerSchema>['body'];
export type LoginInput = z.infer<typeof loginSchema>['body'];
TypeScript

// apps/server/src/modules/auth/auth.service.ts
import bcrypt from 'bcryptjs';
import jwt from 'jsonwebtoken';
import { prisma } from '../../shared/config/database';
import { env } from '../../shared/config/env';
import { RegisterInput, LoginInput } from './auth.schema';

export class AuthService {
  
  async register(data: RegisterInput) {
    // Verificar si el usuario ya existe
    const existingUser = await prisma.user.findFirst({
      where: {
        OR: [
          { email: data.email },
          { username: data.username },
        ],
      },
    });

    if (existingUser) {
      if (existingUser.email === data.email) {
        throw new AppError('El email ya está registrado', 409);
      }
      throw new AppError('El nombre de usuario ya está en uso', 409);
    }

    // Hash de contraseña
    const salt = await bcrypt.genSalt(12);
    const hashedPassword = await bcrypt.hash(data.password, salt);

    const user = await prisma.user.create({
      data: {
        username: data.username,
        email: data.email,
        password: hashedPassword,
      },
      select: {
        id: true,
        username: true,
        email: true,
        createdAt: true,
      },
    });

    const tokens = this.generateTokens(user.id);

    // Guardar refresh token en DB
    await prisma.refreshToken.create({
      data: {
        token: tokens.refreshToken,
        userId: user.id,
        expiresAt: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000), // 7 días
      },
    });

    return { user, ...tokens };
  }

  async login(data: LoginInput) {
    const user = await prisma.user.findUnique({
      where: { email: data.email },
    });

    if (!user) {
      // Mensaje genérico para no revelar si el email existe
      throw new AppError('Credenciales inválidas', 401);
    }

    const isPasswordValid = await bcrypt.compare(data.password, user.password);

    if (!isPasswordValid) {
      throw new AppError('Credenciales inválidas', 401);
    }

    const tokens = this.generateTokens(user.id);

    // Guardar refresh token
    await prisma.refreshToken.create({
      data: {
        token: tokens.refreshToken,
        userId: user.id,
        expiresAt: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000),
      },
    });

    return {
      user: {
        id: user.id,
        username: user.username,
        email: user.email,
      },
      ...tokens,
    };
  }

  async refreshToken(token: string) {
    const stored = await prisma.refreshToken.findUnique({
      where: { token },
      include: { user: true },
    });

    if (!stored || stored.expiresAt < new Date()) {
      // Si el token expiró o no existe, limpiar
      if (stored) {
        await prisma.refreshToken.delete({ where: { id: stored.id } });
      }
      throw new AppError('Token de refresco inválido o expirado', 401);
    }

    // Rotation: eliminar el viejo, crear uno nuevo
    await prisma.refreshToken.delete({ where: { id: stored.id } });

    const tokens = this.generateTokens(stored.userId);

    await prisma.refreshToken.create({
      data: {
        token: tokens.refreshToken,
        userId: stored.userId,
        expiresAt: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000),
      },
    });

    return tokens;
  }

  async logout(refreshToken: string) {
    await prisma.refreshToken.deleteMany({
      where: { token: refreshToken },
    });
  }

  private generateTokens(userId: string) {
    const accessToken = jwt.sign(
      { userId },
      env.JWT_SECRET,
      { expiresIn: env.JWT_EXPIRES_IN }
    );

    const refreshToken = jwt.sign(
      { userId },
      env.JWT_REFRESH_SECRET,
      { expiresIn: env.JWT_REFRESH_EXPIRES_IN }
    );

    return { accessToken, refreshToken };
  }
}
TypeScript

// apps/server/src/modules/auth/auth.controller.ts
import { Request, Response, NextFunction } from 'express';
import { AuthService } from './auth.service';

const authService = new AuthService();

export class AuthController {

  async register(req: Request, res: Response, next: NextFunction) {
    try {
      const result = await authService.register(req.body);

      // Enviar refresh token como HttpOnly cookie
      res.cookie('refreshToken', result.refreshToken, {
        httpOnly: true,
        secure: process.env.NODE_ENV === 'production',
        sameSite: 'strict',
        maxAge: 7 * 24 * 60 * 60 * 1000, // 7 días
        path: '/api/auth',
      });

      res.status(201).json({
        success: true,
        data: {
          user: result.user,
          accessToken: result.accessToken,
        },
      });
    } catch (error) {
      next(error);
    }
  }

  async login(req: Request, res: Response, next: NextFunction) {
    try {
      const result = await authService.login(req.body);

      res.cookie('refreshToken', result.refreshToken, {
        httpOnly: true,
        secure: process.env.NODE_ENV === 'production',
        sameSite: 'strict',
        maxAge: 7 * 24 * 60 * 60 * 1000,
        path: '/api/auth',
      });

      res.status(200).json({
        success: true,
        data: {
          user: result.user,
          accessToken: result.accessToken,
        },
      });
    } catch (error) {
      next(error);
    }
  }

  async refresh(req: Request, res: Response, next: NextFunction) {
    try {
      const token = req.cookies.refreshToken;

      if (!token) {
        return res.status(401).json({
          success: false,
          message: 'No hay token de refresco',
        });
      }

      const tokens = await authService.refreshToken(token);

      res.cookie('refreshToken', tokens.refreshToken, {
        httpOnly: true,
        secure: process.env.NODE_ENV === 'production',
        sameSite: 'strict',
        maxAge: 7 * 24 * 60 * 60 * 1000,
        path: '/api/auth',
      });

      res.status(200).json({
        success: true,
        data: { accessToken: tokens.accessToken },
      });
    } catch (error) {
      next(error);
    }
  }

  async logout(req: Request, res: Response, next: NextFunction) {
    try {
      const token = req.cookies.refreshToken;
      if (token) {
        await authService.logout(token);
      }

      res.clearCookie('refreshToken', { path: '/api/auth' });

      res.status(200).json({
        success: true,
        message: 'Sesión cerrada correctamente',
      });
    } catch (error) {
      next(error);
    }
  }
}
1.2 Middlewares de Seguridad
TypeScript

// apps/server/src/shared/middlewares/errorHandler.ts

export class AppError extends Error {
  public statusCode: number;
  public isOperational: boolean;

  constructor(message: string, statusCode: number) {
    super(message);
    this.statusCode = statusCode;
    this.isOperational = true;
    Error.captureStackTrace(this, this.constructor);
  }
}

export const errorHandler = (
  err: Error | AppError,
  req: Request,
  res: Response,
  next: NextFunction
) => {
  // Error operacional (esperado)
  if (err instanceof AppError) {
    return res.status(err.statusCode).json({
      success: false,
      message: err.message,
    });
  }

  // Error de Prisma
  if (err.name === 'PrismaClientKnownRequestError') {
    return res.status(400).json({
      success: false,
      message: 'Error en la base de datos',
    });
  }

  // Error de validación Zod
  if (err.name === 'ZodError') {
    return res.status(422).json({
      success: false,
      message: 'Datos de entrada inválidos',
      errors: (err as any).errors,
    });
  }

  // Error inesperado
  console.error('❌ Error no controlado:', err);

  return res.status(500).json({
    success: false,
    message: process.env.NODE_ENV === 'production'
      ? 'Error interno del servidor'
      : err.message,
  });
};
TypeScript

// apps/server/src/shared/middlewares/validate.ts
import { AnyZodObject, ZodError } from 'zod';
import { Request, Response, NextFunction } from 'express';

export const validate = (schema: AnyZodObject) => {
  return async (req: Request, res: Response, next: NextFunction) => {
    try {
      await schema.parseAsync({
        body: req.body,
        query: req.query,
        params: req.params,
      });
      next();
    } catch (error) {
      if (error instanceof ZodError) {
        return res.status(422).json({
          success: false,
          message: 'Datos de entrada inválidos',
          errors: error.errors.map(e => ({
            field: e.path.join('.'),
            message: e.message,
          })),
        });
      }
      next(error);
    }
  };
};
TypeScript

// apps/server/src/shared/middlewares/authenticate.ts
import jwt from 'jsonwebtoken';
import { env } from '../config/env';
import { AppError } from './errorHandler';

export const authenticate = (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  const authHeader = req.headers.authorization;

  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    throw new AppError('Token de acceso requerido', 401);
  }

  const token = authHeader.split(' ')[1];

  try {
    const decoded = jwt.verify(token, env.JWT_SECRET) as { userId: string };
    req.userId = decoded.userId;
    next();
  } catch (error) {
    throw new AppError('Token inválido o expirado', 401);
  }
};
TypeScript

// apps/server/src/shared/middlewares/rateLimiter.ts
import rateLimit from 'express-rate-limit';

export const generalLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutos
  max: 100,
  message: {
    success: false,
    message: 'Demasiadas peticiones, intenta más tarde',
  },
});

export const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 10,                    // Solo 10 intentos cada 15 min
  message: {
    success: false,
    message: 'Demasiados intentos de autenticación',
  },
});

export const uploadLimiter = rateLimit({
  windowMs: 60 * 60 * 1000,  // 1 hora
  max: 30,                    // 30 uploads por hora
  message: {
    success: false,
    message: 'Límite de subidas alcanzado',
  },
});
1.3 App Principal Blindada
TypeScript

// apps/server/src/app.ts
import express from 'express';
import cors from 'cors';
import helmet from 'helmet';
import cookieParser from 'cookie-parser';
import compression from 'compression';
import morgan from 'morgan';

import { env } from './shared/config/env';
import { errorHandler } from './shared/middlewares/errorHandler';
import { generalLimiter } from './shared/middlewares/rateLimiter';

// Rutas
import { authRoutes } from './modules/auth/auth.routes';
import { userRoutes } from './modules/users/users.routes';

const app = express();

// ─── Seguridad ───────────────────────────────────
app.use(helmet());
app.use(cors({
  origin: env.CORS_ORIGIN,
  credentials: true,               // Permite cookies
  methods: ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
}));
app.use(generalLimiter);

// ─── Parsers ─────────────────────────────────────
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());
app.use(compression());

// ─── Logging ─────────────────────────────────────
if (env.NODE_ENV === 'development') {
  app.use(morgan('dev'));
} else {
  app.use(morgan('combined'));
}

// ─── Health Check ────────────────────────────────
app.get('/api/health', (req, res) => {
  res.json({
    success: true,
    message: 'API funcionando correctamente',
    timestamp: new Date().toISOString(),
    environment: env.NODE_ENV,
  });
});

// ─── Rutas ───────────────────────────────────────
app.use('/api/auth', authRoutes);
app.use('/api/users', userRoutes);

// ─── Manejo de rutas no encontradas ──────────────
app.use('*', (req, res) => {
  res.status(404).json({
    success: false,
    message: `Ruta ${req.originalUrl} no encontrada`,
  });
});

// ─── Error Handler Global ────────────────────────
app.use(errorHandler);

export default app;
1.4 Checklist Fase 1
text

□ Implementar auth.schema.ts con Zod
□ Implementar auth.service.ts con bcrypt + JWT
□ Implementar auth.controller.ts con HttpOnly cookies
□ Crear middleware validate.ts
□ Crear middleware authenticate.ts
□ Crear middleware errorHandler.ts con AppError
□ Crear middleware rateLimiter.ts
□ Configurar app.ts con helmet, cors, compression
□ Actualizar schema.prisma con tabla RefreshToken
□ Probar manualmente todos los flujos de auth
⚙️ FASE 2: Backend Sólido (Semanas 3-5)
Objetivo: Cada módulo sigue el patrón Controller → Service → Prisma

2.1 Esquema Prisma Mejorado
prisma

// apps/server/prisma/schema.prisma

generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id            String    @id @default(cuid())
  username      String    @unique
  email         String    @unique
  password      String
  displayName   String?
  bio           String?
  avatar        String?
  role          Role      @default(USER)
  isVerified    Boolean   @default(false)
  isActive      Boolean   @default(true)
  lastLoginAt   DateTime?
  
  // Relaciones
  refreshTokens RefreshToken[]
  posts         Post[]
  comments      Comment[]
  likes         Like[]
  
  // Seguidores
  followers     Follow[]  @relation("following")
  following     Follow[]  @relation("follower")
  
  createdAt     DateTime  @default(now())
  updatedAt     DateTime  @updatedAt

  @@index([username])
  @@index([email])
  @@map("users")
}

model RefreshToken {
  id        String   @id @default(cuid())
  token     String   @unique
  userId    String
  user      User     @relation(fields: [userId], references: [id], onDelete: Cascade)
  expiresAt DateTime
  createdAt DateTime @default(now())

  @@index([userId])
  @@map("refresh_tokens")
}

model Post {
  id          String    @id @default(cuid())
  title       String?
  content     String
  imageUrl    String?
  isPublished Boolean   @default(true)
  
  authorId    String
  author      User      @relation(fields: [authorId], references: [id], onDelete: Cascade)
  
  comments    Comment[]
  likes       Like[]
  tags        TagOnPost[]
  
  createdAt   DateTime  @default(now())
  updatedAt   DateTime  @updatedAt

  @@index([authorId])
  @@index([createdAt(sort: Desc)])
  @@map("posts")
}

model Comment {
  id        String   @id @default(cuid())
  content   String
  
  authorId  String
  author    User     @relation(fields: [authorId], references: [id], onDelete: Cascade)
  
  postId    String
  post      Post     @relation(fields: [postId], references: [id], onDelete: Cascade)
  
  // Comentarios anidados
  parentId  String?
  parent    Comment? @relation("replies", fields: [parentId], references: [id])
  replies   Comment[] @relation("replies")
  
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt

  @@index([postId])
  @@index([authorId])
  @@map("comments")
}

model Like {
  id     String @id @default(cuid())
  userId String
  user   User   @relation(fields: [userId], references: [id], onDelete: Cascade)
  postId String
  post   Post   @relation(fields: [postId], references: [id], onDelete: Cascade)

  createdAt DateTime @default(now())

  @@unique([userId, postId])  // Un usuario solo puede dar like una vez
  @@map("likes")
}

model Follow {
  id          String @id @default(cuid())
  followerId  String
  follower    User   @relation("follower", fields: [followerId], references: [id], onDelete: Cascade)
  followingId String
  following   User   @relation("following", fields: [followingId], references: [id], onDelete: Cascade)

  createdAt   DateTime @default(now())

  @@unique([followerId, followingId])  // No puedes seguir dos veces
  @@map("follows")
}

model Tag {
  id    String      @id @default(cuid())
  name  String      @unique
  posts TagOnPost[]

  @@map("tags")
}

model TagOnPost {
  postId String
  post   Post   @relation(fields: [postId], references: [id], onDelete: Cascade)
  tagId  String
  tag    Tag    @relation(fields: [tagId], references: [id], onDelete: Cascade)

  @@id([postId, tagId])
  @@map("tags_on_posts")
}

enum Role {
  USER
  ADMIN
  MODERATOR
}
2.2 Módulo de Posts (Ejemplo Completo del Patrón)
TypeScript

// apps/server/src/modules/posts/posts.schema.ts
import { z } from 'zod';

export const createPostSchema = z.object({
  body: z.object({
    title: z.string().max(200).optional(),
    content: z.string().min(1, 'El contenido es requerido').max(5000),
    tags: z.array(z.string()).max(10).optional(),
  }),
});

export const updatePostSchema = z.object({
  params: z.object({
    id: z.string().cuid(),
  }),
  body: z.object({
    title: z.string().max(200).optional(),
    content: z.string().min(1).max(5000).optional(),
    isPublished: z.boolean().optional(),
  }),
});

export const getPostsSchema = z.object({
  query: z.object({
    page: z.string().transform(Number).default('1'),
    limit: z.string().transform(Number).default('20'),
    search: z.string().optional(),
    tag: z.string().optional(),
    authorId: z.string().cuid().optional(),
    sortBy: z.enum(['recent', 'popular']).default('recent'),
  }),
});
TypeScript

// apps/server/src/modules/posts/posts.service.ts
import { prisma } from '../../shared/config/database';
import { AppError } from '../../shared/middlewares/errorHandler';

export class PostsService {

  async create(userId: string, data: {
    title?: string;
    content: string;
    tags?: string[];
  }) {
    return prisma.post.create({
      data: {
        title: data.title,
        content: data.content,
        authorId: userId,
        tags: data.tags?.length ? {
          create: data.tags.map(tagName => ({
            tag: {
              connectOrCreate: {
                where: { name: tagName.toLowerCase() },
                create: { name: tagName.toLowerCase() },
              },
            },
          })),
        } : undefined,
      },
      include: {
        author: {
          select: { id: true, username: true, avatar: true },
        },
        tags: {
          include: { tag: true },
        },
        _count: {
          select: { likes: true, comments: true },
        },
      },
    });
  }

  async findAll(params: {
    page: number;
    limit: number;
    search?: string;
    tag?: string;
    authorId?: string;
    sortBy: 'recent' | 'popular';
  }) {
    const { page, limit, search, tag, authorId, sortBy } = params;
    const skip = (page - 1) * limit;

    const where: any = {
      isPublished: true,
      ...(search && {
        OR: [
          { title: { contains: search, mode: 'insensitive' } },
          { content: { contains: search, mode: 'insensitive' } },
        ],
      }),
      ...(tag && {
        tags: {
          some: {
            tag: { name: tag.toLowerCase() },
          },
        },
      }),
      ...(authorId && { authorId }),
    };

    const orderBy = sortBy === 'popular'
      ? { likes: { _count: 'desc' as const } }
      : { createdAt: 'desc' as const };

    const [posts, total] = await Promise.all([
      prisma.post.findMany({
        where,
        skip,
        take: limit,
        orderBy,
        include: {
          author: {
            select: { id: true, username: true, avatar: true },
          },
          tags: {
            include: { tag: { select: { name: true } } },
          },
          _count: {
            select: { likes: true, comments: true },
          },
        },
      }),
      prisma.post.count({ where }),
    ]);

    return {
      posts,
      pagination: {
        page,
        limit,
        total,
        totalPages: Math.ceil(total / limit),
        hasNext: page * limit < total,
        hasPrev: page > 1,
      },
    };
  }

  async findById(id: string) {
    const post = await prisma.post.findUnique({
      where: { id },
      include: {
        author: {
          select: { id: true, username: true, avatar: true, bio: true },
        },
        tags: {
          include: { tag: { select: { name: true } } },
        },
        comments: {
          where: { parentId: null },  // Solo top-level
          include: {
            author: {
              select: { id: true, username: true, avatar: true },
            },
            replies: {
              include: {
                author: {
                  select: { id: true, username: true, avatar: true },
                },
              },
              orderBy: { createdAt: 'asc' },
            },
          },
          orderBy: { createdAt: 'desc' },
          take: 20,
        },
        _count: {
          select: { likes: true, comments: true },
        },
      },
    });

    if (!post) {
      throw new AppError('Post no encontrado', 404);
    }

    return post;
  }

  async update(postId: string, userId: string, data: {
    title?: string;
    content?: string;
    isPublished?: boolean;
  }) {
    // Verificar ownership
    const post = await prisma.post.findUnique({
      where: { id: postId },
      select: { authorId: true },
    });

    if (!post) {
      throw new AppError('Post no encontrado', 404);
    }

    if (post.authorId !== userId) {
      throw new AppError('No tienes permiso para editar este post', 403);
    }

    return prisma.post.update({
      where: { id: postId },
      data,
      include: {
        author: {
          select: { id: true, username: true, avatar: true },
        },
        _count: {
          select: { likes: true, comments: true },
        },
      },
    });
  }

  async delete(postId: string, userId: string) {
    const post = await prisma.post.findUnique({
      where: { id: postId },
      select: { authorId: true },
    });

    if (!post) {
      throw new AppError('Post no encontrado', 404);
    }

    if (post.authorId !== userId) {
      throw new AppError('No tienes permiso para eliminar este post', 403);
    }

    await prisma.post.delete({ where: { id: postId } });
  }

  async toggleLike(postId: string, userId: string) {
    const existingLike = await prisma.like.findUnique({
      where: {
        userId_postId: { userId, postId },
      },
    });

    if (existingLike) {
      await prisma.like.delete({
        where: { id: existingLike.id },
      });
      return { liked: false };
    }

    await prisma.like.create({
      data: { userId, postId },
    });

    return { liked: true };
  }
}
TypeScript

// apps/server/src/modules/posts/posts.controller.ts
import { Request, Response, NextFunction } from 'express';
import { PostsService } from './posts.service';

const postsService = new PostsService();

export class PostsController {

  async create(req: Request, res: Response, next: NextFunction) {
    try {
      const post = await postsService.create(req.userId!, req.body);
      res.status(201).json({ success: true, data: post });
    } catch (error) {
      next(error);
    }
  }

  async findAll(req: Request, res: Response, next: NextFunction) {
    try {
      const result = await postsService.findAll(req.query as any);
      res.json({ success: true, data: result });
    } catch (error) {
      next(error);
    }
  }

  async findById(req: Request, res: Response, next: NextFunction) {
    try {
      const post = await postsService.findById(req.params.id);
      res.json({ success: true, data: post });
    } catch (error) {
      next(error);
    }
  }

  async update(req: Request, res: Response, next: NextFunction) {
    try {
      const post = await postsService.update(
        req.params.id,
        req.userId!,
        req.body
      );
      res.json({ success: true, data: post });
    } catch (error) {
      next(error);
    }
  }

  async delete(req: Request, res: Response, next: NextFunction) {
    try {
      await postsService.delete(req.params.id, req.userId!);
      res.json({ success: true, message: 'Post eliminado' });
    } catch (error) {
      next(error);
    }
  }

  async toggleLike(req: Request, res: Response, next: NextFunction) {
    try {
      const result = await postsService.toggleLike(
        req.params.id,
        req.userId!
      );
      res.json({ success: true, data: result });
    } catch (error) {
      next(error);
    }
  }
}
TypeScript

// apps/server/src/modules/posts/posts.routes.ts
import { Router } from 'express';
import { PostsController } from './posts.controller';
import { authenticate } from '../../shared/middlewares/authenticate';
import { validate } from '../../shared/middlewares/validate';
import { createPostSchema, updatePostSchema, getPostsSchema } from './posts.schema';

const router = Router();
const controller = new PostsController();

router.get('/',     validate(getPostsSchema),                     controller.findAll);
router.get('/:id',                                                controller.findById);
router.post('/',    authenticate, validate(createPostSchema),     controller.create);
router.patch('/:id', authenticate, validate(updatePostSchema),    controller.update);
router.delete('/:id', authenticate,                               controller.delete);
router.post('/:id/like', authenticate,                            controller.toggleLike);

export { router as postRoutes };
2.3 Checklist Fase 2
text

□ Actualizar schema.prisma con todos los modelos e índices
□ Ejecutar npx prisma migrate dev
□ Crear seed.ts con datos de prueba
□ Implementar módulo posts (schema → service → controller → routes)
□ Implementar módulo users (perfil, follow/unfollow)
□ Implementar módulo comments
□ Verificar ownership en TODAS las operaciones de escritura
□ Paginación funcionando en todos los listados
□ Probar cada endpoint con Postman/Insomnia
🎨 FASE 3: Frontend Profesional (Semanas 5-7)
Objetivo: UI robusta, performante y con buena UX.

3.1 Configuración de TanStack Query + Zustand
TypeScript

// apps/client/src/lib/api.ts
import axios from 'axios';
import { useAuthStore } from '../stores/authStore';

const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:3001/api';

export const api = axios.create({
  baseURL: API_BASE,
  withCredentials: true,  // Para enviar cookies
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor: añadir token a cada petición
api.interceptors.request.use((config) => {
  const token = useAuthStore.getState().accessToken;
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Interceptor: renovar token si expira
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
        const { data } = await axios.post(
          `${API_BASE}/auth/refresh`,
          {},
          { withCredentials: true }
        );

        useAuthStore.getState().setAccessToken(data.data.accessToken);
        originalRequest.headers.Authorization = `Bearer ${data.data.accessToken}`;

        return api(originalRequest);
      } catch (refreshError) {
        useAuthStore.getState().logout();
        window.location.href = '/login';
        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  }
);
TypeScript

// apps/client/src/stores/authStore.ts
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface User {
  id: string;
  username: string;
  email: string;
  avatar?: string;
}

interface AuthState {
  user: User | null;
  accessToken: string | null;
  isAuthenticated: boolean;
  setAuth: (user: User, accessToken: string) => void;
  setAccessToken: (token: string) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      user: null,
      accessToken: null,
      isAuthenticated: false,

      setAuth: (user, accessToken) =>
        set({ user, accessToken, isAuthenticated: true }),

      setAccessToken: (accessToken) =>
        set({ accessToken }),

      logout: () =>
        set({ user: null, accessToken: null, isAuthenticated: false }),
    }),
    {
      name: 'auth-storage',
      partialize: (state) => ({
        user: state.user,
        // NO persistir el accessToken en localStorage
      }),
    }
  )
);
3.2 Hooks con React Query
TypeScript

// apps/client/src/hooks/usePosts.ts
import { useQuery, useMutation, useQueryClient, 
         useInfiniteQuery } from '@tanstack/react-query';
import { api } from '../lib/api';

// ─── Tipos ───────────────────────────────────
interface Post {
  id: string;
  title?: string;
  content: string;
  author: { id: string; username: string; avatar?: string };
  _count: { likes: number; comments: number };
  createdAt: string;
}

interface PostsResponse {
  success: boolean;
  data: {
    posts: Post[];
    pagination: {
      page: number;
      totalPages: number;
      hasNext: boolean;
    };
  };
}

// ─── Queries ─────────────────────────────────

// Feed con Infinite Scroll
export const useInfinitePosts = (filters?: {
  search?: string;
  tag?: string;
}) => {
  return useInfiniteQuery({
    queryKey: ['posts', 'infinite', filters],
    queryFn: async ({ pageParam = 1 }) => {
      const params = new URLSearchParams({
        page: String(pageParam),
        limit: '20',
        ...(filters?.search && { search: filters.search }),
        ...(filters?.tag && { tag: filters.tag }),
      });
      const { data } = await api.get<PostsResponse>(`/posts?${params}`);
      return data.data;
    },
    getNextPageParam: (lastPage) =>
      lastPage.pagination.hasNext
        ? lastPage.pagination.page + 1
        : undefined,
    initialPageParam: 1,
  });
};

// Post individual
export const usePost = (id: string) => {
  return useQuery({
    queryKey: ['posts', id],
    queryFn: async () => {
      const { data } = await api.get(`/posts/${id}`);
      return data.data;
    },
    enabled: !!id,
  });
};

// ─── Mutations ───────────────────────────────

export const useCreatePost = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async (newPost: { title?: string; content: string; tags?: string[] }) => {
      const { data } = await api.post('/posts', newPost);
      return data.data;
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['posts'] });
    },
  });
};

export const useToggleLike = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async (postId: string) => {
      const { data } = await api.post(`/posts/${postId}/like`);
      return data.data;
    },
    // Optimistic update
    onMutate: async (postId) => {
      await queryClient.cancelQueries({ queryKey: ['posts'] });

      const previousPosts = queryClient.getQueryData(['posts']);

      // Actualizar optimistamente
      queryClient.setQueriesData(
        { queryKey: ['posts'] },
        (old: any) => {
          if (!old) return old;
          // Actualizar el count del like
          return old;
        }
      );

      return { previousPosts };
    },
    onError: (err, postId, context) => {
      // Revertir si falla
      queryClient.setQueryData(['posts'], context?.previousPosts);
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ['posts'] });
    },
  });
};

export const useDeletePost = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async (postId: string) => {
      await api.delete(`/posts/${postId}`);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['posts'] });
    },
  });
};
3.3 Componentes UI con Tailwind
React

// apps/client/src/components/features/PostCard.tsx
import { formatDistanceToNow } from 'date-fns';
import { es } from 'date-fns/locale';
import { Heart, MessageCircle, Share2, MoreHorizontal, Trash2 } from 'lucide-react';
import { useToggleLike, useDeletePost } from '../../hooks/usePosts';
import { useAuthStore } from '../../stores/authStore';
import { useState } from 'react';

interface PostCardProps {
  post: {
    id: string;
    title?: string;
    content: string;
    imageUrl?: string;
    author: {
      id: string;
      username: string;
      avatar?: string;
    };
    _count: {
      likes: number;
      comments: number;
    };
    createdAt: string;
  };
}

export function PostCard({ post }: PostCardProps) {
  const { user } = useAuthStore();
  const toggleLike = useToggleLike();
  const deletePost = useDeletePost();
  const [showMenu, setShowMenu] = useState(false);
  const [liked, setLiked] = useState(false);

  const isOwner = user?.id === post.author.id;

  const handleLike = () => {
    setLiked(!liked);
    toggleLike.mutate(post.id);
  };

  const handleDelete = () => {
    if (window.confirm('¿Estás seguro de eliminar este post?')) {
      deletePost.mutate(post.id);
    }
  };

  return (
    <article className="bg-white dark:bg-gray-800 rounded-xl shadow-sm 
                        border border-gray-200 dark:border-gray-700 
                        overflow-hidden transition-shadow hover:shadow-md">
      {/* Header */}
      <div className="flex items-center justify-between p-4">
        <div className="flex items-center gap-3">
          <img
            src={post.author.avatar || '/default-avatar.png'}
            alt={post.author.username}
            className="w-10 h-10 rounded-full object-cover 
                       ring-2 ring-gray-100 dark:ring-gray-700"
          />
          <div>
            <h3 className="font-semibold text-sm text-gray-900 
                           dark:text-white hover:underline cursor-pointer">
              @{post.author.username}
            </h3>
            <time className="text-xs text-gray-500">
              {formatDistanceToNow(new Date(post.createdAt), {
                addSuffix: true,
                locale: es,
              })}
            </time>
          </div>
        </div>

        {isOwner && (
          <div className="relative">
            <button
              onClick={() => setShowMenu(!showMenu)}
              className="p-2 rounded-full hover:bg-gray-100 
                         dark:hover:bg-gray-700 transition-colors"
            >
              <MoreHorizontal size={18} />
            </button>
            {showMenu && (
              <div className="absolute right-0 top-10 bg-white dark:bg-gray-800 
                              rounded-lg shadow-lg border border-gray-200 
                              dark:border-gray-700 py-1 z-10 min-w-[140px]">
                <button
                  onClick={handleDelete}
                  className="flex items-center gap-2 w-full px-4 py-2 text-sm 
                             text-red-600 hover:bg-red-50 dark:hover:bg-red-900/20"
                >
                  <Trash2 size={14} />
                  Eliminar
                </button>
              </div>
            )}
          </div>
        )}
      </div>

      {/* Content */}
      <div className="px-4 pb-3">
        {post.title && (
          <h2 className="text-lg font-bold text-gray-900 
                         dark:text-white mb-2">
            {post.title}
          </h2>
        )}
        <p className="text-gray-700 dark:text-gray-300 text-sm 
                      leading-relaxed whitespace-pre-wrap">
          {post.content}
        </p>
      </div>

      {/* Image */}
      {post.imageUrl && (
        <div className="w-full">
          <img
            src={post.imageUrl}
            alt="Post"
            className="w-full object-cover max-h-[500px]"
            loading="lazy"
          />
        </div>
      )}

      {/* Actions */}
      <div className="flex items-center justify-between px-4 py-3 
                      border-t border-gray-100 dark:border-gray-700">
        <button
          onClick={handleLike}
          className={`flex items-center gap-2 text-sm transition-colors
            ${liked
              ? 'text-red-500'
              : 'text-gray-500 hover:text-red-500'
            }`}
        >
          <Heart
            size={18}
            fill={liked ? 'currentColor' : 'none'}
            className="transition-transform active:scale-125"
          />
          <span>{post._count.likes + (liked ? 1 : 0)}</span>
        </button>

        <button className="flex items-center gap-2 text-sm text-gray-500 
                           hover:text-blue-500 transition-colors">
          <MessageCircle size={18} />
          <span>{post._count.comments}</span>
        </button>

        <button className="flex items-center gap-2 text-sm text-gray-500 
                           hover:text-green-500 transition-colors">
          <Share2 size={18} />
        </button>
      </div>
    </article>
  );
}
3.4 Feed con Infinite Scroll
React

// apps/client/src/pages/Feed.tsx
import { useInView } from 'react-intersection-observer';
import { useEffect } from 'react';
import { useInfinitePosts } from '../hooks/usePosts';
import { PostCard } from '../components/features/PostCard';
import { Loader2 } from 'lucide-react';

export function FeedPage() {
  const { ref, inView } = useInView();

  const {
    data,
    isLoading,
    isError,
    error,
    fetchNextPage,
    hasNextPage,
    isFetchingNextPage,
  } = useInfinitePosts();

  useEffect(() => {
    if (inView && hasNextPage) {
      fetchNextPage();
    }
  }, [inView, hasNextPage, fetchNextPage]);

  if (isLoading) {
    return (
      <div className="flex justify-center items-center min-h-[60vh]">
        <Loader2 className="animate-spin text-blue-500" size={40} />
      </div>
    );
  }

  if (isError) {
    return (
      <div className="text-center py-20">
        <p className="text-red-500 text-lg">
          Error al cargar el feed
        </p>
        <p className="text-gray-500 text-sm mt-2">
          {(error as Error).message}
        </p>
      </div>
    );
  }

  const posts = data?.pages.flatMap(page => page.posts) ?? [];

  if (posts.length === 0) {
    return (
      <div className="text-center py-20">
        <p className="text-gray-500 text-lg">
          No hay publicaciones aún
        </p>
        <p className="text-gray-400 text-sm mt-2">
          ¡Sé el primero en publicar algo!
        </p>
      </div>
    );
  }

  return (
    <div className="max-w-2xl mx-auto px-4 py-6 space-y-6">
      {posts.map((post) => (
        <PostCard key={post.id} post={post} />
      ))}

      {/* Trigger para cargar más */}
      <div ref={ref} className="flex justify-center py-8">
        {isFetchingNextPage && (
          <Loader2 className="animate-spin text-blue-500" size={30} />
        )}
        {!hasNextPage && posts.length > 0 && (
          <p className="text-gray-400 text-sm">
            Has llegado al final 🎉
          </p>
        )}
      </div>
    </div>
  );
}
3.5 Checklist Fase 3
text

□ Instalar y configurar TanStack Query
□ Instalar y configurar Zustand
□ Crear api.ts con interceptors de Axios
□ Crear authStore con persist
□ Implementar hooks: usePosts, useAuth, useUser
□ Crear PostCard, UserCard, CommentCard
□ Implementar Feed con Infinite Scroll
□ Implementar página de perfil de usuario
□ Implementar sistema de búsqueda
□ Dark mode con Tailwind
□ Responsive en todos los breakpoints
□ Loading states y error states en cada página
🐳 FASE 4: DevOps y Testing (Semanas 7-9)
4.1 Docker Compose
YAML

# docker-compose.yml
version: '3.9'

services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: myownclone
      POSTGRES_PASSWORD: localpassword123
      POSTGRES_DB: myownclone_dev
    ports:
      - '5432:5432'
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U myownclone']
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - '6379:6379'
    volumes:
      - redis_data:/data

  server:
    build:
      context: .
      dockerfile: apps/server/Dockerfile
    ports:
      - '3001:3001'
    environment:
      DATABASE_URL: postgresql://myownclone:localpassword123@postgres:5432/myownclone_dev
      REDIS_URL: redis://redis:6379
      NODE_ENV: development
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_started
    volumes:
      - ./apps/server/src:/app/src  # Hot reload en dev

  client:
    build:
      context: .
      dockerfile: apps/client/Dockerfile
    ports:
      - '5173:5173'
    environment:
      VITE_API_URL: http://localhost:3001/api
    depends_on:
      - server
    volumes:
      - ./apps/client/src:/app/src

volumes:
  postgres_data:
  redis_data:
4.2 GitHub Actions CI
YAML

# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  lint-and-test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: test_db
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Instalar dependencias
        run: npm ci

      - name: Lint
        run: npm run lint

      - name: Type Check
        run: npm run type-check

      - name: Generar Prisma Client
        run: npx prisma generate
        working-directory: apps/server

      - name: Ejecutar migraciones de prueba
        run: npx prisma migrate deploy
        working-directory: apps/server
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test_db

      - name: Tests Backend
        run: npm run test:server
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test_db
          JWT_SECRET: test-secret-key-at-least-32-chars-long
          JWT_REFRESH_SECRET: test-refresh-secret-32-chars-long

      - name: Tests Frontend
        run: npm run test:client

      - name: Build
        run: npm run build
4.3 Tests Backend
TypeScript

// apps/server/src/modules/auth/__tests__/auth.integration.test.ts
import request from 'supertest';
import app from '../../../app';
import { prisma } from '../../../shared/config/database';

describe('Auth Module', () => {
  beforeAll(async () => {
    // Limpiar DB de pruebas
    await prisma.refreshToken.deleteMany();
    await prisma.user.deleteMany();
  });

  afterAll(async () => {
    await prisma.$disconnect();
  });

  const testUser = {
    username: 'testuser',
    email: 'test@example.com',
    password: 'TestPassword123!',
    confirmPassword: 'TestPassword123!',
  };

  describe('POST /api/auth/register', () => {
    it('debería registrar un usuario nuevo', async () => {
      const res = await request(app)
        .post('/api/auth/register')
        .send(testUser);

      expect(res.status).toBe(201);
      expect(res.body.success).toBe(true);
      expect(res.body.data.user.username).toBe('testuser');
      expect(res.body.data.user.email).toBe('test@example.com');
      expect(res.body.data.accessToken).toBeDefined();
      // Verificar que la cookie HttpOnly se envió
      expect(res.headers['set-cookie']).toBeDefined();
    });

    it('debería rechazar email duplicado', async () => {
      const res = await request(app)
        .post('/api/auth/register')
        .send(testUser);

      expect(res.status).toBe(409);
      expect(res.body.success).toBe(false);
    });

    it('debería rechazar contraseña débil', async () => {
      const res = await request(app)
        .post('/api/auth/register')
        .send({ ...testUser, email: 'other@test.com', password: '123', confirmPassword: '123' });

      expect(res.status).toBe(422);
    });
  });

  describe('POST /api/auth/login', () => {
    it('debería hacer login correctamente', async () => {
      const res = await request(app)
        .post('/api/auth/login')
        .send({
          email: testUser.email,
          password: testUser.password,
        });

      expect(res.status).toBe(200);
      expect(res.body.data.accessToken).toBeDefined();
    });

    it('debería rechazar credenciales incorrectas', async () => {
      const res = await request(app)
        .post('/api/auth/login')
        .send({
          email: testUser.email,
          password: 'WrongPassword123!',
        });

      expect(res.status).toBe(401);
    });
  });
});
4.4 Checklist Fase 4
text

□ Crear Dockerfile para server y client
□ Crear docker-compose.yml
□ Verificar que todo arranca con docker-compose up
□ Configurar GitHub Actions CI
□ Escribir tests de integración para auth
□ Escribir tests de integración para posts
□ Escribir tests de integración para users
□ Escribir tests de componentes React (Vitest)
□ Configurar ESLint + Prettier compartido
□ Alcanzar mínimo 60% de cobertura
📊 FASE 5: Optimización y Funcionalidades Avanzadas (Semanas 9-12)
5.1 Sistema de Notificaciones en Tiempo Real
TypeScript

// apps/server/src/modules/notifications/notifications.gateway.ts
import { Server as SocketServer } from 'socket.io';
import jwt from 'jsonwebtoken';
import { env } from '../../shared/config/env';

export function setupWebSocket(io: SocketServer) {
  
  // Autenticar conexiones WebSocket
  io.use((socket, next) => {
    const token = socket.handshake.auth.token;
    
    if (!token) {
      return next(new Error('Token requerido'));
    }

    try {
      const decoded = jwt.verify(token, env.JWT_SECRET) as { userId: string };
      socket.data.userId = decoded.userId;
      next();
    } catch {
      next(new Error('Token inválido'));
    }
  });

  io.on('connection', (socket) => {
    const userId = socket.data.userId;
    
    // Unir al usuario a su room personal
    socket.join(`user:${userId}`);
    console.log(`🔌 Usuario ${userId} conectado`);

    socket.on('disconnect', () => {
      console.log(`❌ Usuario ${userId} desconectado`);
    });
  });

  return {
    // Enviar notificación a un usuario específico
    notifyUser: (userId: string, notification: {
      type: 'like' | 'comment' | 'follow' | 'mention';
      message: string;
      data?: any;
    }) => {
      io.to(`user:${userId}`).emit('notification', {
        ...notification,
        createdAt: new Date().toISOString(),
      });
    },
  };
}
5.2 Sistema de Upload con Sharp
TypeScript

// apps/server/src/shared/utils/upload.ts
import multer from 'multer';
import sharp from 'sharp';
import path from 'path';
import crypto from 'crypto';
import { AppError } from '../middlewares/errorHandler';

const ALLOWED_TYPES = ['image/jpeg', 'image/png', 'image/webp', 'image/gif'];
const MAX_SIZE = 10 * 1024 * 1024; // 10MB

const storage = multer.memoryStorage();

export const upload = multer({
  storage,
  limits: { fileSize: MAX_SIZE },
  fileFilter: (req, file, cb) => {
    if (!ALLOWED_TYPES.includes(file.mimetype)) {
      cb(new AppError('Tipo de archivo no permitido. Solo: JPEG, PNG, WebP, GIF', 400));
      return;
    }
    cb(null, true);
  },
});

export async function processImage(
  buffer: Buffer,
  options: {
    width?: number;
    height?: number;
    quality?: number;
    format?: 'webp' | 'jpeg' | 'png';
  } = {}
) {
  const {
    width = 1200,
    height,
    quality = 80,
    format = 'webp',
  } = options;

  const processed = await sharp(buffer)
    .resize(width, height, {
      fit: 'inside',
      withoutEnlargement: true,
    })
    .toFormat(format, { quality })
    .toBuffer();

  const filename = `${crypto.randomUUID()}.${format}`;

  return { buffer: processed, filename };
}

// Generar thumbnail
export async function generateThumbnail(buffer: Buffer) {
  return processImage(buffer, {
    width: 400,
    height: 400,
    quality: 60,
  });
}
5.3 Otras Mejoras de esta Fase
text

□ WebSocket para notificaciones en tiempo real
□ Sistema de upload con procesamiento de imágenes
□ Sistema de búsqueda con debounce
□ Caché con Redis (sesiones, queries frecuentes)
□ Lazy loading de imágenes
□ SEO básico (meta tags dinámicos, sitemap)
□ PWA (Service Worker, manifest.json)
□ Logging con Winston
□ Error tracking con Sentry (o similar gratuito)
□ Analytics básicos (dashboard de admin)
🗓️ TIMELINE VISUAL
text

Semana  1  ──  FASE 0: Limpieza y estructura
                │
Semana  2  ──  FASE 1: Seguridad
Semana  3  ──  FASE 1: Auth completo + middlewares
                │
Semana  4  ──  FASE 2: Backend modules
Semana  5  ──  FASE 2: API completa + Prisma
                │
Semana  6  ──  FASE 3: Frontend (Query + Zustand)
Semana  7  ──  FASE 3: UI/UX completa
                │
Semana  8  ──  FASE 4: Docker + CI/CD
Semana  9  ──  FASE 4: Testing
                │
Semana 10  ──  FASE 5: WebSockets + Upload
Semana 11  ──  FASE 5: Optimizaciones
Semana 12  ──  FASE 5: Polish + Deploy
                │
            🚀 PRODUCCIÓN
📦 Dependencias Recomendadas
Backend
JSON

{
  "dependencies": {
    "@prisma/client": "^5.x",
    "express": "^4.18",
    "bcryptjs": "^2.4",
    "jsonwebtoken": "^9.0",
    "zod": "^3.22",
    "cors": "^2.8",
    "helmet": "^7.1",
    "cookie-parser": "^1.4",
    "compression": "^1.7",
    "express-rate-limit": "^7.1",
    "multer": "^1.4",
    "sharp": "^0.33",
    "socket.io": "^4.7",
    "winston": "^3.11",
    "morgan": "^1.10"
  },
  "devDependencies": {
    "prisma": "^5.x",
    "typescript": "^5.3",
    "jest": "^29",
    "supertest": "^6.3",
    "ts-jest": "^29",
    "@types/express": "^4.17",
    "tsx": "^4.7",
    "nodemon": "^3.0"
  }
}
Frontend
JSON

{
  "dependencies": {
    "react": "^18.2",
    "react-dom": "^18.2",
    "react-router-dom": "^6.21",
    "@tanstack/react-query": "^5.17",
    "zustand": "^4.4",
    "axios": "^1.6",
    "lucide-react": "^0.303",
    "date-fns": "^3.2",
    "react-intersection-observer": "^9.8",
    "react-hot-toast": "^2.4",
    "clsx": "^2.1",
    "tailwind-merge": "^2.2"
  },
  "devDependencies": {
    "vite": "^5.0",
    "typescript": "^5.3",
    "@vitejs/plugin-react-swc": "^3.5",
    "tailwindcss": "^3.4",
    "vitest": "^1.1",
    "@testing-library/react": "^14.1",
    "autoprefixer": "^10.4",
    "postcss": "^8.4"
  }
}
✅ Métricas de Éxito por Fase
text

FASE 0: ✅ Proyecto arranca limpio sin errores
FASE 1: ✅ Auth seguro, rate limiting, validación Zod en cada endpoint
FASE 2: ✅ CRUD completo, paginación, ownership checks
FASE 3: ✅ UI responsive, infinite scroll, optimistic updates
FASE 4: ✅ Docker funcional, CI verde, >60% cobertura tests
FASE 5: ✅ Notificaciones real-time, uploads optimizados, listo para deploy
