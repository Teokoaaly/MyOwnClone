import "server-only";

const supabaseUrl = process.env.SUPABASE_URL!;
const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY!;

async function supabaseRequest(
  path: string,
  options: RequestInit = {}
): Promise<Response> {
  const url = `${supabaseUrl}/storage/v1${path}`;
  return fetch(url, {
    ...options,
    headers: {
      Authorization: `Bearer ${serviceKey}`,
      ...options.headers,
    },
  });
}

export async function uploadFile(
  bucket: string,
  filePath: string,
  file: Buffer | Blob,
  contentType: string
) {
  const formData = new FormData();
  const blob = file instanceof Buffer ? new Blob([file as unknown as BlobPart], { type: contentType }) : file;
  formData.append("file", blob as Blob);

  return supabaseRequest(`/object/${bucket}/${filePath}`, {
    method: "POST",
    body: formData,
  });
}

export async function deleteFile(bucket: string, filePath: string) {
  return supabaseRequest(`/object/${bucket}/${filePath}`, {
    method: "DELETE",
  });
}

export function getPublicUrl(bucket: string, filePath: string) {
  return `${supabaseUrl}/storage/v1/object/public/${bucket}/${filePath}`;
}
