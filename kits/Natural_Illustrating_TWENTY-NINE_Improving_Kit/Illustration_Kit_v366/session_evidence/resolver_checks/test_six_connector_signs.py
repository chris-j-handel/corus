"""Boundary-only checks: no kernel invocation or internal carrying access.

Run beside Natural_Resolver_Six_Connector_Working.py with:
    python3 -m unittest -v test_six_connector_signs

Supplied signs exercise connector operations only. They are not claimed to
be outgoing signs produced by resolving, or a model of its full momentaries.
"""

import unittest

from Natural_Resolver_Six_Connector_Working import Resolver


class SixConnectorSigns(unittest.TestCase):
    def assert_unread(self, resolver, position):
        with self.assertRaises(LookupError):
            resolver.sign_changed(position)

    def test_across_crossings_preserve_same_and_change(self):
        for direction, source_position, target_position in (
            ('left', 6, 2), ('right', 10, 14)
        ):
            for prior, next_sign in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                with self.subTest(direction=direction, prior=prior, next=next_sign):
                    source, target = Resolver(), Resolver()
                    if direction == 'left':
                        source.connect_left(target)
                        offer = source.n06_other_self_crossing
                    else:
                        source.connect_right(target)
                        offer = source.n10_other_social_surfacing
                    offer(prior)
                    self.assert_unread(source, source_position)
                    self.assert_unread(target, target_position)
                    offer(next_sign)
                    self.assertIs(source.sign_changed(source_position), prior != next_sign)
                    self.assertIs(target.sign_changed(target_position), prior != next_sign)

    def test_repeated_sign_is_an_arrival(self):
        source, target = Resolver(), Resolver()
        source.connect_right(target)
        source.n10_other_social_surfacing(1)
        source.n10_other_social_surfacing(-1)
        self.assertIs(target.sign_changed(14), True)
        source.n10_other_social_surfacing(-1)
        self.assertIs(source.sign_changed(10), False)
        self.assertIs(target.sign_changed(14), False)

    def test_opposite_across_sequences_remain_separate(self):
        left, right = Resolver(), Resolver()
        left.connect_right(right)
        left.n10_other_social_surfacing(1)
        right.n06_other_self_crossing(-1)
        left.n10_other_social_surfacing(-1)
        right.n06_other_self_crossing(-1)
        self.assertIs(left.sign_changed(10), True)
        self.assertIs(right.sign_changed(14), True)
        self.assertIs(right.sign_changed(6), False)
        self.assertIs(left.sign_changed(2), False)

    def test_along_crossing_in_either_direction_without_echo(self):
        for join in ('forward', 'backward'):
            for prior, next_sign in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                with self.subTest(join=join, prior=prior, next=next_sign):
                    first, second = Resolver(), Resolver()
                    if join == 'forward':
                        first.connect_forward(second)
                        offer = first.n17_social_abundancing
                        return_offer = second.n09_other_social_releasing
                        first_position, second_position = 17, 9
                    else:
                        first.connect_backward(second)
                        offer = first.n09_other_social_releasing
                        return_offer = second.n17_social_abundancing
                        first_position, second_position = 9, 17
                    offer(prior)
                    # An automatic echo would create a comparison already.
                    self.assert_unread(first, first_position)
                    self.assert_unread(second, second_position)
                    return_offer(next_sign)
                    self.assertIs(first.sign_changed(first_position), prior != next_sign)
                    self.assertIs(second.sign_changed(second_position), prior != next_sign)

    def test_direct_arriving_does_not_fabricate_outgoing(self):
        resolver = Resolver()
        resolver.n02_self_other_offering(-1)
        resolver.n02_self_other_offering(1)
        resolver.n14_social_other_crossing(1)
        resolver.n14_social_other_crossing(1)
        self.assertIs(resolver.sign_changed(2), True)
        self.assertIs(resolver.sign_changed(14), False)
        for position in (6, 10, 9, 17):
            self.assert_unread(resolver, position)

    def test_no_third_wire_sign_is_accepted(self):
        source, target = Resolver(), Resolver()
        source.connect_right(target)
        source.n10_other_social_surfacing(1)
        for invalid in (0, None, True, False, 1.0, '1'):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    source.n10_other_social_surfacing(invalid)
                with self.assertRaises(ValueError):
                    target.n14_social_other_crossing(invalid)
        self.assert_unread(source, 10)
        self.assert_unread(target, 14)
        source.n10_other_social_surfacing(1)
        self.assertIs(source.sign_changed(10), False)
        self.assertIs(target.sign_changed(14), False)

    def test_unconnected_offer_does_not_create_a_crossing(self):
        source, target = Resolver(), Resolver()
        with self.assertRaises(ValueError):
            source.n06_other_self_crossing(-1)
        self.assert_unread(source, 6)
        source.connect_left(target)
        source.n06_other_self_crossing(1)
        self.assert_unread(source, 6)
        self.assert_unread(target, 2)


if __name__ == '__main__':
    unittest.main()
