"""A concept read by the code's lines: resolving by three is-or-is-nots, prior-existing, now-existing and same. Each case, all or none.

The concept is a suggesting, and likely incorrect as it is worded: this executing decides none of it.
Exhibit ONE's code, read from its file, no line changed. One self, one thing: a prior of +, of - or none, the code's
state; and none to three parities of its others, each +, - or 0.
Run: python3 incoming/V401atom/instruments/three_binaries_check.py Exhibit_ONE_Natural_Resolver_v401mgr.md

  prior  a self has a prior: is-or-is-not.
  now    its possibling is a parity: is-or-is-not. Its is-not: none of its others, each a 0, or two not same-as.
  same   its possibling is same-as its prior: is-or-is-not. It is by prior is and now is only.
"""
import re, sys, itertools, collections
src = open(sys.argv[1], encoding="utf-8").read()
code = re.search(r"```python\n(.*?)```", src, re.S).group(1)
ns = {}
exec(code, ns)
one = ns["_1_now_existing"]
S = "s"
forms = collections.defaultdict(set); n = 0; ex = True
for prior in (1, -1, None):
    for k in range(4):
        for given in itertools.product((1, -1, 0), repeat=k):
            n += 1
            vals = [v for v in given if v != 0]
            poss = None if not vals or len(set(vals)) > 1 else vals[0]
            P, N = prior is not None, poss is not None
            Sm = (P and N and poss == prior) if (P and N) else None
            out, nxt = one([(S, prior)] if P else [], [(S, v) for v in given])
            co, nx = dict(out).get(S), dict(nxt).get(S)
            co_k = "a 0" if co == 0 else "none" if co is None else "its next prior"
            nx_k = ("none" if nx is None else "its prior" if P and nx == prior else "the other one of two" if P else "its possibling's parity")
            forms[(P, N, Sm)].add((co_k, nx_k))
            # each parity exchanged for its other: the three is-or-is-nots and the form are as they were
            out2, nxt2 = one([(S, -prior)] if P else [], [(S, -v) for v in given])
            ex = ex and dict(out2).get(S) == (None if co is None else -co) and dict(nxt2).get(S) == (None if nx is None else -nx)
say = lambda b: "is" if b else "is-not" if b is not None else "by neither"
print("one self, one thing, cases:", n)
print("1 the three is-or-is-nots of each case, and what the lines return by them:")
for (P, N, Sm), v in sorted(forms.items(), key=lambda kv: (not kv[0][0], not kv[0][1], str(kv[0][2]))):
    for co_k, nx_k in sorted(v):
        print(f"    prior {say(P)} · now {say(N)} · same {say(Sm)} : its co-possibling {co_k} ; its next prior {nx_k}")
print("2 a self having a prior: by each form of the three, the lines return one thing and no second:", all(len(v) == 1 for k, v in forms.items() if k[0]))
print("  no prior, the code's state: by now is, one thing; by now is-not, two: a 0 by two not same-as, and none by none of its others:",
      len(forms[(False, True, None)]) == 1 and forms[(False, False, None)] == {("a 0", "none"), ("none", "none")})
print("3 the forms of the three in the lines:", len(forms), "of eight; same is-or-is-not is by prior is and now is, and by no other form")
print("4 each parity exchanged for its other, each case: the three and what is returned are as they were, each parity its other:", ex)
names = {"prior": "_3_now_co_observing", "now": "_2_now_possibling", "same": "_12_next_co_same_existing"}
body = code[code.index("def _1_now_existing"):code.index("def _9_next_co_discovering")]
print("5 in 1-now-existing's lines: a self's prior is read from", names["prior"], "; its others' parities from", names["now"],
      "; and the line of same-as makes", names["same"], ":", all(v in body for v in names.values()))
print("6 names having discovering in 1-now-existing's lines:", sorted(set(re.findall(r"_\d+_\w*discovering", body))) or "none")
