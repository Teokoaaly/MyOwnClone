import "server-only";

const WHEREBY_API_URL = "https://api.whereby.dev/v1";

async function wherebyRequest(
  path: string,
  options: RequestInit = {}
): Promise<Response> {
  return fetch(`${WHEREBY_API_URL}${path}`, {
    ...options,
    headers: {
      Authorization: `Bearer ${process.env.WHEREBY_API_KEY}`,
      "Content-Type": "application/json",
      ...options.headers,
    },
  });
}

export async function createMeeting(params: {
  roomName?: string;
  endDate?: string;
  fields?: string[];
}) {
  const response = await wherebyRequest("/meetings", {
    method: "POST",
    body: JSON.stringify({
      isLocked: false,
      roomNamePrefix: "replica-",
      roomMode: "normal",
      startDate: new Date().toISOString(),
      endDate: params.endDate ?? new Date(Date.now() + 24 * 60 * 60 * 1000).toISOString(),
      fields: params.fields ?? ["hostRoomUrl"],
    }),
  });

  if (!response.ok) {
    throw new Error(`Whereby error: ${response.statusText}`);
  }

  return response.json();
}

export async function getMeeting(meetingId: string) {
  const response = await wherebyRequest(`/meetings/${meetingId}`);
  return response.json();
}

export async function deleteMeeting(meetingId: string) {
  const response = await wherebyRequest(`/meetings/${meetingId}`, {
    method: "DELETE",
  });
  return response.json();
}
