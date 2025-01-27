import unittest
from knights import *


class TestHelperKnights(unittest.TestCase):
    def test01_is_within_bound(self):
        msg = "Testing checking a valid tour"

        board = [[None, None, None],
                 [None, None, None]]
        row = 1
        col = 2
        self.assertTrue(is_within_bound(board, row, col), msg)

if __name__ == '__main__':
    unittest.main()
