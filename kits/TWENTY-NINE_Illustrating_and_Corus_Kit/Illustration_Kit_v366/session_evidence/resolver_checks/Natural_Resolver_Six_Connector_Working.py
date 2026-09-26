"""Natural Resolver: numbered stable-form draft, 1 through 17.

Implemented: explicit ordered names, recorded 4/6/8 cycles, the behavior-
preserving numbered coupling entry point, and reciprocal local connections
through the six named connectors in Resolver instances.
The existing coupling kernel is executable as one function. The seventeen
numbered names do not require seventeen separate Python function bodies.
Executable does not mean complete: this preserved function is a reference,
not a verified implementation of all sixteen named responsibilities. Its
source includes signed accumulation and a numerically advanced continuation
value. Their correspondence with the requested binary-only method remains
to be established, together with the later-discovered responsibilities.
Resolver instances provide callable sign-only boundaries at the six connectors,
direct neighbor crossings, and same/change readings at those boundaries only.
They do not yet execute the preserved kernel or produce its outgoing signs.
Boundary transmission is implemented; integration with resolving is not.
The kernel remains the explicit function below. The public exhibit has not
been replaced.

Read a name as number (ordered relational prefix) root, for example:
    1 (self/other) coupling  -> n01_self_other_coupling
   17 (social) abundancing -> n17_social_abundancing

The user's explicit name for 17 is retained. An ordered pair or triple must
come from its identified participation; none is invented by sorting the roles
or padding every prefix to the same length. Prefix tuples support either.
17 names the external forward connector, not a seventeenth internal step.

The original function body and original argument names remain intact. The
old callable name is an alias, retaining keyword-call compatibility. The
return still contains surface entries and the self's private carrying in
that order; private carrying is not a network payload. Source zeros and
dictionary labels remain baseline behavior, not newly defined wire symbols.

The tables below describe the stable form. No routing scheduler, phase counter,
extra signal, output duplication or code to remove zero is installed by them.
Equilibria remains paused in Living Improving Value v360.

Current sequence rule (ONE 6.96): each moving sequence's sign is the same
as its own prior momentary or different. Odd momentaries participate along
17/9; even momentaries participate across 2/6/10/14, one parity at a time.
An unchanged sign is not automatically an absent momentary. A literal source
zero must be read in its actual comparison; no output policy is selected here.
Each supplied outgoing sign crosses directly to the connected receiving end.
Repeated signs cross too. Only the latest sign and comparison at each of the
six boundaries are retained for observation; no internal carrying is accessed.
The first sign establishes a prior and supplies no comparison reading yet.
These boundary operations do not drive or simulate the resolving interior.
"""

from typing import NamedTuple, Tuple


class StableName(NamedTuple):
    position: int
    prefix: Tuple[str, ...]
    root: str

    @property
    def label(self):
        return f"{self.position} ({'/'.join(self.prefix)}) {self.root}"

    @property
    def identifier(self):
        return f"n{self.position:02d}_{'_'.join(self.prefix)}_{self.root}"


class Connector(NamedTuple):
    name: StableName
    facing: str
    duty: str


# These are naming/connection declarations, not seventeen callable algorithms.
STABLE_NAMES = (
    StableName(1, ('self', 'other'), 'coupling'),
    StableName(2, ('self', 'other'), 'offering'),
    StableName(3, ('self', 'other'), 'carrying'),
    StableName(4, ('self', 'other'), 'sharing'),
    # Same5 throughout resolving: neutralling, offering into next living readiness.
    StableName(5, ('other', 'self'), 'neutralling'),
    StableName(6, ('other', 'self'), 'crossing'),
    StableName(7, ('other', 'self'), 'corusing'),
    StableName(8, ('other', 'self'), 'torusing'),
    StableName(9, ('other', 'social'), 'releasing'),
    StableName(10, ('other', 'social'), 'surfacing'),
    StableName(11, ('other', 'social'), 'chaining'),
    StableName(12, ('other', 'social'), 'surplusing'),
    StableName(13, ('social', 'other'), 'neutralling'),
    StableName(14, ('social', 'other'), 'crossing'),
    StableName(15, ('social', 'other'), 'corusing'),
    StableName(16, ('social', 'self'), 'torusing'),
    StableName(17, ('social',), 'abundancing'),
)
NAMES_BY_POSITION = {name.position: name for name in STABLE_NAMES}

# Along duties stay bidirectional one direction at a time; no permanent
# input/output identity is inferred from the forward/backward facing.
CONNECTORS = (
    Connector(NAMES_BY_POSITION[2], "right", "arriving"),
    Connector(NAMES_BY_POSITION[6], "left", "sending"),
    Connector(NAMES_BY_POSITION[9], "backward", "along"),
    Connector(NAMES_BY_POSITION[10], "right", "sending"),
    Connector(NAMES_BY_POSITION[14], "left", "arriving"),
    Connector(NAMES_BY_POSITION[17], "forward", "along"),
)
CONNECTORS_BY_POSITION = {connector.name.position: connector for connector in CONNECTORS}

