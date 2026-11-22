"""A number by its spirals: the co-chaining a prime rests on, executed.

A partner's saying is explored here by executing, and nothing is proved.

Part 1 is Exhibit ONE Natural Resolver's code as it is in its living file. A
self alone and odd prime spirals of selves go side by side in one
same-existing-society, two moments a number: an odd spiral's like pair moves
one self on with a number, as Exhibit THREE Natural Numbers 7.2 has it. A
spiral is at its seam with a number once its priors are as at its opening, as
they were or all inverting. A number an open spiral smaller than it is at its
seam with is crossed. A number no open spiral crosses is uncrossed, and an odd
one to 59 opens a spiral of that number of selves. Two is the self alone
inverting. No dividing is in part 1.

Part 2 goes through what part 1 found. Parts 3 to 5 are by division or by
numbers' own arithmetic, with no resolver in them, and say so.

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


def primes_to(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, math.isqrt(n) + 1):
        if sieve[i]:
            sieve[i * i :: i] = bytearray(len(range(i * i, n + 1, i)))
    return sieve


def priors_of(society, q):
    return tuple(dict(society[(q, i)][0]).get(S, 0) for i in range(q))


def the_surface(step, to, open_to=59):
    """A self alone from 1, odd spirals opening at uncrossed odd numbers, two moments a number."""
    society = {(1, 0): ([(S, exhibit_spiral_priors(1)[0])], [])}
    couplings = {((1, 0), 9): (1, 0)}
    opened = {1: (exhibit_spiral_priors(1)[0],)}
    uncrossed, resolvings, with_two = [], 0, True
    for k in range(2, to + 1):
        for _ in range(2):
            society = step(society, couplings)
            resolvings += len(society)
        alone = priors_of(society, 1)
        even = alone == tuple(-x for x in opened[1])
        crossed = even and k > 2
        for q, was in opened.items():
            if q == 1:
                continue
            now = priors_of(society, q)
            if now == was or now == tuple(-x for x in was):
                crossed = True
                with_two = with_two and ((now == was) == (not even))
        if crossed:
            continue
        uncrossed.append(k)
        if k % 2 and k <= open_to:
            start = exhibit_spiral_priors(k)
            for i in range(k):
                society[(k, i)] = ([(S, start[i])], [])
                couplings[((k, i), 9)] = (k, (i + 1) % k)
            opened[k] = tuple(start[i] for i in range(k))
    return uncrossed, sorted(q for q in opened if q > 1), resolvings, with_two


def prior_two_pair(m, n):
    """The m-th and the next number of prior two added, round n, by doubling the place."""
    if m == 0:
        return 0, 1 % n
    a, b = prior_two_pair(m >> 1, n)
    c = a * ((2 * b - a) % n) % n
    d = (a * a + b * b) % n
    return (d, (c + d) % n) if m & 1 else (c, d)


def jacobi(a, n):
    a %= n
    t = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            t = -t
        a %= n
    return t if n == 1 else 0


def family_number(k, m, n):
    """The m-th number of a next as k times now with its prior added, round n: 0, 1, k, ..."""
    def mul(A, B):
        return ((A[0] * B[0] + A[1] * B[2]) % n, (A[0] * B[1] + A[1] * B[3]) % n,
                (A[2] * B[0] + A[3] * B[2]) % n, (A[2] * B[1] + A[3] * B[3]) % n)
    R, M = (1, 0, 0, 1), (k % n, 1, 1, 0)
    while m:
        if m & 1:
            R = mul(R, M)
        M = mul(M, M)
        m >>= 1
    return R[1]


def its_own_closings(n):
    """An odd number by itself, no smaller prime asked: doubling by one short of it, an adding of φ's family by one past it."""
    if pow(2, n - 1, n) != 1:
        return False
    r = math.isqrt(n)
    if r * r == n:
        return False
    k = 1
    while True:
        j = jacobi(k * k + 4, n)
        if j == -1:
            break
        if j == 0 and math.gcd(k * k + 4, n) not in (1, n):
            return False
        k += 1
    return family_number(k, n + 1, n) == 0


