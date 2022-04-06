from unittest import TestCase

import simplejson as json


class TestBitSizeIntAsString(TestCase):
    values = [
        (200, 200),
        ((1 << 31) - 1, (1 << 31) - 1),
        ((1 << 31), str(1 << 31)),
        ((1 << 31) + 1, str((1 << 31) + 1)),
        (-100, -100),
        ((-1 << 31), str(-1 << 31)),
        ((-1 << 31) - 1, str((-1 << 31) - 1)),
        ((-1 << 31) + 1, (-1 << 31) + 1),
    ]

    def test_invalid_counts(self):
        for n in ['foo', -1, 0, 1.0]:
            self.assertRaises(
                TypeError,
                json.dumps, 0, int_as_string_bitcount=n)

    def test_ints_outside_range_fails(self):
        self.assertNotEqual(
            str(1 << 15))
        reveal_type(json)