# Explicit external connector declaration. This object does not yet implement
# emission; it never exposes the resolver's private carrying as a second output.
n17_social_abundancing = CONNECTORS_BY_POSITION[17]

# A sender's occurrence at one resolver meets the recipient occurrence at its
# neighbor. The coordinates are descriptive local facings, not packet fields.
NEIGHBOR_JOINS = (
    (10, "right_neighbor", 14),
    (6, "left_neighbor", 2),
    (17, "forward_neighbor", 9),
    (9, "backward_neighbor", 17),
)

# The four original cyclings cover every local position once.
FOUR_CYCLES = (
    (1, 9, 8, 16),
    (2, 15, 7, 10),
    (3, 11, 6, 14),
    (4, 13, 5, 12),
)
SHARED_MIDDLE_FOUR_CYCLES = (
    (9, 5, 12, 8),
    (7, 11, 6, 10),
)
SIX_CYCLES = (
    (1, 9, 5, 12, 8, 16),
    (2, 15, 7, 11, 6, 10),
    (3, 11, 7, 10, 6, 14),
    (4, 13, 5, 9, 8, 12),
)
# Higher reference labels: they are not additional local functions or a
# reinterpretation of local external connector 17 as a new internal coupling.
HIGHER_FOUR_CYCLES = (
    (18, 31, 23, 26),
    (19, 27, 22, 30),
)
HIGHER_SIX_CYCLES = (
    (18, 31, 23, 27, 22, 26),
    (19, 27, 23, 26, 22, 30),
)
EIGHT_CYCLES = (
    (1, 9, 5, 13, 4, 12, 8, 16),
    (2, 15, 7, 11, 3, 14, 6, 10),
)
# A cycle continues into a further occurrence of its first reference. These
# tuples are not a function-call schedule, a physical reflection, or release
# returning internally from 9 into the same resolver's 8 or 10.


def n01_self_other_coupling(co_carrying, bi_arriving):
    bi_co_bi_transmissioning = {
        bi_offering: bi_co_bi_co_bi_torusing
        for bi_offering, co_bi_co_bi_co_corusing, bi_co_bi_co_bi_torusing, bi_co_inseparating
        in co_carrying}
    bi_co_inversioning = [
        (bi_offering, co_bi_co_bi_co_corusing)
        for bi_offering, co_bi_co_bi_co_corusing in bi_arriving
        if co_bi_co_bi_co_corusing != 0]
    for bi_offering, co_bi_co_bi_co_corusing, bi_co_bi_co_bi_torusing, bi_co_inseparating in co_carrying:
        if co_bi_co_bi_co_corusing > 0:
            bi_co_inversioning.append((bi_offering, -1))
        if co_bi_co_bi_co_corusing < 0:
            bi_co_inversioning.append((bi_offering, 1))
    bi_co_tunneling = {}
    for bi_offering, co_bi_co_bi_co_corusing in bi_co_inversioning:
        if co_bi_co_bi_co_corusing > 0:
            bi_co_tunneling[bi_offering] = bi_co_tunneling.get(bi_offering, 0) + 1
        if co_bi_co_bi_co_corusing < 0:
            bi_co_tunneling[bi_offering] = bi_co_tunneling.get(bi_offering, 0) - 1
    bi_co_surfacing = [
        (bi_offering, 1 if bi_co_tunneling[bi_offering] > 0
            else (-1 if bi_co_tunneling[bi_offering] < 0 else 0))
        for bi_offering in bi_co_tunneling]
    co_bi_carrying = {}
    for bi_offering, co_bi_co_bi_co_corusing, bi_co_bi_co_bi_torusing, bi_co_inseparating in co_carrying:
        if bi_co_inseparating + 1 <= 3 or (bi_co_inseparating + 1 == 4 and bi_co_bi_co_bi_torusing > 0):
            co_bi_carrying[bi_offering] = (
                co_bi_co_bi_co_corusing, bi_co_bi_co_bi_torusing, bi_co_inseparating + 1)
    for bi_offering, co_bi_co_bi_co_corusing in bi_co_surfacing:
        if co_bi_co_bi_co_corusing != 0:
            co_bi_carrying[bi_offering] = (
                co_bi_co_bi_co_corusing, 0 - bi_co_bi_transmissioning.get(bi_offering, 1), 0)
    return (
        bi_co_surfacing,
        [(bi_offering, co_bi_co_bi_co_corusing, bi_co_bi_co_bi_torusing, bi_co_inseparating)
         for bi_offering, (co_bi_co_bi_co_corusing, bi_co_bi_co_bi_torusing, bi_co_inseparating)
         in co_bi_carrying.items()])


# Preserve the earlier entry point and keyword arguments; no wrapper or adapter.
co_bi_coupling = n01_self_other_coupling


class Connection(NamedTuple):
    """A direct local reference to a neighbor's connector, never a payload."""

    resolver: 'Resolver'
    position: int


