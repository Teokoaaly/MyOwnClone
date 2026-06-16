#!/usr/bin/env tsx
/**
 * i18n audit script.
 *
 * Walks every .tsx file under src/ and looks for hardcoded user-facing
 * strings inside JSX text. A string is "hardcoded" if it lives in JSX
 * text (`>...<`) and is NOT a known safe token (URL, css class, etc).
 *
 * Output: CSV to stdout. Exit 1 if any hardcoded strings remain.
 *
 * Usage:
 *   npx tsx scripts/i18n/audit.ts
 */
import { readFileSync, readdirSync, statSync } from "node:fs";
import { join, relative, sep } from "node:path";

const ROOT = process.cwd();
const SRC = join(ROOT, "src");

const WORD_HINT = /[A-Za-zÁÉÍÓÚáéíóúÑñ]{3,}/;

const SKIP_VALUE = [
  /^https?:\/\//i,
  /^\/[a-z0-9_/.-]*$/i,
  /^#[0-9a-f]{3,8}$/i,
  /^rgb\(/i,
  /^rgba\(/i,
  /^hsl\(/i,
  /^var\(/i,
  /^\d+(\.\d+)?(px|rem|em|%|vh|vw|s|ms)?$/i,
  /^\{.*\}$/i,
  /^\s*$/,
];

const JSX_TEXT = />([^<>{}]+)</g;

function isHardcodedJsxText(text: string): boolean {
  const cleaned = text.replace(/\s+/g, " ").trim();
  if (cleaned.length < 2) return false;
  if (!WORD_HINT.test(cleaned)) return false;
  if (/^[^A-Za-zÁÉÍÓÚáéíóúÑñ]+$/.test(cleaned)) return false;
  return true;
}

function walk(dir: string, out: string[] = []): string[] {
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    const st = statSync(full);
    if (st.isDirectory()) {
      if (entry === "node_modules" || entry.startsWith(".")) continue;
      walk(full, out);
    } else if (st.isFile() && /\.(tsx|jsx)$/.test(entry)) {
      out.push(full);
    }
  }
  return out;
}

function auditFile(path: string): { hardcoded: number; total: number; samples: string[] } {
  const src = readFileSync(path, "utf8");
  let hardcoded = 0;
  let total = 0;
  const samples: string[] = [];

  const cleaned = src
    .replace(/\/\*[\s\S]*?\*\//g, " ")
    .replace(/^\s*\/\/.*$/gm, " ");

  for (const m of cleaned.matchAll(JSX_TEXT)) {
    const t = m[1];
    if (!isHardcodedJsxText(t)) continue;
    total++;
    hardcoded++;
    if (samples.length < 5) samples.push(t.trim());
  }

  return { hardcoded, total, samples };
}

function main() {
  const files = walk(SRC);
  const rows: { path: string; hardcoded: number; total: number; samples: string[] }[] = [];

  for (const f of files) {
    const { hardcoded, total, samples } = auditFile(f);
    if (hardcoded > 0) {
      rows.push({ path: relative(ROOT, f).split(sep).join("/"), hardcoded, total, samples });
    }
  }

  process.stdout.write("file,hardcoded,total\n");
  rows.sort((a, b) => b.hardcoded - a.hardcoded);
  for (const r of rows) {
    process.stdout.write(`${r.path},${r.hardcoded},${r.total}\n`);
  }
  process.stdout.write(`\n# total files with hardcoded strings: ${rows.length}\n`);
  process.stdout.write(`# total hardcoded occurrences: ${rows.reduce((s, r) => s + r.hardcoded, 0)}\n`);

  if (rows.length > 0) {
    process.stderr.write("\nFirst few samples per file (max 5):\n");
    for (const r of rows.slice(0, 10)) {
      process.stderr.write(`  ${r.path}: ${r.samples.map((s) => JSON.stringify(s)).join(", ")}\n`);
    }
  }

  if (rows.length > 0) process.exit(1);
}

main();
