import unittest

from find_longest import find_longest


GENERIC_TOKENS = [
    'I', ' ',
    'was', ' ',
    'driving', ' ',
    'up', ' ',
    'from', ' ',
    'Tampa'
]


class TestSlidingWindow(unittest.TestCase):
    def test_generic_1(self):
        self.assertListEqual(
            list(find_longest.sliding_window_no_whitespace(GENERIC_TOKENS, 1)),
            [('I', ), ('was', ), ('driving', ), ('up', ), ('from', ), ('Tampa', )]
        )

    def test_generic_2(self):
        self.assertListEqual(
            list(find_longest.sliding_window_no_whitespace(GENERIC_TOKENS, 2)),
            [('I', 'was'),
             ('was', 'driving'),
             ('driving', 'up'),
             ('up', 'from'),
             ('from', 'Tampa')]
        )
