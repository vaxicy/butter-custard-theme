/**
 * Butter Custard Theme - syntax preview
 *
 * Light  canvas #FEFED7  ink #353521  accent #C2AD29
 * Dark   canvas #3C320B  ink #FEFEBE  accent #DBC00F
 */

import { readFileSync } from "node:fs";

export type Sweetness = "plain" | "buttery" | "caramel";

export interface Swatch {
  readonly name: string;
  readonly hex: string;
  readonly sweetness: Sweetness;
}

export const PALETTE: readonly Swatch[] = [
  { name: "custard", hex: "#FDE863", sweetness: "buttery" },
  { name: "caramel", hex: "#CB7E34", sweetness: "caramel" },
  { name: "cream", hex: "#FFFFE5", sweetness: "plain" },
  { name: "cocoa", hex: "#3C320B", sweetness: "caramel" },
];

const CHANNEL = /^#?([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i;

/** Relative luminance, so we can sort the palette by brightness. */
export function luminance(hex: string): number {
  const match = CHANNEL.exec(hex);
  if (!match) {
    throw new TypeError(`Not a hex colour: ${hex}`);
  }

  const [r, g, b] = match.slice(1).map((part) => parseInt(part, 16) / 255);
  const linear = (c: number) => (c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4);

  return 0.2126 * linear(r) + 0.7152 * linear(g) + 0.0722 * linear(b);
}

export function sortByBrightness(swatches: readonly Swatch[] = PALETTE): Swatch[] {
  return [...swatches].sort((a, b) => luminance(b.hex) - luminance(a.hex));
}

export async function loadTheme(path: string): Promise<Record<string, string>> {
  const raw = readFileSync(path, "utf8");
  const { colors } = JSON.parse(raw) as { colors: Record<string, string> };

  for (const [key, value] of Object.entries(colors)) {
    if (key.startsWith("editor.")) {
      console.log(`  ${key.padEnd(34)} ${value}`);
    }
  }

  return colors;
}

if (process.argv[1] && process.argv[2] !== "--no-run") {
  await loadTheme(process.argv[1]);
  console.log(`\n${sortByBrightness().length} swatches ready.`);
}