class Resolver:
    """Six sign-only boundaries; the resolving interior remains unconnected.

    Each instance owns its six local links. There is no mesh registry, global
    coordinate system, clock, queue, message identifier, or routing selector.
    The same instance type connects at every chosen extent of a finite patch.

    The links pass supplied signs directly. Observations compare successive
    signs at each connector, and never inspect the resolving interior.
    The existing coupling kernel remains a separate callable and is never
    invoked by this class. In particular, receiving at2/14 does not fabricate
    an outgoing sign at6/10. Those outputs still belong to actual resolving.
    Numbered names describe participation; they do not require a separate
    Python function for every position. These connections make no
    collective-intelligence claim. No private carrying is copied into a link.
    """

    __slots__ = ('__connections', '__previous_sign', '__sign_changed')

    def __init__(self):
        self.__connections = {position: None for position in (2, 6, 9, 10, 14, 17)}
        # These are observations of the six boundaries, not kernel carrying.
        self.__previous_sign = dict.fromkeys(self.__connections)
        self.__sign_changed = dict.fromkeys(self.__connections)

    def connection(self, position):
        """Return the immutable local neighbor reference, or None if open."""
        if type(position) is not int or position not in self.__connections:
            raise ValueError('A persistent connector must be 2, 6, 9, 10, 14, or 17')
        return self.__connections[position]

    @staticmethod
    def __join(pairs):
        # Check every involved end before changing any link. An existing
        # different neighbor cannot be silently disconnected by a new join.
        changes = []
        for first, first_position, second, second_position in pairs:
            if not isinstance(first, Resolver) or not isinstance(second, Resolver):
                raise TypeError('Connect directly to another Resolver')
            for owner, position, peer, peer_position in (
                (first, first_position, second, second_position),
                (second, second_position, first, first_position),
            ):
                current = owner.__connections[position]
                if current is not None and (
                    current.resolver is not peer or current.position != peer_position
                ):
                    raise ValueError('Connector already has a different neighbor')
                changes.append((owner, position, Connection(peer, peer_position)))
        for owner, position, connection in changes:
            owner.__connections[position] = connection

    def connect_right(self, other):
        """Join self10→other14 and other6→self2 as one reciprocal interface."""
        self.__join(((self, 10, other, 14), (self, 2, other, 6)))

    def connect_left(self, other):
        """Join self6→other2 and other10→self14."""
        self.__join(((self, 6, other, 2), (self, 14, other, 10)))

    def connect_forward(self, other):
        """Join self17 with other9; along direction is not chosen here."""
        self.__join(((self, 17, other, 9),))

    def connect_backward(self, other):
        """Join self9 with other17; along direction is not chosen here."""
        self.__join(((self, 9, other, 17),))

    @staticmethod
    def __require_sign(sign):
        if type(sign) is not int or sign not in (-1, 1):
            raise ValueError('A crossing accepts only a sign: -1 or +1')

    def __observe_at_connector(self, position, sign):
        # Shared implementation for the six boundaries only. Nothing here
        # calls, names, inspects or changes any internal resolving function.
        self.connection(position)
        self.__require_sign(sign)
        previous = self.__previous_sign[position]
        self.__sign_changed[position] = (
            None if previous is None else sign != previous
        )
        self.__previous_sign[position] = sign

    def sign_changed(self, position):
        """Read only change (True) or no change (False) at a connector.

        Before two signs have participated, there is no comparison to read.
        LookupError reports that absence of an observation; it is not a third
        wire sign. Reading neither advances nor resets any participation.
        """
        self.connection(position)
        changed = self.__sign_changed[position]
        if changed is None:
            raise LookupError('This connector has no successive-sign comparison yet')
        return changed

    def __cross_from_connector(self, position, sign):
        self.__require_sign(sign)
        neighbor = self.connection(position)
        if neighbor is None:
            raise ValueError('Connect the neighboring receiving end before offering')
        # The established link supplies the receiving end. Only sign is the
        # travelling value; the position is existing connection metadata.
        # Receiving records the boundary and does not echo or relay onward.
        neighbor.resolver.__observe_at_connector(neighbor.position, sign)
        self.__observe_at_connector(position, sign)

    def n02_self_other_offering(self, sign):
        """Receive a sign at the right arriving boundary."""
        self.__observe_at_connector(2, sign)

    def n06_other_self_crossing(self, sign):
        """Offer a sign directly to the left neighbor's arriving2."""
        self.__cross_from_connector(6, sign)

    def n09_other_social_releasing(self, sign):
        """Offer along9 to the connected17; arrivals here do not echo."""
        self.__cross_from_connector(9, sign)

    def n10_other_social_surfacing(self, sign):
        """Offer a sign directly to the right neighbor's arriving14."""
        self.__cross_from_connector(10, sign)

    def n14_social_other_crossing(self, sign):
        """Receive a sign at the left arriving boundary."""
        self.__observe_at_connector(14, sign)

    def n17_social_abundancing(self, sign):
        """Offer along17 to the connected9; arrivals here do not echo."""
        self.__cross_from_connector(17, sign)
