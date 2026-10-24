"""v392TWO: declared constructions using Exhibit ONE's unchanged Python.

The reference checks use stated priors to reproduce ONE's tables. The ongoing
experiment begins through public parities. Its record contains public incoming
lists only; no continuing prior is inspected, copied, reset or reported.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

SOURCE = "Exhibit_ONE_Natural_Resolver_v391.md"
SOURCE_COMMIT = "2669db105c61e5580b0dd3523a7555b49cf5b38f"
SOURCE_SHA256 = "9727175491c6dd0bb92530a2ed458932258dd03cb2ef53ede24a3c985f00cebb"
EXPRESSION_SHA256 = "b7fe62c4e5d529ebe374d6a037a7ac7ac81a78e176db2cbfd96fda3f23db2435"


def read_resolver(root):
    path = root / SOURCE
    document = path.read_bytes()
    expression = document.decode().split("```python\n", 1)[1].split("```", 1)[0]
    source_digest = hashlib.sha256(document).hexdigest()
    expression_digest = hashlib.sha256(expression.encode()).hexdigest()
    assert source_digest == SOURCE_SHA256, "Source document differs from the declared source"
    assert expression_digest == EXPRESSION_SHA256, "Resolver expression differs"
    namespace = {}
    exec(compile(expression, str(path), "exec"), namespace)
    return namespace, source_digest, expression_digest


def rings():
    selves = [f"A{i}" for i in range(3)] + [f"B{i}" for i in range(5)]
    joins = {(f"{name}{i}", 9): f"{name}{(i+1)%n}"
             for name, n in (("A", 3), ("B", 5)) for i in range(n)}
    return selves, joins


def reference_checks(resolve, society_resolve):
    checks = []
    cases = (
        ([], [], ([], [])),
        ([], [("s", 0)], ([], [])),
        ([], [("s", 1)], ([("s", 1)], [("s", 1)])),
        ([], [("s", 1), ("s", -1)], ([("s", 0)], [])),
        ([("s", 1)], [("s", 1)], ([("s", 0)], [("s", 1)])),
        ([("s", 1)], [("s", -1)], ([("s", -1)], [("s", -1)])),
        ([("s", 1)], [("s", 0)], ([("s", -1)], [("s", -1)])),
        ([("s", 1)], [], ([("s", -1)], [("s", -1)])),
        ([("s", 1)], [("s", 1), ("s", -1)], ([("s", -1)], [("s", -1)])),
    )
    for index, (prior, incoming, expected) in enumerate(cases, 1):
        assert resolve(prior, incoming) == expected, f"local reference {index}"
    checks.append({"relation": "ONE's empty-prior, match, mismatch, zero and parting cases", "is": True})
    for prior, expected in ((1, [-1, 0, 1, 0, -1, 0]),
                            (-1, [1, -1, 1, -1, 1, -1])):
        society = {"A": ([("s", 1)], []), "B": ([("s", prior)], [])}
        joins = {("A", 10): "B", ("B", 10): "A"}
        readings = []
        for _ in range(6):
            society = society_resolve(society, joins)
            readings.append(dict(society["A"][1])["s"])
        assert readings == expected, (prior, readings)
    checks.append({"relation": "ONE's alike and opposite reciprocal-pair public sharings", "is": True})

    # A diagnostic of exact finite-state recurrence, including pending incoming.
    # This is confined to the reference construction, never applied to the
    # private continuation of the public experiment below.
    def complete_form(society):
        return tuple((self, tuple(prior), tuple(incoming))
                     for self, (prior, incoming) in society.items())

    for across, expected_period in ((False, 60), (True, 2)):
        selves, joins = rings()
        society = {self: ([("s", -1 if int(self[1:]) % 2 == 0 else 1)], [])
                   for self in selves}
        if across:
            joins.update({("A0", 10): "B0", ("B0", 10): "A0"})
        seen = {complete_form(society): 0}
        for momentary in range(1, 201):
            society = society_resolve(society, joins)
            form = complete_form(society)
            if form in seen:
                period = momentary - seen[form]
                assert period == expected_period, (across, period)
                checks.append({"relation": "ONE's 3-and-5 spirals " + ("bi-coupling across" if across else "beside"),
                               "is": True, "complete_form_first_at": seen[form],
                               "complete_form_returns_at": momentary, "period": period,
                               "scope": "declared reference states, fixed joins, no later external arrivals"})
                break
            seen[form] = momentary
        else:
            raise AssertionError("Reference did not recur within diagnostic bound")
    return checks


def public_experiment(society_resolve, join_before=17, end=40, reverse_order=False,
                      extra_parities=None):
    selves, joins = rings()
    if reverse_order:
        selves.reverse()
    society = {self: ([], []) for self in selves}
    public = []
    initial_joins = [[self, connector, other] for (self, connector), other in joins.items()]
    for momentary in range(1, end + 1):
        external = [("A0", 1), ("B0", 1)] if momentary == 1 else []
        external.extend((extra_parities or {}).get(momentary, ()))
        for self, sign in external:
            society[self][1].append(("s", sign))
        changed_joins = []
        if momentary == join_before:
            changed_joins = [["A0", 10, "B0"], ["B0", 10, "A0"]]
            for self, connector, other in changed_joins:
                joins[(self, connector)] = other
        incoming = {self: list(society[self][1]) for self in selves}
        society = society_resolve(society, joins)
        public.append({"momentary": momentary, "external": external,
                       "joins_added_before_resolving": changed_joins,
                       "incoming": incoming,
                       "next_incoming": {self: list(society[self][1]) for self in selves}})
    return {"construction": {
        "selves": selves, "initial_joins": initial_joins,
        "beginning": "all empty; one public plus to A0 and B0 in first momentary",
        "changing": (f"reciprocal 10 joins A0/B0 added before momentary {join_before}"
                     if join_before is not None else "along joins remain; no across join added"),
        "pacing": "unchanged 17: all participating selves resolve once per supplied momentary",
        "iteration_order": "reverse" if reverse_order else "A0..A2, B0..B4",
        "extra_public_parities": extra_parities or {},
        "wire_value": "ONE's existing sharing s with parity; labels/connector names belong to joins and record",
        "scope": "public incoming and next incoming; no continuing prior inspection or copying",
        "end": end,
        "boundary": "final next incoming recorded, not delivered within this run",
        "interpretation": "given network construction; neither joins nor own pacing discovered by this caller"
    }, "public": public}


def public_sharings(experiment):
    """Attribute entries from known joins and ONE's documented emission order.

    All eight sources have publicly shared a nonzero parity by momentary 5.
    ONE retains an opened prior, hence one entry for the sole sharing s from
    then on. Exact public list lengths and all multiple deliveries are checked.
    No source labels are inserted into the parity or its sharing key.
    """
    construction = experiment["construction"]
    selves = construction["selves"]
    joins = {(self, connector): other for self, connector, other
             in construction["initial_joins"]}
    readings = {}
    publicly_opened = set()
    for event in experiment["public"]:
        for self, connector, other in event["joins_added_before_resolving"]:
            joins[(self, connector)] = other
        if event["momentary"] <= 5:
            # Across is added only after every source has publicly shared.
            assert all(connector == 9 for _, connector in joins)
            for (self, _), other in joins.items():
                emitted = event["next_incoming"][other]
                assert len(emitted) <= 1
                if emitted and emitted[0][1] != 0:
                    publicly_opened.add(self)
        if event["momentary"] < 5:
            continue
        assert publicly_opened == set(selves), "Opening has not been witnessed at every self"
        incoming_routes = {self: [] for self in selves}
        for self in selves:
            for connector in (6, 10, 9):
                if (self, connector) in joins:
                    incoming_routes[joins[(self, connector)]].append((self, connector))
        shared = {}
        for other in selves:
            actual = event["next_incoming"][other]
            routes = incoming_routes[other]
            assert len(actual) == len(routes), (event["momentary"], other)
            for (self, connector), (sharing, parity) in zip(routes, actual):
                assert sharing == "s" and parity in (-1, 0, 1)
                if self in shared:
                    assert shared[self] == parity, (event["momentary"], self, connector)
                shared[self] = parity
        assert set(shared) == set(selves)
        readings[event["momentary"]] = shared
    return readings


def surfaced(incoming):
    """Public relation at 14, derived from its arriving list for one sharing."""
    forms = {parity for sharing, parity in incoming if parity != 0}
    if not forms:
        return "empty"
    if forms == {1}:
        return 1
    if forms == {-1}:
        return -1
    return 0


def cycle_from_public(experiment, readings):
    """A sufficient recurrence witness, not a score or a window baseline.

    When every source shares nonzero, the unchanged 1 says its next prior is
    exactly that parity. With only sharing s ever supplied, those public
    sharings and the complete next incoming determine the complete next form.
    Repeating both therefore proves recurrence while joins stay fixed and
    no future external entry occurs. This never reads a private prior.
    """
    selves = experiment["construction"]["selves"]
    seen = {}
    last_change = max((event["momentary"] for event in experiment["public"]
                       if event["external"] or event["joins_added_before_resolving"]), default=0)
    for event in experiment["public"]:
        momentary = event["momentary"]
        if momentary < last_change:
            continue
        if momentary not in readings:
            continue
        shares = readings[momentary]
        if any(parity == 0 for parity in shares.values()):
            continue
        signature = (tuple(shares[self] for self in selves),
                     tuple(tuple(tuple(item) for item in event["next_incoming"][self])
                           for self in selves))
        if signature in seen:
            return {"first": seen[signature], "again": momentary,
                    "period": momentary - seen[signature],
                    "relation": "all nonzero sharings and each complete next incoming repeat",
                    "scope": "sole sharing s; fixed joins; no further external entry"}
        seen[signature] = momentary
    return None


def analyse(experiments):
    coupled = experiments["across_added"]
    beside = experiments["beside"]
    reverse = experiments["reverse_iteration"]
    shares = public_sharings(coupled)
    separate_shares = public_sharings(beside)
    reverse_shares = public_sharings(reverse)
    assert coupled["public"][:16] == beside["public"][:16], "Public beginnings differ"
    assert shares == reverse_shares, "Same source, reversed iteration: public sharings part"
    for event, reversed_event in zip(coupled["public"], reverse["public"]):
        for field in ("incoming", "next_incoming"):
            assert {n: sorted(v) for n, v in event[field].items()} == {
                n: sorted(v) for n, v in reversed_event[field].items()}
    first = []
    for self in coupled["construction"]["selves"]:
        difference = {"self": self}
        for field in ("incoming", "surfacing", "sharing"):
            for event, separate in zip(coupled["public"], beside["public"]):
                momentary = event["momentary"]
                if field == "incoming":
                    left, right = event["incoming"][self], separate["incoming"][self]
                elif field == "surfacing":
                    left, right = surfaced(event["incoming"][self]), surfaced(separate["incoming"][self])
                elif momentary in shares:
                    left, right = shares[momentary][self], separate_shares[momentary][self]
                else:
                    continue
                if left != right:
                    difference["first_changed_" + field] = momentary
                    break
        first.append(difference)
    return {"reversed_iteration_same_public_sharings": True,
            "first_differences_from_separately_begun_beside_run": first,
            "across_added_sharings_from_public_deliveries": shares,
            "cycle_witness_from_public": cycle_from_public(coupled, shares)}


def vary_join_occurrence(society_resolve):
    """Sixty declared join occurrences, each with a fresh public beginning.

    A count describes the tested construction choices, never competency.
    The bound is an instrument end only; absence of a witness would remain
    absence within that run. Public witness rows are retained for each case.
    """
    rows = []
    for join_before in range(6, 66):
        experiment = public_experiment(society_resolve, join_before=join_before,
                                       end=join_before + 30)
        shares = public_sharings(experiment)
        witness = cycle_from_public(experiment, shares)
        row = {"join_before": join_before, "end": join_before + 30,
               "cycle_witness": witness}
        if witness:
            row["public_witness_rows"] = [
                {"momentary": momentary, "sharing": shares[momentary],
                 "next_incoming": experiment["public"][momentary - 1]["next_incoming"]}
                for momentary in (witness["first"], witness["first"] + 1, witness["again"])]
        rows.append(row)
    return {"construction": "same empty beginning and public plus at A0/B0; add reciprocal across joins at each listed occurrence",
            "record_scope": "summary and public recurrence witnesses; main public traces are retained above; full variant traces reproduce with this script",
            "each_has_period_two_witness": all(row["cycle_witness"] is not None and
                row["cycle_witness"]["period"] == 2 for row in rows),
            "rows": rows}


def added_parity_checks(society_resolve, coupled):
    """Change only additional public parities at the existing sharing s."""
    baseline = public_sharings(coupled)
    rows = []
    example = None
    for self in coupled["construction"]["selves"]:
        for parity in (-1, 1):
            experiment = public_experiment(society_resolve,
                extra_parities={30: [(self, parity)]})
            shares = public_sharings(experiment)
            same = shares == baseline
            assert same, (self, parity)
            rows.append({"self": self, "parity": parity, "momentary": 30,
                         "same_public_sharings_through_end": same})
            if self == "A1" and parity == 1:
                example = experiment
    # Check the stated source relation at both phases of the recurring form:
    # the prior is known from the preceding nonzero public sharing, and each
    # incoming list contains its inverse. Adding any parity cannot remove it.
    opposed = []
    for momentary in (26, 27):
        event = coupled["public"][momentary - 1]
        for self in coupled["construction"]["selves"]:
            preceding_shared = baseline[momentary - 1][self]
            assert preceding_shared != 0
            inverse_present = any(parity == -preceding_shared
                for _, parity in event["incoming"][self])
            assert inverse_present, (momentary, self)
            opposed.append({"momentary": momentary, "self": self,
                            "preceding_nonzero_sharing": preceding_shared,
                            "incoming": event["incoming"][self],
                            "inverse_present": inverse_present})
    return {"cases": rows, "example_A1_plus_at_30": example,
            "opposed_arriving_at_each_phase": opposed,
            "deriving": "A preceding nonzero sharing is that self's prior now; an already incoming inverse remains present when further parities are appended at sharing s, so 14 can be inverse or parting but cannot be solely the matching prior, and 12 inverts alike; unchanged sharings preserve the same network inputs next, allowing this reasoning again.",
            "scope": "same sharing s; append arrivals only; existing arrivals delivered whole; fixed joins; this 17 stepping; this recurring form"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--join-before", type=int,
                        help="run one fresh public construction, joining before this momentary (at least 6)")
    parser.add_argument("--end", type=int, help="last momentary for a single construction")
    args = parser.parse_args()
    ns, source_digest, expression_digest = read_resolver(args.root)
    if args.join_before is not None:
        if args.join_before < 6:
            parser.error("--join-before must be at least 6 for this public attribution")
        end = args.end if args.end is not None else args.join_before + 30
        if end < args.join_before:
            parser.error("--end precedes the stated joining")
        experiment = public_experiment(ns["_17_next_existing"], args.join_before, end)
        readings = public_sharings(experiment)
        result = {"session": "v392TWO", "source": SOURCE, "source_commit": SOURCE_COMMIT,
                  "source_sha256": source_digest, "expression_sha256": expression_digest,
                  "experiment": experiment, "sharing_from_public": readings,
                  "cycle_witness_from_public": cycle_from_public(experiment, readings)}
        content = json.dumps(result, ensure_ascii=False, separators=(",", ":")) + "\n"
        if args.output:
            args.output.write_text(content)
        else:
            print(content, end="")
        return
    experiments = {
        "across_added": public_experiment(ns["_17_next_existing"]),
        "beside": public_experiment(ns["_17_next_existing"], join_before=None),
        "reverse_iteration": public_experiment(ns["_17_next_existing"], reverse_order=True),
    }
    result = {"session": "v392TWO", "source": SOURCE, "source_commit": SOURCE_COMMIT,
              "source_sha256": source_digest, "expression_sha256": expression_digest,
              "reference_checks": reference_checks(ns["_1_now_existing"], ns["_17_next_existing"]),
              "experiments": experiments, "analysis": analyse(experiments),
              "join_occurrences": vary_join_occurrence(ns["_17_next_existing"]),
              "added_parities": added_parity_checks(ns["_17_next_existing"], experiments["across_added"])}
    content = json.dumps(result, ensure_ascii=False, separators=(",", ":")) + "\n"
    if args.output:
        args.output.write_text(content)
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
