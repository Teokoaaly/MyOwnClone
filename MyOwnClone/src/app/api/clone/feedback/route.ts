import { NextRequest, NextResponse } from "next/server";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:5001";

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { clone_id, message_id, rating, comment } = body;

    if (!clone_id || !rating) {
      return NextResponse.json(
        { error: "clone_id and rating are required" },
        { status: 400 }
      );
    }

    if (!["up", "down"].includes(rating)) {
      return NextResponse.json(
        { error: "rating must be 'up' or 'down'" },
        { status: 400 }
      );
    }

    // Get auth token from cookies
    const token = request.cookies.get("auth-token")?.value;

    const response = await fetch(
      `${API_URL}/console/api/myownclone/feedback`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...(token && { Authorization: `Bearer ${token}` }),
        },
        body: JSON.stringify({ clone_id, message_id, rating, comment }),
      }
    );

    if (!response.ok) {
      const error = await response.text();
      return NextResponse.json(
        { error: `Backend error: ${error}` },
        { status: response.status }
      );
    }

    const data = await response.json();
    return NextResponse.json(data, { status: 200 });
  } catch (error) {
    console.error("Feedback error:", error);
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 }
    );
  }
}

export async function GET(request: NextRequest) {
  try {
    const { searchParams } = new URL(request.url);
    const clone_id = searchParams.get("clone_id");

    if (!clone_id) {
      return NextResponse.json(
        { error: "clone_id is required" },
        { status: 400 }
      );
    }

    const token = request.cookies.get("auth-token")?.value;

    const response = await fetch(
      `${API_URL}/console/api/myownclone/feedback/stats?clone_id=${clone_id}`,
      {
        method: "GET",
        headers: {
          ...(token && { Authorization: `Bearer ${token}` }),
        },
      }
    );

    if (!response.ok) {
      const error = await response.text();
      return NextResponse.json(
        { error: `Backend error: ${error}` },
        { status: response.status }
      );
    }

    const data = await response.json();
    return NextResponse.json(data, { status: 200 });
  } catch (error) {
    console.error("Feedback stats error:", error);
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 }
    );
  }
}