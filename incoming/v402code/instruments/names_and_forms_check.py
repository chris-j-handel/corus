"""v402code · the sentences of names, moves and forms of Exhibit ONE Natural Resolver, read by arithmetic
and by the code's own words. Deciding nothing. Run, R the set's folder: python3 -I names_and_forms_check.py R"""
import re, sys
import glob, os
src = open(sorted(glob.glob(os.path.join(sys.argv[1], "Exhibit_ONE_Natural_Resolver_v*.md")))[-1], encoding='utf-8').read()
code = re.search(r"```python\n(.*?)\n```", src, re.S).group(1)
out = []
def report(name, same, detail=""):
    out.append(same); print(("SAME      " if same else "NOT SAME  ") + name + ((" :: " + detail) if detail else ""))

# seventeen names from the table
rows = re.findall(r"^\| (\d+) \| \*\*([^*]+)\*\* \| ([^|]+) \| ([^|]+) \| (co|one) \| ([a-z-]+) \|$", src, re.M)
NAME = {int(n): nm for n, nm, *_ in rows}
report("Seventeen names, one row each", sorted(NAME) == list(range(1, 18)))
# names with the code's identifiers
ids = {int(a): b for a, b in re.findall(r"\b_(\d+)_([a-z_]+)\b", code)}
report("Each name is its code's word (hyphens as underscores)", all(NAME[n].split("-", 1)[1].replace("-", "_") == ids[n] for n in NAME),
       str([(n, NAME[n], ids.get(n)) for n in NAME if NAME[n].split("-", 1)[1].replace("-", "_") != ids.get(n)]))
funcs = set(int(x) for x in re.findall(r"^def _(\d+)_", code, re.M))
report("Three functions 1, 9 and 17, fourteen variables", funcs == {1, 9, 17} and len(set(ids) - funcs) == 14)
# n − 1 in four binary digits, co, root
bad = []
for n, nm, root, b, co, three in rows:
    n = int(n)
    if n < 17 and b.strip() != format(n - 1, "04b"): bad.append((n, "binary", b))
    if (co == "co") != ("-co-" in nm): bad.append((n, "co"))
    if not nm.endswith(root.split(",")[0].strip()): bad.append((n, "root", root))
report("n − 1 in four binary digits; co with each co name; each root its name's last word", not bad, str(bad))
# its three: a new prefix first, the name before's first two one slot on
first = ["co", "bi", "co", "bi", "co", "bi", "tri", "bi"]
three = {0: ("bi", "tri", "bi")}
for n in range(1, 18): three[n] = (first[(n - 1) % 8], three[n - 1][0], three[n - 1][1])
bad = [(int(n), t) for n, _, _, _, _, t in rows if "-".join(three[int(n)]) != t]
report("Each name's three, by its rolling", not bad, str(bad))
tri_first = [n for n in range(1, 18) if three[n][0] == "tri"]; tri_mid = [n for n in range(1, 18) if three[n][1] == "tri"]; tri_last = [n for n in range(1, 18) if three[n][2] == "tri"]
report("Tri first with 7 and 15, middle with 8 and 16, last with 9, 17 and 1", (tri_first, tri_mid, tri_last) == ([7, 15], [8, 16], [1, 9, 17]), str((tri_first, tri_mid, tri_last)))
# every hyphenated name token in the file is one of the seventeen, whole
tokens = set(re.findall(r"(?<![\w-])(\d{1,2}-(?:now|next)(?:-[a-z]+)+)", src))
stray = sorted(t for t in tokens if t not in NAME.values())
report("Each name written whole wherever it is written", not stray, str(stray))

# moves and forms
BI = [[1, 9, 8, 16], [2, 15, 7, 10], [3, 11, 6, 14], [4, 13, 5, 12]]
MID = [[9, 5, 12, 8], [7, 11, 6, 10]]
SIX = [[1, 9, 5, 12, 8, 16], [2, 15, 7, 11, 6, 10], [3, 11, 7, 10, 6, 14], [4, 13, 5, 9, 8, 12]]
EIGHT = [[1, 9, 5, 13, 4, 12, 8, 16], [2, 15, 7, 11, 3, 14, 6, 10]]
def move(a, b):
    if b == a + 8: return "8up"
    if b == a - 8: return "8down"
    if b == a + 4: return "4up"
    if b == a - 4: return "4down"
    if b == 17 - a: return "17less"
    return None
def moves(c): return [move(c[i], c[(i + 1) % len(c)]) for i in range(len(c))]
report("Each bi-folding: 17 less and a move of 8 in turn, four steps to its first name",
       all(None not in moves(c) and all(("17less" in (m[i], m[i + 1])) and m[i] != m[i + 1] for i in range(3)) for c in BI for m in [moves(c)]), str([moves(c) for c in BI]))
