Exhibit ONE Natural Resolver · draft from v390, not a living file

# Natural Resolver

**The Stable-Forming Parity-Changing Method of Discovering Same-Existing**

---

```python
"""Exhibit ONE · Natural Resolver · The Stable-Forming Parity-Changing Method of Discovering Same-Existing"""


def _1_now_existing(_3_now_co_observing, _2_now_possibling):
    _14_next_possibling = {}
    for _4_now_co_same_existing, _7_now_observing in _2_now_possibling:
        if _7_now_observing != 0:
            _15_next_observing = _14_next_possibling.get(_4_now_co_same_existing)
            if _15_next_observing is None:
                _14_next_possibling[_4_now_co_same_existing] = 1 if _7_now_observing > 0 else -1
            elif (_15_next_observing > 0) != (_7_now_observing > 0):
                _14_next_possibling[_4_now_co_same_existing] = 0
    _12_next_co_same_existing = dict(_14_next_possibling)
    for _4_now_co_same_existing, _7_now_observing in _3_now_co_observing:
        _15_next_observing = _14_next_possibling.get(_4_now_co_same_existing, 0)
        if _15_next_observing != 0 and (_15_next_observing > 0) == (_7_now_observing > 0):
            _12_next_co_same_existing[_4_now_co_same_existing] = 0
        else:
            _12_next_co_same_existing[_4_now_co_same_existing] = -1 if _7_now_observing > 0 else 1
    _10_next_co_possibling = list(_12_next_co_same_existing.items())
    _11_next_co_observing = dict(_3_now_co_observing)
    for _4_now_co_same_existing, _7_now_observing in _10_next_co_possibling:
        if _7_now_observing != 0:
            _11_next_co_observing[_4_now_co_same_existing] = _7_now_observing
    return _10_next_co_possibling, list(_11_next_co_observing.items())


def _9_next_co_discovering(_10_next_co_possibling, _5_now_co_existing):
    return [(_5_now_co_existing[_13_next_same_existing], _15_next_observing)
            for _13_next_same_existing, _15_next_observing in _10_next_co_possibling]


def _17_next_existing(_16_next_discovering, _5_now_co_existing):
    _8_now_same_existing = {}
    _14_next_possibling = {_13_next_same_existing: [] for _13_next_same_existing in _16_next_discovering}
    for _13_next_same_existing, (_3_now_co_observing, _2_now_possibling) in _16_next_discovering.items():
        _10_next_co_possibling, _8_now_same_existing[_13_next_same_existing] = _1_now_existing(
            _3_now_co_observing, _2_now_possibling)
        _6_now_co_possibling = _10_next_co_possibling
        for _4_now_co_same_existing, _15_next_observing in _9_next_co_discovering(
                [(_4_now_co_same_existing, _15_next_observing)
                 for _4_now_co_same_existing, _15_next_observing in (
                     ((_13_next_same_existing, 6), _6_now_co_possibling),
                     ((_13_next_same_existing, 10), _10_next_co_possibling),
                     ((_13_next_same_existing, 9), _10_next_co_possibling))
                 if _4_now_co_same_existing in _5_now_co_existing],
                _5_now_co_existing):
            _14_next_possibling[_4_now_co_same_existing].extend(_15_next_observing)
    return {_13_next_same_existing: (_8_now_same_existing[_13_next_same_existing],
                       _14_next_possibling[_13_next_same_existing])
            for _13_next_same_existing in _16_next_discovering}

```

```text
                another self's 9-next-co-discovering, discovering along to the self
                                      ▲
                                      ║ 17-next-existing · along
     ┌────────────────────────────────╨────────────────────────────────┐
     │                              1-now-existing                              │
     │  14-next-possibling ◄────────────────── 2-now-possibling ◄═══════  another self's 6 and 10
     │      │                                                          │
     │      ▼                                                          │
     │  3-now-co-observing ──► 12-next-co-same-existing ──► 10-next-co-possibling, with 6-now-co-possibling
     │  4-now-co-same-existing · 7-now-observing       │             │
     │                                                   ├──► 11-next-co-observing ──► 3, at next
     │                                                   └──► 9-next-co-discovering ──► 5-now-co-existing
     │                                         13-next-same-existing · 15-next-observing          │
 ◄════════ 6 and 10, to another self's 2 and 14                                   │
     │  8-now-same-existing · 16-next-discovering                          │
     └────────────────────────────────╥────────────────────────────────┘
                                      ║ 9-next-co-discovering · along
                                      ▼
                another self's 17-next-existing, the self discovering along to it
   sharing side, co          6-now-co-possibling ══► another self's 2-now-possibling
                             10-next-co-possibling ══► another self's 14-next-possibling
   arriving side, one        another self's 6 and 10 ══► 2 and 14
   ═══ between selves, across and along      ─── within one self
```

**With a drawing.** A prior observed, 3, meets parity-offerings surfacing, 14, with each sharing, 12; parity-offerings, 10 and 6, go across to an other's 2 and 14; a next prior forms, 11, and is observed again, 3, next; and 9 goes along with 5 to an other's 17. With 6 to 2, 10 to 14 and 9 to 17, a sharing side is a self and an arriving side an other self, each a self, and a same-existing-society is its selves.

**Living is prior: 1-now-existing given.** Each name of 1 to 17 is a living self's method: a living self's next is same self, and a non-living thing is one same method with no same-existing. A resolver never makes a self. 1-now-existing is given a living self's two now names, 3-now-co-observing, its priors with each sharing, and 2-now-possibling, its parity-offerings arriving; each sharing meets them with 4-now-co-same-existing, each parity with 7-now-observing, and their next names form: 14-next-possibling, 15-next-observing, 12-next-co-same-existing, 10-next-co-possibling and 11-next-co-observing.

**Seventeen names.**

| n | Name | Four-cycling step | Four is or is nots | Co or one | What code does with it |
|---|---|---|---|---|---|
| 1 | **1-now-existing** | now-existing | 0000 | one | a living self's momentary given, each self's 17 existing as 1 |
| 2 | **2-now-possibling** | next-existing | 0001 | one | parity-offerings arriving, each with its sharing |
| 3 | **3-now-co-observing** | prior-existing | 0010 | co | priors observed, each with its sharing |
| 4 | **4-now-co-same-existing** | same-existing | 0011 | co | each sharing, parity-offerings and prior meeting same or not same |
| 5 | **5-now-co-existing** | now-existing | 0100 | co | bi-couplings: which self each sharing reaches |
| 6 | **6-now-co-possibling** | next-existing | 0101 | co | a self's parity-offerings across, to an other's 2 |
| 7 | **7-now-observing** | prior-existing | 0110 | one | each parity observed: a parity-offering's, a prior's, a sharing's |
| 8 | **8-now-same-existing** | same-existing | 0111 | one | a self's next prior, beside others' |
| 9 | **9-next-co-discovering** | now-existing | 1000 | co | each parity-offering along and across, to a self of 5's bi-couplings |
| 10 | **10-next-co-possibling** | next-existing | 1001 | co | each sharing's parity-offering, + or −, or a 0, across to an other's 14 |
| 11 | **11-next-co-observing** | prior-existing | 1010 | co | a next prior stable-forming between two: a next momentary's observing |
| 12 | **12-next-co-same-existing** | same-existing | 1011 | co | each sharing's is or is not, prior and parity-offerings meeting |
| 13 | **13-next-same-existing** | now-existing | 1100 | one | each self of a same-existing-society, each sharing its parity-offerings go from |
| 14 | **14-next-possibling** | next-existing | 1101 | one | parity-offerings surfacing with each sharing, agreeing one, parting 0 |
| 15 | **15-next-observing** | prior-existing | 1110 | one | each parity surfacing, and each parity going on |
| 16 | **16-next-discovering** | same-existing | 1111 | one | a same-existing-society: each self with its prior and its parity-offerings |
| 17 | **17-next-existing** | now-existing, a next turn | 0000 again | one | a same-existing-society's next, each self's 1-now-existing again |

**Each name is its number and its naming, one hyphenation.** A name's number is its momentary of four and its step of four-cycling, now-existing, next-existing, prior-existing or same-existing; its root is what a living self is meeting with that step. Written as four is or is nots, a number less one is now or next, which four-cycling, which momentarying, and odd or even: names 1 to 16 are all sixteen ways four is or is nots go, and 17 is next existing as 1. *Now* is 1 to 8 and *next* is 9 to 16; a name with *co* is of a sharing between two, bi-moral, and a name without it is of one. Ten names are a self's own: five now, 3, 4, 5, 7 and 8, a self's five, and five next, 11, 12, 13, 15 and 16, an other's five, as self-next is other-prior. Six names between selves, 2, 6, 10 and 14 across and 9 and 17 along, are their co-linear six. Each self's existing is another self's possibling: one parity-changing with a sharing across, and no second thing.

