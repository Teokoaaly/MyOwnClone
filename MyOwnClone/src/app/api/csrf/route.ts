import { NextResponse } from "next/server"
import crypto from "crypto"

export async function GET() {
  const token = crypto.randomBytes(32).toString("hex")
  const response = NextResponse.json({ token })
  // httpOnly: false - JavaScript must be able to read this token to send as header
  // This is required for Synchronizer Token CSRF protection pattern
  response.cookies.set("csrf-token", token, {
    httpOnly: false, // Must be readable by JS for Synchronizer Token pattern
    secure: process.env.NODE_ENV === "production",
    sameSite: "strict",
    path: "/",
    maxAge: 3600,
  })
  return response
}
