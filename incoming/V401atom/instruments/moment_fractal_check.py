"""A moment as a fractal: each four moments a moment, and each moment four moments, with 1 to 5, 1 to 17 and 1 to 65.

A check of a reading, by cycling: each name's parities from n - 1 in binary, each digit is-or-is-not the same as the
digit one up, as Natural Resolver's gathering-value has a name's four parities; a round of k parities 1 to 2^k + 1,
as Exhibit THREE Natural Numbers has it. Exhibit ONE's table, read from its file, no line changed.
Run: python3 incoming/V401atom/instruments/moment_fractal_check.py Exhibit_ONE_Natural_Resolver_v<version>.md
"""
import re, sys
src = open(sys.argv[1], encoding="utf-8").read()
rows = re.findall(r"^\| (\d+) \| \*\*([\w-]+)\*\* \| ([^|]+) \| ([^|]+) \| (\w+) \| ([\w-]+) \|$", src, re.M)
digits = {int(n): b.strip() for n, _a, _r, b, _c, _t in rows if re.fullmatch(r"[01]{4}", b.strip())}
root = {int(n): r.strip() for n, _a, r, _b, _c, _t in rows}
print("the table's sixteen names, each n - 1 in four binary digits:", all(digits[n] == format(n - 1, "04b") for n in range(1, 17)))

def parities(n, k):                  # k parities of a name: each digit is-or-is-not the same as the digit one up; first parity first
    m = n - 1
    return [((m >> i) ^ (m >> (i + 1))) & 1 for i in range(k)]
say = lambda v: "-" if v else "+"

for k, last in ((2, 5), (4, 17), (6, 65), (8, 257)):
    steps = [[i for i in range(k) if parities(n, k)[i] != parities(n + 1 if n < last - 1 else 1, k)[i]] for n in range(1, last)]
    forms = {tuple(parities(n, k)) for n in range(1, last)}
    print(f"1 to {last}: {k} parities; each next name one parity inverting, and no two: {all(len(s) == 1 for s in steps)} ; each form once: {len(forms) == 2 ** k}")

print("1 to 17, each name with its two pairs of parities, an inner pair and an outer pair:")
for a in range(4):
    line = []
    for n in range(4 * a + 1, 4 * a + 5):
        p = parities(n, 4)
        line.append(f"{n:2} {say(p[0])}{say(p[1])} {say(p[2])}{say(p[3])}")
    print("   ", "   ".join(line), "   ", ", ".join(root[n] for n in range(4 * a + 1, 4 * a + 5)))

def pair_path(k, s, last):           # the forms of pair s, a name after a name
    return [tuple(parities(n, k)[2 * s:2 * s + 2]) for n in range(1, last)]
right = lambda xy: (xy[1], 1 - xy[0])    # a right spiral step, (x, y) to (y, -x), as Natural Naming has it, with x a pair's second parity
def step_kind(a, b):
    if a == b: return "none"
    x, y = (a[1], a[0]), (b[1], b[0])
    return "right" if right(x) == y else "back" if right(y) == x else "other"

for k, last in ((4, 17), (6, 65)):
    print(f"1 to {last}, each pair of parities, a moment of a pair one of its steps:")
    for s in range(k // 2):
        path = pair_path(k, s, last) + [pair_path(k, s, last)[0]]
        kinds = [step_kind(path[i], path[i + 1]) for i in range(last - 1)]
        size = 4 ** s
        own = [kinds[i] for i in range(size - 1, last - 1, size)]            # a step of this pair's own, once with each of its moments
        print(f"    pair {s + 1}: a moment of it {size} name{'s' if size > 1 else ''}; its steps {sum(1 for x in kinds if x != 'none')}, with each a right spiral step {own.count('right')} and that step backward {own.count('back')}, an other {own.count('other')}; its steps in turn: {' '.join(own[:16])}{' ...' if len(own) > 16 else ''}")
        if s + 1 < k // 2:
            four = [own[i:i + 4] for i in range(0, len(own), 4)]
            print(f"            three steps of its own, then none, with each four: {all(f[3] == 'none' and 'none' not in f[:3] for f in four)} ; with each odd four right and each even four backward: {all(set(f[:3]) == ({'right'} if i % 2 == 0 else {'back'}) for i, f in enumerate(four))}")
            out = [tuple(parities(n, k)[2 * s + 2:]) for n in range(1, last)]; out.append(out[0])
            print(f"            with each fourth, and with no other, a pair outward of it steps: {all((out[i] != out[i + 1]) == ((i + 1) % (4 * size) == 0) for i in range(last - 1))}")

print("a pair's forms with each first name of its moments, 1, 2, 3, 4 with 1 to 5; 1, 5, 9, 13 with 1 to 17; 1, 17, 33, 49 with 1 to 65:")
a = [tuple(parities(n, 2)) for n in (1, 2, 3, 4)]
b = [tuple(parities(n, 4)[2:4]) for n in (1, 5, 9, 13)]
c = [tuple(parities(n, 6)[4:6]) for n in (1, 17, 33, 49)]
for name, q in (("1 to 5", a), ("1 to 17", b), ("1 to 65", c)):
    print(f"    {name:8}:", " ".join(say(x) + say(y) for x, y in q))
print("    one same four forms with each:", a == b == c, "; n to 4n - 3, twice:", [4 * n - 3 for n in (1, 2, 3, 4, 5)], [4 * (4 * n - 3) - 3 for n in (1, 2, 3, 4, 5)])
cnt = []
for s in range(3):
    q = pair_path(6, s, 65) + [pair_path(6, s, 65)[0]]
    cnt.append(sum(1 for i in range(64) if q[i] != q[i + 1]))
print("steps of a pair's own, 1 to 65: inner", cnt[0], "middle", cnt[1], "outer", cnt[2], "; three of a pair's own to one of each pair outward of it, twice:",
      cnt[0] == 3 * (cnt[1] + cnt[2]) and cnt[1] == 3 * cnt[2], "; in all", sum(cnt))
