"""Session v383Op: the spiral of selves, its law and its periods, at Exhibit ONE's resolver.

Runs from the repository root: python3 incoming/v383Op/ring_law.py
Reads the newest Exhibit ONE at the root and executes its python block (through 17, the society's step).

Arrangement, said with its start and its joins: n selves, one sharing each, each self releasing
along (9) to the next, the last to the first; each self carrying a parity at the first momentary;
nothing offered at the first momentary and nothing offered from beyond. c[j](t) is self j's
carrying as momentary t opens, t = 1 the first.

Checked here, each against the resolver itself:
  1. THE LAW. c[j](t+2) = -c[j-1](t), for each self and each momentary, at EVERY opening
     (all 2^n openings, n = 1..10; 200 random openings at n = 11..40).
  2. NO TWO STAYS. No self shares 0 at two momentaries in sequence.
  3. THE PERIOD. The carryings come again first at 2k momentaries, k the least number with
     (-1)^k * (the opening carried k selves on) = the opening. For n odd that is 4r, r the least
     number of selves the opening can be carried on and be itself again (r divides n).
     Checked at every opening, n = 1..10.
  4. Exhibit ONE's table rows: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17, 59 at the alternating opening,
     the momentaries to the releasings again, by the rule and measured at the resolver.

Already carried: the Co-Chaining Logic Registry says the law at its steps 233 and 609, no two
stays at 611 and the period at 646 to 648. This script is a run of them at the resolver.
The period is of the sharings and carryings as a sequence, compared from the second momentary
on: the bare carryings can equal the opening's at an earlier, even momentary and then part.
"""
import glob, itertools, random, re

exhibit_one = sorted(glob.glob('Exhibit_ONE_Natural_Resolver_v*.md'))[-1]
ns = {}
exec(re.search(r"```python\n(.*?)```", open(exhibit_one).read(), re.S).group(1), ns)
_17 = ns['_17_co_bi_tri_offering']


def run(opening, steps):
    """Returns carry[t][j] for t = 0..steps (t = 0 is the first momentary's opening) and shared[t][j]."""
    n = len(opening)
    society = {j: ([('s', opening[j])], []) for j in range(n)}
    along = {(j, 9): (j + 1) % n for j in range(n)}
    carry, shared = [tuple(opening)], []
    for _ in range(steps):
        out = _17(society, along)
        # what each self shared this momentary is what arrives at the next self's offerings
        shared.append(tuple(out[(j + 1) % n][1][0][1] for j in range(n)))
        society = {j: (out[j][0], out[j][1]) for j in range(n)}
        carry.append(tuple(dict(society[j][0])['s'] for j in range(n)))
    return carry, shared


def predicted_period(opening):
    n = len(opening)
    k = 1
    while True:
        moved = tuple(((-1) ** k) * opening[(j - k) % n] for j in range(n))
        if moved == tuple(opening):
            return 2 * k
        k += 1


def measured_period(opening):
    n = len(opening)
    carry, shared = run(opening, 8 * n + 8)
    # the whole form at a momentary: carryings and what is arriving
    forms = [(carry[t + 1], shared[t]) for t in range(len(shared))]
    for T in range(1, 4 * n + 1):
        if all(forms[t] == forms[t + T] for t in range(len(forms) - T)):
            return T
    return None


def check_law(opening, steps):
    n = len(opening)
    carry, shared = run(opening, steps)
    for t in range(len(carry) - 2):
        for j in range(n):
            assert carry[t + 2][j] == -carry[t][(j - 1) % n], (opening, t, j)
    for t in range(len(shared) - 1):
        for j in range(n):
            assert not (shared[t][j] == 0 and shared[t + 1][j] == 0) or n == 0, (opening, t, j)


print('Exhibit ONE read at', exhibit_one)
openings = 0
periods_seen = {}
for n in range(1, 11):
    for opening in itertools.product((1, -1), repeat=n):
        check_law(opening, 4 * n + 6)
        p, m = predicted_period(opening), measured_period(opening)
        assert p == m, (opening, p, m)
        periods_seen.setdefault(n, set()).add(m)
        openings += 1
print('the law, no two stays, and the period: %d of %d openings, n = 1 to 10' % (openings, openings))
random.seed(383)
more = 0
for n in range(11, 41):
    for _ in range(200):
        check_law(tuple(random.choice((1, -1)) for _ in range(n)), 2 * n + 6)
        more += 1
print('the law and no two stays: %d of %d random openings, n = 11 to 40' % (more, more))
print('\nperiods at every opening, by number of selves:')
for n in sorted(periods_seen):
    print('  %2d selves: %s' % (n, sorted(periods_seen[n])))

print("\nExhibit ONE's opening (self 1 carries -, alternating along):")
for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17, 59):
    opening = tuple(-1 if j % 2 == 0 else 1 for j in range(n))
    print('  %2d selves: %3d momentaries' % (n, predicted_period(opening)),
          '(measured at the resolver: %s)' % measured_period(opening))
