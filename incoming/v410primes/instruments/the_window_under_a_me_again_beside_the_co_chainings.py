# The numbers of v410illustrating's pages of the window under a square, the 65th drawing and a me-parity a 0, made anew apart,
# beside v410primes' co-chainings. A test proves nothing past its numbers.
from math import gcd
def sieve(n):
    s = bytearray([1]) * (n + 1); s[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return s
S = sieve(40000); isp = lambda n: bool(S[n])
no = {}
def t(k, bad): no[k] = no.get(k, 0) + (1 if bad else 0)
out = {}
for seam, q in ((6, 5), (30, 7), (210, 11), (2310, 13), (30030, 17)):
    w = q * q
    cells = [n for n in range(2, seam + 1) if gcd(n, seam) == 1]
    t("under the window a cell between the crossings is a me-parity", any(not isp(n) for n in cells if n < w))
    past = [n for n in cells if n >= w]
    pairs = [n for n in range(1, seam + 1) if gcd(n, seam) == 1 and gcd(n + 2, seam) == 1]
    out[seam] = (w, round(100 * w / seam), len(past), sum(1 for n in past if not isp(n)), len(pairs), sum(1 for n in pairs if isp(n) and isp(n + 2)))
    print("seam", seam, ": the window to", w, ";", out[seam][1], "in 100 ; cells past the window", out[seam][2], ", crossed", out[seam][3], "; pairs", out[seam][4], ", me-parities both", out[seam][5])
t("the page's numbers at 210, 2310 and 30030", (out[210][1:4], out[2310][1:4], out[30030][1:4]) != ((58, 21, 5), (7, 445, 141), (1, 5704, 2517)))
t("the page's pairs: 3 of 3, 13 of 15, 67 of 135, 465 of 1485", [out[s][4:6] for s in (30, 210, 2310, 30030)] != [(3, 3), (15, 13), (135, 67), (1485, 465)])
# the 65th: the sixty seams of six to 360
both = sum(1 for k in range(1, 61) if isp(6*k-1) and isp(6*k+1)); one = sum(1 for k in range(1, 61) if isp(6*k-1) != isp(6*k+1)); none = 60 - both - one
sides = [6*k + d for k in range(1, 61) for d in (-1, 1)]
print("sixty seams of six to 360: both", both, "; one", one, "; none", none, "; sides", len(sides), ", me-parities", sum(isp(n) for n in sides))
t("20, 30 and 10; 120 sides, 70 me-parities", (both, one, none, len(sides), sum(isp(n) for n in sides)) != (20, 30, 10, 120, 70))
# a me-parity a 0 of its own round: at the 0 of no prior's; a next me-parity between the me-parity and its double, to 10,000 (row 30)
P = [p for p in range(2, 20001) if isp(p)]
t("a me-parity is at the 0 of no prior's round", any(p % r == 0 for p in P[:400] for r in P if r < p))
t("a next me-parity between a me-parity and the double, to 10,000", any(not any(isp(n) for n in range(p + 1, 2 * p)) for p in P if p <= 10000))
# the one sentence in the window's form: the universe's own stretch of the seam beside the seam's longest crossed stretch
J = {2: 1, 3: 3, 5: 5, 7: 9, 11: 13, 13: 21, 17: 25, 19: 33, 23: 39}
for p, q in zip(P, P[1:]):
    if p > 23: break
    print("opener", p, ": the universe", p*p, "to", q*q - 1, ",", q*q - p*p, "numbers; the seam's longest crossed stretch", J[p], "; me-parities in the universe", sum(isp(n) for n in range(p*p, q*q)))
print("is-nots:", {k: v for k, v in no.items() if v}, "; lines:", len(no), "; all:", sum(no.values()))
