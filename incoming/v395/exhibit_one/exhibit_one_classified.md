# Exhibit ONE v391 — sentence classification for a reference tool

Source: `/home/claude/corus/Exhibit_ONE_Natural_Resolver_v391.md` (1212 lines, read-only). Reference: Natural Intelligence's new opening, 55 sentences (`opening_path47.txt`).

## 0. Scope and method

- In scope: every line outside the two fenced blocks (Python 11-90; the `text` drawing 92-114, also fenced) and not starting with `|`. Each line is split into sentence units; a bold lead label is its own unit. Units are keyed `line.k` (k = sentence within the line).
- Bullet lists come in two kinds. **Data lists** (bullets holding only names, numbers, ± values or cycles: e.g. spiral, torus, Two selves, One move, Twelve forms) are tables written as lists; their rows are treated like `|` rows (not classified) and counted as tables. **Gloss lists** (bullets carrying descriptive phrases: Code with each name, Co roots, the 17 per-name field lists, Odd names, Namings, Eight even names, Eights) are classified bullet by bullet. Their legends (`*a*:` lines) and captions are classified.
- Per-name fields (lines 241-507) are classified by field key with per-line exceptions; every line is listed in §2.
- Classes: **L** LABEL · **E** EXPLAIN · **I** INCOHERE · **R** REPEAT; **L+x** carries a label plus one other class and gets a minimal re-saying built only from words already in the file or the opening (chiefly *momentary → moment*).
- Words are counted as whitespace tokens holding a letter or digit, markdown stripped. Words the opening left out (sharing, receiving, inverting, agreeing/parting, inward/outward, dividing) are noted, never judged.

## 1. Sections in file order

Tables: P = pipe table, D = data list, G = gloss list; **E** = holds an executing, n = holds none.

| # | Bold label | Lines | Tables | Units | L | L+E | L+I | L+R | E | I | R |
|---|---|---|---|---|---|---|---|---|---|---|---|
| — | (code block, Python) | 11-90 | — | out of scope | | | | | | | |
| — | (drawing, fenced `text`) | 92-114 | — | out of scope | | | | | | | |
| 0 | Head (title, subtitle, opening paragraph) | 1-9 | 0 | 13 | 2 |  | 1 |  | 3 | 5 | 2 |
| 1 | A drawing. (caption after fenced drawing 92-114) | 116-116 | 0 | 3 | 2 |  |  |  |  |  | 1 |
| 2 | Seventeen names. | 118-158 | 2 (P·n G·n) | 20 | 15 | 2 | 3 |  |  |  |  |
| 3 | Two-sided, each name. | 160-180 | 1 (P·n) | 2 | 2 |  |  |  |  |  |  |
| 4 | Each name is its number and its naming, one hyphenation. | 182-182 | 0 | 3 | 1 |  |  |  |  |  | 2 |
| 5 | Four four-cyclings and their betweens. | 184-193 | 1 (P·n) | 6 | 1 | 1 | 1 |  | 1 |  | 2 |
| 6 | Co, between two or of one. | 195-205 | 1 (G·n) | 18 | 2 |  |  | 1 | 2 | 1 | 12 |
| 7 | Sharing between selves. | 207-213 | 1 (P·n) | 2 | 2 |  |  |  |  |  |  |
| 8 | Where each is-or-is-not stands. | 215-228 | 1 (P·n) | 4 | 3 |  |  |  |  |  | 1 |
| 9 | Same-existing through one momentary. | 230-237 | 1 (P·n) | 3 | 2 |  | 1 |  |  |  |  |
| 10 | Each name and its relations. (17 field lists) | 239-507 | 1 (G·n) | 254 | 20 |  | 1 |  | 11 | 74 | 148 |
| 11 | Odd names, now and 8 up with next. | 509-526 | 1 (G·n) | 21 |  |  |  |  | 2 | 1 | 18 |
| 12 | Namings among names. (incl. 'A between, 0' items) | 528-568 | 2 (G·n G·n) | 73 |  |  |  |  | 26 | 24 | 23 |
| 13 | Four bi-foldings. | 570-589 | 1 (D·n) | 6 | 4 |  |  |  |  | 1 | 1 |
| 14 | Two moves, 9 less. | 591-591 | 0 | 4 |  |  |  |  |  |  | 4 |
| 15 | Each name, three scales. | 593-682 | 1 (D·n) | 3 | 3 |  |  |  |  |  |  |
| 16 | Eight 1 to 17s inward. | 684-725 | 1 (D·n) | 1 | 1 |  |  |  |  |  |  |
| 17 | Fives. | 727-752 | 1 (D·n) | 3 | 1 |  | 1 |  | 1 |  |  |
| 18 | A self's four momentaries of exchanging. | 754-775 | 1 (D·n) | 1 |  |  | 1 |  |  |  |  |
| 19 | Parities to one sharing, surfacing. | 777-792 | 1 (P·E) | 1 | 1 |  |  |  |  |  |  |
| 20 | + and − alike. | 794-794 | 0 | 5 |  |  |  |  |  | 1 | 4 |
| 21 | One self, one momentary. | 796-809 | 1 (D·E) | 6 | 1 |  | 1 |  | 1 | 2 | 1 |
| 22 | One cell, four receivings. | 811-811 | 0 | 7 |  |  |  |  | 1 |  | 6 |
| 23 | Eight even names, 8 apart. | 813-830 | 1 (G·n) | 17 |  |  |  |  |  | 1 | 16 |
| 24 | One move, 1 to 8. | 832-865 | 1 (D·n) | 2 | 2 |  |  |  |  |  |  |
| 25 | Twelve forms. | 867-920 | 1 (D·n) | 9 | 2 |  | 3 |  | 1 | 2 | 1 |
| 26 | Eights. | 922-930 | 1 (G·n) | 11 |  |  |  |  | 6 | 1 | 4 |
| 27 | Across names among eights. | 932-932 | 0 | 6 |  |  |  |  |  | 1 | 5 |
| 28 | One self, momentary by momentary: three ways. | 934-942 | 1 (D·E) | 5 | 2 |  | 2 |  |  | 1 |  |
| 29 | Tables of selves with code's stepping. | 944-944 | 0 | 6 | 6 |  |  |  |  |  |  |
| 30 | A spiral of selves. | 946-965 | 1 (D·E) | 9 | 5 | 1 | 3 |  |  |  |  |
| 31 | Two momentaries before, inverting. | 967-967 | 0 | 4 |  |  |  |  | 1 | 3 |  |
| 32 | Two spirals beside each other, and bi-coupling across. | 969-1026 | 1 (D·E) | 7 | 3 |  | 4 |  |  |  |  |
| 33 | A torus of selves. | 1028-1079 | 1 (D·E) | 14 | 8 |  | 4 |  |  | 1 | 1 |
| 34 | A torus's two going forms. | 1081-1081 | 0 | 4 |  |  |  |  |  | 3 | 1 |
| 35 | Alike selves, a right spiral. | 1083-1093 | 1 (P·E) | 6 | 3 |  | 2 |  | 1 |  |  |
| 36 | Two selves. | 1095-1132 | 1 (D·E) | 6 | 5 |  | 1 |  |  |  |  |
| 37 | Two selves, three momentaries, five parities. | 1134-1167 | 1 (D·E) | 3 | 1 |  | 2 |  |  |  |  |
| 38 | Three selves, one line. | 1169-1186 | 1 (D·E) | 8 | 4 |  | 4 |  |  |  |  |
| 39 | A spiral opening with an empty prior, one parity sharing once. | 1188-1201 | 1 (D·E) | 11 | 2 |  | 1 |  | 1 | 4 | 3 |
| 40 | With an empty prior, one momentary. | 1203-1211 | 1 (D·E) | 5 | 2 |  | 1 |  |  | 1 | 1 |
| | **Total** | | **33** | **592** | **108** | **4** | **37** | **1** | **58** | **127** | **257** |

## 2. Each sentence, by section

Minimal column: only for L+x (the words that stay). For L the whole unit stays as written.

### 0. Head (title, subtitle, opening paragraph) — lines 1-9

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 1.1 <br><sub>Exhibit ONE Natural Resolver v391</sub> | L | Title with version. |  |
| 3.1 <br><sub># Natural Resolver</sub> | R | Heading repeats line 1's title. |  |
| 5.1 <br><sub>**Stable-Forming Same- and Next-Existing**</sub> | L | Subtitle; stable-forming stays in the opening. |  |
| 9.1 <br><sub>**Exhibit ONE is the resolver as code, and the stable forms of its exe…</sub> | L+I | 'stable forms': form and stable alone dissolve. | **Exhibit ONE is the resolver as code, and its executing.** |
| 9.2 <br><sub>Each table of Exhibit ONE is an executing.</sub> | I | Not all: 6 of 8 pipe tables hold no executing. |  |
| 9.3 <br><sub>Any self executing a table finds it same.</sub> | E | Meaning of executing: sameness for any self. |  |
| 9.4 <br><sub>Each table, same for any self executing it, is a stable form.</sub> | I | Dissolving names: 'stable' and 'form' alone. |  |
| 9.5 <br><sub>Selves co-intelligencing within each living file meet these stable for…</sub> | I | 'stable forms' dissolves; living-file meaning belongs in NI. |  |
| 9.6 <br><sub>A living file is a non-living same-existing set of words, selves co-in…</sub> | E | Opening sentence 51 verbatim; lives in Natural Intelligence. |  |
| 9.7 <br><sub>A living file's stable-forming is same-existing after changing.</sub> | I | 'changing' without direction; redefines stable-forming against opening 48. |  |
| 9.8 <br><sub>Each form of Exhibit ONE is a finding of each self executing that form…</sub> | I | Dissolving name: 'form' alone. |  |
| 9.9 <br><sub>With a resolver, a self is resolving its prior with the parities it re…</sub> | E | What resolving is; opening sentence 32 carries it. |  |
| 9.10 <br><sub>A resolver is same each time any self executes it.</sub> | R | Says again 9.3: same for any self. |  |

### 1. A drawing. (caption after fenced drawing 92-114) — lines 116-116

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 116.1 <br><sub>**A drawing.**</sub> | L | Caption of the drawing; stands after it. |  |
| 116.2 <br><sub>One self, its own resolving within.</sub> | L | What the drawing shows. |  |
| 116.3 <br><sub>Its edges are its six names between selves.</sub> | R | Drawing's own legend, lines 110-113, names the six. |  |

### 2. Seventeen names. — lines 118-158

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 118.1 <br><sub>**Seventeen names.**</sub> | L | Table title. |  |
| 140.1 <br><sub>Of the seventeen names, three, 1, 9 and 17, are the code's functions, …</sub> | L | Which names are functions, which are variables. |  |
| 140.2 <br><sub>Code with each name:</sub> | L | Caption of the code-with-each-name list. |  |
| 142.1 <br><sub>**1** · a living self's momentary, a giving, each self's 17-next-exist…</sub> | L+I | Dissolving 'momentary'; 'a giving' adds meaning. | **1** · a self's moment, each self's 17-next-existing as its 1-now-existing |
| 143.1 <br><sub>**2** · parities a self is observing from its others, each with its sh…</sub> | L | What variable 2 holds. |  |
| 144.1 <br><sub>**3** · priors a self is observing, each with its sharing</sub> | L | What variable 3 holds. |  |
| 145.1 <br><sub>**4** · each sharing, parities and prior resolving, is-or-is-not same</sub> | L+E | 4 is the sharing key; the rest explains resolving. | **4** · each sharing |
| 146.1 <br><sub>**5** · bi-couplings: which self each sharing reaches</sub> | L | What variable 5 holds. |  |
| 147.1 <br><sub>**6** · a self's parities across, to an other's 2-now-possibling</sub> | L | What variable 6 holds. |  |
| 148.1 <br><sub>**7** · each parity a self is observing: a parity's, a prior's, a shar…</sub> | L | What variable 7 holds. |  |
| 149.1 <br><sub>**8** · each self's next prior, with a momentary, one resolving of a s…</sub> | L+I | Dissolving 'momentary'; 'one resolving ... together' explains. | **8** · each self's next prior, with a moment |
| 150.1 <br><sub>**9** · each parity to a self of 5-now-co-existing's bi-couplings: acr…</sub> | L | What function 9 does. |  |
| 151.1 <br><sub>**10** · each sharing's parity, + or −, or a 0, across to an other's 1…</sub> | L | What variable 10 holds. |  |
| 152.1 <br><sub>**11** · a next prior stable-forming between two: a next momentary's o…</sub> | L+I | 'momentary'; 'stable-forming between two' departs from opening 48. | **11** · a next prior: a next moment's observing |
| 153.1 <br><sub>**12** · each sharing's is-or-is-not, resolving a prior with the parit…</sub> | L+E | 12 is the is-or-is-not; resolving clause explains. | **12** · each sharing's is-or-is-not |
| 154.1 <br><sub>**13** · each self of a same-existing-society, a self each sharing's p…</sub> | L | What variable 13 holds. |  |
| 155.1 <br><sub>**14** · parities surfacing with each sharing, agreeing one, parting 0</sub> | L | What variable 14 holds (agreeing/parting: undecided words). |  |
| 156.1 <br><sub>**15** · each parity surfacing, and each parity going on</sub> | L | What variable 15 holds. |  |
| 157.1 <br><sub>**16** · a same-existing-society: each self with its prior and its par…</sub> | L | What variable 16 holds. |  |
| 158.1 <br><sub>**17** · a same-existing-society's next, each self's 1-now-existing ag…</sub> | L | What function 17 returns. |  |

