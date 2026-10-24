"""v392TWO: carrying forming through two continuing sequences.

The exact Python expression in current Exhibit ONE is executed unchanged.
Starting priors are empty. Only the declared incoming sequences start them;
each next prior is passed onward solely by the resolver. Public sharing is
recorded; private priors are never inspected, copied, replaced or cleared.

The two boundary sequences are supplied test conditions, one parity each per
ONE society momentary. They are not independently paced living participants.
All labels, source positions and occurrence numbers belong to the instrument.
Only ONE's one sharing with its parity is passed between the resolvers.
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
FIRST_SEQUENCE = (1, 1, -1, -1)
SECOND_SEQUENCE = (1, 1, 1, -1, -1, -1)
SHARING = "sharing"


def read_resolver(root):
    document = (root / SOURCE).read_bytes()
    expression = document.decode().split("```python\n", 1)[1].split("```", 1)[0]
    assert hashlib.sha256(document).hexdigest() == SOURCE_SHA256
    assert hashlib.sha256(expression.encode()).hexdigest() == EXPRESSION_SHA256
    namespace = {}
    exec(compile(expression, str(root / SOURCE), "exec"), namespace)
    return namespace


def construction(form):
    if form in ("two selves bi-coupling", "two selves separately"):
        selves = ("self receiving the first sequence", "self receiving the second sequence")
        joins = {(selves[0], 10): selves[1], (selves[1], 10): selves[0]}
        if form == "two selves separately":
            joins = {}
        return selves, joins, selves
    assert form == "three along and five across"
    names = {}
    for along in range(3):
        for across in range(5):
            if (along, across) == (0, 0):
                name = "self receiving the first sequence"
            elif (along, across) == (0, 1):
                name = "self receiving the second sequence"
            else:
                path = []
                if along:
                    path.append("one self along" if along == 1 else "two selves along")
                if across:
                    path.append("one self across" if across == 1 else
                                ("two", "three", "four")[across - 2] + " selves across")
                name = "self reached from the first sequence by " + " and ".join(path)
            names[along, across] = name
    selves = tuple(names.values())
    joins = {}
    for (along, across), name in names.items():
        joins[name, 9] = names[(along + 1) % 3, across]
        joins[name, 10] = names[along, (across + 1) % 5]
    return selves, joins, (names[0, 0], names[0, 1])


def source_parities(momentary, program, first_shift=1, second_shift=1):
    first_offset = second_offset = 0
    phase = "original sequences"
    if program == "change second, return, withdraw, return":
        if 49 <= momentary <= 96:
            second_offset = second_shift
            phase = "second sequence further along by " + str(second_shift)
        elif 97 <= momentary <= 144:
            phase = "original sequences returning"
        elif 145 <= momentary <= 168:
            return [None, None], "no external sequences", (None, None)
        elif momentary >= 169:
            phase = "original sequences after no external sequences"
    elif program == "change first, then return":
        if 49 <= momentary <= 96:
            first_offset = first_shift
            phase = "first sequence further along by " + str(first_shift)
        elif momentary >= 97:
            phase = "original sequences returning"
    elif program == "different forming, then original sequences":
        if momentary <= 48:
            second_offset = 1
            phase = "second sequence one parity further along"
        else:
            phase = "original sequences after different forming"
    else:
        assert program == "original sequences throughout"
    parities = [FIRST_SEQUENCE[(momentary - 1 + first_offset) % len(FIRST_SEQUENCE)],
                SECOND_SEQUENCE[(momentary - 1 + second_offset) % len(SECOND_SEQUENCE)]]
    # The next source positions condition a recurrence under this phase's
    # continuation. They make no claim beyond a later declared intervention.
    next_positions = ((momentary + first_offset) % len(FIRST_SEQUENCE),
                      (momentary + second_offset) % len(SECOND_SEQUENCE))
    return parities, phase, next_positions


def execute(namespace, form, program, end=216, reverse_order=False, first_shift=1, second_shift=1):
    selves, joins, source_receivers = construction(form)
    execution_order = tuple(reversed(selves)) if reverse_order else selves
    society = {self: ([], []) for self in execution_order}
    indicated_prior = {self: None for self in selves}
    first_public_prior = {}
    public = []
    seen_in_phase = {}
    recurrence = []
    phase_before = None
    phase_first = None
    phase_closed = False

    for momentary in range(1, end + 1):
        parities, phase, next_positions = source_parities(momentary, program, first_shift, second_shift)
        if phase != phase_before:
            seen_in_phase = {}
            phase_first = momentary
            phase_closed = False
        for self, parity in zip(source_receivers, parities):
            if parity is not None:
                society[self][1].append((SHARING, parity))
        receiving = {self: [parity for sharing, parity in society[self][1]] for self in selves}
        for self in selves:
            assert all(sharing == SHARING for sharing, parity in society[self][1])

        if form == "two selves separately":
            next_society = {}
            shared = {}
            for self in execution_order:
                emission, next_prior = namespace["_1_now_existing"](*society[self])
                assert len(emission) <= 1
                shared[self] = emission[0][1] if emission else None
                next_society[self] = (next_prior, [])
            society = next_society
        else:
            # With the one declared sharing, an emission is present if a
            # prior is already publicly established, or a nonzero parity is
            # now received. This needs no inspection of a private prior.
            gives = {self: indicated_prior[self] is not None or any(receiving[self])
                     for self in selves}
            society = namespace["_17_next_existing"](society, joins)
            offsets = {self: 0 for self in selves}
            shared = {self: None for self in selves}
            for self in execution_order:
                if not gives[self]:
                    continue
                for connector in (6, 10, 9):
                    if (self, connector) not in joins:
                        continue
                    receiver = joins[self, connector]
                    sharing, parity = society[receiver][1][offsets[receiver]]
                    offsets[receiver] += 1
                    assert sharing == SHARING and parity in (-1, 0, 1)
                    if shared[self] is not None:
                        assert shared[self] == parity
                    shared[self] = parity
                assert shared[self] is not None
            for self in selves:
                assert offsets[self] == len(society[self][1])

        for self, parity in shared.items():
            if parity in (-1, 1):
                if self not in first_public_prior:
                    first_public_prior[self] = {"momentary": momentary, "parity": parity}
                indicated_prior[self] = parity
        next_receiving = [[parity for sharing, parity in society[self][1]] for self in selves]
        row = {"momentary": momentary, "phase": phase, "source_parities": parities,
               "receiving": [receiving[self] for self in selves],
               "sharing": [shared[self] for self in selves],
               "next_receiving": next_receiving}
        public.append(row)

        # For this declared single sharing, a nonzero public sharing becomes
        # its prior and a zero retains it. Thus public history, initially
        # empty, indicates the entire prior without reading private returns.
        signature = (tuple(indicated_prior[self] for self in selves),
                     tuple(tuple(values) for values in next_receiving), next_positions)
        if not phase_closed and signature in seen_in_phase:
            first_at = seen_in_phase[signature]
            recurrence.append({"phase": phase, "phase_begins": phase_first,
                               "after_momentary": first_at, "again_after_momentary": momentary,
                               "momentaries_between": momentary - first_at,
                               "priors_indicated_by_public_sharing": [indicated_prior[self] for self in selves],
                               "next_receiving": next_receiving,
                               "next_source_positions": next_positions,
                               "condition": "these joins and this phase's source continuation remain as declared"})
            phase_closed = True
        seen_in_phase.setdefault(signature, momentary)
        phase_before = phase

    return {"construction": {"form": form, "program": program, "selves": list(selves),
                             "source_receivers": list(source_receivers),
                             "joins": [[self, connector, other] for (self, connector), other in joins.items()],
                             "beginning": "no priors supplied; first priors form through incoming sequences",
                             "sharing": SHARING,
                             "pacing": "one parity from each active source per supplied society momentary; all selves resolve once together",
                             "execution_order": list(execution_order),
                             "first_sequence_shift_when_changed": first_shift,
                             "second_sequence_shift_when_changed": second_shift,
                             "end": end,
                             "boundary": "final next_receiving is recorded and remains undelivered at the end"},
            "first_priors_through_public_sharing": first_public_prior,
            "conditional_recurrences": recurrence,
            "public_record": public}


def first_differences(first, second, after=0, through=None):
    assert first["construction"]["selves"] == second["construction"]["selves"]
    differences = {}
    for left, right in zip(first["public_record"], second["public_record"]):
        assert left["momentary"] == right["momentary"]
        if left["momentary"] <= after or (through is not None and left["momentary"] > through):
            continue
        for position, self in enumerate(first["construction"]["selves"]):
            if self not in differences and left["sharing"][position] != right["sharing"][position]:
                differences[self] = {"momentary": left["momentary"],
                                     "first_receiving": left["receiving"][position],
                                     "second_receiving": right["receiving"][position],
                                     "first_sharing": left["sharing"][position],
                                     "second_sharing": right["sharing"][position]}
    return differences


def same_receiving_different_carrying(first, second, after=48):
    selves = first["construction"]["selves"]
    priors = [[None for self in selves], [None for self in selves]]
    prior_shared_at = [[None for self in selves], [None for self in selves]]
    witnesses = {}
    for left, right in zip(first["public_record"], second["public_record"]):
        if left["momentary"] > after:
            assert left["source_parities"] == right["source_parities"]
            for position, self in enumerate(selves):
                if (self not in witnesses
                    and left["receiving"][position] == right["receiving"][position]
                    and left["sharing"][position] != right["sharing"][position]
                    and all(prior[position] is not None for prior in priors)):
                    witnesses[self] = {"momentary": left["momentary"],
                                       "same_receiving": left["receiving"][position],
                                       "first_prior_from_public_sharing": priors[0][position],
                                       "second_prior_from_public_sharing": priors[1][position],
                                       "first_prior_shared_at": prior_shared_at[0][position],
                                       "second_prior_shared_at": prior_shared_at[1][position],
                                       "first_sharing": left["sharing"][position],
                                       "second_sharing": right["sharing"][position]}
        for indicated, shared_at, row in zip(priors, prior_shared_at, (left, right)):
            for position, parity in enumerate(row["sharing"]):
                if parity in (-1, 1):
                    indicated[position] = parity
                    shared_at[position] = row["momentary"]
    return witnesses


def build_study(namespace):
    studies = {}
    for form in ("two selves bi-coupling", "three along and five across"):
        continuing = execute(namespace, form, "original sequences throughout")
        changed_second = execute(namespace, form, "change second, return, withdraw, return")
        changed_first = execute(namespace, form, "change first, then return")
        differently_formed = execute(namespace, form, "different forming, then original sequences")
        reversed_execution = execute(namespace, form, "change second, return, withdraw, return", reverse_order=True)
        order_same = all(left["sharing"] == right["sharing"]
                         for left, right in zip(changed_second["public_record"], reversed_execution["public_record"]))
        assert order_same
        same_until_change = all(left["sharing"] == right["sharing"]
                                and left["receiving"] == right["receiving"]
                                for left, right in zip(continuing["public_record"][:48], changed_second["public_record"][:48]))
        assert same_until_change
        studies[form] = {
            "going_on_through_changing_sources": changed_second,
            "original_sequences_throughout": continuing,
            "first_sequence_changing": changed_first,
            "different_forming_then_same_sources": differently_formed,
            "findings": {
                "every_self_forms_a_prior_through_sharing": len(changed_second["first_priors_through_public_sharing"]) == len(changed_second["construction"]["selves"]),
                "original_and_changed_source_constructions_share_their_first_48_momentaries": same_until_change,
                "first_changes_when_second_sequence_changes": first_differences(continuing, changed_second, after=48, through=96),
                "first_changes_when_first_sequence_changes": first_differences(continuing, changed_first, after=48, through=96),
                "changed_source_comparison_interval": [49, 96],
                "different_carrying_with_same_later_receiving": same_receiving_different_carrying(continuing, differently_formed),
                "reversing_execution_order_preserves_public_sharings": order_same,
                "order_check_scope": "permutation inside ONE's same society momentary; independent pacing is not tested"}}
        variations = []
        for which, pattern, program in (("first", FIRST_SEQUENCE, "change first, then return"),
                                        ("second", SECOND_SEQUENCE, "change second, return, withdraw, return")):
            for shift in range(1, len(pattern)):
                parameters = {which + "_shift": shift}
                variant = execute(namespace, form, program, end=96, **parameters)
                assert all(left["receiving"] == right["receiving"] and left["sharing"] == right["sharing"]
                           for left, right in zip(continuing["public_record"][:48], variant["public_record"][:48]))
                variations.append({"sequence_changed": which, "positions_further_along": shift,
                                   "changed_receivings": [49, 96],
                                   "first_sharing_differences": first_differences(continuing, variant, after=48, through=96),
                                   "conditional_recurrences_after_change": [r for r in variant["conditional_recurrences"] if r["phase_begins"] == 49]})
                if which == "second" and shift == 2:
                    studies[form]["second_sequence_two_places_further"] = variant
        studies[form]["all_other_positions_of_either_sequence"] = variations
    separate = execute(namespace, "two selves separately", "original sequences throughout")
    studies["two selves bi-coupling"]["each_sequence_with_its_self_separately"] = separate
    studies["two selves bi-coupling"]["findings"]["sharing_with_other_compared_with_separate_going_on"] = first_differences(
        separate, studies["two selves bi-coupling"]["original_sequences_throughout"])
    return {"source": {"document": SOURCE, "commit": SOURCE_COMMIT,
                        "document_sha256": SOURCE_SHA256, "expression_sha256": EXPRESSION_SHA256},
            "sequences": {"first": FIRST_SEQUENCE, "second": SECOND_SEQUENCE,
                          "meaning": "repeat each parity list in order; equal successive parities are not-changing, opposite successive parities changing; zero in a resolver's sharing is a different subject"},
            "observing": {"private_prior": "passed onward only, never inspected or copied; publicly established parity is inferred from ONE's specified nonzero sharing and retained through zero sharing",
                          "source": "external prescribed parities; not a claim that source sequences learn or respond",
                          "taking": "previous network sharings are received together with this momentary's source parities; no previous sharing discarded",
                          "ledger": "one same sharing at every self; no source identity, timestamp, sequence position or expected answer crosses",
                          "refusing": "source hash and structural routing checks raise on instrument faults; recurrence or pattern-match failure is reported, never filtered",
                          "recurrence": "publicly indicated priors plus pending parities plus source positions; conditional on the stated source continuation",
                          "status": "executed finite constructions; no claim of arbitrary sequence learning or independently paced natural society"},
            "studies": studies}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    study = build_study(read_resolver(root))
    args.output.write_text(json.dumps(study, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(json.dumps({form: {"findings": result["findings"],
                            "recurrences": result["going_on_through_changing_sources"]["conditional_recurrences"]}
                      for form, result in study["studies"].items()}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
