"""Exhibit ONE · Natural Resolver · v372"""


def _1_self_coupling(_3_self_carrying, _2_self_offering):
    _6_other_crossing = {
        _4_self_sharing: _8_other_torusing
        for _4_self_sharing, _7_other_corusing, _8_other_torusing, _16_social_torusing
        in _3_self_carrying}
    _14_social_crossing = [
        (_4_self_sharing, _7_other_corusing)
        for _4_self_sharing, _7_other_corusing in _2_self_offering
        if _7_other_corusing != 0]
    for _4_self_sharing, _7_other_corusing, _8_other_torusing, _16_social_torusing in _3_self_carrying:
        if _7_other_corusing > 0:
            _14_social_crossing.append((_4_self_sharing, -1))
        if _7_other_corusing < 0:
            _14_social_crossing.append((_4_self_sharing, 1))
    _12_other_surplusing = {}
    for _4_self_sharing, _7_other_corusing in _14_social_crossing:
        if _7_other_corusing > 0:
            _12_other_surplusing[_4_self_sharing] = _12_other_surplusing.get(_4_self_sharing, 0) + 1
        if _7_other_corusing < 0:
            _12_other_surplusing[_4_self_sharing] = _12_other_surplusing.get(_4_self_sharing, 0) - 1
    _10_other_surfacing = [
        (_4_self_sharing, 1 if _12_other_surplusing[_4_self_sharing] > 0
            else (-1 if _12_other_surplusing[_4_self_sharing] < 0 else 0))
        for _4_self_sharing in _12_other_surplusing]
    _11_other_chaining = {}
    for _4_self_sharing, _7_other_corusing, _8_other_torusing, _16_social_torusing in _3_self_carrying:
        if _16_social_torusing + 1 <= 3 or (_16_social_torusing + 1 == 4 and _8_other_torusing > 0):
            _11_other_chaining[_4_self_sharing] = (
                _7_other_corusing, _8_other_torusing, _16_social_torusing + 1)
    for _4_self_sharing, _7_other_corusing in _10_other_surfacing:
        if _7_other_corusing != 0:
            _11_other_chaining[_4_self_sharing] = (
                _7_other_corusing, 0 - _6_other_crossing.get(_4_self_sharing, 1), 0)
    return (
        _10_other_surfacing,
        [(_4_self_sharing, _7_other_corusing, _8_other_torusing, _16_social_torusing)
         for _4_self_sharing, (_7_other_corusing, _8_other_torusing, _16_social_torusing)
         in _11_other_chaining.items()])


def _9_other_releasing(_10_other_surfacing, _5_other_neutralling):
    return [(_5_other_neutralling[_13_social_neutralling], _15_social_corusing)
            for _13_social_neutralling, _15_social_corusing in _10_other_surfacing]


CONNECTORS = {
    2: ('2-self-offering', 'right', 'arriving'),
    6: ('6-other-crossing', 'left', 'releasing'),
    9: ('9-other-releasing', 'backward', 'along'),
    10: ('10-other-surfacing', 'right', 'releasing'),
    14: ('14-social-crossing', 'left', 'arriving'),
    17: ('17-social-abundancing', 'forward', 'along'),
}
JOINS = {10: 14, 6: 2, 17: 9, 9: 17}


def _17_social_abundancing(_3_self_carrying, _2_self_offering, _5_other_neutralling, SURFACE):
    _11_other_chaining = {}
    _2_self_offering_next = {self: {2: [], 14: [], 17: []} for self in SURFACE}
    for self, facings in SURFACE.items():
        carrying = _3_self_carrying.get(self, [])
        arriving = [sign for connector in (2, 14, 17)
                    for sign in _2_self_offering.get(self, {}).get(connector, [])]
        _10_other_surfacing, _11_other_chaining[self] = _1_self_coupling(carrying, arriving)
        _6_other_crossing = [
            (_4_self_sharing, _8_other_torusing)
            for _4_self_sharing, _7_other_corusing, _8_other_torusing, _16_social_torusing in carrying]
        released = _9_other_releasing(_10_other_surfacing, _5_other_neutralling.get(self, {
            _13_social_neutralling: _13_social_neutralling
            for _13_social_neutralling, _15_social_corusing in _10_other_surfacing}))
        for releasing, signs in ((6, _6_other_crossing), (10, _10_other_surfacing), (9, released)):
            for neighbour in facings.get(CONNECTORS[releasing][1], []):
                if neighbour in _2_self_offering_next:
                    _2_self_offering_next[neighbour][JOINS[releasing]] += signs
    return _11_other_chaining, _2_self_offering_next