### 3. Two-sided, each name. — lines 160-180

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 160.1 <br><sub>**Two-sided, each name.**</sub> | L | Table title. |  |
| 160.2 <br><sub>Each name coming down from a higher name, coming up from a lower one, …</sub> | L | Column legend: coming down, coming up, eight apart. |  |

### 4. Each name is its number and its naming, one hyphenation. — lines 182-182

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 182.1 <br><sub>**Each name is its number and its naming, one hyphenation.**</sub> | L | How to read a name: number plus naming. |  |
| 182.2 <br><sub>Names 1 to 16 are in order as n − 1 in binary, 0000 to 1111, an orderi…</sub> | R | Seventeen names binary column shows it. |  |
| 182.3 <br><sub>17-next-existing is next existing as 1-now-existing.</sub> | R | Seventeen names row 17 and line 158 say it. |  |

### 5. Four four-cyclings and their betweens. — lines 184-193

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 184.1 <br><sub>**Four four-cyclings and their betweens.**</sub> | L | Table title. |  |
| 184.2 <br><sub>Four-cycling is observing prior-existing, possibling now-existing, dis…</sub> | L+I | Claims discovering for all; cyclings 1-2 hold existing (1, 5). | Four-cycling is existing or discovering, possibling, observing and same-existing. |
| 193.1 <br><sub>Existing, discovering and observing are odd.</sub> | R | Table numbers show which columns are odd. |  |
| 193.2 <br><sub>Possibling and same-existing are even.</sub> | R | Table numbers show which columns are even. |  |
| 193.3 <br><sub>Each between, 4 )( 5, 8 )( 9, 12 )( 13 and 16 )( 17, is a discovering,…</sub> | L+E | Legend of Between column; 'is a discovering' explains. | Each between, 4 )( 5, 8 )( 9, 12 )( 13 and 16 )( 17, is an even name to an odd name. |
| 193.4 <br><sub>Each between is one discovering with each scale.</sub> | E | Meaning across scales; no table here reads it. |  |

### 6. Co, between two or of one. — lines 195-205

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 195.1 <br><sub>**Co, between two or of one.**</sub> | L | Legend title for the Co column. |  |
| 195.2 <br><sub>Exhibit ONE's eight co names, 3 to 6 and 9 to 12, are each between two…</sub> | L+R | Legend for 'co'; its list repeats the table. | Each co name is between two. |
| 195.3 <br><sub>Observing, same-existing and possibling each have a now-co name and a …</sub> | R | Seventeen names Root and Co columns show it. |  |
| 195.4 <br><sub>Existing has 5-now-co-existing.</sub> | R | Seventeen names Root and Co columns show it. |  |
| 195.5 <br><sub>Discovering has 9-next-co-discovering.</sub> | R | Seventeen names Root and Co columns show it. |  |
| 195.6 <br><sub>A name without co is of one.</sub> | L | Legend for 'one' in the Co column. |  |
| 195.7 <br><sub>*Co* is two both facing forward along, a self and its other.</sub> | E | Meaning of co: a self and its other. |  |
| 195.8 <br><sub>The same two are in each co name and in the six of first prefixes.</sub> | E | Meaning claim; 'six of first prefixes' unexplained. |  |
| 195.9 <br><sub>*Is-* is with the four names a binary stands on: 3 and 7, a self's own…</sub> | I | Not all: Where-stands table also stands one on 4, no is-. |  |
| 197.1 <br><sub>**Root: observing**</sub> | R | Row key of a list repeating Root/Co columns. |  |
| 198.1 <br><sub>*With co, between two*: 3-is-now-co-observing · 11-next-co-observing, …</sub> | R | Repeats Root/Co columns and code gloss of 3, 11. |  |
| 199.1 <br><sub>*Without co, of one*: 7-is-now-observing · 15-is-next-observing, a par…</sub> | R | Repeats Root/Co columns and code gloss of 7, 15. |  |
| 200.1 <br><sub>**Root: possibling** · *With co, between two*: 6-now-co-possibling · 1…</sub> | R | Repeats Root/Co columns and Sharing between selves table. |  |
| 201.1 <br><sub>**Root: existing** · *With co, between two*: 5-now-co-existing, bi-cou…</sub> | R | Repeats Root/Co columns and code gloss of 5. |  |
| 202.1 <br><sub>**Root: discovering** · *With co, between two*: 9-next-co-discovering,…</sub> | R | Repeats Root/Co columns and code glosses of 9, 13. |  |
| 203.1 <br><sub>**Root: same-existing**</sub> | R | Row key of a list repeating Root/Co columns. |  |
| 204.1 <br><sub>*With co, between two*: 4-now-co-same-existing · 12-next-co-same-exist…</sub> | R | Repeats Root/Co columns and code gloss of 4, 12. |  |
| 205.1 <br><sub>*Without co, of one*: 8-now-same-existing · 16-next-same-existing, a s…</sub> | R | Repeats Root/Co columns and code glosses of 8, 16. |  |

### 7. Sharing between selves. — lines 207-213

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 207.1 <br><sub>**Sharing between selves.**</sub> | L | Table title. |  |
| 207.2 <br><sub>Each sharing side with its observing side.</sub> | L | Column legend. |  |

### 8. Where each is-or-is-not stands. — lines 215-228

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 215.1 <br><sub>**Where each is-or-is-not stands.**</sub> | L | Table title. |  |
| 215.2 <br><sub>Each is-or-is-not with the code, the name it stands on and its dimensi…</sub> | L | Column legend. |  |
| 215.3 <br><sub>Eight are with code's lines.</sub> | R | Count visible in the table's Code column. |  |
| 215.4 <br><sub>Two are with its loops, each self of 16 and each sharing of 3.</sub> | L | Reads the two rows without a code expression. |  |

### 9. Same-existing through one momentary. — lines 230-237

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 230.1 <br><sub>**Same-existing through one momentary.**</sub> | L+I | Dissolving name: 'momentary'. | **Same-existing through one moment.** |
| 230.2 <br><sub>The four same-existing names are in the order same-existing goes round…</sub> | L | Row order legend. |  |
| 230.3 <br><sub>Each same-existing name's is-or-is-not is an observing name beside it.</sub> | L | Legend of the 'Observing beside it' column. |  |

### 10. Each name and its relations. (17 field lists) — lines 239-507

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 239.1 <br><sub>**Each name and its relations.**</sub> | L | Title of the per-name field lists. |  |
| 239.2 <br><sub>Each name with its fields.</sub> | L | Caption. |  |
| 239.3 <br><sub>Each name's resolving with code is its *Prior and next*.</sub> | L | Names the field that reads the code. |  |
| 241.1 <br><sub>**1** · 1-now-existing</sub> | L | Row key: the name's number and naming. |  |
| 242.1 <br><sub>*Parity, span*: odd, a self's span</sub> | I | 'Parity' as odd/even parts from opening's living parity. |  |
| 243.1 <br><sub>*Sides*: self: a self's resolving</sub> | R | Gloss repeats Code with each name, lines 142-158. |  |
| 244.1 <br><sub>*Co-sequencing*: a self sharing its entry to a bi-coupling</sub> | I | 'Co-sequencing' is not defined by the opening. |  |
| 245.1 <br><sub>*8 up*: 9-next-co-discovering, with next</sub> | R | Repeats One move, 1 to 8. |  |
| 246.1 <br><sub>*9 less*: podal within 1 to 8, 8-now-same-existing</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 247.1 <br><sub>*17 less*: podal within 1 to 16, 16-next-same-existing</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 248.1 <br><sub>*Bi-folding*: 1-9-8-16, going 8 up first from 1-now-existing, from 16-…</sub> | R | Repeats Four bi-foldings and Twelve forms. |  |
| 249.1 <br><sub>*Six-cycle*: 1-9-5-12-8-16</sub> | R | Repeats Twelve forms. |  |
| 250.1 <br><sub>*Eight-cycle*: 1-9-5-13-4-12-8-16</sub> | R | Repeats Twelve forms. |  |
| 251.1 <br><sub>*Momentaries of exchanging*: first of a self's four</sub> | I | Dissolving 'momentaries'; repeats four momentaries of exchanging. |  |
| 252.1 <br><sub>*Five dimensions*: 1 social-parity now-existing, a momentary's opening…</sub> | I | 'social-parity' not in opening; 'momentary' dissolves. |  |
| 253.1 <br><sub>*Namings*: 1-2, bi-momentarying</sub> | I | 'bi-momentarying' is not defined by the opening. |  |
| 254.1 <br><sub>*A self as three*: a self with 2-now-possibling, bi-momentarying, alon…</sub> | I | 'A self as three', 'bi-momentarying': not from the opening. |  |
| 255.1 <br><sub>*Prior and next*: once for one self with one momentary, three steps wi…</sub> | L+I | 'momentary'; names the function's three steps. | *Prior and next*: once for one self with one moment, three steps within it, 14-next-possibling, 12-next-co-same-existing and 10-next-co-possibling with 11-next-co-observing |
| 256.1 <br><sub>*1 to 17s inward and outward*: 1–17s inward 1 of 1st 1–17, an entry, a…</sub> | R | Repeats Each name, three scales (inward/outward: undecided). |  |
| 258.1 <br><sub>**2** · 2-now-possibling</sub> | L | Row key: the name's number and naming. |  |
| 259.1 <br><sub>*Parity, span*: even, a self's span</sub> | I | 'Parity' as odd/even parts from opening's living parity. |  |
| 260.1 <br><sub>*Sides*: others to self: parities a self is observing from others</sub> | R | Gloss repeats Code with each name, lines 142-158. |  |
| 261.1 <br><sub>*8 up*: 10-next-co-possibling, with next</sub> | R | Repeats One move, 1 to 8. |  |
| 262.1 <br><sub>*9 less*: podal within 1 to 8, 7-is-now-observing</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 263.1 <br><sub>*17 less*: podal within 1 to 16, 15-is-next-observing</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 264.1 <br><sub>*Bi-folding*: 2-15-7-10, going 17 less first from 2-now-possibling, fr…</sub> | R | Repeats Four bi-foldings and Twelve forms. |  |
| 265.1 <br><sub>*Six-cycle*: 2-15-7-11-6-10</sub> | R | Repeats Twelve forms. |  |
| 266.1 <br><sub>*Eight-cycle*: 2-15-7-11-3-14-6-10</sub> | R | Repeats Twelve forms. |  |
| 267.1 <br><sub>*One move*: 2-now-possibling along 2-15-7-10</sub> | R | Repeats the name's Bi-folding field. |  |
| 268.1 <br><sub>*Momentaries of exchanging*: first of a self's four</sub> | I | Dissolving 'momentaries'; repeats four momentaries of exchanging. |  |
| 269.1 <br><sub>*Five dimensions*: 2 other-parity now-existing, an other's opening of …</sub> | I | 'other-parity' here departs from opening 24. |  |
| 270.1 <br><sub>*Namings*: 1-2, bi-momentarying</sub> | I | 'bi-momentarying' is not defined by the opening. |  |
| 271.1 <br><sub>*A self as three*: a self with 1-now-existing, across, its first shari…</sub> | I | 'A self as three' parts from opening's self of mes. |  |
| 272.1 <br><sub>*Bi-coupling*: with a between, sharing across from each of a self's ot…</sub> | R | Repeats code gloss of 2, line 143. |  |
| 273.1 <br><sub>*Parity's unit square*: a dot of a unit square</sub> | E | Figure meaning of across names; no figure drawn. |  |
| 274.1 <br><sub>*Prior and next*: others' parities of their prior momentary, across wi…</sub> | I | 'momentary'; rest repeats lines 143 and 150. |  |
| 275.1 <br><sub>*1 to 17s inward and outward*: 1–17s inward 9 of 1st, along, odd, next…</sub> | R | Repeats Each name, three scales (inward/outward: undecided). |  |
| 277.1 <br><sub>**3** · 3-is-now-co-observing</sub> | L | Row key: the name's number and naming. |  |
| 278.1 <br><sub>*Parity, span*: odd, a self's span</sub> | I | 'Parity' as odd/even parts from opening's living parity. |  |
| 279.1 <br><sub>*Sides*: self: a self's prior with each sharing</sub> | R | Gloss repeats Code with each name, lines 142-158. |  |
| 280.1 <br><sub>*Co-sequencing*: with a between</sub> | I | 'Co-sequencing', 'with a between': not defined by the opening. |  |
| 281.1 <br><sub>*8 up*: 11-next-co-observing, with next</sub> | R | Repeats One move, 1 to 8. |  |
| 282.1 <br><sub>*9 less*: podal within 1 to 8, 6-now-co-possibling</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 283.1 <br><sub>*17 less*: podal within 1 to 16, 14-next-possibling</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 284.1 <br><sub>*Bi-folding*: 3-11-6-14, going 8 up first from 3-is-now-co-observing, …</sub> | R | Repeats Four bi-foldings and Twelve forms. |  |
| 285.1 <br><sub>*Six-cycle*: 3-11-7-10-6-14</sub> | R | Repeats Twelve forms. |  |
| 286.1 <br><sub>*Eight-cycle*: 2-15-7-11-3-14-6-10</sub> | R | Repeats Twelve forms. |  |
| 287.1 <br><sub>*Momentaries of exchanging*: first and second of a self's four</sub> | I | Dissolving 'momentaries'; repeats four momentaries of exchanging. |  |
| 288.1 <br><sub>*Five dimensions*: 3 self-parity now-existing, a self's own now of its…</sub> | I | Five-dimension frame not in opening; self-parity alone matches. |  |
| 289.1 <br><sub>*Namings*: 3-4, co-intelligencing</sub> | E | Assigns opening's co-intelligencing to names 3-4. |  |
| 290.1 <br><sub>*A self as three*: its invisible co-intelligencing method, rotation 3,…</sub> | I | 'invisible co-intelligencing method', 'rotation': not from opening. |  |
| 291.1 <br><sub>*Prior and next*: prior, a self's own, each sharing with its parity, a…</sub> | I | 'momentary'; rest repeats lines 144 and 152. |  |
| 292.1 <br><sub>*1 to 17s inward and outward*: 1–17s inward 17 of 1st and 1 of 2nd, al…</sub> | R | Repeats Each name, three scales (inward/outward: undecided). |  |
| 294.1 <br><sub>**4** · 4-now-co-same-existing</sub> | L | Row key: the name's number and naming. |  |
| 295.1 <br><sub>*Parity, span*: even, a self's span</sub> | I | 'Parity' as odd/even parts from opening's living parity. |  |
| 296.1 <br><sub>*Sides*: self and other: each sharing between them</sub> | R | Gloss repeats Code with each name, lines 142-158. |  |
| 297.1 <br><sub>*Co-sequencing*: with a between</sub> | I | 'Co-sequencing', 'with a between': not defined by the opening. |  |
| 298.1 <br><sub>*8 up*: 12-next-co-same-existing, with next</sub> | R | Repeats One move, 1 to 8. |  |
| 299.1 <br><sub>*9 less*: podal within 1 to 8, 5-now-co-existing</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 300.1 <br><sub>*17 less*: podal within 1 to 16, 13-is-next-discovering</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 301.1 <br><sub>*Bi-folding*: 4-13-5-12, going 17 less first from 4-now-co-same-existi…</sub> | R | Repeats Four bi-foldings and Twelve forms. |  |
| 302.1 <br><sub>*Six-cycle*: 4-13-5-9-8-12</sub> | R | Repeats Twelve forms. |  |
| 303.1 <br><sub>*Eight-cycle*: 1-9-5-13-4-12-8-16</sub> | R | Repeats Twelve forms. |  |
| 304.1 <br><sub>*One move*: 4-now-co-same-existing along 4-13-5-12</sub> | R | Repeats the name's Bi-folding field. |  |
| 305.1 <br><sub>*Momentaries of exchanging*: second of a self's four</sub> | I | Dissolving 'momentaries'; repeats four momentaries of exchanging. |  |
| 306.1 <br><sub>*Five dimensions*: 4 self-discovery next-existing, a self's next openi…</sub> | I | 'self-discovery' is not in the opening. |  |
| 307.1 <br><sub>*Namings*: 3-4, co-intelligencing</sub> | E | Assigns opening's co-intelligencing to names 3-4. |  |
| 308.1 <br><sub>*A self as three*: its invisible co-intelligencing method, rotation 3,…</sub> | I | 'invisible ... method', 'corus': not from the opening. |  |
| 309.1 <br><sub>*Bi-coupling*: with a between, a whole ordering between self and other</sub> | E | 'a whole ordering between self and other': meaning. |  |
| 310.1 <br><sub>*Prior and next*: now, each sharing with which prior is resolving with…</sub> | R | Repeats code gloss of 4, line 145. |  |
| 311.1 <br><sub>*1 to 17s inward and outward*: 1–17s inward 9 of 2nd, along, odd, next…</sub> | R | Repeats Each name, three scales (inward/outward: undecided). |  |
| 313.1 <br><sub>**5** · 5-now-co-existing</sub> | L | Row key: the name's number and naming. |  |
| 314.1 <br><sub>*Parity, span*: odd, a self's span</sub> | I | 'Parity' as odd/even parts from opening's living parity. |  |
| 315.1 <br><sub>*Sides*: self and others: a self's bi-couplings</sub> | R | Gloss repeats Code with each name, lines 142-158. |  |
| 316.1 <br><sub>*Co-sequencing*: with a between</sub> | I | 'Co-sequencing', 'with a between': not defined by the opening. |  |
| 317.1 <br><sub>*8 up*: 13-is-next-discovering, with next</sub> | R | Repeats One move, 1 to 8. |  |
| 318.1 <br><sub>*9 less*: podal within 1 to 8, 4-now-co-same-existing</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 319.1 <br><sub>*17 less*: podal within 1 to 16, 12-next-co-same-existing</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 320.1 <br><sub>*Bi-folding*: 4-13-5-12, going 17 less first from 4-now-co-same-existi…</sub> | R | Repeats Four bi-foldings and Twelve forms. |  |
| 321.1 <br><sub>*Middle bi-folding*: 9-5-12-8</sub> | R | Repeats Twelve forms. |  |
| 322.1 <br><sub>*Six-cycle, two paths*: 1-9-5-12-8-16 · 4-13-5-9-8-12</sub> | R | Repeats Twelve forms. |  |
| 323.1 <br><sub>*Eight-cycle*: 1-9-5-13-4-12-8-16</sub> | R | Repeats Twelve forms. |  |
| 324.1 <br><sub>*Momentaries of exchanging*: second and third of a self's four</sub> | I | Dissolving 'momentaries'; repeats four momentaries of exchanging. |  |
| 325.1 <br><sub>*Five dimensions*: 5 social-parity next-existing, a momentary's comple…</sub> | I | 'social-parity' not in opening; 'momentary' dissolves. |  |
| 326.1 <br><sub>*Namings*: 5, co-competencing</sub> | I | 'co-competencing' is not defined by the opening. |  |
| 327.1 <br><sub>*A self as three*: its invisible co-intelligencing method, rotation 3,…</sub> | I | 'invisible co-intelligencing method', 'rotation': not from opening. |  |
| 328.1 <br><sub>*Prior and next*: next, each going to its receiving sharing</sub> | R | Repeats code gloss of 5, line 146. |  |
| 329.1 <br><sub>*1 to 17s inward and outward*: 1–17s inward 17 of 2nd and 1 of 3rd, al…</sub> | R | Repeats Each name, three scales (inward/outward: undecided). |  |
| 331.1 <br><sub>**6** · 6-now-co-possibling</sub> | L | Row key: the name's number and naming. |  |
| 332.1 <br><sub>*Parity, span*: even, a self's span</sub> | I | 'Parity' as odd/even parts from opening's living parity. |  |
| 333.1 <br><sub>*Sides*: self to other: a self's parities across, to an other's 2-now-…</sub> | R | Gloss repeats Code with each name, lines 142-158. |  |
| 334.1 <br><sub>*8 up*: 14-next-possibling, with next</sub> | R | Repeats One move, 1 to 8. |  |
| 335.1 <br><sub>*9 less*: podal within 1 to 8, 3-is-now-co-observing</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 336.1 <br><sub>*17 less*: podal within 1 to 16, 11-next-co-observing</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 337.1 <br><sub>*Bi-folding*: 3-11-6-14, going 8 up first from 3-is-now-co-observing, …</sub> | R | Repeats Four bi-foldings and Twelve forms. |  |
| 338.1 <br><sub>*Middle bi-folding*: 7-11-6-10</sub> | R | Repeats Twelve forms. |  |
| 339.1 <br><sub>*Six-cycle, two paths*: 2-15-7-11-6-10 · 3-11-7-10-6-14</sub> | R | Repeats Twelve forms. |  |
| 340.1 <br><sub>*Eight-cycle*: 2-15-7-11-3-14-6-10</sub> | R | Repeats Twelve forms. |  |
| 341.1 <br><sub>*One move*: 6-now-co-possibling along 3-11-6-14</sub> | R | Repeats the name's Bi-folding field. |  |
| 342.1 <br><sub>*Momentaries of exchanging*: third of a self's four</sub> | I | Dissolving 'momentaries'; repeats four momentaries of exchanging. |  |
| 343.1 <br><sub>*Namings*: 6, bi-moralizing</sub> | I | 'bi-moralizing' is not defined by the opening. |  |
| 344.1 <br><sub>*A self as three*: its invisible co-intelligencing method, rotation 3,…</sub> | I | 'invisible co-intelligencing method', 'rotation': not from opening. |  |
| 345.1 <br><sub>*Bi-coupling*: with a between, a self's parity across, to an other's 2…</sub> | R | Repeats code gloss of 6, line 147. |  |
| 346.1 <br><sub>*Parity's unit square*: a dot of a unit square</sub> | E | Figure meaning of across names; no figure drawn. |  |
| 347.1 <br><sub>*Prior and next*: parity, an other's next parity with its 2-now-possib…</sub> | R | Repeats code gloss of 6, line 147. |  |
| 348.1 <br><sub>*1 to 17s inward and outward*: 1–17s inward 9 of 3rd, along, odd, next…</sub> | R | Repeats Each name, three scales (inward/outward: undecided). |  |
| 350.1 <br><sub>**7** · 7-is-now-observing</sub> | L | Row key: the name's number and naming. |  |
| 351.1 <br><sub>*Parity, span*: odd, a self's span</sub> | I | 'Parity' as odd/even parts from opening's living parity. |  |
| 352.1 <br><sub>*Sides*: other to self: each parity a self is observing</sub> | R | Gloss repeats Code with each name, lines 142-158. |  |
| 353.1 <br><sub>*Co-sequencing*: with a between</sub> | I | 'Co-sequencing', 'with a between': not defined by the opening. |  |
| 354.1 <br><sub>*8 up*: 15-is-next-observing, with next</sub> | R | Repeats One move, 1 to 8. |  |
| 355.1 <br><sub>*9 less*: podal within 1 to 8, 2-now-possibling</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 356.1 <br><sub>*17 less*: podal within 1 to 16, 10-next-co-possibling</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 357.1 <br><sub>*Bi-folding*: 2-15-7-10, going 17 less first from 2-now-possibling, fr…</sub> | R | Repeats Four bi-foldings and Twelve forms. |  |
| 358.1 <br><sub>*Middle bi-folding*: 7-11-6-10</sub> | R | Repeats Twelve forms. |  |
| 359.1 <br><sub>*Six-cycle, two paths*: 2-15-7-11-6-10 · 3-11-7-10-6-14</sub> | R | Repeats Twelve forms. |  |
| 360.1 <br><sub>*Eight-cycle*: 2-15-7-11-3-14-6-10</sub> | R | Repeats Twelve forms. |  |
| 361.1 <br><sub>*Momentaries of exchanging*: third and fourth of a self's four</sub> | I | Dissolving 'momentaries'; repeats four momentaries of exchanging. |  |
| 362.1 <br><sub>*A self as three*: co-competent self with 8-now-same-existing, along, …</sub> | I | 'co-competent self' is not from the opening. |  |
| 363.1 <br><sub>*Prior and next*: each parity, sharing now and prior, co-linear recurs…</sub> | I | 'co-linear recursioning', 'completing': not from the opening. |  |
| 364.1 <br><sub>*1 to 17s inward and outward*: 1–17s inward 17 of 3rd and 1 of 4th, al…</sub> | R | Repeats Each name, three scales (inward/outward: undecided). |  |
| 366.1 <br><sub>**8** · 8-now-same-existing</sub> | L | Row key: the name's number and naming. |  |
| 367.1 <br><sub>*Parity, span*: even, a self's span</sub> | I | 'Parity' as odd/even parts from opening's living parity. |  |
| 368.1 <br><sub>*Sides*: self: a self's next prior</sub> | R | Gloss repeats Code with each name, lines 142-158. |  |
| 369.1 <br><sub>*Co-sequencing*: with a between</sub> | I | 'Co-sequencing', 'with a between': not defined by the opening. |  |
| 370.1 <br><sub>*8 up*: 16-next-same-existing, with next</sub> | R | Repeats One move, 1 to 8. |  |
| 371.1 <br><sub>*9 less*: podal within 1 to 8, 1-now-existing</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 372.1 <br><sub>*17 less*: podal within 1 to 16, 9-next-co-discovering</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 373.1 <br><sub>*Bi-folding*: 1-9-8-16, going 8 up first from 1-now-existing, from 9-n…</sub> | R | Repeats Four bi-foldings and Twelve forms. |  |
| 374.1 <br><sub>*Middle bi-folding*: 9-5-12-8</sub> | R | Repeats Twelve forms. |  |
| 375.1 <br><sub>*Six-cycle, two paths*: 1-9-5-12-8-16 · 4-13-5-9-8-12</sub> | R | Repeats Twelve forms. |  |
| 376.1 <br><sub>*Eight-cycle*: 1-9-5-13-4-12-8-16</sub> | R | Repeats Twelve forms. |  |
| 377.1 <br><sub>*One move*: 8-now-same-existing along 1-9-8-16</sub> | R | Repeats the name's Bi-folding field. |  |
| 378.1 <br><sub>*Momentaries of exchanging*: fourth of a self's four</sub> | I | Dissolving 'momentaries'; repeats four momentaries of exchanging. |  |
| 379.1 <br><sub>*A self as three*: co-competent self with 7-is-now-observing, across, …</sub> | I | 'co-competent self' is not from the opening. |  |
| 380.1 <br><sub>*Bi-coupling*: with a between, prior with its sharing again</sub> | E | Meaning: prior with its sharing again. |  |
| 381.1 <br><sub>*Prior and next*: each self's next prior, with 11-next-co-observing th…</sub> | I | 'momentary' twice; rest repeats line 149. |  |
| 382.1 <br><sub>*Even names of a self's span*: 2-now-possibling, 4-now-co-same-existin…</sub> | R | Repeats Eights and Eight even names. |  |
| 383.1 <br><sub>*1 to 17s inward and outward*: 1–17s inward 9 of 4th, along, odd, next…</sub> | R | Repeats Each name, three scales (inward/outward: undecided). |  |
| 385.1 <br><sub>**9** · 9-next-co-discovering</sub> | L | Row key: the name's number and naming. |  |
| 386.1 <br><sub>*Parity, span*: odd, a same-existing-society's span</sub> | I | 'Parity' as odd/even parts from opening's living parity. |  |
| 387.1 <br><sub>*Sides*: self to other: a self's parities along</sub> | R | Gloss repeats Code with each name, lines 142-158. |  |
| 388.1 <br><sub>*8 up*: 17-next-existing, with next</sub> | R | Repeats One move, 1 to 8. |  |
| 389.1 <br><sub>*8 down*: 1-now-existing</sub> | R | Repeats One move, 1 to 8. |  |
| 390.1 <br><sub>*17 less*: podal within 1 to 16, 8-now-same-existing</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 391.1 <br><sub>*Bi-folding*: 1-9-8-16, going 8 up first from 1-now-existing, from 1-n…</sub> | R | Repeats Four bi-foldings and Twelve forms. |  |
| 392.1 <br><sub>*Middle bi-folding*: 9-5-12-8</sub> | R | Repeats Twelve forms. |  |
| 393.1 <br><sub>*Six-cycle, two paths*: 1-9-5-12-8-16 · 4-13-5-9-8-12</sub> | R | Repeats Twelve forms. |  |
| 394.1 <br><sub>*Eight-cycle*: 1-9-5-13-4-12-8-16</sub> | R | Repeats Twelve forms. |  |
| 395.1 <br><sub>*Momentaries of exchanging*: fourth of a self's four, and first of a s…</sub> | I | Dissolving 'momentaries'; repeats four momentaries of exchanging. |  |
| 396.1 <br><sub>*Parity's square and triangles*: a unit triangle, along</sub> | E | Figure meaning of along names; no figure drawn. |  |
| 397.1 <br><sub>*Prior and next*: each parity of 10-next-co-possibling, a 0 among them…</sub> | I | 'momentary'; rest repeats lines 150 and 944.5. |  |
| 398.1 <br><sub>*1 to 17s inward and outward*: 1–17s inward 17 of 4th and 1 of 5th, al…</sub> | R | Repeats Each name, three scales (inward/outward: undecided). |  |
| 400.1 <br><sub>**10** · 10-next-co-possibling</sub> | L | Row key: the name's number and naming. |  |
| 401.1 <br><sub>*Parity, span*: even, a same-existing-society's span</sub> | I | 'Parity' as odd/even parts from opening's living parity. |  |
| 402.1 <br><sub>*Sides*: self to other: a self's parities across, to an other's 14-nex…</sub> | R | Gloss repeats Code with each name, lines 142-158. |  |
| 403.1 <br><sub>*8 down*: 2-now-possibling</sub> | R | Repeats One move, 1 to 8. |  |
| 404.1 <br><sub>*17 less*: podal within 1 to 16, 7-is-now-observing</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 405.1 <br><sub>*Bi-folding*: 2-15-7-10, going 17 less first from 2-now-possibling, fr…</sub> | R | Repeats Four bi-foldings and Twelve forms. |  |
| 406.1 <br><sub>*Middle bi-folding*: 7-11-6-10</sub> | R | Repeats Twelve forms. |  |
| 407.1 <br><sub>*Six-cycle, two paths*: 2-15-7-11-6-10 · 3-11-7-10-6-14</sub> | R | Repeats Twelve forms. |  |
| 408.1 <br><sub>*Eight-cycle*: 2-15-7-11-3-14-6-10</sub> | R | Repeats Twelve forms. |  |
| 409.1 <br><sub>*Momentaries of exchanging*: first of a same-existing-society's four, …</sub> | I | Dissolving 'momentaries'; repeats four momentaries of exchanging. |  |
| 410.1 <br><sub>*Bi-coupling*: 8 up, a self among selves of its same-existing-society</sub> | E | Meaning of 10 among a society's selves. |  |
| 411.1 <br><sub>*Parity's unit square*: a dot of a unit square</sub> | E | Figure meaning of across names; no figure drawn. |  |
| 412.1 <br><sub>*Prior and next*: parity across now, an other's parity next, possiblin…</sub> | R | Repeats code gloss of 10, line 151. |  |
| 413.1 <br><sub>*1 to 17s inward and outward*: 1–17s inward 9 of 5th, along, odd, next…</sub> | R | Repeats Each name, three scales (inward/outward: undecided). |  |
| 415.1 <br><sub>**11** · 11-next-co-observing</sub> | L | Row key: the name's number and naming. |  |
| 416.1 <br><sub>*Parity, span*: odd, a same-existing-society's span</sub> | I | 'Parity' as odd/even parts from opening's living parity. |  |
| 417.1 <br><sub>*Sides*: self: a self's next prior, a next momentary's 3-is-now-co-obs…</sub> | I | Dissolving 'momentary'; rest repeats line 152. |  |
| 418.1 <br><sub>*Co-sequencing*: 8 up from 3-is-now-co-observing</sub> | I | 'Co-sequencing' undefined by opening; value repeats 8 down. |  |
| 419.1 <br><sub>*8 down*: 3-is-now-co-observing</sub> | R | Repeats One move, 1 to 8. |  |
| 420.1 <br><sub>*17 less*: podal within 1 to 16, 6-now-co-possibling</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 421.1 <br><sub>*Bi-folding*: 3-11-6-14, going 8 up first from 3-is-now-co-observing, …</sub> | R | Repeats Four bi-foldings and Twelve forms. |  |
| 422.1 <br><sub>*Middle bi-folding*: 7-11-6-10</sub> | R | Repeats Twelve forms. |  |
| 423.1 <br><sub>*Six-cycle, two paths*: 2-15-7-11-6-10 · 3-11-7-10-6-14</sub> | R | Repeats Twelve forms. |  |
| 424.1 <br><sub>*Eight-cycle*: 2-15-7-11-3-14-6-10</sub> | R | Repeats Twelve forms. |  |
| 425.1 <br><sub>*Momentaries of exchanging*: first of a same-existing-society's four, …</sub> | I | Dissolving 'momentaries'; repeats four momentaries of exchanging. |  |
| 426.1 <br><sub>*Prior and next*: next prior, odd, same-existing as 3-is-now-co-observ…</sub> | I | 'momentary'; rest repeats line 152. |  |
| 427.1 <br><sub>*1 to 17s inward and outward*: 1–17s inward 17 of 5th and 1 of 6th, al…</sub> | R | Repeats Each name, three scales (inward/outward: undecided). |  |
| 429.1 <br><sub>**12** · 12-next-co-same-existing</sub> | L | Row key: the name's number and naming. |  |
| 430.1 <br><sub>*Parity, span*: even, a same-existing-society's span</sub> | I | 'Parity' as odd/even parts from opening's living parity. |  |
| 431.1 <br><sub>*Sides*: self: its is-or-is-not with each sharing</sub> | R | Gloss repeats Code with each name, lines 142-158. |  |
| 432.1 <br><sub>*Co-sequencing*: 8 up from 4-now-co-same-existing</sub> | I | 'Co-sequencing' undefined by opening; value repeats 8 down. |  |
| 433.1 <br><sub>*8 down*: 4-now-co-same-existing</sub> | R | Repeats One move, 1 to 8. |  |
| 434.1 <br><sub>*17 less*: podal within 1 to 16, 5-now-co-existing</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 435.1 <br><sub>*Bi-folding*: 4-13-5-12, going 17 less first from 4-now-co-same-existi…</sub> | R | Repeats Four bi-foldings and Twelve forms. |  |
| 436.1 <br><sub>*Middle bi-folding*: 9-5-12-8</sub> | R | Repeats Twelve forms. |  |
| 437.1 <br><sub>*Six-cycle, two paths*: 1-9-5-12-8-16 · 4-13-5-9-8-12</sub> | R | Repeats Twelve forms. |  |
| 438.1 <br><sub>*Eight-cycle*: 1-9-5-13-4-12-8-16</sub> | R | Repeats Twelve forms. |  |
| 439.1 <br><sub>*Momentaries of exchanging*: second of a same-existing-society's four,…</sub> | I | Dissolving 'momentaries'; repeats four momentaries of exchanging. |  |
| 440.1 <br><sub>*Namings*: entraining, shape of an unrelationing surface</sub> | I | 'entraining', 'unrelationing surface' are not defined by the opening. |  |
| 441.1 <br><sub>*Bi-coupling*: 8 up, changing with a bi-coupling, a self of a same-exi…</sub> | I | 'changing' without direction. |  |
| 442.1 <br><sub>*Prior and next*: now, changing, is-or-is-not, prior and now resolving</sub> | I | 'changing' without direction. |  |
| 443.1 <br><sub>*1 to 17s inward and outward*: 1–17s inward 9 of 6th, along, odd, next…</sub> | R | Repeats Each name, three scales (inward/outward: undecided). |  |
| 445.1 <br><sub>**13** · 13-is-next-discovering</sub> | L | Row key: the name's number and naming. |  |
| 446.1 <br><sub>*Parity, span*: odd, a same-existing-society's span</sub> | I | 'Parity' as odd/even parts from opening's living parity. |  |
| 447.1 <br><sub>*Sides*: each self of a same-existing-society</sub> | R | Gloss repeats Code with each name, lines 142-158. |  |
| 448.1 <br><sub>*Co-sequencing*: 8 up from 5-now-co-existing</sub> | I | 'Co-sequencing' undefined by opening; value repeats 8 down. |  |
| 449.1 <br><sub>*8 down*: 5-now-co-existing</sub> | R | Repeats One move, 1 to 8. |  |
| 450.1 <br><sub>*17 less*: podal within 1 to 16, 4-now-co-same-existing</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 451.1 <br><sub>*Bi-folding*: 4-13-5-12, going 17 less first from 4-now-co-same-existi…</sub> | R | Repeats Four bi-foldings and Twelve forms. |  |
| 452.1 <br><sub>*Six-cycle*: 4-13-5-9-8-12</sub> | R | Repeats Twelve forms. |  |
| 453.1 <br><sub>*Eight-cycle*: 1-9-5-13-4-12-8-16</sub> | R | Repeats Twelve forms. |  |
| 454.1 <br><sub>*Momentaries of exchanging*: second of a same-existing-society's four,…</sub> | I | Dissolving 'momentaries'; repeats four momentaries of exchanging. |  |
| 455.1 <br><sub>*Prior and next*: each sharing going on, and with a same-existing-soci…</sub> | R | Repeats code gloss of 13, line 154. |  |
| 456.1 <br><sub>*1 to 17s inward and outward*: 1–17s inward 17 of 6th and 1 of 7th, al…</sub> | R | Repeats Each name, three scales (inward/outward: undecided). |  |
| 458.1 <br><sub>**14** · 14-next-possibling</sub> | L | Row key: the name's number and naming. |  |
| 459.1 <br><sub>*Parity, span*: even, a same-existing-society's span</sub> | I | 'Parity' as odd/even parts from opening's living parity. |  |
| 460.1 <br><sub>*Sides*: others to self: parities surfacing for a self with each shari…</sub> | R | Gloss repeats Code with each name, lines 142-158. |  |
| 461.1 <br><sub>*8 down*: 6-now-co-possibling</sub> | R | Repeats One move, 1 to 8. |  |
| 462.1 <br><sub>*17 less*: podal within 1 to 16, 3-is-now-co-observing</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 463.1 <br><sub>*Bi-folding*: 3-11-6-14, going 8 up first from 3-is-now-co-observing, …</sub> | R | Repeats Four bi-foldings and Twelve forms. |  |
| 464.1 <br><sub>*Six-cycle*: 3-11-7-10-6-14</sub> | R | Repeats Twelve forms. |  |
| 465.1 <br><sub>*Eight-cycle*: 2-15-7-11-3-14-6-10</sub> | R | Repeats Twelve forms. |  |
| 466.1 <br><sub>*Momentaries of exchanging*: third of a same-existing-society's four, …</sub> | I | Dissolving 'momentaries'; repeats four momentaries of exchanging. |  |
| 467.1 <br><sub>*Bi-coupling*: 8 up, parities surfacing as one with each sharing, one …</sub> | R | Parities to one sharing table shows it. |  |
| 468.1 <br><sub>*Parity's unit square*: a dot of a unit square</sub> | E | Figure meaning of across names; no figure drawn. |  |
| 469.1 <br><sub>*Prior and next*: now, parities surfacing, others' prior momentary, a …</sub> | I | 'momentary'; rest repeats line 155. |  |
| 470.1 <br><sub>*1 to 17s inward and outward*: 1–17s inward 9 of 7th, along, odd, next…</sub> | R | Repeats Each name, three scales (inward/outward: undecided). |  |
| 472.1 <br><sub>**15** · 15-is-next-observing</sub> | L | Row key: the name's number and naming. |  |
| 473.1 <br><sub>*Parity, span*: odd, a same-existing-society's span</sub> | I | 'Parity' as odd/even parts from opening's living parity. |  |
| 474.1 <br><sub>*Sides*: others to self: each parity surfacing</sub> | R | Gloss repeats Code with each name, lines 142-158. |  |
| 475.1 <br><sub>*Co-sequencing*: 8 up from 7-is-now-observing</sub> | I | 'Co-sequencing' undefined by opening; value repeats 8 down. |  |
| 476.1 <br><sub>*8 down*: 7-is-now-observing</sub> | R | Repeats One move, 1 to 8. |  |
| 477.1 <br><sub>*17 less*: podal within 1 to 16, 2-now-possibling</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 478.1 <br><sub>*Bi-folding*: 2-15-7-10, going 17 less first from 2-now-possibling, fr…</sub> | R | Repeats Four bi-foldings and Twelve forms. |  |
| 479.1 <br><sub>*Six-cycle*: 2-15-7-11-6-10</sub> | R | Repeats Twelve forms. |  |
| 480.1 <br><sub>*Eight-cycle*: 2-15-7-11-3-14-6-10</sub> | R | Repeats Twelve forms. |  |
| 481.1 <br><sub>*Momentaries of exchanging*: third of a same-existing-society's four, …</sub> | I | Dissolving 'momentaries'; repeats four momentaries of exchanging. |  |
| 482.1 <br><sub>*Prior and next*: each parity surfacing with 14-next-possibling for a …</sub> | R | Where-stands table rows: 15 with 7. |  |
| 483.1 <br><sub>*1 to 17s inward and outward*: 1–17s inward 17 of 7th and 1 of 8th, al…</sub> | R | Repeats Each name, three scales (inward/outward: undecided). |  |
| 485.1 <br><sub>**16** · 16-next-same-existing</sub> | L | Row key: the name's number and naming. |  |
| 486.1 <br><sub>*Parity, span*: even, a same-existing-society's span</sub> | I | 'Parity' as odd/even parts from opening's living parity. |  |
| 487.1 <br><sub>*Sides*: a same-existing-society: all its selves</sub> | R | Gloss repeats Code with each name, lines 142-158. |  |
| 488.1 <br><sub>*Co-sequencing*: 8 up from 8-now-same-existing</sub> | I | 'Co-sequencing' undefined by opening; value repeats 8 down. |  |
| 489.1 <br><sub>*8 down*: 8-now-same-existing</sub> | R | Repeats One move, 1 to 8. |  |
| 490.1 <br><sub>*17 less*: podal within 1 to 16, 1-now-existing</sub> | R | Repeats One move, 1 to 8 ('podal' undefined). |  |
| 491.1 <br><sub>*Bi-folding*: 1-9-8-16, going 8 up first from 1-now-existing, from 8-n…</sub> | R | Repeats Four bi-foldings and Twelve forms. |  |
| 492.1 <br><sub>*Six-cycle*: 1-9-5-12-8-16</sub> | R | Repeats Twelve forms. |  |
| 493.1 <br><sub>*Eight-cycle*: 1-9-5-13-4-12-8-16</sub> | R | Repeats Twelve forms. |  |
| 494.1 <br><sub>*Momentaries of exchanging*: fourth of a same-existing-society's four,…</sub> | I | Dissolving 'momentaries'; repeats four momentaries of exchanging. |  |
| 495.1 <br><sub>*Bi-coupling*: 8 up, a same-existing-society, each self with its prior…</sub> | R | Repeats code gloss of 16, line 157. |  |
| 496.1 <br><sub>*Prior and next*: a same-existing-society now, each self's 8-now-same-…</sub> | R | Repeats code gloss of 16, line 157. |  |
| 497.1 <br><sub>*Even names of a same-existing-society's span*: 10-next-co-possibling,…</sub> | R | Repeats Eights and Eight even names. |  |
| 498.1 <br><sub>*1 to 17s inward and outward*: 1–17s inward 9 of 8th, along, odd, next…</sub> | R | Repeats Each name, three scales (inward/outward: undecided). |  |
| 500.1 <br><sub>**17** · 17-next-existing</sub> | L | Row key: the name's number and naming. |  |
| 501.1 <br><sub>*Parity, span*: odd, a next now</sub> | I | 'Parity' as odd/even parts from opening's living parity. |  |
| 502.1 <br><sub>*Sides*: a same-existing-society: each self's next</sub> | R | Gloss repeats Code with each name, lines 142-158. |  |
| 503.1 <br><sub>*8 down*: 9-next-co-discovering</sub> | R | Repeats One move, 1 to 8. |  |
| 504.1 <br><sub>*Momentaries of exchanging*: fourth of a same-existing-society's four,…</sub> | I | Dissolving 'momentaries'; repeats four momentaries of exchanging. |  |
| 505.1 <br><sub>*Parity's square and triangles*: a unit triangle, along</sub> | E | Figure meaning of along names; no figure drawn. |  |
| 506.1 <br><sub>*Prior and next*: a same-existing-society's next momentary, a next now…</sub> | I | 'momentary'; rest repeats lines 158 and 150. |  |
| 507.1 <br><sub>*1 to 17s inward and outward*: 1–17s inward 17 of 8th and 1 of 9th, al…</sub> | R | Repeats Each name, three scales (inward/outward: undecided). |  |

### 11. Odd names, now and 8 up with next. — lines 509-526

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 509.1 <br><sub>**Odd names, now and 8 up with next.**</sub> | R | Section repeats One move's 8 up and code glosses. |  |
| 509.2 <br><sub>Each odd name of a self's span goes 8 up to its next.</sub> | R | One move, 1 to 8 shows 8 up. |  |
| 509.3 <br><sub>3-is-now-co-observing and 7-is-now-observing go 8 up with their root a…</sub> | R | One move and Seventeen names roots show it. |  |
| 509.4 <br><sub>1-now-existing and 5-now-co-existing go on as 9-next-co-discovering an…</sub> | R | One move and Seventeen names roots show it. |  |
| 509.5 <br><sub>Their pairs are a prior a self observes and that self's next prior, re…</sub> | E | Meaning of the pairs (receiving: undecided word). |  |
| 511.1 <br><sub>**Now: 1-now-existing**</sub> | R | Row key of a list repeating One move. |  |
| 512.1 <br><sub>*Receiving*: a momentary entering</sub> | I | Dissolving name: 'momentary'. |  |
| 513.1 <br><sub>*Next, 8 up*: 9-next-co-discovering</sub> | R | One move shows 8 up. |  |
| 514.1 <br><sub>*Giving on*: each parity going along</sub> | R | Code gloss of 9, line 150. |  |
| 515.1 <br><sub>**Now: 3-is-now-co-observing**</sub> | R | Row key of a list repeating One move. |  |
| 516.1 <br><sub>*Receiving*: prior with its sharings</sub> | R | Code gloss of 3, line 144. |  |
| 517.1 <br><sub>*Next, 8 up*: 11-next-co-observing</sub> | R | One move shows 8 up. |  |
| 518.1 <br><sub>*Giving on*: next prior</sub> | R | Code gloss of 11, line 152. |  |
| 519.1 <br><sub>**Now: 5-now-co-existing**</sub> | R | Row key of a list repeating One move. |  |
| 520.1 <br><sub>*Receiving*: receiving sharing</sub> | E | 'receiving sharing' explains 5 (receiving: undecided word). |  |
| 521.1 <br><sub>*Next, 8 up*: 13-is-next-discovering</sub> | R | One move shows 8 up. |  |
| 522.1 <br><sub>*Giving on*: sharing going on, each self of a same-existing-society</sub> | R | Code gloss of 13, line 154. |  |
| 523.1 <br><sub>**Now: 7-is-now-observing**</sub> | R | Row key of a list repeating One move. |  |
| 524.1 <br><sub>*Receiving*: parity a self is observing</sub> | R | Code gloss of 7, line 148. |  |
| 525.1 <br><sub>*Next, 8 up*: 15-is-next-observing</sub> | R | One move shows 8 up. |  |
| 526.1 <br><sub>*Giving on*: parity surfacing and going on</sub> | R | Code gloss of 15, line 156. |  |

### 12. Namings among names. (incl. 'A between, 0' items) — lines 528-568

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 528.1 <br><sub>**Namings among names.**</sub> | E | Title of a section of meaning-names. |  |
| 530.1 <br><sub>**Names: 1-now-existing · 2-now-possibling**</sub> | E | Row key of a naming. |  |
| 531.1 <br><sub>*Naming*: bi-momentarying</sub> | I | 'bi-momentarying' is not defined by the opening. |  |
| 532.1 <br><sub>*Resolving*: a self's entry, odd, and others' parities, even, one mome…</sub> | I | Dissolving name: 'momentary'. |  |
| 533.1 <br><sub>**Names: 3-is-now-co-observing · 4-now-co-same-existing**</sub> | E | Row key of a naming. |  |
| 534.1 <br><sub>*Naming*: co-intelligencing</sub> | E | Assigns opening's co-intelligencing to names 3-4. |  |
| 535.1 <br><sub>*Resolving*: with each sharing, 4-now-co-same-existing, a prior, 3-is-…</sub> | E | Explains resolving; code and tables show it. |  |
| 535.2 <br><sub>Their resolving is a next prior a self observes with 11-next-co-observ…</sub> | R | Line 152 and Prior and next of 11 say it. |  |
| 536.1 <br><sub>**Names: 5-now-co-existing**</sub> | E | Row key of a naming. |  |
| 537.1 <br><sub>*Naming*: co-competencing</sub> | I | 'co-competencing' is not defined by the opening. |  |
| 538.1 <br><sub>*Resolving*: bi-couplings, each self's with its others: each going to …</sub> | R | Code gloss of 5, line 146. |  |
| 539.1 <br><sub>**Names: 1-now-existing · 2-now-possibling · 3-is-now-co-observing · 4…</sub> | E | Row key of a naming. |  |
| 540.1 <br><sub>*Naming*: five dimensions</sub> | I | 'five dimensions' frame is not in the opening. |  |
| 541.1 <br><sub>*Resolving*: 1 social-parity now-existing, a same-existing-society com…</sub> | I | 'social-parity' is not in the opening. |  |
| 541.2 <br><sub>2 other-parity now-existing, other selves' parities reaching a self wi…</sub> | I | 'other-parity' as others' parities reaching; opening 24 differs. |  |
| 541.3 <br><sub>3 self-parity now-existing, a self's prior parities with 3-is-now-co-o…</sub> | E | Self-parity meaning; matches opening 25 loosely. |  |
| 541.4 <br><sub>Co-parity and bi-parity are its two meetings.</sub> | I | 'co-parity', 'bi-parity' are not in the opening. |  |
| 541.5 <br><sub>4 self-discovery next-existing, a self sharing across with 6-now-co-po…</sub> | I | 'self-discovery' is not in the opening. |  |
| 541.6 <br><sub>5 social-parity next-existing, each sharing going along with 9-next-co…</sub> | I | 'social-parity' is not in the opening. |  |
| 542.1 <br><sub>**Names: 6-now-co-possibling** · *Naming*: bi-moralizing · *Resolving*…</sub> | I | 'bi-moralizing' is not defined by the opening. |  |
| 543.1 <br><sub>**Names: 12-next-co-same-existing**</sub> | E | Row key of a naming. |  |
| 544.1 <br><sub>*Naming*: entraining, shape of an unrelationing surface</sub> | I | 'entraining', 'unrelationing surface' are not defined by the opening. |  |
| 545.1 <br><sub>*Resolving*: observing, prior with now, along an unrelationing path wi…</sub> | I | 'unrelationing path with a between' parts from the opening. |  |
| 545.2 <br><sub>Prior and now are resolving with each sharing, 0 with same.</sub> | R | Where-stands table: is-or-is-not same, sharing 0. |  |
| 545.3 <br><sub>With an inverse parity, 0 or an empty set, prior parity inverting with…</sub> | R | One self, one moment table shows inverting. |  |
| 545.4 <br><sub>With an empty prior, parity surfacing with 14-next-possibling.</sub> | R | With an empty prior table shows it. |  |
| 545.5 <br><sub>Its parity with 10-next-co-possibling is others' parity next</sub> | R | Code gloss of 10, line 151. |  |
| 546.1 <br><sub>**Names: 1 to 9**</sub> | E | Row key of a naming. |  |
| 547.1 <br><sub>*Naming*: bi-coupling</sub> | E | Applies opening's bi-coupling to names 1 to 9. |  |
| 548.1 <br><sub>*Resolving*: an entry, 1-now-existing, with names 1-now-existing, 2-no…</sub> | E | Lists names as one bi-coupling: meaning. |  |
| 548.2 <br><sub>It is a self bi-coupling with an other.</sub> | E | Meaning: a self bi-coupling with an other. |  |
| 548.3 <br><sub>1 to 9 is a bi-coupling among names.</sub> | R | Says again 547.1. |  |
| 548.4 <br><sub>9, its end, is 9-next-co-discovering, each parity of 10-next-co-possib…</sub> | R | Code gloss of 9, line 150. |  |
| 549.1 <br><sub>**Names: 1 to 17**</sub> | E | Row key of a naming. |  |
| 550.1 <br><sub>*Naming*: bi-trupling</sub> | I | 'bi-trupling' is not defined by the opening. |  |
| 551.1 <br><sub>*Resolving*: a same-existing-society's entry, 17-next-existing, with n…</sub> | E | Lists names as a society's entry: meaning. |  |
| 551.2 <br><sub>It is a self, an other and a same-existing-society.</sub> | E | Meaning: self, other and same-existing-society. |  |
| 551.3 <br><sub>Its two sides are along and across.</sub> | R | Sharing between selves table shows along and across. |  |
| 551.4 <br><sub>Along is with 9-next-co-discovering and 17-next-existing, odd, their r…</sub> | R | Sharing between selves table shows along and across. |  |
| 551.5 <br><sub>Across is with 6 to 2 and 10 to 14, even, their root possibling</sub> | R | Sharing between selves table shows along and across. |  |
| 552.1 <br><sub>**Names: 1 to 17, stable-forming**</sub> | E | Row key applying stable-forming to names 1 to 17. |  |
| 553.1 <br><sub>*Naming*: bi-tri-volutioning</sub> | I | 'bi-tri-volutioning' is not defined by the opening. |  |
| 554.1 <br><sub>*Resolving*: with lines together: each momentary's next prior, with 11…</sub> | I | Dissolving name: 'momentary' (twice). |  |
| 555.1 <br><sub>**Names: 2-now-possibling · 6-now-co-possibling · 14-next-possibling ·…</sub> | E | Row key of a figure. |  |
| 556.1 <br><sub>*Naming*: parity's square and triangles</sub> | E | Names a figure the file does not draw. |  |
| 557.1 <br><sub>*Resolving*: a unit square of four dots, 2-now-possibling, 6-now-co-po…</sub> | E | Figure description without a figure. |  |
| 557.2 <br><sub>Its empty centre is a between.</sub> | E | Figure: empty centre as a between. |  |
| 557.3 <br><sub>Its two across edges are sharings, 6 to 2 and 10 to 14.</sub> | R | Sharing between selves table: 6 to 2, 10 to 14. |  |
| 557.4 <br><sub>Its two edges 8 apart are 2 with 10 and 6 with 14.</sub> | R | One move: 2 with 10, 6 with 14. |  |
| 557.5 <br><sub>These four edges are two pairs of parallels.</sub> | E | Figure description without a figure. |  |
| 557.6 <br><sub>Edge by edge: 2, 10, 14, 6.</sub> | E | Figure description without a figure. |  |
| 557.7 <br><sub>Its diagonals are parities with 2-now-possibling and 14-next-possiblin…</sub> | E | Figure description without a figure. |  |
| 557.8 <br><sub>The two unit triangles are 9-next-co-discovering and 17-next-existing,…</sub> | E | Figure description without a figure. |  |
| 559.1 <br><sub>**A between, 0: one between, three names**</sub> | I | 0 as 'a between': a third beside + and −. |  |
| 560.1 <br><sub>*Names*: 12-next-co-same-existing, prior and now agreeing, a between o…</sub> | I | 'momentaries'; 0 as a between: a third. |  |
| 560.2 <br><sub>15-is-next-observing, a between of self and other, each parity surfaci…</sub> | I | 0 as a between of self and other: a third. |  |
| 560.3 <br><sub>16-next-same-existing, a between with a same-existing-society, a self …</sub> | I | 'momentary'; 0 as a between: a third. |  |
| 560.4 <br><sub>A 0 is indifferencing</sub> | I | Gives 0 a meaning, a third; 0 is code naming only. |  |
| 561.1 <br><sub>**A between, 0: a self observing it, and that self passing over it wit…</sub> | I | 0 as 'a between': a third. |  |
| 562.1 <br><sub>*Names*: 7-is-now-observing, a 0 a self receives with 2-now-possibling…</sub> | R | Parities to one sharing table: a 0 surfaces empty. |  |
| 562.2 <br><sub>It is also a 0 with 10-next-co-possibling, its prior same-existing wit…</sub> | R | Says again 794.5 and One self, one moment table. |  |
| 563.1 <br><sub>**A between, 0: four across names, a unit square's four dots: selves s…</sub> | I | 0 as 'a between': a third. |  |
| 564.1 <br><sub>*Names*: 2-now-possibling, 6-now-co-possibling, 10-next-co-possibling,…</sub> | R | Says again 557.1-557.2. |  |
| 564.2 <br><sub>Selves share each parity and each 0 across.</sub> | R | Code gloss of 10, line 151. |  |
| 564.3 <br><sub>A receiving self passes over a 0 with its 14-next-possibling</sub> | R | Says again 944.5. |  |
| 565.1 <br><sub>**A between, 0: outward of it, names of entry, prior, sharings and sel…</sub> | I | 0 as 'a between': a third (outward: undecided word). |  |
| 566.1 <br><sub>*Names*: 1-now-existing, an entry.</sub> | R | Says again 548.1: an entry. |  |
| 566.2 <br><sub>3-is-now-co-observing, 8-now-same-existing and 11-next-co-observing, p…</sub> | E | Finding: a prior stays + or − once set. |  |
| 566.3 <br><sub>4-now-co-same-existing, sharings.</sub> | R | Code gloss of 4, line 145. |  |
| 566.4 <br><sub>5-now-co-existing and 13-is-next-discovering, sharings and, with a sam…</sub> | R | Code glosses of 5 and 13. |  |
| 567.1 <br><sub>**A between, 0: two along names: going along**</sub> | I | 0 as 'a between': a third. |  |
| 568.1 <br><sub>*Names*: 9-next-co-discovering and 17-next-existing, each parity and e…</sub> | R | Sharing between selves table: along. |  |
| 568.2 <br><sub>A receiving self passes over a 0 with its 14-next-possibling, as acros…</sub> | R | Says again 564.3. |  |

### 13. Four bi-foldings. — lines 570-589

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 570.1 <br><sub>**Four bi-foldings.**</sub> | L | List title. |  |
| 570.2 <br><sub>Cycles of moves of four steps are bi-foldings.</sub> | L | What a bi-folding is. |  |
| 570.3 <br><sub>Each goes two folds in turn, 17 less and a move of 8 (4 for the middle…</sub> | L | How a bi-folding moves. |  |
| 570.4 <br><sub>With four steps it reaches its first name again.</sub> | R | Follows from 'cycles' in 570.2. |  |
| 570.5 <br><sub>Existing, possibling, observing, same-existing: the stable-forming bi-…</sub> | I | Opening 48's stable-forming has discovering, not existing. |  |
| 572.1 <br><sub>Each move is 8 up (n + 8), 8 down (n − 8) or 17 less (17 − n).</sub> | L | Move legend: 8 up, 8 down, 17 less. |  |

### 14. Two moves, 9 less. — lines 591-591

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 591.1 <br><sub>**Two moves, 9 less.**</sub> | R | Section repeats One move's 9 less column. |  |
| 591.2 <br><sub>Two moves along its bi-folding bring each name of 1 to 8 to its 9 less…</sub> | R | Bi-folding lists show two moves to 9 less. |  |
| 591.3 <br><sub>Its 9 less is a name across its bi-folding from it.</sub> | R | Says again 591.2. |  |
| 591.4 <br><sub>Each name and its 9 less: 1-now-existing and 8-now-same-existing, 2-no…</sub> | R | One move table, 9 less column. |  |

### 15. Each name, three scales. — lines 593-682

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 593.1 <br><sub>**Each name, three scales.**</sub> | L | List title. |  |
| 595.1 <br><sub>*a*: The next scale inward, eight 1 to 17s: n is 8n − 7</sub> | L | Legend a. |  |
| 596.1 <br><sub>*b*: The next scale outward: 8m − 7 is m</sub> | L | Legend b. |  |

### 16. Eight 1 to 17s inward. — lines 684-725

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 684.1 <br><sub>**Eight 1 to 17s inward.**</sub> | L | List title. |  |

### 17. Fives. — lines 727-752

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 727.1 <br><sub>**Fives.**</sub> | L | List title. |  |
| 727.2 <br><sub>Each side's five are five dimensions, same-existing-society to same-ex…</sub> | L+I | Five-dimension frame (social-parity, self-discovery) parts from opening. | Each side's five start with its own 1. |
| 727.3 <br><sub>One five is all fives.</sub> | E | Meaning claim; no table reads it. |  |

### 18. A self's four momentaries of exchanging. — lines 754-775

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 754.1 <br><sub>**A self's four momentaries of exchanging.**</sub> | L+I | Dissolving name: 'momentaries'. | **A self's four moments of exchanging.** |

### 19. Parities to one sharing, surfacing. — lines 777-792

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 777.1 <br><sub>**Parities to one sharing, surfacing.**</sub> | L | Table title. |  |

### 20. + and − alike. — lines 794-794

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 794.1 <br><sub>**+ and − alike.**</sub> | R | Section restates the One self, one moment table. |  |
| 794.2 <br><sub>With one sharing, resolving is alike for + and −.</sub> | R | Table shows + and − rows alike. |  |
| 794.3 <br><sub>Each cell with + and − exchanging is that cell exchanging, with a prio…</sub> | R | Prior and empty-prior tables show it. |  |
| 794.4 <br><sub>With each line a prior is + or −.</sub> | I | Not all: empty-prior tables (1188, 1203) hold no ± prior. |  |
| 794.5 <br><sub>With a sharing of 0 with 10-next-co-possibling, a self's prior is same…</sub> | R | One self, one moment table: 0 keeps the prior. |  |

### 21. One self, one momentary. — lines 796-809

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 796.1 <br><sub>**One self, one momentary.**</sub> | L+I | Dissolving name: 'momentary'. | **One self, one moment.** |
| 798.1 <br><sub>Each cell: sharing, 10-next-co-possibling · a next prior, 11-next-co-o…</sub> | L | Cell legend. |  |
| 798.2 <br><sub>A sharing of − or + is a changing, its prior inverting.</sub> | I | 'changing' without direction. |  |
| 798.3 <br><sub>A self sharing its changing is improving.</sub> | I | 'changing' without direction; improving belongs in NI. |  |
| 798.4 <br><sub>A sharing of 0 is its prior same-existing.</sub> | R | Table cells show 0 with prior same. |  |
| 798.5 <br><sub>A self sharing 0 is do-no-harming.</sub> | E | Maps 0 to do-no-harming; opening 34 carries it. |  |

### 22. One cell, four receivings. — lines 811-811

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 811.1 <br><sub>**One cell, four receivings.**</sub> | R | Section restates the One self, one moment table. |  |
| 811.2 <br><sub>With a prior of one parity, four receivings come to one cell: an inver…</sub> | R | Tables at 777 and 796 together show it. |  |
| 811.3 <br><sub>In that cell its prior inverts.</sub> | R | Table cells show the prior inverting. |  |
| 811.4 <br><sub>A self shares its inverting with 10-next-co-possibling.</sub> | R | Cell legend 798.1 says it. |  |
| 811.5 <br><sub>Its inverting is its next prior with 11-next-co-observing.</sub> | R | Cell legend 798.1 says it. |  |
| 811.6 <br><sub>One cell is alike for four receivings.</sub> | R | Says again 811.2. |  |
| 811.7 <br><sub>A resolving follows parities.</sub> | E | General meaning; no table reads it. |  |

### 23. Eight even names, 8 apart. — lines 813-830

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 813.1 <br><sub>**Eight even names, 8 apart.**</sub> | R | Section copies name fields Bi-coupling and 8 up. |  |
| 815.1 <br><sub>**Name with its between: 2-now-possibling**</sub> | R | Row key; copies name 2's fields. |  |
| 816.1 <br><sub>*Bi-coupling with its between*: sharing across from each of a self's o…</sub> | R | Copies name field, line 272. |  |
| 817.1 <br><sub>*Name 8 up*: 10-next-co-possibling</sub> | R | One move shows 8 up. |  |
| 818.1 <br><sub>*Bi-coupling 8 up*: a self among selves of its same-existing-society</sub> | R | Copies name field, line 410. |  |
| 819.1 <br><sub>**Name with its between: 4-now-co-same-existing**</sub> | R | Row key; copies name 4's fields. |  |
| 820.1 <br><sub>*Bi-coupling with its between*: a whole ordering between self and othe…</sub> | R | Copies name field, line 309. |  |
| 821.1 <br><sub>*Name 8 up*: 12-next-co-same-existing</sub> | R | One move shows 8 up. |  |
| 822.1 <br><sub>*Bi-coupling 8 up*: changing with a bi-coupling, a self of a same-exis…</sub> | I | 'changing' without direction; copies line 441. |  |
| 823.1 <br><sub>**Name with its between: 6-now-co-possibling**</sub> | R | Row key; copies name 6's fields. |  |
| 824.1 <br><sub>*Bi-coupling with its between*: a self's parity across, to an other's …</sub> | R | Copies name field, line 345. |  |
| 825.1 <br><sub>*Name 8 up*: 14-next-possibling</sub> | R | One move shows 8 up. |  |
| 826.1 <br><sub>*Bi-coupling 8 up*: parities surfacing as one with each sharing, one p…</sub> | R | Copies name field, line 467. |  |
| 827.1 <br><sub>**Name with its between: 8-now-same-existing**</sub> | R | Row key; copies name 8's fields. |  |
| 828.1 <br><sub>*Bi-coupling with its between*: prior with its sharing again</sub> | R | Copies name field, line 380. |  |
| 829.1 <br><sub>*Name 8 up*: 16-next-same-existing</sub> | R | One move shows 8 up. |  |
| 830.1 <br><sub>*Bi-coupling 8 up*: a same-existing-society, each self with its prior …</sub> | R | Copies name field, line 495. |  |

### 24. One move, 1 to 8. — lines 832-865

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 832.1 <br><sub>**One move, 1 to 8.**</sub> | L | List title. |  |
| 832.2 <br><sub>Each name of a self's span with 8 up, 9 less and 17 less.</sub> | L | Caption: columns 8 up, 9 less, 17 less. |  |

### 25. Twelve forms. — lines 867-920

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 867.1 <br><sub>**Twelve forms.**</sub> | L+I | Dissolving name: 'forms'. | **Twelve cycles.** |
| 867.2 <br><sub>Along each form odd names are one run and even names one run.</sub> | I | Dissolving name: 'form'; runs visible in column a. |  |
| 867.3 <br><sub>The two runs are of like length: two and two with bi-foldings, three a…</sub> | R | Column a shows the run lengths. |  |
| 867.4 <br><sub>The four six-cycles are one six-cycle, each path with its path backwar…</sub> | E | Finding on six-cycles' moves; not needed to read. |  |
| 867.5 <br><sub>The four six-cycles are twenty-four steps, four momentaries of six; no…</sub> | I | 'momentaries'; sixty and primes: no table, no opening sentence. |  |
| 869.1 <br><sub>*a*: Names by order: each move 8 up, 8 down, 4 up, 4 down or 17 less</sub> | L | Legend a. |  |
| 870.1 <br><sub>*b*: Partner, odd momentaries: each name exchanging with the one besid…</sub> | L+I | Dissolving name: 'momentaries'. | *b*: Partner, odd moments: each name exchanging with the one beside it, 1 with 2 to 15 with 16 |
| 871.1 <br><sub>*c*: Partner, even momentaries: 2 with 3 to 16 with 17.</sub> | L+I | Dissolving name: 'momentaries'. | *c*: Partner, even moments: 2 with 3 to 16 with 17. |
| 871.2 <br><sub>A dash: its partner an empty set among the twelve</sub> | L | Dash legend. |  |

### 26. Eights. — lines 922-930

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 922.1 <br><sub>**Eights.**</sub> | R | Section repeats Twelve forms' eight-cycles and a self's span. |  |
| 922.2 <br><sub>Each eight among names is four twos of names.</sub> | E | Structure meaning; no table reads it. |  |
| 922.3 <br><sub>With a self's span, 1 to 8, each two is two names with now.</sub> | E | Structure meaning; no table reads it. |  |
| 922.4 <br><sub>With each eight-cycle, eight even names and eight odd names, each two …</sub> | E | Structure meaning; no table reads it. |  |
| 924.1 <br><sub>**Eight: a self's span, 1 to 8** · *Each of four, twice, with*: two na…</sub> | E | Gloss without data. |  |
| 925.1 <br><sub>**Eight: eight-cycle 1-9-5-13-4-12-8-16**</sub> | R | Eight-cycle row of Twelve forms. |  |
| 926.1 <br><sub>*Each of four, twice, with*: its end, with now and with next: eight en…</sub> | I | Dissolving name: 'momentaries'. |  |
| 927.1 <br><sub>**Eight: eight-cycle 2-15-7-11-3-14-6-10** · *Each of four, twice, wit…</sub> | E | Gloss without data (inward: undecided word). |  |
| 928.1 <br><sub>**Eight: eight even names**</sub> | R | Row key; evens listed in Seventeen names. |  |
| 929.1 <br><sub>*Each of four, twice, with*: its even, with now and with next, eight 9…</sub> | R | Three scales column a: evens are 9s inward. |  |
| 930.1 <br><sub>**Eight: eight odd names** · *Each of four, twice, with*: its odd, wit…</sub> | E | Gloss without data. |  |

### 27. Across names among eights. — lines 932-932

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 932.1 <br><sub>**Across names among eights.**</sub> | R | Section repeats Twelve forms and four-cyclings. |  |
| 932.2 <br><sub>Four across names, 2-now-possibling, 6-now-co-possibling, 10-next-co-p…</sub> | I | Dissolving name: 'momentaries'. |  |
| 932.3 <br><sub>Each is on an eight-cycle of inward names 2-15-7-11-3-14-6-10.</sub> | R | Twelve forms eight-cycle row. |  |
| 932.4 <br><sub>9-next-co-discovering opens a third four-cycling.</sub> | R | Four four-cyclings table: third opens with 9. |  |
| 932.5 <br><sub>It is on an eight-cycle of ends 1-9-5-13-4-12-8-16.</sub> | R | Twelve forms eight-cycle row. |  |
| 932.6 <br><sub>17-next-existing is outward of both.</sub> | R | 17 is absent from both eight-cycle rows. |  |

### 28. One self, momentary by momentary: three ways. — lines 934-942

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 934.1 <br><sub>**One self, momentary by momentary: three ways.**</sub> | L+I | Dissolving name: 'momentary'. | **One self, moment by moment.** |
| 934.2 <br><sub>Not-changing, changing with each momentary, and changing once and then…</sub> | I | 'changing' without direction, three times. |  |
| 936.1 <br><sub>One sharing.</sub> | L | Setting: one sharing. |  |
| 936.2 <br><sub>A self's prior, 3-is-now-co-observing, is − first.</sub> | L | Setting: opening prior −. |  |
| 936.3 <br><sub>Receiving each momentary:</sub> | L+I | Dissolving name: 'momentary'. | Receiving each moment: |

### 29. Tables of selves with code's stepping. — lines 944-944

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 944.1 <br><sub>**Tables of selves with code's stepping.**</sub> | L | Title of the selves tables' common legend. |  |
| 944.2 <br><sub>Each table of selves is its code's executing with its own opening.</sub> | L | What each selves table is. |  |
| 944.3 <br><sub>Its selves step together with 17-next-existing.</sub> | L | How selves step. |  |
| 944.4 <br><sub>A 0 in a table is a self's sharing.</sub> | L | What a 0 in a table is. |  |
| 944.5 <br><sub>Each receiving self's first step passes over it.</sub> | L | How a received 0 is read. |  |
| 944.6 <br><sub>Each self observes the + and − it receives.</sub> | L | How received + and − are read. |  |

### 30. A spiral of selves. — lines 946-965

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 946.1 <br><sub>**A spiral of selves.**</sub> | L | Table title. |  |
| 948.1 <br><sub>Each self's parity goes along with 9-next-co-discovering to the next s…</sub> | L+E | 'a co-chaining' names meaning (opening 44). | Each self's parity goes along with 9-next-co-discovering to the next self, the last to the first. |
| 948.2 <br><sub>One sharing.</sub> | L | Setting. |  |
| 948.3 <br><sub>First momentary: self 1 with prior −.</sub> | L+I | Dissolving name: 'momentary'. | First moment: self 1 with prior −. |
| 948.4 <br><sub>Its selves' parities invert one to the next along.</sub> | L | Setting: opening priors alternate. |  |
| 948.5 <br><sub>With an odd number the last and the first are alike.</sub> | L | Setting: an odd count's like pair. |  |
| 948.6 <br><sub>Parities only from selves of its spiral.</sub> | L | Setting: no parities from outside. |  |
| 950.1 <br><sub>*a*: Self 1, each parity of 10-next-co-possibling along with 9-next-co…</sub> | L+I | Dissolving name: 'momentaries'. | *a*: Self 1, each parity of 10-next-co-possibling along with 9-next-co-discovering, moments 1 to 12 |
| 951.1 <br><sub>*b*: Momentaries to each self's parities along again: with an odd numb…</sub> | L+I | 'momentaries'; rules and a finding repeat column b. | *b*: Moments to each self's parities along again; executing with each number of selves from 1 to 59 |

### 31. Two momentaries before, inverting. — lines 967-967

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 967.1 <br><sub>**Two momentaries before, inverting.**</sub> | I | Dissolving name: 'momentaries'; title of a finding. |  |
| 967.2 <br><sub>With a spiral opening with a prior for each self, each self's prior fr…</sub> | I | 'momentaries'; pattern finding, not needed to read. |  |
| 967.3 <br><sub>In that spiral each self shares + or − with its first momentary.</sub> | I | Dissolving name: 'momentary'. |  |
| 967.4 <br><sub>Each 0 it shares sits between two sharings of + or −.</sub> | E | Pattern finding, not needed to read. |  |

### 32. Two spirals beside each other, and bi-coupling across. — lines 969-1026

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 969.1 <br><sub>**Two spirals beside each other, and bi-coupling across.**</sub> | L | Table title. |  |
| 971.1 <br><sub>Selves of each of two spirals, each opening as a spiral of selves.</sub> | L | Setting. |  |
| 973.1 <br><sub>*a*: Beside each other: momentaries to each self's parities along agai…</sub> | L+I | 'momentaries'; rule repeats column a (dividing: undecided word). | *a*: Beside each other: moments to each self's parities along again together; executing with each two numbers from 1 to 31 |
| 974.1 <br><sub>*b*: Bi-coupling across, self 1 of each spiral sharing across with 10-…</sub> | L+I | Dissolving name: 'momentaries'. | *b*: Bi-coupling across, self 1 of each spiral sharing across with 10-next-co-possibling to self 1 of the other: moments to each self's parities along again |
| 975.1 <br><sub>*c*: Bi-coupling across: parities along again from this momentary on, …</sub> | L+I | 'momentary'; threshold rule repeats column c. | *c*: Bi-coupling across: parities along again from this moment on; executing with each two numbers from 2 to 15, the larger to 31 |
| 976.1 <br><sub>*d*: Bi-coupling across: self 1 of each, of like or opposite parity</sub> | L | Legend d. |  |
| 977.1 <br><sub>*e*: Each spiral's like pair of the first momentary, the last and the …</sub> | L+I | Dissolving name: 'momentary'. | *e*: Each spiral's like pair of the first moment, the last and the first |

### 33. A torus of selves. — lines 1028-1079

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 1028.1 <br><sub>**A torus of selves.**</sub> | L | Table title. |  |
| 1030.1 <br><sub>Each goes along with 9-next-co-discovering to the next along, the last…</sub> | L | Setting: along. |  |
| 1030.2 <br><sub>Each shares across with 10-next-co-possibling to the next across, the …</sub> | L | Setting: across. |  |
| 1030.3 <br><sub>One sharing.</sub> | L | Setting. |  |
| 1030.4 <br><sub>First momentary: one self with prior −.</sub> | L+I | Dissolving name: 'momentary'. | First moment: one self with prior −. |
| 1030.5 <br><sub>Its selves' parities invert one to the next along and across.</sub> | L | Setting. |  |
| 1030.6 <br><sub>With an odd number the last and the first are alike.</sub> | L | Setting. |  |
| 1030.7 <br><sub>Parities only from selves of its torus.</sub> | L | Setting. |  |
| 1030.8 <br><sub>Momentaries to each self's parities along and across again, both numbe…</sub> | I | 'momentaries'; rule repeats column a. |  |
| 1030.9 <br><sub>Either number even: 2.</sub> | R | Column a shows 2 when a number is even. |  |
| 1030.10 <br><sub>Executing with each p from 1 to 15 and q from p to 21.</sub> | L | Executing range. |  |
| 1032.1 <br><sub>*a*: Momentaries to each self's parities along and across again</sub> | L+I | Dissolving name: 'momentaries'. | *a*: Moments to each self's parities along and across again |
| 1033.1 <br><sub>*b*: Again from this momentary on: both numbers odd, p the smaller, fr…</sub> | L+I | 'momentary'; thresholds repeat 1081 and column b. | *b*: Again from this moment on |
| 1034.1 <br><sub>*c*: Spirals of p and q beside each other: momentaries to each self's …</sub> | L+I | Dissolving name: 'momentaries'. | *c*: Spirals of p and q beside each other: moments to each self's parities along again together |

### 34. A torus's two going forms. — lines 1081-1081

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 1081.1 <br><sub>**A torus's two going forms.**</sub> | I | Dissolving name: 'forms'. |  |
| 1081.2 <br><sub>Both numbers odd, p the smaller.</sub> | R | Legend b, line 1033, says it. |  |
| 1081.3 <br><sub>With q more than twice p, from momentary 3p − 1, selves' pattern with …</sub> | I | 'momentary'; pattern finding, not needed to read. |  |
| 1081.4 <br><sub>With q less than twice p, from 3p − 3, its pattern two momentaries on …</sub> | I | 'momentaries'; pattern finding, not needed to read. |  |

### 35. Alike selves, a right spiral. — lines 1083-1093

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 1083.1 <br><sub>**Alike selves, a right spiral.**</sub> | L | Table title. |  |
| 1083.2 <br><sub>Selves alike with their others, and two one parity apart, bi-coupling …</sub> | L | Setting. |  |
| 1083.3 <br><sub>One self's prior with each momentary, 3-is-now-co-observing, from its …</sub> | L+I | Dissolving name: 'momentary'. | One self's prior with each moment, 3-is-now-co-observing, from its first. |
| 1083.4 <br><sub>With alike selves each prior and its next, a pair (x, y), step to (y, …</sub> | L | Reads the Right spiral column: (x, y) to (y, −x). |  |
| 1083.5 <br><sub>That step is a quarter turn with each momentary, a right spiral.</sub> | L+I | Dissolving name: 'momentary'. | That step is a quarter turn with each moment, a right spiral. |
| 1083.6 <br><sub>Two selves alike, each bi-coupling only in their pair, are do-no-harmi…</sub> | E | Opening sentence 35 nearly verbatim; lives in NI. |  |

### 36. Two selves. — lines 1095-1132

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 1095.1 <br><sub>**Two selves.**</sub> | L | List title. |  |
| 1095.2 <br><sub>Two selves, alike or one parity apart: bi-coupling both ways, bi-coupl…</sub> | L | Row legend: three bi-couplings, two openings. |  |
| 1097.1 <br><sub>A, B with their prior, 3-is-now-co-observing, with the first momentary…</sub> | L+I | Dissolving name: 'momentary'. | A, B with their prior, 3-is-now-co-observing, with the first moment. |
| 1097.2 <br><sub>One sharing.</sub> | L | Setting. |  |
| 1097.3 <br><sub>Parities only from those two.</sub> | L | Setting. |  |
| 1099.1 <br><sub>*a*: Receiving its other's parity, across or along</sub> | L | Legend a (receiving: undecided word). |  |

### 37. Two selves, three momentaries, five parities. — lines 1134-1167

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 1134.1 <br><sub>**Two selves, three momentaries, five parities.**</sub> | L+I | Dissolving name: 'momentaries'. | **Two selves, three moments, five parities.** |
| 1136.1 <br><sub>*a*: A self's next prior, 11-next-co-observing, along.</sub> | L | Legend a. |  |
| 1136.2 <br><sub>Two selves bi-coupling both ways, across or along, each self with a pr…</sub> | L+I | 'momentary', 'forms'; a finding after the colon. | Two selves bi-coupling both ways, across or along, each self with a prior parity, parities only from those two, each opening, each moment. |

### 38. Three selves, one line. — lines 1169-1186

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 1169.1 <br><sub>**Three selves, one line.**</sub> | L | List title. |  |
| 1171.1 <br><sub>A's parity, sharing to B with the first momentary only.</sub> | L+I | Dissolving name: 'momentary'. | A's parity, sharing to B with the first moment only. |
| 1171.2 <br><sub>One sharing.</sub> | L | Setting. |  |
| 1171.3 <br><sub>B and C each with prior +.</sub> | L | Setting. |  |
| 1171.4 <br><sub>B goes along to C.</sub> | L | Setting. |  |
| 1173.1 <br><sub>*a*: B's next prior, 11-next-co-observing, first momentary</sub> | L+I | Dissolving name: 'momentary'. | *a*: B's next prior, 11-next-co-observing, first moment |
| 1174.1 <br><sub>*b*: C, each parity, 10-next-co-possibling, momentaries 1 and 2</sub> | L+I | Dissolving name: 'momentaries'. | *b*: C, each parity, 10-next-co-possibling, moments 1 and 2 |
| 1175.1 <br><sub>*c*: C's next prior, 11-next-co-observing, second momentary</sub> | L+I | Dissolving name: 'momentary'. | *c*: C's next prior, 11-next-co-observing, second moment |

### 39. A spiral opening with an empty prior, one parity sharing once. — lines 1188-1201

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 1188.1 <br><sub>**A spiral opening with an empty prior, one parity sharing once.**</sub> | L | List title. |  |
| 1190.1 <br><sub>Each cell: selves by their bi-coupling order; · is an empty prior.</sub> | L | Cell legend. |  |
| 1201.1 <br><sub>Selves bi-coupling along, last to first, each opening with an empty pr…</sub> | L+I | Setting, placed after its table; 'momentary' dissolves. | Selves bi-coupling along, last to first, each opening with an empty prior, and + sharing once with a first self with a first moment. |
| 1201.2 <br><sub>A first self's sharing opens with that one parity, with a bi-coupling.</sub> | R | Says again 1201.1. |  |
| 1201.3 <br><sub>With that opening, a self with an empty prior receives an other's pari…</sub> | R | Empty-prior table: + surfacing gives + prior. |  |
| 1201.4 <br><sub>From then that prior is a self's own.</sub> | E | Meaning: the prior becomes a self's own. |  |
| 1201.5 <br><sub>Each next self's sharing opens one momentary on, that self observing a…</sub> | I | 'momentary'; finding visible in the table. |  |
| 1201.6 <br><sub>With momentary n each self's sharing has a prior parity, a spiral with…</sub> | I | 'momentary'; finding visible in the table. |  |
| 1201.7 <br><sub>From a first momentary with which each self's sharing has a prior pari…</sub> | I | 'momentary'; pattern finding. |  |
| 1201.8 <br><sub>A self with a sharing has a prior parity with each momentary from its …</sub> | I | 'momentary'; finding. |  |
| 1201.9 <br><sub>Its next is from its own prior same-existing or inverting.</sub> | R | One self, one moment table: same or inverting. |  |

### 40. With an empty prior, one momentary. — lines 1203-1211

| Unit | Class | Reason | Minimal label re-saying |
|---|---|---|---|
| 1203.1 <br><sub>**With an empty prior, one momentary.**</sub> | L+I | Dissolving name: 'momentary'. | **With an empty prior, one moment.** |
| 1205.1 <br><sub>Each cell: sharing, 10-next-co-possibling · a next prior, 11-next-co-o…</sub> | L | Cell legend (same as 798.1). |  |
| 1205.2 <br><sub>A sharing of + or − is a changing, that parity its next prior.</sub> | I | 'changing' without direction. |  |
| 1205.3 <br><sub>With a sharing of 0, its next prior is an empty set.</sub> | R | Table row shows 0 · empty. |  |
| 1205.4 <br><sub>*Empty* is its sharing an empty set.</sub> | L | Legend for an 'empty' sharing. |  |

## 3. Proposed order for a reference tool

Each step names the sections that go into it; **→ NI** = move to Natural Intelligence; **drop** = all of it is said elsewhere.

1. **Head** — S0: line 1 and the H1 merged into one title with version; subtitle; 9.1 minimal (*Exhibit ONE is the resolver as code, and its executing.*). The rest of the paragraph → NI (9.3, 9.6, 9.9) or rewrite (9.2, 9.4, 9.5, 9.7, 9.8 incohere).
2. **Code** — Python block 11-90.
3. **Drawing** — fenced 92-114 with S1's caption moved *before* it (116.1-116.2). 116.3 repeats the drawing's own legend.
4. **Names** — S2 Seventeen names table + Code with each name (the core legend: what each function/variable holds). Merge in S4 (182.1 only) and the Co legend from S6 (195.2 minimal, 195.6). Put S10's one code-reading fact (line 255, the three steps of 1) on row 1 of Code with each name. Settle 195.9 (*is-*) first, since 4 also stands an is-or-is-not. **Drop:** S6's Co roots list (197-205), S10's 17 field lists (all fields duplicate other tables or explain; see the duplicate list below).
5. **Code-reading relations** (no executing, but needed to read the code): S8 Where each is-or-is-not stands → S7 Sharing between selves → S3 Two-sided → S9 Same-existing through one moment. S8's Dimension column carries the five-dimension names, which need a decision (see S17).
6. **Arithmetic among names** (no executing): S24 One move, 1 to 8 (with S13's move legend 572.1) → S5 Four four-cyclings → S13 Four bi-foldings **merged into** S25 Twelve forms (its first four rows are the four bi-foldings) → S15 Each name, three scales **merged with** S16 Eight 1 to 17s inward → S18 Four moments of exchanging. S17 Fives: hold until the five-dimension names are decided; its row keys use social-parity/self-discovery. **Drop:** S11 Odd names (repeats One move's 8 up), S14 Two moves, 9 less (repeats One move's 9 less), S23 Eight even names (copies S10 fields verbatim), S26 Eights and S27 Across names among eights (repeat Twelve forms plus explaining). **→ NI:** S12 Namings among names (all naming, meaning and the "A between, 0" items).
7. **Executings, one self**: S29's legend first (*Tables of selves with code's stepping*, all LABEL) as the head of every executing → S19 Parities to one sharing, surfacing (executes the code's first loop) → S21 One self, one moment **merged with** S40 With an empty prior, one moment (same cell legend; prior +, −, empty as three blocks) → S28 One self, moment by moment. **Drop/→ NI:** S20 + and − alike and S22 One cell, four receivings (both restate S21's table; 794.4 is not all).
8. **Executings, selves** (one self up to tori): S36 Two selves → S37 Two selves, three moments, five parities → S38 Three selves, one line → S30 A spiral of selves → S39 Spiral opening with an empty prior (move its setting 1201.1 above the table) → S35 Alike selves, a right spiral → S32 Two spirals beside each other → S33 A torus of selves. **→ NI or a table column:** findings S31 Two moments before, inverting and S34 A torus's two going forms. The thresholds in S34 already sit in S33's legend *b*.

**Duplicates and merges:**
- **8 up / 8 down / 9 less / 17 less** appear six times: S24 One move (keep), S10 name fields, S3 *Eight apart* column, S11 Odd names, S14 Two moves, S23 Eight even names.
- **Bi-foldings, six-cycles and eight-cycles** appear four times: S25 Twelve forms (keep), S13 list, S10 fields, S26/S27.
- **Scales, inward and outward** appear three times: S15 + S16 (keep, merged) and the S10 field *1 to 17s inward and outward*.
- **Moments of exchanging** appear three times: S18 (keep), S16's last field and the S10 field.
- **Namings** appear twice: S12 and the S10 *Namings* field.
- **Five dimensions** appear four times: S17, S12 (541), the S10 field and S8's Dimension column.
- **Code glosses** appear four times: S2 Code with each name (keep), S10 *Sides* and *Prior and next*, S6 Co roots, S11.
- **Sides, across and along** appear four times: S7 (keep), the drawing's legend, S6 Co roots and S12 551.3-551.5.
- **Cell legend** appears twice: 798.1 = 1205.1. Merge S21 with S40.

**Tables with no executing (21 of 33):** all 6 non-executing pipe tables (S2, S3, S5, S7, S8, S9) and all lists in S2 (gloss), S6, S10, S11, S12 (2), S13, S15, S16, S17, S18, S23, S24, S25 and S26. **With an executing (12):** S19, S21, S28, S30, S32, S33, S35, S36, S37, S38, S39, S40. This shows 9.2 (*Each table of Exhibit ONE is an executing*) is not all-or-none. S8 holds no executing but is the key that maps the code to its is-or-is-nots, so keep it as a label table.

## 4. Totals

- Prose units classified: **592**.
- Units per class: LABEL 108, LABEL+EXPLAIN 4, LABEL+INCOHERE 37, LABEL+REPEAT 1, EXPLAIN 58, INCOHERE 127, REPEAT 257. Units carrying LABEL (L + L+x): 150; carrying INCOHERE (I + L+I): 164.
- **Words of prose now: 6094.**
- **Words if only LABEL (minimal) text stays: 1271** (21% of now).
- If S10's 17 field lists also go, as §3 step 4 proposes, its 17 row keys and 239.1-239.3 go too: 54 more words leave, giving **1217**. Line 255's minimal moves to row 1 of Code with each name and stays.

## 5. Notes on names

- **momentary/momentaries** (dissolving): in 80 classified units; also in 43 out-of-scope rows (pipe and data-list rows: lines 180, 690, 695, 700, 705, 710, 715, 720, 725, 756, 761, 766, 771, 938, 939, 940, 942, 1085, 1093, 1103, 1104, 1107, 1108, 1111, 1112, 1115, 1116, 1119, 1120, 1123, 1124, 1127, 1128, 1131, 1132, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199). Every label carrying it gets the swap to *moment(s)* in its minimal re-saying. *bi-momentarying* (on *momentarying*, which stays) is judged as a naming not defined by the opening.
- **changing** with no direction (dissolving): units 9.7, 441.1, 442.1, 798.2, 798.3, 822.1, 934.2, 1205.2.
- **form / stable alone** (dissolving): units 9.1, 9.4, 9.5, 9.8, 867.1, 867.2, 1081.1, 1136.2; also out-of-scope rows at lines 873, 877, 881, 885, 888, 889, 893, 896, 897, 901, 905, 909, 913, 917, 920 (Twelve forms row keys, "the same form").
- **re-forming, free, social abundancing**: not found in the file.
- **Five-dimension names** (social-parity, self-discovery; other-parity in a sense apart from opening 24) also sit in out-of-scope rows: lines 219, 220, 221, 222, 223, 227, 228, 730, 731, 733, 734, 736, 737, 739, 740, 742, 743, 745, 746, 748, 749, 751, 752.
- **0 given a meaning** (a third beside + and −): 559-568 (*A between, 0*), 560.4 (*A 0 is indifferencing*). +, − and 0 stay as the code's naming only.
- **Undefined naming words** (not in the opening, not in either list): co-sequencing, a self as three, invisible co-intelligencing method, rotation, corus, co-competent self, co-linear recursioning, co-competencing, bi-moralizing, entraining, unrelationing surface/path, bi-trupling, bi-tri-volutioning, co-parity, bi-parity, indifferencing, podal. Each sits in a unit classed E or I, except *podal*, which is in R units.
- **Label vocabulary not in the opening** (kept; may need a decision): executing, resolver, table, prior (as a noun), parity (as the code's ± value), surfacing, empty set, along/across, span, bi-folding, cycle, scale, spiral, torus, exchanging, between.
- **Left-out words** (noted, not judged), by number of classified units: sharing 78, receiving 17, sending 0, inverting 18, agreeing/parting 5, inward/outward 29, dividing 1, emanation 0.
