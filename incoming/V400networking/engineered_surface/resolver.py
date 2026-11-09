"""Exhibit ONE · Natural Resolver
Stable-Forming Same- and Next-Existing
"""

def _1_now_existing(_3_is_now_co_observing, _2_now_possibling):
    _14_next_possibling = {}
    for _4_now_co_same_existing, _7_is_now_observing in _2_now_possibling:
        if _7_is_now_observing != 0:
            _15_is_next_observing = _14_next_possibling.get(
                _4_now_co_same_existing
            )
            if _15_is_next_observing is None:
                _14_next_possibling[_4_now_co_same_existing] = (
                    1 if _7_is_now_observing > 0 else -1
                )
            elif (_15_is_next_observing > 0) != (_7_is_now_observing > 0):
                _14_next_possibling[_4_now_co_same_existing] = 0
    _12_next_co_same_existing = dict(_14_next_possibling)
    for _4_now_co_same_existing, _7_is_now_observing in _3_is_now_co_observing:
        _15_is_next_observing = _14_next_possibling.get(_4_now_co_same_existing, 0)
        if _15_is_next_observing != 0 and (_15_is_next_observing > 0) == (_7_is_now_observing > 0):
            _12_next_co_same_existing[_4_now_co_same_existing] = 0
        else:
            _12_next_co_same_existing[_4_now_co_same_existing] = (
                -1 if _7_is_now_observing > 0 else 1
            )
    _10_next_co_possibling = list(_12_next_co_same_existing.items())
    _11_next_co_observing = dict(_3_is_now_co_observing)
    for _4_now_co_same_existing, _7_is_now_observing in _10_next_co_possibling:
        if _7_is_now_observing != 0:
            _11_next_co_observing[_4_now_co_same_existing] = _7_is_now_observing
    return _10_next_co_possibling, list(_11_next_co_observing.items())

def _9_next_co_discovering(_10_next_co_possibling, _5_now_co_existing):
    return [
        (_5_now_co_existing[_13_is_next_discovering], _15_is_next_observing)
        for _13_is_next_discovering, _15_is_next_observing in _10_next_co_possibling
    ]

def _17_next_existing(_16_next_same_existing, _5_now_co_existing):
    _8_now_same_existing = {}
    _14_next_possibling = {
        _13_is_next_discovering: []
        for _13_is_next_discovering in _16_next_same_existing
    }
    for _13_is_next_discovering, (
        _3_is_now_co_observing,
        _2_now_possibling,
    ) in _16_next_same_existing.items():
        _10_next_co_possibling, _8_now_same_existing[_13_is_next_discovering] = (
            _1_now_existing(_3_is_now_co_observing, _2_now_possibling)
        )
        _6_now_co_possibling = _10_next_co_possibling
        for (
            _4_now_co_same_existing,
            _15_is_next_observing,
        ) in _9_next_co_discovering(
            [
                (_4_now_co_same_existing, _15_is_next_observing)
                for _4_now_co_same_existing, _15_is_next_observing in (
                    ((_13_is_next_discovering, 6), _6_now_co_possibling),
                    ((_13_is_next_discovering, 10), _10_next_co_possibling),
                    ((_13_is_next_discovering, 9), _10_next_co_possibling),
                )
                if _4_now_co_same_existing in _5_now_co_existing
            ],
            _5_now_co_existing,
        ):
            _14_next_possibling[_4_now_co_same_existing].extend(
                _15_is_next_observing
            )
    return {
        _13_is_next_discovering: (
            _8_now_same_existing[_13_is_next_discovering],
            _14_next_possibling[_13_is_next_discovering],
        )
        for _13_is_next_discovering in _16_next_same_existing
    }
