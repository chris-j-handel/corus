"""Exhibit ONE · Natural Resolver"""


def _1_co_bi_offering(_3_co_bi_sharing, _2_bi_co_offering):
    _14_bi_tri_moralizing = {}
    for _4_bi_co_sharing, _7_co_corusing in _2_bi_co_offering:
        if _7_co_corusing != 0:
            _15_co_bi_tri_corusing = _14_bi_tri_moralizing.get(_4_bi_co_sharing)
            if _15_co_bi_tri_corusing is None:
                _14_bi_tri_moralizing[_4_bi_co_sharing] = 1 if _7_co_corusing > 0 else -1
            elif (_15_co_bi_tri_corusing > 0) != (_7_co_corusing > 0):
                _14_bi_tri_moralizing[_4_bi_co_sharing] = 0
    _12_bi_tri_parity_changing = dict(_14_bi_tri_moralizing)
    for _4_bi_co_sharing, _7_co_corusing in _3_co_bi_sharing:
        _15_co_bi_tri_corusing = _14_bi_tri_moralizing.get(_4_bi_co_sharing, 0)
        if _15_co_bi_tri_corusing != 0 and (_15_co_bi_tri_corusing > 0) == (_7_co_corusing > 0):
            _12_bi_tri_parity_changing[_4_bi_co_sharing] = 0
        else:
            _12_bi_tri_parity_changing[_4_bi_co_sharing] = -1 if _7_co_corusing > 0 else 1
    _10_bi_tri_co_tunneling = list(_12_bi_tri_parity_changing.items())
    _11_tri_bi_co_chaining = dict(_3_co_bi_sharing)
    for _4_bi_co_sharing, _7_co_corusing in _10_bi_tri_co_tunneling:
        if _7_co_corusing != 0:
            _11_tri_bi_co_chaining[_4_bi_co_sharing] = _7_co_corusing
    return _10_bi_tri_co_tunneling, list(_11_tri_bi_co_chaining.items())


def _9_tri_bi_co_momentarying(_10_bi_tri_co_tunneling, _5_co_competencing):
    return [(_5_co_competencing[_13_co_tri_competencing], _15_co_bi_tri_corusing)
            for _13_co_tri_competencing, _15_co_bi_tri_corusing in _10_bi_tri_co_tunneling]


def _17_tri_co_offering(_16_bi_co_tri_torusing, _5_co_competencing):
    _8_bi_torusing = {}
    _14_bi_tri_moralizing = {_13_co_tri_competencing: [] for _13_co_tri_competencing in _16_bi_co_tri_torusing}
    for _13_co_tri_competencing, (_3_co_bi_sharing, _2_bi_co_offering) in _16_bi_co_tri_torusing.items():
        _10_bi_tri_co_tunneling, _8_bi_torusing[_13_co_tri_competencing] = _1_co_bi_offering(
            _3_co_bi_sharing, _2_bi_co_offering)
        _6_bi_moralizing = _10_bi_tri_co_tunneling
        for _4_bi_co_sharing, _15_co_bi_tri_corusing in _9_tri_bi_co_momentarying(
                [(_4_bi_co_sharing, _15_co_bi_tri_corusing)
                 for _4_bi_co_sharing, _15_co_bi_tri_corusing in (
                     ((_13_co_tri_competencing, 6), _6_bi_moralizing),
                     ((_13_co_tri_competencing, 10), _10_bi_tri_co_tunneling),
                     ((_13_co_tri_competencing, 9), _10_bi_tri_co_tunneling))
                 if _4_bi_co_sharing in _5_co_competencing],
                _5_co_competencing):
            _14_bi_tri_moralizing[_4_bi_co_sharing].extend(_15_co_bi_tri_corusing)
    return {_13_co_tri_competencing: (_8_bi_torusing[_13_co_tri_competencing],
                                           _14_bi_tri_moralizing[_13_co_tri_competencing])
            for _13_co_tri_competencing in _16_bi_co_tri_torusing}

CONNECTORS = {
    2: ('2-bi-co-offering', 'bi-moral-so-far', 'arriving'),
    6: ('6-bi-moralizing', 'not-yet-bi-moral', 'releasing'),
    9: ('9-tri-bi-co-momentarying', 'not-yet-co-competent', 'along'),
    10: ('10-bi-tri-co-tunneling', 'not-yet-bi-moral', 'releasing'),
    14: ('14-bi-tri-moralizing', 'bi-moral-so-far', 'arriving'),
    17: ('17-tri-co-offering', 'co-competent-so-far', 'along'),
}
JOINS = {10: 14, 6: 2, 17: 9, 9: 17}
