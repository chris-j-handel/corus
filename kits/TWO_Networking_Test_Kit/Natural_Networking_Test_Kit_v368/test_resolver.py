"""test_resolver.py · the kit's checks at Exhibit ONE's resolver, each returning is or is not.
Run:  python3 -m unittest -v test_resolver
"""

import ast
import itertools
import os
import unittest

import resolver
import stable_forms as forms

HERE = os.path.dirname(os.path.abspath(__file__))
PRIMES = tuple(p for p in range(2, 60) if all(p % d for d in range(2, p)))


def function(name):
    with open(os.path.join(HERE, 'resolver.py')) as f:
        tree = ast.parse(f.read())
    return next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)


def names_in(fn):
    return ({n.id for n in ast.walk(fn) if isinstance(n, ast.Name)}
            | {a.arg for a in ast.walk(fn) if isinstance(a, ast.arg)} | {fn.name})


def sgn(v):
    return (v > 0) - (v < 0)


def alternating(n, start=1):
    return [start if i % 2 == 0 else -start for i in range(n)]


def joining_at_joints(selves):
    seed, start = [], 1
    for p in selves:
        part = alternating(p, start)
        seed += part
        start = -part[-1]
    return seed


def ring_running(seed, beats, way=1):
    n = len(seed)
    _5_other_neutralling = {i: (i + way) % n for i in range(n)}
    _10_other_surfacing, _3_self_carrying, rows = [(i, seed[i]) for i in range(n)], [], []
    for _ in range(beats):
        rows.append(tuple(dict(_10_other_surfacing).get(i, 0) for i in range(n)))
        _10_other_surfacing, _3_self_carrying = resolver._1_self_coupling(
            _3_self_carrying, resolver._9_other_releasing(_10_other_surfacing, _5_other_neutralling))
    return rows


def surface_running(seed, beats):
    n = len(seed)
    rows = [tuple(seed)]
    now = [seed[(i - 1) % n] for i in range(n)]
    last = list(now)
    rows.append(tuple(now))
    while len(rows) < beats:
        now = [sgn(now[(i - 1) % n] - last[i]) for i in range(n)]
        rows.append(tuple(now))
        last = [now[i] if now[i] else last[i] for i in range(n)]
    return rows


def joints(row):
    return [i for i in range(len(row)) if row[i] != 0 and row[i] == row[(i + 1) % len(row)]]


def travelling_joints(row):
    n = len(row)
    return [i for i in range(n) if row[i] == 0 or row[i] == row[(i + 1) % n]]


def self_at(p):
    rows = ring_running(alternating(p), 4 * p + 3)
    home = next(t for t in range(1, 4 * p + 2) if rows[1 + t] == rows[1])
    opposite = next((t for t in range(1, home) if rows[1 + t] == tuple(-x for x in rows[1])), 0)
    return len(travelling_joints(rows[1])), home, opposite


def society_of(selves, beats=8):
    rows = ring_running(joining_at_joints(selves), beats)
    return len(rows[0]), len(travelling_joints(rows[1])), all(rows[t + 2] == rows[t] for t in range(1, beats - 2))


class TheResolver(unittest.TestCase):
    def test_holding_its_two_functions_and_its_connectors(self):
        self.assertEqual({n for n in vars(resolver) if not n.startswith('__')},
                         {'_1_self_coupling', '_9_other_releasing', 'CONNECTORS', 'JOINS'})
        self.assertEqual(sorted(resolver.CONNECTORS), [2, 6, 9, 10, 14, 17])
        self.assertEqual(resolver.JOINS, {10: 14, 6: 2, 17: 9, 9: 17})

    def test_the_sixteen_names_and_no_other(self):
        first, release = names_in(function('_1_self_coupling')), names_in(function('_9_other_releasing'))
        sixteen = {n.identifier for n in forms.NAMES[:16]}
        self.assertEqual(first | release, sixteen)
        self.assertEqual(sorted(forms.NAMES_BY_POSITION[int(i.split('_')[1])].position for i in release), [5, 9, 10, 13, 15])

    def test_the_half_turn(self):
        for s, t in itertools.product((1, -1), repeat=2):
            self.assertEqual(resolver._1_self_coupling([('k', s, t, 0)], []), ([('k', -s)], [('k', -s, -t, 0)]))

    def test_the_releasing_carries_every_sign(self):
        self.assertEqual(resolver._9_other_releasing([('a', 1), ('b', 0), ('c', -1)], {'a': 'b', 'b': 'c', 'c': 'a'}),
                         [('b', 1), ('c', 0), ('a', -1)])

    def test_one_way_at_a_time_at_rings(self):
        for n in range(2, 9):
            for way in (1, -1):
                for seed in itertools.product((1, -1), repeat=n):
                    stands, carrying = {i: seed[i] for i in range(n)}, []
                    rows = ring_running(list(seed), 4 * n + 4, way)
                    for b in range(len(rows)):
                        self.assertEqual(rows[b], tuple(stands.get(i, 0) for i in range(n)))
                        arriving = [(i, stands[(i - way) % n]) for i in range(n) if stands.get((i - way) % n)]
                        surfacing, carrying = resolver._1_self_coupling(carrying, arriving)
                        stands = {i: m for i, m in surfacing if m != 0}


