/**
 * Resolves the active clone ID on mount and stores it in a cookie.
 * This is used by the middleware to proxy API calls to the correct clone.
 */
"use client";

import { useEffect } from "react";
import { resolveActiveCloneId } from "@/lib/clone-resolver";

export function CloneIdResolver() {
  useEffect(() => {
    resolveActiveCloneId();
  }, []);

  return null;
}
