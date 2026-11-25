"""v407nanding · the walk of the primes with its one cell two of the twelve lines' mes, beside nand of two is-or-is-nots.

Usage, from the repository's root, with v406other2's walk in its folder:
  python3 -I incoming/v407nanding/instruments/the_walk_of_the_primes_by_the_twelve_lines_mes_check.py . [horizon]

A partner's asking of 24 November, a part apiece: v407nanding's, the part of a test, the walk with one cell, beside the
fifteen lines. v406other2's walk is opened from its file and written in no second place; its nand is said again as two
mes of a partner's twelve lines front to back, opened from this session's file. All or none.
"""
import contextlib
import io
import re
import sys
import time
from pathlib import Path

root = Path(sys.argv[1])
H = int(sys.argv[2]) if len(sys.argv) > 2 else 13
cells = {}
exec(re.search(r"CODE = '''(.*?)'''", (root / "incoming/v407nanding/instruments/the_now_and_same_existing_me_parity_check.py").read_text(encoding="utf-8"), re.S).group(1), cells)
cell, MINUS = cells["now_and_same_existing_me_parity"], (False, True)


def two_mes(a, b):
    front = cell(MINUS, [(False, bool(b))])[0][0]
    return int(cell(MINUS, [(front, bool(a))])[0][0])


walk = (root / "incoming/v406other2/instruments/the_walk_of_the_primes_with_nand_alone_executed.py").read_text(encoding="utf-8")
table_nand = "def nand(a, b):\n    calls[0] += 1\n    return 1 - (a & b)"
results = []


def say(sentence, ok):
    results.append(bool(ok))
    print(f"{sentence} ({'is' if ok else 'is not'})")


def walked_with(nand_line):
    ns = {"TWO_MES": two_mes, "__name__": "the_walk"}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(walk.replace("HORIZON = 61", f"HORIZON = {H}").replace(table_nand, nand_line), ns)
    return ns["walked"], ns["calls"][0]


say("W1. The walk's one cell is nand of two is-or-is-nots, at one place in its lines", walk.count(table_nand) == 1)
say("W2. Two mes of the twelve lines front to back are nand of two is-or-is-nots, all four cases",
    all(two_mes(a, b) == 1 - (a & b) for a in (0, 1) for b in (0, 1)))
started = time.time()
by_table, n_table = walked_with(table_nand)
by_mes, n_mes = walked_with("def nand(a, b):\n    calls[0] += 1\n    return TWO_MES(a, b)")
plain = [n for n in range(2, H + 1) if all(n % d for d in range(2, n))]
say(f"W3. With its one cell two mes of the twelve lines, the walk from 2 finds the primes to {H}, the same as with the table's nand, "
    f"its one cell called {n_mes:,} times", by_mes == by_table == plain and n_mes == n_table)
print(f"\n{'All is.' if all(results) else 'Not all is.'}  ({time.time() - started:.0f} s)")