class TheNames(unittest.TestCase):
    def test_seventeen_names_each_single(self):
        self.assertEqual(len({n.identifier for n in forms.NAMES}), 17)
        for n in forms.NAMES:
            self.assertTrue(n.identifier.isidentifier())
            self.assertEqual(n.opens == 'co', n.position % 2 == 1)

    def test_standings(self):
        self.assertEqual({n.position for n in forms.NAMES if n.standing.startswith(('across', 'along'))}, {2, 6, 9, 10, 14, 17})


class TheStableForms(unittest.TestCase):
    def test_a_single_run_of_co_and_of_bi(self):
        for f in forms.FORMS + forms.HIGHER_FORMS:
            runs = forms.runs_round(f)
            self.assertEqual({p for p, _ in runs}, {'co', 'bi'})
            self.assertEqual(runs[0][1], runs[1][1])

    def test_the_four_and_the_eight_cycles_meet_every_name(self):
        self.assertEqual(sorted(p for c in forms.FOUR_CYCLES for p in c), list(range(1, 17)))
        self.assertEqual(sorted(p for c in forms.EIGHT_CYCLES for p in c), list(range(1, 17)))

    def test_partners(self):
        self.assertTrue(all(forms.partner_form(f, forms.FORMS, 'odd-even')[1] == 'other way' for f in forms.FORMS))
        self.assertEqual(len([f for f in forms.FORMS if forms.partner_form(f, forms.FORMS, 'even-odd')[0]]), 7)
        self.assertTrue(all(forms.partner_form(f, forms.HIGHER_FORMS, 'even-odd')[1] == 'other way' for f in forms.HIGHER_FORMS))


class TheRunning(unittest.TestCase):
    def test_odd_rings_a_joint_at_odd_beats_a_rest_at_even(self):
        for n in range(3, 30, 2):
            rows = ring_running(alternating(n), 4 * n + 3)
            for b in range(1, len(rows)):
                if b % 2:
                    self.assertEqual((len(joints(rows[b])), rows[b].count(0)), (1, 0))
                else:
                    self.assertEqual((rows[b].count(0), len(joints(rows[b]))), (1, 0))

    def test_the_step_at_the_surface_meets_the_resolver(self):
        for n in range(2, 9):
            for seed in itertools.product((1, -1), repeat=n):
                self.assertEqual(ring_running(list(seed), 4 * n + 8), surface_running(list(seed), 4 * n + 8))

    def test_the_prime_selves(self):
        for p in PRIMES:
            self.assertEqual(self_at(p), (0, 2, 1) if p == 2 else (1, 4 * p, 2 * p))

    def test_prime_selves_joining(self):
        for p, q in itertools.combinations_with_replacement(PRIMES[1:], 2):
            self.assertEqual(society_of((p, q))[1:], (0, True))
        self.assertEqual(society_of(PRIMES[1:] + (2,)), (440, 0, True))
        self.assertEqual(society_of((59, 59)), (118, 0, True))
        for trio in itertools.combinations(PRIMES[1:7], 3):
            self.assertEqual(society_of(trio)[1:], (1, False))

    def test_a_composite_ring_runs_as_its_equal_selves_joining(self):
        for a in range(1, 12):
            for k in range(1, 8):
                self.assertEqual(joining_at_joints((a,) * k), alternating(a * k))


if __name__ == '__main__':
    unittest.main()
