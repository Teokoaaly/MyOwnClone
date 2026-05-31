import { NextRequest, NextResponse } from "next/server";
import { db, schema } from "@/lib/db";
import { eq, and, inArray } from "drizzle-orm";
import { createMeeting } from "@/lib/video";
import { sendBookingConfirmation } from "@/lib/email";

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const cloneId = searchParams.get("cloneId");

  if (!cloneId) {
    return NextResponse.json({ error: "cloneId is required" }, { status: 400 });
  }

  const meetingTypesForClone = await db.query.meetingTypes.findMany({
    where: eq(schema.meetingTypes.cloneId, cloneId),
    columns: { id: true },
  });
  const mtIds = meetingTypesForClone.map((mt) => mt.id);

  if (mtIds.length === 0) {
    return NextResponse.json({ bookings: [] });
  }

  const bookings = await db.query.bookings.findMany({
    where: inArray(schema.bookings.meetingTypeId, mtIds),
    orderBy: (bookings, { desc }) => [desc(bookings.createdAt)],
  });

  return NextResponse.json({ bookings });
}

export async function POST(request: NextRequest) {
  try {
    let meetingTypeId: string;
    let visitorName: string;
    let visitorEmail: string;
    let date: string;
    let startTime: string;
    let time: string;

    const contentType = request.headers.get("content-type") || "";

    if (contentType.includes("application/json")) {
      const body = await request.json();
      meetingTypeId = body.meetingTypeId;
      visitorName = body.visitorName;
      visitorEmail = body.visitorEmail;
      date = body.date;
      time = body.time || body.startTime || "";
    } else {
      const formData = await request.formData();
      meetingTypeId = formData.get("meetingTypeId") as string;
      visitorName = formData.get("visitorName") as string;
      visitorEmail = formData.get("visitorEmail") as string;
      date = formData.get("date") as string;
      time = (formData.get("startTime") || formData.get("time")) as string;
    }

    if (!meetingTypeId || !visitorName || !visitorEmail || !date) {
      return NextResponse.json(
        { error: "meetingTypeId, visitorName, visitorEmail, and date are required" },
        { status: 400 },
      );
    }

    const conflict = await db.query.bookings.findFirst({
      where: and(
        eq(schema.bookings.meetingTypeId, meetingTypeId),
        eq(schema.bookings.date, date),
        eq(schema.bookings.time, time),
      ),
    });

    if (conflict && conflict.status !== "cancelled") {
      return NextResponse.json({ error: "Time slot already booked" }, { status: 409 });
    }

    const booking = await db
      .insert(schema.bookings)
      .values({
        id: crypto.randomUUID(),
        meetingTypeId,
        visitorName,
        visitorEmail,
        date,
        time,
        notes: null,
        status: "confirmed",
      })
      .returning();

    const mt = await db.query.meetingTypes.findFirst({
      where: eq(schema.meetingTypes.id, meetingTypeId),
    });

    try {
      if (mt) {
        const meeting = await createMeeting({ roomName: `booking-${booking[0].id}` });
        const meetingUrl = meeting.roomUrl || meeting.hostRoomUrl || "";
        if (meetingUrl) {
          await db.update(schema.bookings)
            .set({ meetingUrl })
            .where(eq(schema.bookings.id, booking[0].id));
          booking[0].meetingUrl = meetingUrl;
        }
      }
    } catch (e) {
      console.error("Failed to create meeting room:", e);
    }

    try {
      if (mt) {
        await sendBookingConfirmation({
          to: visitorEmail,
          visitorName,
          cloneName: "Réplica",
          date,
          time,
          meetingUrl: booking[0].meetingUrl || undefined,
        });
      }
    } catch (e) {
      console.error("Failed to send booking confirmation:", e);
    }

    return NextResponse.redirect(
      new URL(`/booking-confirmed?ref=${booking[0].id}`, request.url),
    );
  } catch (error) {
    console.error("Booking error:", error);
    return NextResponse.json({ error: "Error creating booking" }, { status: 500 });
  }
}
