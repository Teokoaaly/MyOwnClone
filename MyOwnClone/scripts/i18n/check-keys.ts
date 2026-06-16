#!/usr/bin/env tsx
/**
 * i18n key parity check.
 *
 * Compares en.json and es.json recursively. Fails (exit 1) if:
 *   - a key exists in en.json but is missing in es.json
 *   - a key exists in es.json but is missing in en.json
 *   - placeholders {name} in en.json are not matched in es.json (or vice versa)
 *
 * Usage:
 *   npx tsx scripts/i18n/check-keys.ts
 */
import { readFileSync } from "node:fs";
import { join } from "node:path";

const ROOT = process.cwd();
const EN = join(ROOT, "src/i18n/en.json");
const ES = join(ROOT, "src/i18n/es.json");

type Json = Record<string, unknown>;

function load(p: string): Json {
  return JSON.parse(readFileSync(p, "utf8")) as Json;
}

function walk(
  node: Json,
  prefix: string,
  out: Map<string, { value: string; path: string }>,
): void {
  for (const [k, v] of Object.entries(node)) {
    const path = prefix ? `${prefix}.${k}` : k;
    if (v && typeof v === "object" && !Array.isArray(v)) {
      walk(v as Json, path, out);
    } else if (typeof v === "string") {
      out.set(path, { value: v, path });
    }
  }
}

function placeholders(s: string): Set<string> {
  const out = new Set<string>();
  const re = /\{([a-zA-Z_][a-zA-Z0-9_]*)/g;
  let m: RegExpExecArray | null;
  while ((m = re.exec(s)) !== null) {
    out.add(m[1]);
  }
  return out;
}

function main() {
  const en = load(EN);
  const es = load(ES);

  const enMap = new Map<string, { value: string; path: string }>();
  const esMap = new Map<string, { value: string; path: string }>();
  walk(en, "", enMap);
  walk(es, "", esMap);

  const enKeys = new Set(enMap.keys());
  const esKeys = new Set(esMap.keys());

  const missingInEs: string[] = [];
  const missingInEn: string[] = [];
  const placeholderMismatch: string[] = [];

  for (const k of enKeys) {
    if (!esKeys.has(k)) {
      missingInEs.push(k);
      continue;
    }
    const a = placeholders(enMap.get(k)!.value);
    const b = placeholders(esMap.get(k)!.value);
    if (a.size !== b.size || ![...a].every((x) => b.has(x))) {
      placeholderMismatch.push(
        `${k}: en={${[...a].sort().join(",")}} es={${[...b].sort().join(",")}}`,
      );
    }
  }
  for (const k of esKeys) {
    if (!enKeys.has(k)) missingInEn.push(k);
  }

  let ok = true;

  if (missingInEs.length > 0) {
    ok = false;
    process.stderr.write(`\nMissing in es.json (${missingInEs.length}):\n`);
    for (const k of missingInEs) process.stderr.write(`  - ${k}\n`);
  }
  if (missingInEn.length > 0) {
    ok = false;
    process.stderr.write(`\nMissing in en.json (${missingInEn.length}):\n`);
    for (const k of missingInEn) process.stderr.write(`  - ${k}\n`);
  }
  if (placeholderMismatch.length > 0) {
    ok = false;
    process.stderr.write(`\nPlaceholder mismatch (${placeholderMismatch.length}):\n`);
    for (const k of placeholderMismatch) process.stderr.write(`  - ${k}\n`);
  }

  if (ok) {
    process.stdout.write(
      `OK i18n key parity - ${enKeys.size} keys matched between en.json and es.json\n`,
    );
    process.exit(0);
  } else {
    process.stderr.write(`\nFAILED i18n key parity.\n`);
    process.exit(1);
  }
}

main();
