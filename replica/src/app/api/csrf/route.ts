import { NextResponse } from "next/server"
import crypto from "crypto"

export async function GET() {
  const token = crypto.randomBytes(32).toString("hex")
  const response = NextResponse.json({ token })
  response.cookies.set("csrf-token", token, {
    httpOnly: true,
    secure: process.env.NODE_ENV === "production",
    sameSite: "strict",
    path: "/",
    maxAge: 3600,
  })
  return response
}