report("Each middle bi-folding: 17 less and a move of 4 in turn", all(set(moves(c)) <= {"17less", "4up", "4down"} for c in MID), str([moves(c) for c in MID]))
m6 = [moves(c) for c in SIX]
fwd = ["8up", "4down", "17less", "4down", "8up", "17less"]
inv = {"8up": "8down", "8down": "8up", "4up": "4down", "4down": "4up", "17less": "17less"}
back = [inv[x] for x in reversed(fwd)]
def rot_eq(a, b): return any(a[i:] + a[:i] == b for i in range(len(a)))
report("Six-cycles: 1-9-5-12-8-16 and 3-11-7-10-6-14 by 8 up, 4 down, 17 less, 4 down, 8 up, 17 less; the other two the same moves backward",
       m6[0] == fwd and m6[2] == fwd and rot_eq(m6[1], back) and rot_eq(m6[3], back), str(m6))
report("Eight-cycles: each move 8 up, 8 down, 4 up, 4 down or 17 less", all(None not in moves(c) for c in EIGHT), str([moves(c) for c in EIGHT]))
ALL = BI + MID + SIX + EIGHT
bad = []
for c in ALL:
    odd_runs = sum(1 for i in range(len(c)) if c[i] % 2 == 1 and c[i - 1] % 2 == 0)
    if odd_runs != 1 or sum(1 for x in c if x % 2) * 2 != len(c): bad.append(c)
report("Twelve forms: along each, odd names one run and even names one run, of like length", not bad, str(bad))
# partners
def swap_odd(n): return n + 1 if n % 2 else n - 1            # 1 with 2 ... 15 with 16
def swap_even(n): return n if n == 1 else (n + 1 if n % 2 == 0 else n - 1)   # 2 with 3 ... 16 with 17
label = lambda c: "-".join(map(str, c))
def partner(c, f):
    img = [f(x) for x in c]
    for d in ALL:
        if len(d) == len(c) and (rot_eq(d, img) or rot_eq(d, img[::-1])): return label(d), "same order round"
    for d in ALL:
        if len(d) == len(c) and set(d) == set(img): return label(d), "its names, another order"
    return None, None
blocks = re.findall(r"- \*\*Form: (?:middle )?(?:bi-folding|six-cycle|eight-cycle) ([\d-]+)\*\*\n  - \*a\*: ([^\n]+)\n  - \*b\*: ([^\n]+)\n  - \*c\*: ([^\n]+)", src)
bad = []
for lab, a, b, c in blocks:
    form = [int(x) for x in lab.split("-")]
    if [int(x.split("-")[0]) for x in a.split(" · ")] != form: bad.append((lab, "a"))
    for txt, f in ((b, swap_odd), (c, swap_even)):
        got, how = partner(form, f)
        said = re.search(r"([\d]+(?:-\d+)+)", txt)
        said = said.group(1) if said else None
        if txt.startswith("—"):
            if got is not None and "its own six names" not in txt: bad.append((lab, txt, got))
            if "its own six names" in txt and not (got == lab and how == "its names, another order"): bad.append((lab, txt, got, how))
        elif said != got or how != "same order round": bad.append((lab, txt, got, how))
report("Twelve forms: each form's names by order and its two partners (%d forms read)" % len(blocks), len(blocks) == 12 and not bad, str(bad))

# each name and its relations
sec = src[src.index("**Each name and its relations.**"):src.index("**Odd names, now and 8 up with next.**")]
nb = re.split(r"\n\*\*(\d+)\*\* · ", sec)[1:]
bad = []
for i in range(0, len(nb), 2):
    n = int(nb[i]); body = nb[i + 1]
    f = dict(re.findall(r"^- \*([^*]+)\*: (.*)$", body, re.M))
    def num(s): return int(re.match(r"(?:podal within 1 to \d+, )?(\d+)", s).group(1))
    if not body.startswith(NAME[n]): bad.append((n, "name"))
    if ("8 up" in f) != (n <= 9) or ("8 up" in f and num(f["8 up"]) != n + 8): bad.append((n, "8 up"))
    if ("8 down" in f) != (n >= 9) or ("8 down" in f and num(f["8 down"]) != n - 8): bad.append((n, "8 down"))
    if ("9 less" in f) != (n <= 8) or ("9 less" in f and num(f["9 less"]) != 9 - n): bad.append((n, "9 less"))
    if ("17 less" in f) != (n <= 16) or ("17 less" in f and num(f["17 less"]) != 17 - n): bad.append((n, "17 less"))
    if n <= 16:
        bf = [c for c in BI if n in c][0]
        m = re.match(r"([\d-]+), going (8 up|17 less) first from (\d+)-[a-z-]+, from (\d+)-[a-z-]+ to it and on to (\d+)-", f["Bi-folding"])
        if not m: bad.append((n, "bi-folding unread"))
        else:
            k = bf.index(n)
            want = (label(bf), {"8up": "8 up", "17less": "17 less"}[move(bf[0], bf[1])], bf[0], bf[k - 1], bf[(k + 1) % 4])
            got = (m.group(1), m.group(2), int(m.group(3)), int(m.group(4)), int(m.group(5)))
            if got != want: bad.append((n, "bi-folding", got, want))
        beside = sorted(label(c) for c in BI if c is not bf and abs(BI.index(c) - BI.index(bf)) == 1)
        said = sorted(re.findall(r"(\d+-\d+-\d+-\d+)", f["Bi-folding"].split("each name one apart from")[1]))
        if said != beside: bad.append((n, "beside", said, beside))
        mids = [label(c) for c in MID if n in c]
        if ([f["Middle bi-folding"]] if "Middle bi-folding" in f else []) != mids: bad.append((n, "middle", mids))
        six = [label(c) for c in SIX if n in c]
        said6 = f.get("Six-cycle", f.get("Six-cycle, two paths", "")).split(" · ")
        if sorted(said6) != sorted(six): bad.append((n, "six", said6, six))
        if f.get("Eight-cycle") != [label(c) for c in EIGHT if n in c][0]: bad.append((n, "eight"))
        # 1 to 17s inward
        pos = 8 * n - 7; k, r = divmod(pos - 1, 16)
        txt = f["1 to 17s inward and outward"]
        ordn = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th"]
        want_in = ("9 of %s" % ordn[k]) if r == 8 else (("1 of 1st" if k == 0 else "17 of %s and 1 of %s" % (ordn[k - 1], ordn[k])))
        if want_in not in txt: bad.append((n, "inward", want_in, txt[:50]))
