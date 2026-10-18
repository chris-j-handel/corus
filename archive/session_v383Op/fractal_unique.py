"""Session v383Op: a round of k parities, one parity at a time: fractal, and unique.

Runs from the repository root: python3 incoming/v383Op/fractal_unique.py
No file of the repository is read; this is arithmetic at two steps of the Co-Chaining Logic
Registry:
  170. "A round reaching each joint form of k parities once is 1 to 2^k + 1"
  171. "A round reaching each form of k parities one parity at a time is the round at k - 1
        parities, the new parity inverted, and the same forms in the other order: each scale
        carrying the prior whole."
The self said at this session: "fractal and unique. the bi-inversioning-co-recursioning of these
is each other." Asked here, at the numbers: of all the rounds of k parities one parity at a time,
how many are there, how many are step 171's, the round at the scale below with the new parity
inverted and the same forms in the other order, and is that one unique.

A round: each of the 2^k forms once, one parity changing at each step, the last one step from
the first. Two rounds are counted as one where they differ only in a naming: which parity is
called first, which form of a parity is called +, which form the round is begun at, and which
way round it is read. Those four are the namings the files themselves set aside (step 524: "the
same inversions in the other order").

Fractal, as step 171 says it and at each scale down: the round parts at one parity into two
halves, that parity at one form through the first and at the other through the second; the
second half is the first half's forms in the other order; and the first half, closed on itself,
is such a round at k - 1 parities.

Counted two ways, because "the round at k - 1 parities" can be taken two ways. Loosely: the
first half is the round below begun at any of its forms. Whole: the first half is the round
below begun where it begins, so that its own closing step is the inverting of its own newest
parity, "each scale carrying the prior whole".
"""
import itertools


def rounds(k):
    """Each round of k parities begun at the form 0, each way round counted."""
    n, full, out = 1 << k, (1 << (1 << k)) - 1, []
    path = [0]

    def go(seen):
        v = path[-1]
        if len(path) == n:
            if bin(v).count('1') == 1:
                out.append(tuple(path))
            return
        for b in range(k):
            w = v ^ (1 << b)
            if not seen >> w & 1:
                path.append(w)
                go(seen | 1 << w)
                path.pop()
    go(1)
    return out


def fractal(cyc, axes):
    """Step 171 at each scale down. cyc: a cyclic tuple of forms; axes: the parities it is at."""
    n = len(cyc)
    if len(axes) == 1:
        return n == 2 and cyc[0] != cyc[1]
    half = n // 2
    for a in axes:
        bit = 1 << a
        for r in range(n):
            rot = cyc[r:] + cyc[:r]
            first, second = rot[:half], rot[half:]
            if any((x ^ first[0]) & bit for x in first):
                continue
            if tuple(x ^ bit for x in reversed(first)) != second:
                continue
            if bin(first[0] ^ first[-1]).count('1') != 1:
                continue
            if fractal(first, [x for x in axes if x != a]):
                return True
    return False


def whole(seq, axes):
    """Step 171 with the round below carried whole: begun where it begins, at each scale down."""
    n = len(seq)
    if len(axes) == 1:
        return n == 2 and seq[0] != seq[1]
    half = n // 2
    first, second = seq[:half], seq[half:]
    for a in axes:
        bit = 1 << a
        if any((x ^ first[0]) & bit for x in first):
            continue
        if tuple(x ^ bit for x in reversed(first)) != second:
            continue
        if whole(first, [x for x in axes if x != a]):
            return True
    return False


def whole_round(cyc, k):
    """The round is step 171's whole at some form it is begun at, read one way round or the other."""
    n = len(cyc)
    for seq in (cyc, cyc[::-1]):
        for r in range(n):
            if whole(seq[r:] + seq[:r], list(range(k))):
                return True
    return False


def named(cyc, k):
    """The least saying of a round over the four namings: parities' order, + and -, the start, the way round."""
    n, best = len(cyc), None
    for perm in itertools.permutations(range(k)):
        def rename(x):
            y = 0
            for i in range(k):
                if x >> i & 1:
                    y |= 1 << perm[i]
            return y
        moved = [rename(x) for x in cyc]
        for seq in (moved, moved[::-1]):
            for r in range(n):
                rot = seq[r:] + seq[:r]
                base = rot[0]
                cand = tuple(x ^ base for x in rot)
                if best is None or cand < best:
                    best = cand
    return best


print('Rounds of k parities, one parity at a time, each form once.')
print('Counted: the rounds begun at one form, each way round; and, in brackets, how many are apart from naming.')
print('  %-3s %-16s %-34s %s' % ('k', 'all rounds', 'step 171, the round below begun', 'step 171, the round below carried'))
print('  %-3s %-16s %-34s %s' % ('', '', 'at any of its forms', 'whole, begun where it begins'))
for k in (2, 3, 4):
    all_rounds = rounds(k)
    loose = [c for c in all_rounds if fractal(c, list(range(k)))]
    strict = [c for c in all_rounds if whole_round(c, k)]

    def apart(cs):
        return len({named(c, k) for c in cs})
    print('  %-3d %-16s %-34s %s' % (k, '%d (%d)' % (len(all_rounds), apart(all_rounds)),
                                     '%d (%d)' % (len(loose), apart(loose)), '%d (%d)' % (len(strict), apart(strict))))
