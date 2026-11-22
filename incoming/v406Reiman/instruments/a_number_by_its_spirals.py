"""A number by its spirals: the resolver's 0 placed on a number, adding along and multiplying across.

A partner's saying is explored here by executing, and nothing is proved.

Part 1 is Exhibit ONE Natural Resolver's code as it is in its living file.
Odd prime spirals of selves go side by side in one same-existing-society, four
moments a number, as Exhibit THREE Natural Numbers 7.2 has sixteen of them. A
number is crossed once an open spiral's priors are again as at its opening. A
number no open spiral crosses is uncrossed, and to 59 a spiral of that number
of selves opens at it. The spiral of two is executed apart, at its own pace.

Part 2 goes through what part 1 found. Parts 3 and 4 are by division, with no
resolver in them, and say so.

    python3 -I incoming/v406Reiman/instruments/a_number_by_its_spirals.py . [--to 3720]
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from resolver_as_it_is import S, exhibit_spiral_priors, resolver


def by_division(n):
    if n < 2:
        return False
    for q in range(2, math.isqrt(n) + 1):
        if n % q == 0:
            return False
    return True


def witness(n):
    """A field's test of one number, apart from the spirals: Miller and Rabin's, certain to 3.3 * 10^24."""
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def priors_of(society, q):
    return tuple(dict(society[(q, i)][0]).get(S, 0) for i in range(q))


def the_surface(step, to, open_to=59):
    society, couplings, opened, uncrossed, resolvings = {}, {}, {}, [], 0
    two = {i: ([(S, p)], []) for i, p in exhibit_spiral_priors(2).items()}
    two_couplings = {(0, 9): 1, (1, 9): 0}
    two_opening = tuple(dict(two[i][0])[S] for i in range(2))
    two_open = False
    for k in range(2, to + 1):
        if society:
            for _ in range(4):
                society = step(society, couplings)
                resolvings += len(society)
        if two_open:
            two = step(two, two_couplings)
            resolvings += 2
        crossed = [q for q, was in opened.items() if priors_of(society, q) == was]
        if two_open and tuple(dict(two[i][0])[S] for i in range(2)) == two_opening:
            crossed.append(2)
        if crossed:
            continue
        uncrossed.append(k)
        if k == 2:
            two_open = True
        elif k <= open_to:
            start = exhibit_spiral_priors(k)
            for i in range(k):
                society[(k, i)] = ([(S, start[i])], [])
                couplings[((k, i), 9)] = (k, (i + 1) % k)
            opened[k] = tuple(start[i] for i in range(k))
    return uncrossed, sorted(opened), resolvings


if __name__ == "__main__":
    root = sys.argv[1]
    to = int(sys.argv[sys.argv.index("--to") + 1]) if "--to" in sys.argv else 3720
    names, page = resolver(root)
    step = names["_17_next_existing"]
    all_is = True

    print("1. Odd prime spirals side by side, four moments a number, a spiral opening at an uncrossed number")
    uncrossed, opened, resolvings = the_surface(step, to)
    primes = [n for n in range(2, to + 1) if by_division(n)]
    same = uncrossed == primes
    all_is = all_is and same
    print(f"   spirals opened, beside the spiral of two: {len(opened)}, of {opened[0]} to {opened[-1]} selves, {sum(opened)} selves together")
    print(f"   numbers gone through: 2 to {to} · uncrossed: {len(uncrossed)} · the primes to {to} by division: {'the same' if same else 'other-than'}")
    print(f"   resolvings of a self executed: {resolvings:,}")
    strikings = sum(len(range(p * p, to + 1, p)) for p in primes if p * p <= to)
    print(f"   beside it, by division: a field's sieve comes to the same with {strikings:,} strikings, a prime striking from its square on")
    two = {i: ([(S, p)], []) for i, p in exhibit_spiral_priors(2).items()}
    was = tuple(dict(two[i][0])[S] for i in range(2))
    at_four, at_one = [], []
    for moment in range(1, 81):
        two = step(two, {(0, 9): 1, (1, 9): 0})
        again = tuple(dict(two[i][0])[S] for i in range(2)) == was
        if moment % 4 == 0:
            at_four.append(again)
        if moment <= 20:
            at_one.append(again)
    with_all = all(at_four)
    with_even = at_one == [m % 2 == 0 for m in range(1, 21)]
    all_is = all_is and with_all and with_even
    print(f"   the spiral of two at four moments a number, its priors again with all numbers, distinguishing none: {'is' if with_all else 'is-not'}")
    print(f"   the spiral of two at one moment a number, its priors again with the even numbers alone: {'is' if with_even else 'is-not'}")
    print()

    print("2. What the surface found, from its uncrossed numbers alone")
    U = set(uncrossed)
    gaps = [b - a for a, b in zip(uncrossed, uncrossed[1:])]
    seen = {}
    for g in gaps:
        seen[g] = seen.get(g, 0) + 1
    print("   gaps between neighbouring uncrossed numbers · " + " · ".join(f"of {g}: {seen[g]}" for g in sorted(seen)[:8]) + f" · wider: {sum(v for g, v in seen.items() if g > sorted(seen)[7])}")
    widest = max(gaps)
    at = uncrossed[gaps.index(widest)]
    print(f"   the widest gap: {widest}, from {at} to {at + widest} · the square of the natural logarithm of {at}: {math.log(at) ** 2:.1f}")
    pairs = [p for p in uncrossed if p + 2 in U]
    print(f"   pairs two apart: {len(pairs)} · the last of them: {pairs[-1]} and {pairs[-1] + 2}")
    for n in (1000, 2000, 3000):
        below = max(p for p in uncrossed if p < n)
        above = min(p for p in uncrossed if p > n)
        pair = min(p for p in pairs if p > n)
        print(f"   from {n} · nearest uncrossed: {below} and {above} · next pair two apart: {pair} and {pair + 2}")
    worst_k, worst_n = 0, 0
    for n in range(2, to // 2 + 1):
        k = next(k for k in range(0, n) if n - k in U and n + k in U)
        if k > worst_k:
            worst_k, worst_n = k, n
    print(f"   an uncrossed number on both sides at one distance, from all numbers 2 to {to // 2}: is · the farthest such nearest distance: {worst_k}, from {worst_n}")
    squares = all(any(p in U for p in range(m * m + 1, (m + 1) ** 2)) for m in range(1, math.isqrt(to + 1)))
    all_is = all_is and squares
    print(f"   an uncrossed number between two neighbouring squares, to {math.isqrt(to + 1)} squared: {'is' if squares else 'is-not'}")
    print()

    print("3. By division, no resolver in it: spirals side by side again together, a closed turn")
    turn = 1
    for q in (2, 3, 5, 7, 11):
        turn *= q
        clear = [r for r in range(1, turn + 1) if math.gcd(r, turn) == 1]
        two_apart = sum(1 for r in clear if math.gcd(r + 2, turn) == 1)
        beyond = next(n for n in range(q + 1, 10 ** 6) if math.gcd(n, turn) == 1 and not by_division(n))
        print(f"   spirals to {q:>2} · a turn of {turn:>4} · uncrossed in a turn: {len(clear):>3} · pairs two apart in a turn: {two_apart:>3} · the turn's uncrossed are primes as far as {beyond - 1}, and {beyond} is crossed by a spiral not yet open")
    print()

    print("4. By division, no resolver in it: the 0 placed on a far number, its places on its spirals, then stepping alone")
    reach = 3000
    for n in (10 ** 6, 10 ** 9, 10 ** 12):
        root_n = math.isqrt(n + reach)
        sieve = bytearray([1]) * (root_n + 1)
        sieve[0:2] = b"\x00\x00"
        for i in range(2, math.isqrt(root_n) + 1):
            if sieve[i]:
                sieve[i * i :: i] = bytearray(len(range(i * i, root_n + 1, i)))
        spirals = [q for q in range(2, root_n + 1) if sieve[q]]
        places = [n % q for q in spirals]  # one dividing a spiral
        steps = 0
        clear = []
        for d in range(-reach, reach + 1):
            crossed = False
            for q, place in zip(spirals, places):
                steps += 1
                if (place + d) % q == 0 and n + d != q:
                    crossed = True
                    break
            if not crossed:
                clear.append(n + d)
        same = clear == [m for m in range(n - reach, n + reach + 1) if witness(m)]
        all_is = all_is and same
        C = set(clear)
        below, above = max(p for p in clear if p < n), min(p for p in clear if p > n)
        pair = min((p for p in clear if p > n and p + 2 in C), default=None)
        k = next((k for k in range(0, reach + 1) if n - k in C and n + k in C), None)
        print(f"   from {n:,} · spirals asked: {len(spirals):,} · nearest uncrossed: {n - below} below and {above - n} above · next pair two apart: {pair - n if pair else 'none'} on · both sides at one distance: {k if k is not None else 'none to ' + str(reach)} · the square of its natural logarithm: {math.log(n) ** 2:.0f} · the same as a field's test of the numbers one by one: {'is' if same else 'is-not'}")
    print()
    print("All is." if all_is else "An is-not is above.")
    sys.exit(0 if all_is else 1)
