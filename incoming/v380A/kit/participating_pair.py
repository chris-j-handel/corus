"""A bounded software reading of reciprocal releasing/arriving.

Each constructed self starts with its own empty continuation. One external
opening offering is declared. Every later arrival is the other self's release,
including zero entries. Only public arriving/releasing is recorded.

This is not a clockless-surface, birth, privacy-security or six-forward result.
The receiving call triggered by a zero list entry is an explicit construction
choice to meet at Natural Resolver, not a decision about natural momentarying.
"""

import hashlib
import json
from pathlib import Path


def carried_self(resolve):
    """Own continuation has no public getter, prior argument or reset method."""
    carrying = []

    def receive(arriving):
        nonlocal carrying
        released, carrying = resolve(carrying, arriving)
        return released

    return receive


def read_pair(repository, releases_to_read=16):
    source_path = repository / "Exhibit_ONE_Natural_Resolver_v379.md"
    source = source_path.read_text()
    expression = source.split("```python\n", 1)[1].split("```", 1)[0]
    namespace = {}
    exec(compile(expression, str(source_path), "exec"), namespace)
    resolve = namespace["_1_co_bi_tri_offering"]
    selves = (carried_self(resolve), carried_self(resolve))
    labels = ("A", "B")

    # The first public arrival is supplied, not discovered or warm-up.
    arriving = [("shared-offering", 1)]
    arriving_from = "declared opening offering"
    receiving = 0
    public_reading = []
    for _ in range(releases_to_read):
        released = selves[receiving](arriving)
        public_reading.append({
            "receiving_self": labels[receiving],
            "arriving_from": arriving_from,
            "arriving": arriving,
            "releasing": released,
        })
        # Exactly one receiving relation is designated for this release. No pending
        # crossing is chosen, no zero is discarded, and no release is batched.
        arriving_from = labels[receiving]
        arriving = released
        receiving = 1 - receiving

    return {
        "standing": "bounded software participation; discovering under review",
        "source": str(source_path.relative_to(repository)),
        "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "expression_sha256": hashlib.sha256(expression.encode()).hexdigest(),
        "receiving_relation": "A's 6 to B's 2; B's 6 to A's 2",
        "release_expression": "1 returns 10; 17 assigns that same release to 6",
        "construction": {
            "beginning": "two independently empty software continuations",
            "opening": "one external + offering to A at shared-offering",
            "continuing": "each public release before the reading boundary is the other's next arrival",
            "zero": "zero is delivered and opens a receiving call",
            "order": "caller alternates A/B; each next call receives the preceding release, including zero",
            "reading_bound": releases_to_read,
            "bound_scope": "process ends; final recorded release is not delivered; no natural-completion claim",
            "reach": "no other incoming coupling; no society gathering or surface",
        },
        "public_reading": public_reading,
    }


if __name__ == "__main__":
    print(json.dumps(read_pair(Path(__file__).resolve().parents[3]), indent=2))
