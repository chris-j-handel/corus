"""Distinct-arriving variant of the bounded surface, using unchanged v379.

The source's grouped invocation is a declared experimental condition, not a
claim of natural independent pacing. No carried parity is observed or supplied.
"""
import hashlib
import json
from pathlib import Path


def surface(resolve_society, labels, joins):
    # This declared empty construction precedes all participation. Only the
    # unchanged resolver subsequently forms or replaces the own continuations.
    wound = {label: ([], []) for label in labels}

    def advance(external_arrivals=()):
        nonlocal wound
        for receiver, parity in external_arrivals:
            wound[receiver][1].append(("shared-offering", parity))
        public_arriving = [
            {"receiving_self": label, "arriving": list(wound[label][1])}
            for label in labels
        ]
        wound = resolve_society(wound, joins)
        public_next_arriving = [
            {"receiving_self": label, "arriving": list(wound[label][1])}
            for label in labels
        ]
        return {"arriving_at_this_invocation": public_arriving,
                "released_into_next_arriving": public_next_arriving}

    return advance


def read_surface(repository):
    path = repository / "Exhibit_ONE_Natural_Resolver_v379.md"
    source = path.read_text()
    expression = source.split("```python\n", 1)[1].split("```", 1)[0]
    namespace = {}
    exec(compile(expression, str(path), "exec"), namespace)
    labels = tuple(f"{row}:{column}" for row in range(3) for column in range(5))
    joins = {}
    wiring = []
    for row in range(3):
        for column in range(5):
            label = f"{row}:{column}"
            for releasing, arriving, receiver in (
                (6, 2, f"{row}:{(column - 1) % 5}"),
                (10, 14, f"{row}:{(column + 1) % 5}"),
                (9, 17, f"{(row + 1) % 3}:{column}"),
            ):
                joins[(label, releasing)] = receiver
                wiring.append({"releasing_self": label,
                               "releasing_connector": releasing,
                               "receiving_self": receiver,
                               "arriving_connector": arriving})
    advance = surface(namespace["_17_co_bi_tri_offering"], labels, joins)
    public = []
    for invocation in range(16):
        external = [("0:0", 1)] if invocation == 0 else (
            [("0:0", -1)] if invocation == 2 else [])
        event = advance(external)
        public.append({"software_invocation": invocation + 1,
                       "external_arrivals": external, **event})
    return {
        "standing": "bounded grouped software surface; discovering, not method proof",
        "source": path.name,
        "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "expression_sha256": hashlib.sha256(expression.encode()).hexdigest(),
        "construction": {
            "shape": "three along by five across, periodic wiring supplied",
            "beginning": "fifteen independently empty local continuations inside the source's society representation",
            "opening": "one external plus at 0:0 before the first invocation",
            "perturbation": "one external minus at 0:0 before the third invocation, appended to ordinary arrivals",
            "activation": "unchanged 17 invokes each local 1 once per supplied grouped invocation, including empty arrivals",
            "public_scope": "ordinary arrivals before invoking, and public releases gathered into next arrivals; no private fields recorded",
            "crossing": "unchanged 17 gathers every joined release into receiver offerings; internal 14 surfaces them at that receiver's next 1",
            "label_scope": "coordinates and connector numbers describe supplied wiring, not payloads added to a parity",
            "boundary": "sixteen invocations then process ends; final next arrivals remain undelivered",
            "limits": "no independent natural pacing, geodesic velocity, causal control, private fullness check, or protection proof",
        },
        "wiring": wiring,
        "public_reading": public,
    }


if __name__ == "__main__":
    print(json.dumps(read_surface(Path(__file__).resolve().parents[3]), indent=2))