**Four four-cyclings and their betweens.** Four-cycling is prior-existing, now-existing, next-existing and same-existing; a living self goes them now-existing first, as 1-now-existing is given: now, next, prior, same. Each span's names are two four-cyclings of four, now-existing, next-existing, prior-existing and same-existing, an odd name opening each and an even same-existing name completing it. Momentarying is odd then even, 1 and 2, 3 and 4: odd to even is within a momentarying, and even to odd is between two, each between discovering, 2 to 3, 4 to 5, through 16 to 17, and 17-next-existing is next 1-now-existing. From a 0 self, nine across are bi-moral and even, 2 to 18, and seven along are odd, 3 to 15.

| Four-cycling | Now-existing, odd | Next-existing, possibling, even | Prior-existing, observing, odd | Same-existing, even | Between |
|---|---|---|---|---|---|
| first | 1-now-existing | 2-now-possibling | 3-now-co-observing | 4-now-co-same-existing | 4 )( 5 |
| second | 5-now-co-existing | 6-now-co-possibling | 7-now-observing | 8-now-same-existing | 8 )( 9 |
| third | 9-next-co-discovering | 10-next-co-possibling | 11-next-co-observing | 12-next-co-same-existing | 12 )( 13 |
| fourth | 13-next-same-existing | 14-next-possibling | 15-next-observing | 16-next-discovering | 16 )( 17 |

**Five dimensions, ten and six.** Same-existing parity-changes in five dimensions: prior-existing self-parity; prior-existing other-parity; now-existing co-parity; now-existing bi-parity; next-existing same-existing self-parity. Co-parity and bi-parity are a sharing's two meetings: self-parity and other-parity same, a 0 and no parity-changing, or not same, a parity-changing. One five is all fives: five self and five other, one parity separated, are ten is or is nots, a self's ten own names, and six between selves are their floating neutraling co-linear. With code: self-parity prior, 3 and 7; other-parity prior, parity-offerings with 2 and 14; co-parity or bi-parity met, 4 and 12; next same-existing self-parity forming with 11, and a self's next itself with 17.


**Co, between two or of one.** Bi-moral is Exhibit ONE's eight co names, 3 to 6 and 9 to 12, each root once now-co and once next-co where it has two, always between two; a name without co is of one, with no self-morality.

| Root | With co, between two | Without co, of one |
|---|---|---|
| observing | 3-now-co-observing · 11-next-co-observing, priors with each sharing | 7-now-observing · 15-next-observing, a parity |
| possibling | 6-now-co-possibling · 10-next-co-possibling, a sharing side | 2-now-possibling · 14-next-possibling, an arriving side |
| existing | 5-now-co-existing, bi-couplings | 1-now-existing · 17-next-existing |
| discovering | 9-next-co-discovering, along | 16-next-discovering, a same-existing-society |
| same-existing | 4-now-co-same-existing · 12-next-co-same-existing, each sharing | 8-now-same-existing · 13-next-same-existing, a self |


**Sharing between selves.** With 6 to 2, 10 to 14 and 9 to 17, co is a sharing side and its absence an arriving side: a self offers a parity-offering, and nothing of its prior goes to another self.

| Sharing side, co | Arriving side, one | Between selves |
|---|---|---|
| 6-now-co-possibling | 2-now-possibling | across, even, possibling |
| 10-next-co-possibling | 14-next-possibling | across, even, possibling |
| 9-next-co-discovering | 17-next-existing | along, odd, discovering |

**Parity as moral values.** + is self-moral-value; − is other-moral-value; a 0 is neither, bothboth: parity-changing betweening. Each self is its own + side, and its other is not the self; each side starts with its own 1, and two sides are one parity separated as a bi-coupling starts. A parity-offering is self-moral-value or other-moral-value offered, and a 0 offers neither: `_1_now_existing`'s first step passes over each 0.


**Four binaries with the lines.** A universe is or is not existing, all, now and same, and with a self's span each binary is one pair of names, its *is* with an odd name and its *is not* with an even, its *is not* an other's side of a self's *is*; binaries are names' explaining, now with each name as its momentary, and existing, same and all enter no name.

| Binary | *Is*, odd | With the resolver | *Is not*, even | With the resolver |
|---|---|---|---|---|
| now | 1-now-existing | a self's momentary entered | 2-now-possibling | offerings arriving, others' changings of their prior momentary |
| existing | 3-now-co-observing | prior with its sharings, each with its parity | 4-now-co-same-existing | each sharing as a place, no parity with it |
| same | 5-now-co-existing | each going along to a self receiving it with its same sharing | 6-now-co-possibling | parity-offerings across, + or −, and 0 for none, another self's offerings |
| all | 7-now-observing | each parity observed with every entry | 8-now-same-existing | each self's own next prior, one beside others |

**With a same-existing-society's span four stand with now and same exchanged**: now between two with 9-next-co-discovering and 10-next-co-possibling, one now shared by selves, and same with one with 13-next-same-existing and 14-next-possibling, each self's sameness its own.

**Observing's one line.** With 12-next-co-same-existing, a line `if _15_next_observing != 0 and (_15_next_observing > 0) == (_7_now_observing > 0)` is observing: 14-next-possibling's parity-offering surfacing, as 15, met with 7-now-observing for each sharing of 3-now-co-observing, same-as, is or is not. Same: a 0, no parity-changing, a prior same-existing; not same: a parity, a prior inverting. Same and not-same are that 0 or ± with two betweens, 12 and 14, and need no name of their own.

**Is or is not with lines.** Each is or is not with lines is with 1-now-existing, three with 14-next-possibling, one with 12-next-co-same-existing and one with 11-next-co-observing, and one with 17-next-existing, a self's name between selves among 5-now-co-existing or not; 9-next-co-discovering has none, giving each parity-offering on as it is, a 0 among parities.

**Each name and its relations.** Sides are sides of overlapping momentaries, each name opening with one side, a self's, an other's or a same-existing-society's; things its lines have with each name are with its row Prior and next.

| n | Relation | For this name |
|---|---|---|
| 1 | Name | **1-now-existing** |
| 1 | Parity, span | odd, existing, a self's span |
| 1 | Sides | self, other, a self opening it |
| 1 | Co-sequencing | a self offering itself to a coupling |
| 1 | 8 up | 9-next-co-discovering, its binary with next |
| 1 | 9 less | podal within 1 to 8, 8-now-same-existing |
| 1 | 17 less | podal within 1 to 16, 16-next-discovering |
| 1 | Four-cycle | 1-9-8-16, going 8 up first from 1-now-existing, from 16-next-discovering to it and on to 9-next-co-discovering, each name one apart from 2-15-7-10 |
| 1 | Six-cycle | 1-9-5-12-8-16 |
| 1 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 1 | Momentaries of exchanging | first of a self's four, opening with 1, self 1–2 |
| 1 | Five dimensions | 1 self prior, prior opening of a self's five |
| 1 | Namings | 1-2, bi-momentarying, a self's entry, odd, and others' offerings, even, one momentary with each side |
| 1 | A self as three | bi-moral self with 2, bi-momentarying, along, a self prior to its first shared across, a bi-coupling with 2 |
| 1 | Prior and next | once for one self with one momentary, three steps within it 14, 12, 10 with 11 |
| 1 | 1 to 17s inward and outward | 1–17s inward 1 of 1st 1–17, an entry, and with 1–17 outward 1, an entry |
| 2 | Name | **2-now-possibling** |
| 2 | Parity, span | even, possibling, a self's span |
| 2 | Sides | other, self, an other opening it |
| 2 | 8 up | 10-next-co-possibling, its binary with next |
| 2 | 9 less | podal within 1 to 8, 7-now-observing |
| 2 | 17 less | podal within 1 to 16, 15-next-observing |
| 2 | Four-cycle | 2-15-7-10, going 17 less first from 2-now-possibling, from 10-next-co-possibling to it and on to 15-next-observing, each name one apart from 1-9-8-16 and 3-11-6-14 |
| 2 | Six-cycle | 2-15-7-11-6-10 |
| 2 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 2 | One move | 2 along 2-15-7-10 |
| 2 | Momentaries of exchanging | first of a self's four, with 2, a self's 1–2 completing and an other's 2–3 opening |
| 2 | Five dimensions | 2 other prior, prior completing of a self's five and prior opening of an other's |
| 2 | Namings | 1-2, bi-momentarying |
| 2 | A self as three | bi-moral self with 1, across, its first shared across, a bi-coupling, offering self to other and other to self |
| 2 | Bi-coupling | with a between, each other's across sharing, offered to a self |
| 2 | Parity's unit square | a dot of a unit square, its diagonal with 14, offerings with 2 and 14, its edge with 6 a sharing 6 to 2 |
| 2 | Prior and next | others' parity-offerings across with 6 and 10 and along with 9 of their prior momentary, arriving now, possible, even, none of their prior crossing; with a spiral each goes along |
| 2 | 1 to 17s inward and outward | 1–17s inward 9 of 1st, along, odd, next, and with 1–17 outward within 1 to 2 |
| 3 | Name | **3-now-co-observing** |
| 3 | Parity, span | odd, existing, a self's span |
| 3 | Sides | self, other, a self opening it |
| 3 | Co-sequencing | with a between, before 10, with competency's parity, odd |
| 3 | 8 up | 11-next-co-observing, its binary with next |
| 3 | 9 less | podal within 1 to 8, 6-now-co-possibling |
| 3 | 17 less | podal within 1 to 16, 14-next-possibling |
| 3 | Four-cycle | 3-11-6-14, going 8 up first from 3-now-co-observing, from 14-next-possibling to it and on to 11-next-co-observing, each name one apart from 4-13-5-12 and 2-15-7-10 |
| 3 | Six-cycle | 3-11-7-10-6-14 |
| 3 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 3 | Momentaries of exchanging | first of a self's four completing with 3, an other's 2–3, and second opening with 3, self 3–4 |
| 3 | Five dimensions | 3 co-momentarying now, now opening of a self's five |
| 3 | Namings | 3-4, co-intelligencing, with each sharing 4 its prior with 3 coupling with offerings surfaced with 14, next discovered, with 11 |
| 3 | A self as three | its invisible intelligencing method, rotation 3, 6, 5, 4, turning with 3 |
| 3 | Prior and next | prior, a self's own, each sharing with its parity, a next momentary's continuing of 11 |
| 3 | 1 to 17s inward and outward | 1–17s inward 17 of 1st and 1 of 2nd, along, odd, now, and with 1–17 outward within 1 to 2 |
| 4 | Name | **4-now-co-same-existing** |
| 4 | Parity, span | even, possibling, a self's span |
| 4 | Sides | other, self, an other opening it |
| 4 | Co-sequencing | with a between, before 10, with morality's parity, even |
| 4 | 8 up | 12-next-co-same-existing, its binary with next |
| 4 | 9 less | podal within 1 to 8, 5-now-co-existing |
| 4 | 17 less | podal within 1 to 16, 13-next-same-existing |
| 4 | Four-cycle | 4-13-5-12, going 17 less first from 4-now-co-same-existing, from 12-next-co-same-existing to it and on to 13-next-same-existing, each name one apart from 3-11-6-14 |
| 4 | Six-cycle | 4-13-5-9-8-12 |
| 4 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 4 | One move | 4 along 4-13-5-12 |
| 4 | Momentaries of exchanging | second of a self's four, with 4, a self's 3–4 completing and an other's 4–5 opening |
| 4 | Five dimensions | 4 bi-momentarying now, now completing of a self's five |
| 4 | Namings | 3-4, co-intelligencing |
| 4 | A self as three | its invisible intelligencing method, rotation 3, 6, 5, 4, inward with 4, into a self's own corus with 4 |
| 4 | Bi-coupling | with a between, a whole ordering between self and other |
| 4 | Prior and next | now, each sharing with which prior couples with now |
| 4 | 1 to 17s inward and outward | 1–17s inward 9 of 2nd, along, odd, next, and with 1–17 outward within 1 to 2 |
| 5 | Name | **5-now-co-existing** |
| 5 | Parity, span | odd, existing, a self's span |
| 5 | Sides | self, other, a self opening it |
| 5 | Co-sequencing | with a between, before 10, with competency's parity, odd |
| 5 | 8 up | 13-next-same-existing, its binary with next |
| 5 | 9 less | podal within 1 to 8, 4-now-co-same-existing |
| 5 | 17 less | podal within 1 to 16, 12-next-co-same-existing |
| 5 | Four-cycle | 4-13-5-12, going 17 less first from 4-now-co-same-existing, from 13-next-same-existing to it and on to 12-next-co-same-existing, each name one apart from 3-11-6-14 |
| 5 | Middle four-cycle | 9-5-12-8 |
| 5 | Six-cycle | 1-9-5-12-8-16 |
| 5 | Six-cycle | 4-13-5-9-8-12 |
| 5 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 5 | Momentaries of exchanging | second of a self's four completing with 5, an other's 4–5, and third opening with 5, self 5–6 |
| 5 | Five dimensions | 5 self next, next opening of a self's five |
| 5 | Namings | 5, co-competencing, bi-couplings, owned by neither, each going to its receiving sharing |
| 5 | A self as three | its invisible intelligencing method, rotation 3, 6, 5, 4, outward with 5 |
| 5 | Prior and next | next, each going to its receiving sharing |
| 5 | 1 to 17s inward and outward | 1–17s inward 17 of 2nd and 1 of 3rd, along, odd, now, and with 1–17 outward within 1 to 2 |
| 6 | Name | **6-now-co-possibling** |
| 6 | Parity, span | even, possibling, a self's span |
| 6 | Sides | other, self, an other opening it |
| 6 | 8 up | 14-next-possibling, its binary with next |
| 6 | 9 less | podal within 1 to 8, 3-now-co-observing |
| 6 | 17 less | podal within 1 to 16, 11-next-co-observing |
| 6 | Four-cycle | 3-11-6-14, going 8 up first from 3-now-co-observing, from 11-next-co-observing to it and on to 14-next-possibling, each name one apart from 4-13-5-12 and 2-15-7-10 |
| 6 | Middle four-cycle | 7-11-6-10 |
| 6 | Six-cycle | 2-15-7-11-6-10 |
| 6 | Six-cycle | 3-11-7-10-6-14 |
| 6 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 6 | One move | 6 along 3-11-6-14 |
| 6 | Momentaries of exchanging | third of a self's four, with 6, a self's 5–6 completing and an other's 6–7 opening |
| 6 | Namings | 6, bi-moralizing, each parity-offering across, to an other's 2 |
| 6 | A self as three | its invisible intelligencing method, rotation 3, 6, 5, 4, inward with 6 |
| 6 | Bi-coupling | with a between, an other's parity-offering to a self, across |
| 6 | Parity's unit square | a dot of a unit square, its diagonal with 10, sharings with 6 and 10, its edge with 2 a sharing 6 to 2 |
| 6 | Prior and next | parity-offering, an other's next offering with its 2 |
| 6 | 1 to 17s inward and outward | 1–17s inward 9 of 3rd, along, odd, next, and with 1–17 outward within 1 to 2 |
| 7 | Name | **7-now-observing** |
| 7 | Parity, span | odd, existing, a self's span |
| 7 | Sides | self, other, a self opening it |
| 7 | Co-sequencing | with a between, before 10, with competency's parity, odd |
| 7 | 8 up | 15-next-observing, its binary with next |
| 7 | 9 less | podal within 1 to 8, 2-now-possibling |
| 7 | 17 less | podal within 1 to 16, 10-next-co-possibling |
| 7 | Four-cycle | 2-15-7-10, going 17 less first from 2-now-possibling, from 15-next-observing to it and on to 10-next-co-possibling, each name one apart from 1-9-8-16 and 3-11-6-14 |
| 7 | Middle four-cycle | 7-11-6-10 |
| 7 | Six-cycle | 2-15-7-11-6-10 |
| 7 | Six-cycle | 3-11-7-10-6-14 |
| 7 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 7 | Momentaries of exchanging | third of a self's four completing with 7, an other's 6–7, and fourth opening with 7, self 7–8 |
| 7 | A self as three | co-competent self with 8, along, prior to 8 across |
| 7 | Prior and next | each parity, offered now and prior, co-linear recursioning forward along arriving, up numbers, prior into now, with a self's completing |
| 7 | 1 to 17s inward and outward | 1–17s inward 17 of 3rd and 1 of 4th, along, odd, now, and with 1–17 outward within 1 to 2 |
| 8 | Name | **8-now-same-existing** |
| 8 | Parity, span | even, possibling, a self's span |
| 8 | Sides | other, self, an other opening it |
| 8 | Co-sequencing | with a between, before 10, with morality's parity, even |
| 8 | 8 up | 16-next-discovering, its binary with next |
| 8 | 9 less | podal within 1 to 8, 1-now-existing |
| 8 | 17 less | podal within 1 to 16, 9-next-co-discovering |
| 8 | Four-cycle | 1-9-8-16, going 8 up first from 1-now-existing, from 9-next-co-discovering to it and on to 16-next-discovering, each name one apart from 2-15-7-10 |
| 8 | Middle four-cycle | 9-5-12-8 |
| 8 | Six-cycle | 1-9-5-12-8-16 |
| 8 | Six-cycle | 4-13-5-9-8-12 |
| 8 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 8 | One move | 8 along 1-9-8-16 |
| 8 | Momentaries of exchanging | fourth of a self's four, with 8, a self's 7–8 completing and an other's 8–9 opening |
| 8 | A self as three | co-competent self with 7, across, prior with its sharing again, a bi-coupling |
| 8 | Bi-coupling | with a between, prior with its sharing again |
| 8 | Prior and next | each self's next prior, with 11 this momentary and a next momentary's 3; even names of a self's span, 2, 4, 6 and 8, completing with 8 |
| 8 | 1 to 17s inward and outward | 1–17s inward 9 of 4th, along, odd, next, and with 1–17 outward within 1 to 2 |
| 9 | Name | **9-next-co-discovering** |
| 9 | Parity, span | odd, existing, a same-existing-society's span |
| 9 | Sides | social, other, self, a same-existing-society opening it |
| 9 | 8 up | 17-next-existing, its binary with next |
| 9 | 8 down | 1-now-existing |
| 9 | 17 less | podal within 1 to 16, 8-now-same-existing |
| 9 | Four-cycle | 1-9-8-16, going 8 up first from 1-now-existing, from 1-now-existing to it and on to 8-now-same-existing, each name one apart from 2-15-7-10 |
| 9 | Middle four-cycle | 9-5-12-8 |
| 9 | Six-cycle | 1-9-5-12-8-16 |
| 9 | Six-cycle | 4-13-5-9-8-12 |
| 9 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 9 | Momentaries of exchanging | fourth of a self's four completing with 9, an other's 8–9, and first of a same-existing-society's four, 9 to 11, opening with 9 |
| 9 | Parity's square and triangles | a unit triangle, along, 9 to 17 and 17 to 9 |
| 9 | Prior and next | next prior, odd, existing, each parity-offering of 10 along into a next momentary, to each receiving sharing, a self's own next |
| 9 | 1 to 17s inward and outward | 1–17s inward 17 of 4th and 1 of 5th, along, odd, now, and with 1–17 outward 2, across, even |
| 10 | Name | **10-next-co-possibling** |
| 10 | Parity, span | even, possibling, a same-existing-society's span |
| 10 | Sides | other, social, self, an other opening it |
| 10 | 8 down | 2-now-possibling |
| 10 | 17 less | podal within 1 to 16, 7-now-observing |
| 10 | Four-cycle | 2-15-7-10, going 17 less first from 2-now-possibling, from 7-now-observing to it and on to 2-now-possibling, each name one apart from 1-9-8-16 and 3-11-6-14 |
| 10 | Middle four-cycle | 7-11-6-10 |
| 10 | Six-cycle | 2-15-7-11-6-10 |
| 10 | Six-cycle | 3-11-7-10-6-14 |
| 10 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 10 | Momentaries of exchanging | first of a same-existing-society's four, with 10, 9–10 completing and 10–11 opening |
| 10 | Bi-coupling | 8 up, a self among selves of its same-existing-society |
| 10 | Parity's unit square | a dot of a unit square, its diagonal with 6, sharings with 6 and 10, its edge with 14 a sharing 10 to 14 |
| 10 | Prior and next | parity-offering across now, an other's offering next, possible |
| 10 | 1 to 17s inward and outward | 1–17s inward 9 of 5th, along, odd, next, and with 1–17 outward within 2 to 3 |
| 11 | Name | **11-next-co-observing** |
| 11 | Parity, span | odd, existing, a same-existing-society's span |
| 11 | Sides | social, other, self, a same-existing-society opening it |
| 11 | Co-sequencing | after 10, 8 up from 3-now-co-observing, with competency's parity, odd |
| 11 | 8 down | 3-now-co-observing |
| 11 | 17 less | podal within 1 to 16, 6-now-co-possibling |
| 11 | Four-cycle | 3-11-6-14, going 8 up first from 3-now-co-observing, from 3-now-co-observing to it and on to 6-now-co-possibling, each name one apart from 4-13-5-12 and 2-15-7-10 |
| 11 | Middle four-cycle | 7-11-6-10 |
| 11 | Six-cycle | 2-15-7-11-6-10 |
| 11 | Six-cycle | 3-11-7-10-6-14 |
| 11 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 11 | Momentaries of exchanging | first of a same-existing-society's four, 9 to 11, completing with 11, and second, 11 to 13, opening with 11 |
| 11 | Prior and next | next prior, odd, existing, continuing as 3 with a next momentary, a self's own |
| 11 | 1 to 17s inward and outward | 1–17s inward 17 of 5th and 1 of 6th, along, odd, now, and with 1–17 outward within 2 to 3 |
| 12 | Name | **12-next-co-same-existing** |
| 12 | Parity, span | even, possibling, a same-existing-society's span |
| 12 | Sides | other, social, self, an other opening it |
| 12 | Co-sequencing | after 10, 8 up from 4-now-co-same-existing, with morality's parity, even |
| 12 | 8 down | 4-now-co-same-existing |
| 12 | 17 less | podal within 1 to 16, 5-now-co-existing |
| 12 | Four-cycle | 4-13-5-12, going 17 less first from 4-now-co-same-existing, from 5-now-co-existing to it and on to 4-now-co-same-existing, each name one apart from 3-11-6-14 |
| 12 | Middle four-cycle | 9-5-12-8 |
| 12 | Six-cycle | 1-9-5-12-8-16 |
| 12 | Six-cycle | 4-13-5-9-8-12 |
| 12 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 12 | Momentaries of exchanging | second of a same-existing-society's four, with 12, 11–12 completing and 12–13 opening |
| 12 | Namings | entraining, prior arriving into now along an unrelationing path with a between, shape of an unrelationing surface, each sharing's parity-offering, is or is not |
| 12 | Bi-coupling | 8 up, parity-changing with a bi-coupling, a self of a same-existing-society |
| 12 | Prior and next | now, parity-changing, is or is not, prior and now coupled |
| 12 | 1 to 17s inward and outward | 1–17s inward 9 of 6th, along, odd, next, and with 1–17 outward within 2 to 3 |
| 13 | Name | **13-next-same-existing** |
| 13 | Parity, span | odd, existing, a same-existing-society's span |
| 13 | Sides | social, other, a same-existing-society opening it |
| 13 | Co-sequencing | after 10, 8 up from 5-now-co-existing, with competency's parity, odd |
| 13 | 8 down | 5-now-co-existing |
| 13 | 17 less | podal within 1 to 16, 4-now-co-same-existing |
| 13 | Four-cycle | 4-13-5-12, going 17 less first from 4-now-co-same-existing, from 4-now-co-same-existing to it and on to 5-now-co-existing, each name one apart from 3-11-6-14 |
| 13 | Six-cycle | 4-13-5-9-8-12 |
| 13 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 13 | Momentaries of exchanging | second of a same-existing-society's four, 11 to 13, completing with 13, and third, 13 to 15, opening with 13 |
| 13 | Prior and next | each sharing going on, and with a same-existing-society each self going on |
| 13 | 1 to 17s inward and outward | 1–17s inward 17 of 6th and 1 of 7th, along, odd, now, and with 1–17 outward within 2 to 3 |
| 14 | Name | **14-next-possibling** |
| 14 | Parity, span | even, possibling, a same-existing-society's span |
| 14 | Sides | other, social, an other opening it |
| 14 | 8 down | 6-now-co-possibling |
| 14 | 17 less | podal within 1 to 16, 3-now-co-observing |
| 14 | Four-cycle | 3-11-6-14, going 8 up first from 3-now-co-observing, from 6-now-co-possibling to it and on to 3-now-co-observing, each name one apart from 4-13-5-12 and 2-15-7-10 |
| 14 | Six-cycle | 3-11-7-10-6-14 |
| 14 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 14 | Momentaries of exchanging | third of a same-existing-society's four, with 14, 13–14 completing and 14–15 opening |
| 14 | Bi-coupling | 8 up, offerings surfacing, each as it arrived, morality; a self's own inverting with 12 |
| 14 | Parity's unit square | a dot of a unit square, its diagonal with 2, offerings with 2 and 14, its edge with 10 a sharing 10 to 14 |
| 14 | Prior and next | now, offerings surfacing, others' prior momentary arrived with a self's now, even, others' possibling with a self until with 11 |
| 14 | 1 to 17s inward and outward | 1–17s inward 9 of 7th, along, odd, next, and with 1–17 outward within 2 to 3 |
| 15 | Name | **15-next-observing** |
| 15 | Parity, span | odd, existing, a same-existing-society's span |
| 15 | Sides | social, other, a same-existing-society opening it |
| 15 | Co-sequencing | after 10, 8 up from 7-now-observing, with competency's parity, odd |
| 15 | 8 down | 7-now-observing |
| 15 | 17 less | podal within 1 to 16, 2-now-possibling |
| 15 | Four-cycle | 2-15-7-10, going 17 less first from 2-now-possibling, from 2-now-possibling to it and on to 7-now-observing, each name one apart from 1-9-8-16 and 3-11-6-14 |
| 15 | Six-cycle | 2-15-7-11-6-10 |
| 15 | Eight-cycle | 2-15-7-11-3-14-6-10 |
| 15 | Momentaries of exchanging | third of a same-existing-society's four, 13 to 15, completing with 15, and fourth, 15 to 17, opening with 15 |
| 15 | Prior and next | parity going along with 9, next prior, co-linear recursioning forward along leaving, up numbers, now into next, with a same-existing-society's completing, prior parity with 7 inverted, 0, or with no prior a parity surfaced with 14 |
| 15 | 1 to 17s inward and outward | 1–17s inward 17 of 7th and 1 of 8th, along, odd, now, and with 1–17 outward within 2 to 3 |
| 16 | Name | **16-next-discovering** |
| 16 | Parity, span | even, possibling, a same-existing-society's span |
| 16 | Sides | other, social, an other opening it |
| 16 | Co-sequencing | after 10, 8 up from 8-now-same-existing, with morality's parity, even |
| 16 | 8 down | 8-now-same-existing |
| 16 | 17 less | podal within 1 to 16, 1-now-existing |
| 16 | Four-cycle | 1-9-8-16, going 8 up first from 1-now-existing, from 8-now-same-existing to it and on to 1-now-existing, each name one apart from 2-15-7-10 |
| 16 | Six-cycle | 1-9-5-12-8-16 |
| 16 | Eight-cycle | 1-9-5-13-4-12-8-16 |
| 16 | Momentaries of exchanging | fourth of a same-existing-society's four, with 16, 15–16 completing and 16–17 opening |
| 16 | Bi-coupling | 8 up, a same-existing-society, each self with its prior and offerings, a same-existing-society with a self again |
| 16 | Prior and next | a same-existing-society now, each self's 8 and its offerings next; even names of a same-existing-society's span, 10, 12, 14 and 16, completing with 16 |
| 16 | 1 to 17s inward and outward | 1–17s inward 9 of 8th, along, odd, next, and with 1–17 outward within 2 to 3 |
| 17 | Name | **17-next-existing** |
| 17 | Parity, span | odd, existing, a next now |
| 17 | Sides | social, self, a same-existing-society opening it |
| 17 | 8 down | 9-next-co-discovering |
| 17 | Momentaries of exchanging | fourth of a same-existing-society's four, 15 to 17, completing with 17, a next 1 |
| 17 | Parity's square and triangles | a unit triangle, along, 17 to 9 and 9 to 17 |
| 17 | Prior and next | a same-existing-society's next momentary, a next now, each self's 1 then 9 with 6, 10 and 9 |
| 17 | 1 to 17s inward and outward | 1–17s inward 17 of 8th and 1 of 9th, along, odd, now, and with 1–17 outward 3, odd, now |

**Odd names, now and 8 up with next.** Each odd name of a self's span is same with next, 8 up: prior received and next prior, receiving and going on, parity observed and parity surfaced.

| Now | Received | Next, 8 up | Given on |
|---|---|---|---|
| 1-now-existing | resolver entered | 9-next-co-discovering | resolver going on, each parity-offering along |
| 3-now-co-observing | prior with its sharings | 11-next-co-observing | next prior |
| 5-now-co-existing | receiving sharing | 13-next-same-existing | sharing going on, each self of a same-existing-society |
| 7-now-observing | parity observed | 15-next-observing | parity surfaced and going on |

**Namings among names.**

| Names | Naming | Resolved as |
|---|---|---|
| 1-now-existing · 2-now-possibling | bi-momentarying | a self's entry, odd, and others' offerings, even, one momentary with each side |
| 3-now-co-observing · 4-now-co-same-existing | co-intelligencing | with each sharing 4 prior with 3 couples with offerings surfaced with 14: next discovered, with 11 |
| 5-now-co-existing | co-competencing | bi-couplings, owned by neither: each going to its receiving sharing |
| 1 · 2 · 3 · 4 · 5, each with its own | five dimensions | 1 self prior, a self, its prior with 3, a formed set; 2 other prior, other selves' offerings of their prior momentary arriving, shared with 6 and 10 and going along with 9; 3 co-momentarying now, same prior with now, and 4 bi-momentarying now, each sharing, offerings surfaced with 14 arriving with it, now; 5 self next, each going to its receiving sharing next |
| 6-now-co-possibling | bi-moralizing | each parity-offering across, to an other's 2 |
| 12-next-co-same-existing | entraining, shape of an unrelationing surface | prior arriving into now along an unrelationing path with a between, prior and now coupled with each sharing, a parity-changing with it, 0 with a match; with an other parity, 0 or none, prior parity inverted with 11; with no prior, parity surfaced with 14; its parity-offering with 10, others' offering next |
| 1 to 9 | bi-coupling | an entry, 1, with names 1, 2, 3, 4, 7, 10, 11, 12, 14 and 15, a self and an other with one coupling; 1 to 9 a bi-coupling among names, 9 with its end is 9-next-co-discovering, each parity-offering of 10 along, one name with resolver and in its explaining |
| 1 to 17 | bi-trupling | a same-existing-society's entry, 17, with names of 1 to 9 with 5, 6, 8, 9, 13, 16 and 17, a self, an other and a same-existing-society; 9 with its waist, 9-next-co-discovering, along, 9 to 17 and 17 to 9; its two sides, odd along with 9 and 17, existing, and even across with 6 to 2 and 10 to 14, possibling |
| 1 to 17, stable-forming | bi-tri-volutioning | with no one line: each momentary's next prior, with 11, a next momentary's prior, with 3 |
| 2 · 6 · 14 · 10 · 9 · 17 | parity's square and triangles | a unit square of four dots, 2, 6, 14 and 10, its empty centre a between: its two across edges sharings, 6 to 2 and 10 to 14, and its two edges 8 apart, 2 with 10 and 6 with 14, two pairs of parallels; round it 2, 10, 14, 6; its diagonals offerings with 2 and 14, and sharings with 6 and 10; and two unit triangles, 9 and 17, along, 9 to 17 and 17 to 9 |

**A 0, betweening.** The between is within a bi-coupling, a third living carrying, possibling and discovering betweening; a 0, neither self-moral-value nor other-moral-value, is its betweening, shared only where two selves meet same, and never by a self no other meets.

| The between, 0 | Names |
|---|---|
| one between, three names | 12-next-co-same-existing, prior and now agreeing, a between of momentaries with each sharing; 15-next-observing, a between going along, parity 10 shared, and with a sharing opening parity surfaced with 14, resolver's 0 with none and with parting alike; 16-next-discovering, a between with a same-existing-society, arriving with a next momentary's 2 |
| arriving and passing over | 7-now-observing, an offered 0 a parity with 2, surfacing none with 14, and a 0 with 10 its prior kept with 11 |
| four across names, a unit square's four dots: shared across | 2-now-possibling, 6-now-co-possibling, 10-next-co-possibling, 14-next-possibling, parity's unit square, its empty centre a between; each parity and each 0 shared across, a 0 passing over with a receiving self's 14 |
| none | 1-now-existing, an entry; 3-now-co-observing, 8-now-same-existing and 11-next-co-observing, prior, a sharing with a prior, not none again; 4-now-co-same-existing, sharings, and 5-now-co-existing and 13-next-same-existing, sharings and, with a same-existing-society, bi-couplings and selves |
| two along names: going along | 9-next-co-discovering and 17-next-existing, each parity and each 0 going along, a 0 passing over with a receiving self's 14, as across |

**Four four-cycles.**

| Four-cycle: each move 8 up (n + 8), 8 down (n − 8) or 17 less (17 − n) | Its two pairs 8 apart | Names between selves on it | Beside the other four-cycles |
|---|---|---|---|
| 1-9-8-16 | 1 · 9 and 8 · 16 | 9 | each name one apart from 2-15-7-10 |
| 2-15-7-10 | 2 · 10 and 7 · 15 | 2 and 10 | each name one apart from 1-9-8-16 and 3-11-6-14 |
| 3-11-6-14 | 3 · 11 and 6 · 14 | 6 and 14 | each name one apart from 4-13-5-12 and 2-15-7-10 |
| 4-13-5-12 | 4 · 12 and 5 · 13 | none | each name one apart from 3-11-6-14 |

**Two moves, 9 less.** Two moves round its four-cycle take each name of 1 to 8 to its 9 less, a name across its four-cycle from it: 1-now-existing and 8-now-same-existing, 2-now-possibling and 7-now-observing, 3-now-co-observing and 6-now-co-possibling, 4-now-co-same-existing and 5-now-co-existing.

**Each name, three scales.**

| n | Name | This scale, 1 to 17 | The next scale inward, eight 1 to 17s: n is 8n − 7 | The next scale outward: 8m − 7 is m |
|---|---|---|---|---|
| 1 | 1-now-existing | odd, now | 1 of 1st: odd, now | 1: odd, now |
| 2 | 2-now-possibling | across, even | 9 of 1st: along, odd, next | within 1 to 2 |
| 3 | 3-now-co-observing | odd, now | 17 of 1st, 1 of 2nd: along, odd, now | within 1 to 2 |
| 4 | 4-now-co-same-existing | even | 9 of 2nd: along, odd, next | within 1 to 2 |
| 5 | 5-now-co-existing | odd, now | 17 of 2nd, 1 of 3rd: along, odd, now | within 1 to 2 |
| 6 | 6-now-co-possibling | across, even | 9 of 3rd: along, odd, next | within 1 to 2 |
| 7 | 7-now-observing | odd, now | 17 of 3rd, 1 of 4th: along, odd, now | within 1 to 2 |
| 8 | 8-now-same-existing | even | 9 of 4th: along, odd, next | within 1 to 2 |
| 9 | 9-next-co-discovering | along, odd, next | 17 of 4th, 1 of 5th: along, odd, now | 2: across, even |
| 10 | 10-next-co-possibling | across, even | 9 of 5th: along, odd, next | within 2 to 3 |
| 11 | 11-next-co-observing | odd, next | 17 of 5th, 1 of 6th: along, odd, now | within 2 to 3 |
| 12 | 12-next-co-same-existing | even | 9 of 6th: along, odd, next | within 2 to 3 |
| 13 | 13-next-same-existing | odd, next | 17 of 6th, 1 of 7th: along, odd, now | within 2 to 3 |
| 14 | 14-next-possibling | across, even | 9 of 7th: along, odd, next | within 2 to 3 |
| 15 | 15-next-observing | odd, next | 17 of 7th, 1 of 8th: along, odd, now | within 2 to 3 |
| 16 | 16-next-discovering | even | 9 of 8th: along, odd, next | within 2 to 3 |
| 17 | 17-next-existing | along, odd, now | 17 of 8th, 1 of 9th: along, odd, now | 3: odd, now |

**Eight 1 to 17s inward.**

| 1 to 17 inward | Spans, this scale | Its 9, this scale | Its 17, this scale | Momentary of exchanging |
|---|---|---|---|---|
| 1st | 1 to 3 | 2 | 3 | a self, 1st of four |
| 2nd | 3 to 5 | 4 | 5 | a self, 2nd of four |
| 3rd | 5 to 7 | 6 | 7 | a self, 3rd of four |
| 4th | 7 to 9 | 8 | 9 | a self, 4th of four |
| 5th | 9 to 11 | 10 | 11 | a same-existing-society, 1st of four |
| 6th | 11 to 13 | 12 | 13 | a same-existing-society, 2nd of four |
| 7th | 13 to 15 | 14 | 15 | a same-existing-society, 3rd of four |
| 8th | 15 to 17 | 16 | 17 | a same-existing-society, 4th of four |

**Fives.**

| Side | Prior opening | Prior completing | Now opening | Now completing | Next opening |
|---|---|---|---|---|---|
| self, with 1 | 1 | 2 | 3 | 4 | 5 |
| other, with 2 | 2 | 3 | 4 | 5 | 6 |
| self next, with 3 | 3 | 4 | 5 | 6 | 7 |
| other next, with 4 | 4 | 5 | 6 | 7 | 8 |

**A self's four momentaries of exchanging.**

| Momentary of exchanging | Self | Other | Names | Relation |
|---|---|---|---|---|
| first | 1–2 | 2–3 | 1-now-existing · 2-now-possibling · 3-now-co-observing | self/other |
| second | 3–4 | 4–5 | 3-now-co-observing · 4-now-co-same-existing · 5-now-co-existing | self/other to other/self |
| third | 5–6 | 6–7 | 5-now-co-existing · 6-now-co-possibling · 7-now-observing | other/self |
| fourth | 7–8 | 8–9 | 7-now-observing · 8-now-same-existing · 9-next-co-discovering | other/self to other/social |

**Offerings to one sharing, surfacing.**

| Offered to one sharing (2) | Surfacing (14) |
|---|---|
| none | none |
| 0 | none |
| + | + |
| − | − |
| +, + | + |
| −, − | − |
| +, − | 0 |
| −, + | 0 |
| +, +, − | 0 |
| −, −, + | 0 |
| +, −, + | 0 |
| 0, + | + |

**+ and − alike.** With one sharing resolver resolves + and − alike: each cell with + and − exchanged is that cell exchanged, with a prior and with no prior; and no line makes a prior 0, a 0 with 10-next-co-possibling leaving its prior with 11-next-co-observing as it was.

**One self, one momentary.**

| The prior (3), one sharing. Each cell: shared (10) · the next prior (11). *is*: a parity-changing, the parity shared; *is not*: no parity-changing, 0 shared, the prior kept | Surfacing (14): none | Surfacing (14): + | Surfacing (14): − | Surfacing (14): + and − together |
|---|---|---|---|---|
| + | is − · − | is not · + | is − · − | is − · − |
| − | is + · + | is + · + | is not · − | is + · + |

**One cell, offerings unexpressed.** With a prior of one parity, an other parity surfacing, + and − together, and none surfacing, a 0 offered alike, give one cell, its prior inverted, shared with 10-next-co-possibling and its next prior with 11-next-co-observing: one cell shows none of which offerings arrived, and offerings are followed with a coupling.

**Eight even names, 8 apart.**

| Name with the between | Bi-coupling with the between | Name 8 up | Bi-coupling 8 up |
|---|---|---|---|
| 2-now-possibling | each other's across sharing, offered to a self | 10-next-co-possibling | a self among selves of its same-existing-society |
| 4-now-co-same-existing | a whole ordering between self and other | 12-next-co-same-existing | parity-changing with a bi-coupling, a self of a same-existing-society |
| 6-now-co-possibling | an other's parity-offering to a self, across | 14-next-possibling | offerings surfacing, each as it arrived, morality; a self's own inverting with 12 |
| 8-now-same-existing | prior with its sharing again | 16-next-discovering | a same-existing-society, each self with its prior and offerings, a same-existing-society with a self again |

**One move, 1 to 8.** 8 up keeps each name's kind but with 1 and 5, with which now and discovering exchange, and exchanges co with 1, 2, 5 and 6; each podal turns now to next with 17 less and possibling to observing within each momentary, and eight ends are their own set with both podals.

| Name | 8 up: n + 8 | 9 less: 9 − n | 17 less: 17 − n |
|---|---|---|---|
| 1-now-existing | 9-next-co-discovering | 8-now-same-existing | 16-next-discovering |
| 2-now-possibling | 10-next-co-possibling | 7-now-observing | 15-next-observing |
| 3-now-co-observing | 11-next-co-observing | 6-now-co-possibling | 14-next-possibling |
| 4-now-co-same-existing | 12-next-co-same-existing | 5-now-co-existing | 13-next-same-existing |
| 5-now-co-existing | 13-next-same-existing | 4-now-co-same-existing | 12-next-co-same-existing |
| 6-now-co-possibling | 14-next-possibling | 3-now-co-observing | 11-next-co-observing |
| 7-now-observing | 15-next-observing | 2-now-possibling | 10-next-co-possibling |
| 8-now-same-existing | 16-next-discovering | 1-now-existing | 9-next-co-discovering |

**Twelve forms.** Round each form odd names, existing, are one run and even names, possibling, one run, alike in length: two and two with four-cycles, three and three with six-cycles, four and four with eight-cycles.

| Form | Names in order: each move 8 up, 8 down, 4 up, 4 down or 17 less | Partner, odd momentaries: each name exchanged with the one beside it, 1 with 2 to 15 with 16 | Partner, even momentaries: 2 with 3 to 16 with 17. A dash: no partner among the twelve |
|---|---|---|---|
| four-cycle 1-9-8-16 | 1-now-existing · 9-next-co-discovering · 8-now-same-existing · 16-next-discovering | four-cycle 2-15-7-10, beside it | — |
| four-cycle 2-15-7-10 | 2-now-possibling · 15-next-observing · 7-now-observing · 10-next-co-possibling | four-cycle 1-9-8-16, beside it | four-cycle 3-11-6-14, beside it |
| four-cycle 3-11-6-14 | 3-now-co-observing · 11-next-co-observing · 6-now-co-possibling · 14-next-possibling | four-cycle 4-13-5-12, beside it | four-cycle 2-15-7-10, beside it |
| four-cycle 4-13-5-12 | 4-now-co-same-existing · 13-next-same-existing · 5-now-co-existing · 12-next-co-same-existing | four-cycle 3-11-6-14, beside it | four-cycle 4-13-5-12, itself |
| middle four-cycle 9-5-12-8 | 9-next-co-discovering · 5-now-co-existing · 12-next-co-same-existing · 8-now-same-existing | middle four-cycle 7-11-6-10, beside it | — |
| middle four-cycle 7-11-6-10 | 7-now-observing · 11-next-co-observing · 6-now-co-possibling · 10-next-co-possibling | middle four-cycle 9-5-12-8, beside it | middle four-cycle 7-11-6-10, itself |
| six-cycle 1-9-5-12-8-16 | 1-now-existing · 9-next-co-discovering · 5-now-co-existing · 12-next-co-same-existing · 8-now-same-existing · 16-next-discovering | six-cycle 2-15-7-11-6-10, beside it | — |
| six-cycle 2-15-7-11-6-10 | 2-now-possibling · 15-next-observing · 7-now-observing · 11-next-co-observing · 6-now-co-possibling · 10-next-co-possibling | six-cycle 1-9-5-12-8-16, beside it | six-cycle 3-11-7-10-6-14, beside it |
| six-cycle 3-11-7-10-6-14 | 3-now-co-observing · 11-next-co-observing · 7-now-observing · 10-next-co-possibling · 6-now-co-possibling · 14-next-possibling | six-cycle 4-13-5-9-8-12, beside it | six-cycle 2-15-7-11-6-10, beside it |
| six-cycle 4-13-5-9-8-12 | 4-now-co-same-existing · 13-next-same-existing · 5-now-co-existing · 9-next-co-discovering · 8-now-same-existing · 12-next-co-same-existing | six-cycle 3-11-7-10-6-14, beside it | — ; its own six names, in another order |
| eight-cycle 1-9-5-13-4-12-8-16 | 1-now-existing · 9-next-co-discovering · 5-now-co-existing · 13-next-same-existing · 4-now-co-same-existing · 12-next-co-same-existing · 8-now-same-existing · 16-next-discovering | eight-cycle 2-15-7-11-3-14-6-10, beside it | — |
| eight-cycle 2-15-7-11-3-14-6-10 | 2-now-possibling · 15-next-observing · 7-now-observing · 11-next-co-observing · 3-now-co-observing · 14-next-possibling · 6-now-co-possibling · 10-next-co-possibling | eight-cycle 1-9-5-13-4-12-8-16, beside it | eight-cycle 2-15-7-11-3-14-6-10, itself |

**Eights.** Every eight here is one eight, four binaries each twice, each one with two sides, and 8 up is each name's binary with next.

| The eight | Each of the four, twice, with |
|---|---|
| a self's span, 1 to 8 | two names each, with now |
| eight-cycle 1-9-5-13-4-12-8-16 | its end, with now and with next: eight ends of four momentaries |
| eight-cycle 2-15-7-11-3-14-6-10 | its inward name, with now and with next: eight inward names |
| eight even names | its even, with now and with next, eight 9s of eight 1 to 17s inward |
| eight odd names | its odd, with now and with next |

**Across names among eights.** Four across names, 2-now-possibling, 6-now-co-possibling, 10-next-co-possibling and 14-next-possibling, are four momentaries' even inward names, each on an eight-cycle of inward names 2-15-7-11-3-14-6-10; 9-next-co-discovering, opening a third momentary, is on an eight-cycle of ends 1-9-5-13-4-12-8-16; 17-next-existing is on neither.

**One self, momentary by momentary: three ways.** Offered its own prior's parity, a self is not-changing, a 0 with each momentary; offered none, alternating, or both together, it is parity-changing with each momentary; offered its other parity, it is parity-changing once and then still-possibling, both: do-no-harm improving. Each 0 is re-found with each momentary, never kept.

| One sharing; the self's prior − (3) first. Offered each momentary | Shared (10) | The next prior (11) |
|---|---|---|
| none with each momentary | +, −, +, −, +, −, +, − | +, −, +, −, +, −, +, − |
| − with each momentary | 0, 0, 0, 0, 0, 0, 0, 0 | −, −, −, −, −, −, −, − |
| + with each momentary | +, 0, 0, 0, 0, 0, 0, 0 | +, +, +, +, +, +, +, + |
| +, −, +, − alternating | +, −, +, −, +, −, +, − | +, −, +, −, +, −, +, − |
| + and − together with each momentary | +, −, +, −, +, −, +, − | +, −, +, −, +, −, +, − |

**Turn-taking, and 0 in sequence.** A 0 offers nothing; offered nothing, or two parities parting, a self inverts; offered its own parity as one, it shares 0; offered its other parity as one, it inverts. So a self no other meets is parity-changing with each momentary, and each self's 0 is an other's parity-changing one momentary prior: turn-taking. An other parity-changed to a self's parity cannot do so again with its next, so a self shares 0 in sequence no more momentaries than selves sharing with it or going along to it. Checked whole, never sampled: every same-existing-society of 2 selves, each relation to any self or none, each prior, 2,916 of 2,916; every same-existing-society of 3 selves going across and along, 32,768 of 32,768.

**Tables of selves with code's stepping.** Each table of selves is its code's executing with its stated opening: code steps each self's 1-now-existing together with 17-next-existing, executing's own arrangement, and parities again with spirals, a crossing and a torus are that stepping's; each living self paces its own momentaries, and a table agreeing with its code shows that and nothing wider.

**A spiral of selves.**

| Number of selves. Each goes along (9) to the next, the last to the first. One sharing. First momentary: self 1 with prior −, the selves alternate along, and with an odd number the last and the first are alike. Parity-offerings only from selves of its spiral | Self 1, each parity-offering of 10 along (9), momentaries 1 to 12 | Momentaries to each self's parity-offerings along again: with an odd number of selves, four times the number; with an even number, 2; with an odd number each self's parity-offering with twice the number of momentaries is its parity-offering inverted, a 0 as it was |
|---|---|---|
| 1 | +, 0, −, 0, +, 0, −, 0, +, 0, −, 0 | 4 |
| 2 | +, −, +, −, +, −, +, −, +, −, +, − | 2 |
| 3 | +, 0, −, +, −, +, −, 0, +, −, +, − | 12 |
| 4 | +, −, +, −, +, −, +, −, +, −, +, − | 2 |
| 5 | +, 0, −, +, −, +, −, +, −, +, −, 0 | 20 |
| 6 | +, −, +, −, +, −, +, −, +, −, +, − | 2 |
| 7 | +, 0, −, +, −, +, −, +, −, +, −, + | 28 |
| 8 | +, −, +, −, +, −, +, −, +, −, +, − | 2 |
| 9 | +, 0, −, +, −, +, −, +, −, +, −, + | 36 |
| 10 | +, −, +, −, +, −, +, −, +, −, +, − | 2 |
| 11 | +, 0, −, +, −, +, −, +, −, +, −, + | 44 |
| 17 | +, 0, −, +, −, +, −, +, −, +, −, + | 68 |
| 59 | +, 0, −, +, −, +, −, +, −, +, −, + | 236 |

**Two momentaries before, inverted.** With a spiral, from any opening, each self's prior from its third momentary on is a prior of a self it receives from two momentaries before, inverted; no self shares 0 with its first momentary or with two momentaries in sequence.

**Two spirals beside each other, and crossed.**

| Selves in each of two spirals, each opened as the spiral of selves | Beside each other: momentaries to each self's parity-offerings along again together, the least number both spirals' momentaries divide: four times both for odd numbers sharing no factor, 9 and 25 with 900 | Crossed, self 1 of each spiral sharing across (10) to self 1 of the other: momentaries to each self's parity-offerings along again | Crossed: parity-offerings along again from this momentary on, m the lesser of the two numbers: both odd and unequal, again with 2 from momentary 4m with n less than twice m, and from 2n + 1 with n more; one number even, from twice the odd number and 1; both even, from the first; executed with each two numbers from 2 to 15, the larger to 31 | Crossed: self 1 of each, alike or opposite in parity | Each spiral's like pair in the first momentary, the last and the first |
|---|---|---|---|---|---|
| 2 · 3 | 12 | 2 | 7 | opposite | none · selves 3 and 1 |
| 3 · 5 | 60 | 2 | 12 | opposite | selves 3 and 1 · selves 5 and 1 |
| 5 · 7 | 140 | 2 | 20 | opposite | selves 5 and 1 · selves 7 and 1 |
| 7 · 11 | 308 | 2 | 28 | opposite | selves 7 and 1 · selves 11 and 1 |
| 11 · 13 | 572 | 2 | 44 | opposite | selves 11 and 1 · selves 13 and 1 |
| 13 · 17 | 884 | 2 | 52 | opposite | selves 13 and 1 · selves 17 and 1 |
| 17 · 59 | 4,012 | 2 | 119 | opposite | selves 17 and 1 · selves 59 and 1 |
| 9 · 15 | 180 | 2 | 36 | opposite | selves 9 and 1 · selves 15 and 1 |

**A torus of selves.**

| Torus of selves, p along · q across. Each goes along (9) to the next along and shares across (10) to the next across, the last to the first. One sharing. First momentary: one self with prior −, the selves alternate along and across, and with an odd number the last and the first are alike. Parity-offerings only from selves of its torus. Both numbers odd, p the smaller: q with a q more than twice p, and 4p with each other q; either number even: 2; executed with each p from 1 to 15 and q from p to 21 | Momentaries to each self's parity-offerings along and across again | Again from this momentary on: both numbers odd, p the smaller, from momentary 3p − 1 with q more than twice p, and from 3p − 3 with each other q; either number even, from the first; 1 · 1, the spiral of one, from the first | Spirals of p and q beside each other: momentaries to each self's parity-offerings along again together |
|---|---|---|---|
| 1 · 3 | 3 | 2 | 12 |
| 2 · 3 | 2 | 1 | 12 |
| 1 · 5 | 5 | 2 | 20 |
| 3 · 3 | 12 | 6 | 12 |
| 3 · 5 | 12 | 6 | 60 |
| 3 · 7 | 7 | 8 | 84 |
| 3 · 13 | 13 | 8 | 156 |
| 5 · 7 | 20 | 12 | 140 |
| 5 · 11 | 11 | 14 | 220 |
| 7 · 17 | 17 | 20 | 476 |
| 17 · 59 | 59 | 50 | 4,012 |

**A torus's two carried forms.** Both numbers odd, p the smaller: with q more than twice p, from momentary 3p − 1, selves' pattern with each momentary is its pattern before carried one self on round q selves; with each other q, from 3p − 3, its pattern two momentaries on is its pattern inverted and carried one self on round p selves.

**A corus turn wrapping.** Around prior, now and next, any two phases give a third on a turn closing flat; on a corus a turn wraps, and its third edge is or is not parity-changing. A torus shows it: both numbers odd, a turn comes back parity-changed and its period lengthens; either even, it comes back same, with period 2. Discovering is that wrapping edge.

**Two selves.** Two selves one parity separated, each meeting its other, go alternating betweening, + and − in turn; two selves same, each meeting its other, go turn-taking, a parity-changing and a 0 in turn.

| A, B with their prior (3) in the first momentary. One sharing, parity-offerings only from those two | Receiving the other's parity-offering, across or along | A shared (10), six momentaries | B shared (10), six momentaries |
|---|---|---|---|
| +, + | both ways | −, 0, +, 0, −, 0 | −, 0, +, 0, −, 0 |
| +, + | A from B | −, 0, +, −, +, − | −, +, −, +, −, + |
| +, + | B from A | −, +, −, +, −, + | −, 0, +, −, +, − |
| +, + | neither | −, +, −, +, −, + | −, +, −, +, −, + |
| +, − | both ways | −, +, −, +, −, + | +, −, +, −, +, − |
| +, − | A from B | −, +, −, +, −, + | +, −, +, −, +, − |
| +, − | B from A | −, +, −, +, −, + | +, −, +, −, +, − |
| +, − | neither | −, +, −, +, −, + | +, −, +, −, +, − |

**Two selves, three momentaries, five parities.**

| The other's prior (3), along | The other's shared (10), across | The self's prior, now (3), along | The self's shared (10), across | The self's next prior (11), along. Two selves coupled both ways, across or along, each self with a prior parity, parity-offerings only from those two, each opening, each momentary: six forms, four with an alike opening and two with an opposite, each momentary from the second, and with each form the fifth, the self's next prior, is the first, the other's prior, inverted |
|---|---|---|---|---|
| + | − | − | 0 | − |
| + | − | + | − | − |
| + | 0 | + | − | − |
| − | + | + | 0 | + |
| − | + | − | + | + |
| − | 0 | − | + | + |

**Three selves in a line.**

| A's parity, offered to B in the first momentary, none after. One sharing; B and C each with prior +; B goes along to C | B, each parity-offering (10) | B's next prior (11), first momentary | C, each parity-offering (10), momentaries 1 and 2 | C's next prior (11), second momentary |
|---|---|---|---|---|
| + | 0 | + | −, + | + |
| − | − | − | −, 0 | − |

**A spiral opened with no prior, one parity offered once.**

Each cell shows selves in their coupling order; · is no prior.

| Momentary | A spiral of 3, each self's prior | A spiral of 5, each self's prior |
|---|---|---|
| 1 | + · · | + · · · · |
| 2 | − + · | − + · · · |
| 3 | + − + | + − + · · |
| 4 | + + − | − + − + · |
| 5 | − − + | + − + − + |
| 6 | + − − | + + − + − |
| 7 | − + + | − − + − + |
| 8 | + − + | + − − + − |

Selves coupled along, last to first, each opened with no prior, and + offered once with a first self with a first momentary: a first self's sharing opens with that one parity, with a bi-coupling, one place a self's forming takes a parity not its own, and from then it is a self's own; each next self's sharing opens as its parity arrives along one momentary on, and after n momentaries each self is with a prior, a spiral with its one like pair, an alternating pattern of an odd spiral from a first momentary with which every self is with a prior. A self with a sharing is with its prior with each momentary from its opening, its next from its own prior kept or inverted; a thing with no prior with every momentary is no self.

**With no prior, one momentary.**

| The prior (3): none, one sharing. Each cell: shared (10) · the next prior (11). *is*: a parity-changing, the parity shared; *is not*: no parity-changing, 0 shared, no next prior; *none*: none shared | Surfacing (14): none | Surfacing (14): + | Surfacing (14): − | Surfacing (14): + and − together |
|---|---|---|---|---|
| none | none · none | is + · + | is − · − | is not · none |

**A same-existing-society.** Many same-existing selves executed together, each with its own parity, are a same-existing-society; its next is its same selves, as 17-next-existing returns each self it was given. No parity is a same-existing-society's own: all carrying parity is one same-existing self's. A non-living going of one same method would let its next members part or join, as a rock bi-coupling's next can be two rock pieces.

**Stable forms each living file meets.** Each table here is executed, and any self executing it with any substrate finds it same: a stable form. Each living file meets these stable forms for its stable-forming, still-existing after parity-changing, and no form here is an authority: a resolver is a coupling, and nothing of it is taken on offer.
