# The stem's whole beside the stem's opening: the stem's longest crossed run, and longest stretch with no uncrossed pair 2 apart,
# beside the universe's spans and the universe's length. All of a seam gone through: proved, all, in the seam it names.
import sys, numpy as np
openers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
top = int(sys.argv[1]) if len(sys.argv) > 1 else 23
seam = 1
print("opener | seam | uncrossed | longest crossed run | span, me again to next me again | carried | universe | length | carried | longest stretch with no pair 2 apart | births 2 apart carried")
for k, p in enumerate(openers):
    if p > top: break
    seam *= p
    q = openers[k + 1]
    s = np.ones(seam + 3, dtype=np.uint8)          # the numbers 0 to seam + 2
    s[0] = 0
    for r in openers[:k + 1]: s[::r] = 0
    pos = np.flatnonzero(s[:seam + 2])              # uncrossed places 1 to seam + 1
    gaps = np.diff(pos)
    run = int(gaps.max()) - 1                        # the longest run of crossed numbers
    where = int(pos[int(gaps.argmax())]) + 1
    starts = pos[:-1][gaps == 2]                     # the lower place of an uncrossed pair 2 apart
    if len(starts) >= 1:
        sg = np.diff(np.concatenate([starts, [starts[0] + seam]]))
        nopair = int(sg.max()) + 1                   # the longest stretch with no pair whole in the stretch
    else:
        nopair = None
    span = 2 * p                                     # the numbers between the opener's me again and the next number's me again
    L = q * q - p * p                                # the universe's length
    c1 = span > run
    c2 = L > run
    c3 = (nopair is not None) and (L > nopair)
    print(f"{p} | {seam} | {len(pos) - 1} | {run} (opening at {where}) | {span} | {c1} | {p*p} to {q*q-1} | {L} | {c2} | {nopair} | {c3}")
    del s, pos, gaps