report("Each name and its relations: 8 up, 8 down, 9 less, 17 less, its bi-folding with before and after, forms beside, middle, six-cycles, eight-cycle, its place inward (17 names)",
       len(nb) == 34 and not bad, str(bad))

# each name, three scales ; eight 1 to 17s inward
bad = []
for n, a, b in re.findall(r"- \*\*n: (\d+)\*\*\n(?:  - [^\n]+\n){2}  - \*a\*: ([^\n]+)\n  - \*b\*: ([^\n]+)", src):
    n = int(n); pos = 8 * n - 7; k, r = divmod(pos - 1, 16)
    ordn = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th"]
    want = "9 of %s" % ordn[k] if r == 8 else ("1 of 1st" if k == 0 else "17 of %s, 1 of %s" % (ordn[k - 1], ordn[k]))
    if not a.startswith(want): bad.append((n, "a", a))
    wb = str((n + 7) // 8) + ":" if (n + 7) % 8 == 0 else "within %d to %d" % ((n + 7) // 8, (n + 7) // 8 + 1)
    if not b.startswith(wb): bad.append((n, "b", b, wb))
report("Each name, three scales: inward n is 8n − 7, outward 8m − 7 is m (17 names)", not bad, str(bad))
bad = []
inw = re.findall(r"1 to 17 inward: (\d)\w\w\*\*\n  - \*Spans, this scale\*: (\d+) to (\d+)\n  - \*Its 9, this scale\*: (\d+)\n  - \*Its 17, this scale\*: (\d+)", src)
for k, a, b, nine, sev in inw:
    k = int(k)
    if (int(a), int(b), int(nine), int(sev)) != (2 * k - 1, 2 * k + 1, 2 * k, 2 * k + 1): bad.append(k)
report("Eight 1 to 17s inward: each one's span, its 9 and its 17 at this scale", len(inw) == 8 and not bad, str(bad))
# two-sided, eight apart
bad = [(int(n), e) for n, e in re.findall(r"^\| (\d+) \| [^|]+ \| [^|]+ \| ([^|]+) \|$", src, re.M) if int(n) <= 17 and not (e.strip().startswith(str(int(n) + 8 if int(n) <= 8 else int(n) - 8)) or (int(n) == 17 and e.strip().startswith("1,")))]
report("Two-sided, each name: eight apart", not bad, str(bad))
# primes behind and ahead of twenty-four within nought to sixty
pr = [x for x in range(2, 60) if all(x % d for d in range(2, x))]
report("Nine primes behind twenty-four and eight ahead, to sixty", (len([x for x in pr if x < 24]), len([x for x in pr if x > 24])) == (9, 8))
# the code's words in the table of is-or-is-nots
cells = re.findall(r"^\| ([^|]*`[^|]*) \| [^|]+ \| [^|]+ \| [^|]+ \|$", src, re.M)
word_for_word, shortened = [], []
for c in cells:
    for q in re.findall(r"`([^`]+)`", c):
        (word_for_word if " ".join(q.split()) in " ".join(code.split()) else shortened).append(q)
print("          the code's words in 'Where each is-or-is-not stands': word for word in the code:", len(word_for_word), "; not word for word:", shortened)
print()
print("%d of %d same" % (sum(out), len(out)))
