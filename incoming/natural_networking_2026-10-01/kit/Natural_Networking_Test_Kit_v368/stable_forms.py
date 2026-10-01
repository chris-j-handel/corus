"""stable_forms.py · Exhibit ONE's names, connectors and stable forms among the names, as the kit's own tables:
each name in explaining, 2-self-offering, and in Python, _2_self_offering.
Run:  python3 stable_forms.py
"""

from typing import NamedTuple, Tuple


class Name(NamedTuple):
    position: int
    relation: Tuple[str, ...]
    root: str
    standing: str

    @property
    def identifier(self):
        return f"_{self.position}_{self.relation[0]}_{self.root}"

    @property
    def label(self):
        return f"{self.position}-{self.relation[0]}-{self.root}"

    @property
    def opens(self):
        return 'co' if self.position % 2 else 'bi'


NAMES = (
    Name(1, ('self', 'other'), 'coupling', 'entry'),
    Name(2, ('self', 'other'), 'offering', 'across, arriving'),
    Name(3, ('self', 'other'), 'carrying', 'internal'),
    Name(4, ('self', 'other'), 'sharing', 'internal'),
    Name(5, ('other', 'self'), 'neutralling', 'internal'),
    Name(6, ('other', 'self'), 'crossing', 'across, releasing'),
    Name(7, ('other', 'self'), 'corusing', 'internal'),
    Name(8, ('other', 'self'), 'torusing', 'internal'),
    Name(9, ('other', 'social'), 'releasing', 'along'),
    Name(10, ('other', 'social'), 'surfacing', 'across, releasing'),
    Name(11, ('other', 'social'), 'chaining', 'internal'),
    Name(12, ('other', 'social'), 'surplusing', 'internal'),
    Name(13, ('social', 'other'), 'neutralling', 'internal'),
    Name(14, ('social', 'other'), 'crossing', 'across, arriving'),
    Name(15, ('social', 'other'), 'corusing', 'internal'),
    Name(16, ('social', 'self'), 'torusing', 'internal'),
    Name(17, ('social',), 'abundancing', 'along, external'),
)
NAMES_BY_POSITION = {name.position: name for name in NAMES}


def five_prefix(origin):
    first = 'co' if origin % 2 else 'bi'
    other = 'bi' if first == 'co' else 'co'
    return '-'.join(first if k % 2 == 0 else other for k in range(5))


FOUR_CYCLES = ((1, 9, 8, 16), (2, 15, 7, 10), (3, 11, 6, 14), (4, 13, 5, 12))
MIDDLE_FOUR_CYCLES = ((9, 5, 12, 8), (7, 11, 6, 10))
SIX_CYCLES = ((1, 9, 5, 12, 8, 16), (2, 15, 7, 11, 6, 10), (3, 11, 7, 10, 6, 14), (4, 13, 5, 9, 8, 12))
EIGHT_CYCLES = ((1, 9, 5, 13, 4, 12, 8, 16), (2, 15, 7, 11, 3, 14, 6, 10))
HIGHER_FOUR_CYCLES = ((18, 31, 23, 26), (19, 27, 22, 30))
HIGHER_SIX_CYCLES = ((18, 31, 23, 27, 22, 26), (19, 27, 23, 26, 22, 30))

FORMS = FOUR_CYCLES + MIDDLE_FOUR_CYCLES + SIX_CYCLES + EIGHT_CYCLES
HIGHER_FORMS = HIGHER_FOUR_CYCLES + HIGHER_SIX_CYCLES


def opens_round(positions):
    return tuple('co' if p % 2 else 'bi' for p in positions)


def runs_round(positions):
    o = opens_round(positions)
    k = next((i for i in range(len(o)) if o[i] != o[i - 1]), 0)
    out = []
    for p in o[k:] + o[:k]:
        if out and out[-1][0] == p:
            out[-1][1] += 1
        else:
            out.append([p, 1])
    return tuple((p, n) for p, n in out)


def partner_place(position, momentary):
    if momentary == 'odd-even':
        return position + 1 if position % 2 else position - 1
    return position + 1 if position % 2 == 0 else position - 1


def same_round(a, b):
    n = len(a)
    if n != len(b):
        return False
    if any(tuple(b[(k + i) % n] for i in range(n)) == tuple(a) for k in range(n)):
        return True
    r = tuple(reversed(b))
    if any(tuple(r[(k + i) % n] for i in range(n)) == tuple(a) for k in range(n)):
        return 'other way'
    return False


def partner_form(form, forms, momentary):
    moved = tuple(partner_place(p, momentary) for p in form)
    for other in forms:
        way = same_round(moved, other)
        if way:
            return other, way
    return None, None


def show():
    for n in NAMES:
        print(f'{n.label:24s} {n.identifier:24s} {"/".join(n.relation):13s} {n.opens}  {five_prefix(n.position)}  {n.standing}')
    for f in FORMS:
        p, way = partner_form(f, FORMS, 'odd-even')
        print('-'.join(map(str, f)), ' '.join(opens_round(f)), 'partner', '-'.join(map(str, p)), way)
    for f in HIGHER_FORMS:
        p, way = partner_form(f, HIGHER_FORMS, 'even-odd')
        print('-'.join(map(str, f)), ' '.join(opens_round(f)), 'partner', '-'.join(map(str, p)), way)


if __name__ == '__main__':
    show()