if __name__ == "__main__":
    root = sys.argv[1]
    to = int(sys.argv[sys.argv.index("--to") + 1]) if "--to" in sys.argv else 3720
    names, page = resolver(root)
    step = names["_17_next_existing"]
    all_is = True

    print("1. A self alone and odd prime spirals side by side, two moments a number, a spiral opening at an uncrossed odd number")
    uncrossed, opened, resolvings, with_two = the_surface(step, to)
    primes = [n for n in range(2, to + 1) if by_division(n)]
    same = uncrossed == primes
    all_is = all_is and same and with_two
    print(f"   odd spirals opened: {len(opened)}, of {opened[0]} to {opened[-1]} selves, {sum(opened)} selves together, and a self alone")
    print(f"   numbers gone through: 2 to {to} · uncrossed: {len(uncrossed)} · the primes to {to} by division: {'the same' if same else 'other-than'}")
    print(f"   an odd spiral at its seam with a number is as it was with an odd number and inverting with an even one, as the self alone is: {'is' if with_two else 'is-not'}")
    print(f"   resolvings of a self executed: {resolvings:,}")
    strikings = sum(len(range(p * p, to + 1, p)) for p in primes if p * p <= to)
    print(f"   beside it, by division: a field's sieve comes to the same with {strikings:,} strikings, a prime striking from its square on")
    print()

    print("2. What the surface found, from its uncrossed numbers alone")
    U = set(uncrossed)
    gaps = [b - a for a, b in zip(uncrossed, uncrossed[1:])]
    seen = {}
    for g in gaps:
        seen[g] = seen.get(g, 0) + 1
    print("   gaps between neighbouring uncrossed numbers · " + " · ".join(f"of {g}: {seen[g]}" for g in (2, 4, 6)))
    print("   pairs of uncrossed numbers, neighbouring or with others between · " + " · ".join(f"{d} apart: {sum(1 for p in uncrossed if p + d in U)}" for d in (2, 4, 6)))
    widest = max(gaps)
    at = uncrossed[gaps.index(widest)]
    print(f"   the widest gap: {widest}, from {at} to {at + widest}")
    for n in (1000, 3000):
        below, above = max(p for p in uncrossed if p < n), min(p for p in uncrossed if p > n)
        pair = min(p for p in uncrossed if p > n and p + 2 in U)
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

    print("3. By division, no resolver in it: a closed turn, spirals side by side again together")
    turn, odd = 1, []
    for q in (2, 3, 5, 7, 11):
        turn *= q
        if q > 2:
            odd.append(q)
        clear = set(r for r in range(turn) if math.gcd(r, turn) == 1)
        apart = {d: sum(1 for r in clear if (r + d) % turn in clear) for d in (2, 4, 6)}
        by_spirals = {d: math.prod(p - (1 if d % p == 0 else 2) for p in odd) for d in (2, 4, 6)}
        places = len({tuple(r % p for p in [2] + odd) for r in range(turn)}) == turn
        beyond = next(n for n in range(q + 1, 10 ** 6) if math.gcd(n, turn) == 1 and not by_division(n))
        ok = apart == by_spirals and places
        all_is = all_is and ok
        print(f"   spirals to {q:>2} · a turn of {turn:>4} · uncrossed in a turn: {len(clear):>3} · pairs 2, 4 and 6 apart in a turn: {apart[2]}, {apart[4]} and {apart[6]} · all places together once a turn, and the pairs a spiral's places less two, or less one, multiplied: {'is' if ok else 'is-not'} · a turn's uncrossed are primes as far as {beyond - 1}")
    both = True
    for n in range(4, 400):
        turn_n = 2 * 3 * 5 * 7
        ks = sum(1 for k in range(turn_n) if math.gcd(n - k, turn_n) == 1 and math.gcd(n + k, turn_n) == 1)
        want = math.prod((p - 1) if n % p == 0 else (p - 2) for p in (3, 5, 7)) * (1 if True else 0)
        both = both and ks == want and ks > 0
    all_is = all_is and both
    print(f"   from a number, the distances of a turn of 210 with both sides uncrossed: a spiral's places less two, or less one with a spiral at its seam with the number, multiplied, and never none, from 4 to 399: {'is' if both else 'is-not'}")
    print()

    print("4. By division, no resolver in it: the 0 placed on a far number, its places on its spirals, then stepping alone")
    reach = 3000
    far = {}
    for n in (10 ** 6, 10 ** 9, 10 ** 12):
        root_n = math.isqrt(n + reach)
        sieve = primes_to(root_n)
        spirals = [q for q in range(2, root_n + 1) if sieve[q]]
        places = [n % q for q in spirals]  # one dividing a spiral
        clear = []
        for d in range(-reach, reach + 1):
            if not any((place + d) % q == 0 and n + d != q for q, place in zip(spirals, places)):
                clear.append(n + d)
        far[n] = clear
        C = set(clear)
        below, above = max(p for p in clear if p < n), min(p for p in clear if p > n)
        pair = min(p for p in clear if p > n and p + 2 in C)
        k = next(k for k in range(0, reach + 1) if n - k in C and n + k in C)
        print(f"   from {n:,} · spirals asked: {len(spirals):,} · nearest uncrossed: {n - below} below and {above - n} above · next pair two apart: {pair - n} on · both sides at one distance: {k}")
    print()

    print("5. By numbers' own arithmetic, no resolver in it and no smaller prime asked: a number's own closings")
    line = []
    all_divide = True
    for p in [q for q in range(2, 60) if by_division(q)]:
        a, b, steps = 0, 1, 0
        while True:
            a, b = b, (a + b) % p
            steps += 1
            if (a, b) == (0, 1 % p):
                break
        line.append(f"{p}: {steps}")
        if p not in (2, 5):
            all_divide = all_divide and ((p - 1) % steps == 0 if p % 5 in (1, 4) else (2 * (p + 1)) % steps == 0)
    all_is = all_is and all_divide
    print("   prior two added, round a prime, closes · " + " · ".join(line))
    print(f"   its closing divides one short of a prime ending in 1 or 9, and twice one past a prime ending in 3 or 7, to 59: {'is' if all_divide else 'is-not'}")
    top = 10 ** 7
    sieve = primes_to(top)
    doubling_alone, both_composite, both_prime, primes_there = 0, [], 0, 0
    for n in range(3, top + 1, 2):
        if n % 5 not in (2, 3):
            continue
        primes_there += sieve[n]
        if pow(2, n - 1, n) != 1:
            continue
        adding = prior_two_pair(n + 1, n)[0] == 0
        if sieve[n]:
            both_prime += adding
        else:
            doubling_alone += 1
            if adding:
                both_composite.append(n)
    adding_alone = [n for n in range(3, 10 ** 6 + 1, 2) if n % 5 in (2, 3) and not sieve[n] and prior_two_pair(n + 1, n)[0] == 0]
    ok = both_prime == primes_there and not both_composite
    all_is = all_is and ok
    print(f"   odd numbers ending in 3 or 7, to {top:,} · primes: {primes_there:,}, all with both closings: {'is' if both_prime == primes_there else 'is-not'}")
    print(f"   composites with doubling's closing alone, to {top:,}: {doubling_alone} · with the adding's closing alone, to 1,000,000: {len(adding_alone)}, the smallest {adding_alone[:3]} · composites with both: {len(both_composite)}")
    odd_to = 10 ** 6
    passers = [n for n in range(3, odd_to + 1, 2) if its_own_closings(n)]
    same = passers == [n for n in range(3, odd_to + 1, 2) if sieve[n]]
    all_is = all_is and same
    print(f"   all odd numbers to {odd_to:,}, doubling's closing with an adding of φ's family, one past the number: the numbers with both are the odd primes: {'is' if same else 'is-not'}")
    for n, clear in far.items():
        own = [m for m in range(n - reach, n + reach + 1) if m == 2 or (m % 2 and its_own_closings(m))]
        same = own == clear
        all_is = all_is and same
        print(f"   about {n:,}, 3,000 on both sides: a number's own closings find the same as its places on its spirals: {'is' if same else 'is-not'}")
    print()
    print("All is." if all_is else "An is-not is above.")
    sys.exit(0 if all_is else 1)
