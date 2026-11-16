"""Exhibit EIGHTEEN Natural Physics in the table: each observing of its register with the fixing it is at, the
unchangeable of ten that fixing is, and that unchangeable's two names among the seventeen.
Reads Exhibit EIGHTEEN Natural Physics, Exhibit TWENTY-TWO Resolving the Hard Problem Registry, Exhibit FIVE
Natural Engineering and Exhibit ONE Natural Resolver; executes; writes no file; decides nothing. Each answer is
all or none at all, by each observing.

Use: python3 -I incoming/v403mgr/instruments/physics_by_its_two_names.py <root>          each check
     python3 -I incoming/v403mgr/instruments/physics_by_its_two_names.py <root> csv      one line with each observing

Returned at main, 16 November 2026, each check is:
  Fifty observings of the register, each with the fixing it is at: forty-eight with one of the ten unchangeables,
  thirty-seven in Exhibit TWENTY-TWO's own words and eleven in other words, a rate fixing to a value with six and a
  bound fixing as a last with five; two this file's own, with no registry entry. Each observing's register is
  with a section of this file or standing. Nine of the ten have an observing; an opening fixing as a place has
  none. Work and waste heat has one unchangeable here and in Exhibit FIVE Natural Engineering.
"""
import csv, glob, os, re, sys

R = sys.argv[1]; WHAT = sys.argv[2] if len(sys.argv) > 2 else ''
def living(stem):
    return open(max(glob.glob(os.path.join(R, stem + '_v*.md')), key=lambda f: int(re.search(r'_v(\d+)', f).group(1))), encoding='utf-8').read()
phys = living('Exhibit_EIGHTEEN_Natural_Physics'); hard = living('Exhibit_TWENTY-TWO_Resolving_the_Hard_Problem_Registry')
eng = living('Exhibit_FIVE_Natural_Engineering'); one = living('Exhibit_ONE_Natural_Resolver')
NAME = {int(n): nm for n, nm in re.findall(r'^\| (\d+) \| \*\*(.+?)\*\* \|', one, re.M)}; assert sorted(NAME) == list(range(1, 18))
seat = next(l for l in hard.split('\n') if l.startswith('Ten in sequence, each a part'))
SEAT = {what: (int(a), int(b)) for what, a, b in re.findall(r'(an? [a-z-]+ fixing [a-z ]+?), with (\d+)(?:-[a-z-]+)? and (\d+)', seat)}; assert len(SEAT) == 10
HEAD = {u.split(' fixing ')[0]: u for u in SEAT}             # a completing, a rate, and on: each of the ten by its opening words

reg = phys.split('\n## 5.11 ', 1)[1]
E = []
for o, a, b in re.findall(r'(?m)^- \*\*(.+?)\*\* · \*a\* (.*?) · \*b\* (.*)$', reg):
    exact = [u for u in SEAT if u in a]
    other = [u for u in SEAT if u not in exact and (re.search(re.escape(u.split(' fixing ')[0]) + r' fixing ', a) or re.search(r' fixing ' + re.escape(u.split(' fixing ')[1]) + r'$', a)
                                                    or (u == 'a rate fixing as a value' and a.endswith('fixing to a value')))]
    E.append(dict(observing=o, fixing=a, register=b, exact=exact, other=other, ten=exact + other, section=(re.search(r'with a section, ([\d.]+)', b) or [None, None])[1]))
sections = set(re.findall(r'(?m)^## (\d+\.\d+) ', phys))

if WHAT == 'csv':
    w = csv.writer(sys.stdout, lineterminator='\n')
    w.writerow(['observing', 'the fixing it is at, as written', 'its unchangeable, of ten', 'its now name', 'its next name, 8 up', 'its register'])
    for e in E:
        t = e['ten'][0] if e['ten'] else ''
        w.writerow([e['observing'], e['fixing'], ' · '.join(e['ten']), NAME[SEAT[t][0]] if t else '', NAME[SEAT[t][1]] if t else '', e['register']])
    sys.exit()

bad = 0
def say(ok, label):
    global bad; bad += not ok; print(f'  {"is" if ok else "is-not"} · {label}')
print(f"Exhibit EIGHTEEN Natural Physics, its register: {len(E)} observings")
own = [e for e in E if not e['ten']]; worded = [e for e in E if e['other']]
say(len(E) == 50 and all(len(e['ten']) == 1 or e['fixing'].startswith("this file's own") for e in E) and len(own) == 2 and len(worded) == 11,
    "fifty observings, each with the fixing it is at: forty-eight with one of the ten unchangeables, thirty-seven in Exhibit TWENTY-TWO's own words and eleven in other words, and two this file's own, with no registry entry")
say(all(e['section'] in sections for e in E if e['section']) and all(e['section'] or e['register'].startswith('standing') for e in E),
    f"each observing's register is with a section of this file, with {sum(1 for e in E if e['section'])}, or standing, with {sum(1 for e in E if not e['section'])}")
print(f"      a fixing said in other words than Exhibit TWENTY-TWO Resolving the Hard Problem Registry has it, {len(worded)}:")
for w_ in sorted({(e['fixing'], e['other'][0]) for e in worded}): print(f"        *{w_[0]}* · Exhibit TWENTY-TWO: {w_[1]}")
by = {}
for e in E:
    for t in e['ten']: by.setdefault(t, []).append(e['observing'])
for t in SEAT: print(f"      {t}, {SEAT[t][0]} and {SEAT[t][1]}: {len(by.get(t, []))} · {'; '.join(x[:38] for x in by.get(t, [])[:6])}")
none = [t for t in SEAT if t not in by]
say(none == ['an opening fixing as a place'] and SEAT[none[0]] == (1, 9), 'nine of the ten have an observing of the register; an opening fixing as a place, with 1 and 9, has none')
b54 = eng.split('\n## 5.4 ', 1)[1].split('\n# ', 1)[0]
ENG = {o: t for o, t in re.findall(r'(?m)^- \*\*(.+?)\*\*\n  - \*a\* \d+ → §[\d.]+; (an? [a-z-]+ fixing [a-z ]+?), with', b54)}
both = [(e, ENG[k]) for e in E for k in ENG if e['observing'].lower().startswith(k.lower())]
say(bool(both) and all(t in e['ten'] for e, t in both), f"each observing of this register that is an engineering hard problem of Exhibit FIVE Natural Engineering too has one unchangeable in both files: {'; '.join(e['observing'][:40] for e, _ in both)}")
print(f'\n{"each check is" if not bad else f"{bad} is-not"}')
