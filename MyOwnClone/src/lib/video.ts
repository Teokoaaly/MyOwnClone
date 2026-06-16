import "server-only";

const WHEREBY_API_URL = "https://api.whereby.dev/v1";

async function wherebyRequest(
  path: string,
  options: RequestInit = {},
  signal?: AbortSignal
): Promise<Response> {
  return fetch(`${WHEREBY_API_URL}${path}`, {
    ...options,
    headers: {
      Authorization: `Bearer ${process.env.WHEREBY_API_KEY}`,
      "Content-Type": "application/json",
      ...options.headers,
    },
    signal,
  });
}

export async function createMeeting(params: {
  roomName?: string;
  endDate?: string;
***REMOVED***elds?: string[];
}, signal?: AbortSignal) {
  const response = await wherebyRequest("/meetings", {
    method: "POST",
    body: JSON.stringify({
      isLocked: false,
      roomNamePrefix: "replica-",
      roomMode: "normal",
      startDate: new Date().toISOString(),
      endDate: params.endDate ?? new Date(Date.now() + 24 * 60 * 60 * 1000).toISOString(),
    ***REMOVED***elds: params.fields ?? ["hostRoomUrl"],
    }),
  }, signal);

  if (!response.ok) {
    throw new Error(`Whereby error: ${response.statusText}`);
  }

  return response.json();
}

export async function getMeeting(meetingId: string, signal?: AbortSignal) {
  const response = await wherebyRequest(`/meetings/${meetingId}`, {}, signal);
  return response.json();
}

export async function deleteMeeting(meetingId: string, signal?: AbortSignal) {
  const response = await wherebyRequest(`/meetings/${meetingId}`, {
    method: "DELETE",
  }, signal);
  return response.json();
}
