# v408primes · inhaling and exhaling, odd and even, now, across; exhausting, next after now, along.
# Whole numbers alone. Execute: python3 -I inhaling_exhaling_across_exhausting_along.py
N = 4 ** 11
spf = list(range(N + 1))
for i in range(2, int(N ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, N + 1, i):
            if spf[j] == j:
                spf[j] = i
def count(n):
    c = 0
    while n > 1:
        n //= spf[n]; c += 1
    return c
results = []
def say(s, ok):
    results.append(ok); print(("is     " if ok else "is-not ") + s)
# Across, now: a number's parts multiplied, odd or even by their count.
show = [(n, count(n), "odd" if count(n) % 2 else "even") for n in (7, 12, 30, 36, 49)]
say("across, now, a number is odd or even by the count of its prime parts multiplied: %s" % show, True)
# Along, next after now: the next's parity added to all before it, the lead.
lead, odd, even, zeros, most, k, side, rows = 0, 0, 0, 0, 0, 1, 2, []
for n in range(1, N + 1):
    c = count(n)
    if c % 2: odd += 1; lead -= 1
    else: even += 1; lead += 1
    if lead == 0: zeros += 1
    most = max(most, abs(lead))
    if n == 4 ** k:
        rows.append((n, side, most, odd, even, zeros)); k += 1; side *= 2
for r in rows[-4:]:
    print("        surface %9d  side %5d  lead's most %5d  odd %8d  even %8d  apart %4d  back at 0 %5d" % (r[0], r[1], r[2], r[3], r[4], abs(r[3]-r[4]), r[5]))
say("along, the exhausted lead's most is short of twice the side on all surfaces to 4,194,304", all(r[2] < 2 * r[1] for r in rows))
say("odd and even are near half and half: to 4,194,304, %d odd and %d even" % (odd, even), abs(odd - even) < 2 * 2048)
print("All is." if all(results) else "A line is-not.")
