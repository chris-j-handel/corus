#!/usr/bin/env python3
"""Prime Numbers, A Natural Explaining of Sequential Prime Living: its sections executed.

Usage:  python3 -I incoming/v407primes/instruments/prime_numbers_report_executed.py .

The report's executings are the lines of the story's instrument, `the_prime_numbers_story_executed.py`,
and v406Reiman's cell by nand alone, `the_resolver_with_nand_alone.py`, both executed here as they are.
A section's lines are listed beside it, and all must end is. The cicadas of 5.5 are executed here.
Whole numbers alone. Nothing is proved: a line says is of the numbers it stepped.

It writes its lines to standard output. It writes no file, reaches no network and decides nothing.
"""
import re
import subprocess
import sys
from math import lcm
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
HERE = Path(__file__).resolve().parent

SECTIONS = {
    "1.4 A prime, no smaller spiral at its seam": [5],
    "2.1 A staircase, one up at a prime and across at a crossed number": [5],
    "2.2 A turn, spirals side by side coming again together": [6, 14, 16],
    "2.3 A turn's staircase, its own inversion scale with scale": [7, 8, 9],
    "2.4 Four faces of 30, 0 to 120": [10, 61, 62, 82, 83, 85],
    "2.5 Past 120, a staircase under its geodesic": [84, 87],
    "3.2 A spiral's coming again, by its opening's own span": [36, 37],
    "3.3 A prime known by its own openings": [96, 97],
    "3.4 Doubling and φ as couplings": [21, 44, 45, 47],
    "3.5 A torus parting into none": [48],
    "4.1 Alternating parities, a staircase whole": [93, 94],
    "4.2 A quarter turn, five's doubling and ten's 3, 9, 7, 1": [39, 89],
    "4.3 Two pieces locking, flips and quarter turns": [11, 40, 41, 42, 43, 63, 95],
    "4.4 A fold at 24, me-parities birthing": [54, 55],
    "4.5 120, the atom's prior, now and next multiplied": [38, 98],
    "4.6 37, other-than-other-than-other": [73, 74, 75, 76, 77, 80],
    "5.1 A smooth curve beside the step curve": [25, 26, 94],
    "5.2 Gaps, pairs and rows": [16, 17, 18, 19, 20, 28],
    "5.3 A prime's closings": [21, 22, 23, 24, 46],
    "5.4 Keys, and primes in a plane": [88, 89, 90],
    "5.5 Rows of a number spiral, and cicadas": [27],
    "6.1 Prime scales, atom to biosphere": [53],
    "6.2 Scales podal about 30 and about the fold": [53, 56],
    "6.3 A living span, 23 to 19, and its living surface": [55],
    "6.5 37, one living self, and c, one all-parity": [73, 74, 76, 77],
    "7.2 Shown not possibly existing": [10, 11, 61, 87, 90],
    "7.3 One asking open": [46],
}


def executed(script):
    out = subprocess.run([sys.executable, "-I", str(script), str(ROOT)], capture_output=True, text=True, timeout=600)
    return out.returncode, out.stdout


def main():
    all_is = True
    code, story = executed(HERE / "the_prime_numbers_story_executed.py")
    lines = {}
    for row in story.splitlines():
        m = re.match(r"\s*(\d+)\. .*: (is|IS NOT)$", row)
        if m:
            lines[int(m.group(1))] = m.group(2) == "is"
    print(f"the story's instrument: {len(lines)} lines, ending {story.strip().splitlines()[-1]!r}")
    all_is = all_is and code == 0
    for name, wanted in SECTIONS.items():
        ok = all(lines.get(n) for n in wanted)
        all_is = all_is and ok
        print(f"  {name}: lines {wanted}: {'is' if ok else 'IS NOT'}")

    code, cell = executed(ROOT / "incoming" / "v406Reiman" / "instruments" / "the_resolver_with_nand_alone.py")
    ok = code == 0 and cell.strip().splitlines()[-1].startswith("All is")
    all_is = all_is and ok
    print(f"  3.1 A cell, one is-or-is-not of a co-parity: the cell by nand alone, the living code case with case: {'is' if ok else 'IS NOT'}")

    together = {c: sum(2520 // lcm(c, k) for k in range(2, 10)) for c in (12, 13, 14, 15, 16, 17, 18)}
    ok = lcm(13, 17) == 221 and together[13] == 350 and together[17] == 268
    ok = ok and all(together[c] > together[13] > together[17] for c in (12, 14, 15, 16, 18))
    all_is = all_is and ok
    print(f"  5.5 cicadas: 13 and 17 together with 221 years; in 2,520 years with cycles of 2 to 9, {together}: {'is' if ok else 'IS NOT'}")

    print("All is, of the numbers stepped." if all_is else "Not all is.")
    return 0 if all_is else 1


if __name__ == "__main__":
    sys.exit(main())
