import unittest
from knights import *


class TestKnights(unittest.TestCase):
    def test01_check_tour(self):
        msg = "Testing checking a valid tour"

        board = [["N"]]
        tour = [(0, 0)]

        self.assertTrue(check_tour(board, tour), msg)

    def test02_check_tour(self):
        msg = "Testing checking an invalid tour"

        board = [["N",  None, None],
                 [None, None, None]]
        tour = [(0, 0), (1, 2)]

        self.assertFalse(check_tour(board, tour), msg)

    def test03_find_tour(self):
        msg = "Testing finding a trivial tour"

        board = [["N"]]
        tour = find_tour(board, 0, 0)

        self.assertIsNotNone(tour, msg)
        self.assertEqual(len(tour), 1, msg)
        self.assertTrue(check_tour(board, tour), msg)

    def test04_find_tour(self):
        msg = "Testing finding a nonexistent tour"

        board = [[None, None, None],
                 [None, "N",  None]]
        tour = find_tour(board, 1, 1)

        self.assertIsNone(tour, msg)

    def test05_find_tour(self):
        msg = "Testing finding a longer tour"

        board = [["B",  None, None, None, "Q" ],
                 [None, "N",  "P",  None, None],
                 [None, None, None, "P",  None],
                 [None, None, None, None, None],
                 [None, "K",  None, None, "R" ]]
        tour = find_tour(board, 1, 1)

        self.assertIsNotNone(tour, msg)
        self.assertEqual(len(tour), 19, msg)
        self.assertTrue(check_tour(board, tour), msg)

    def test06_check_tour(self):
        msg = "Testing checking an invalid move"

        board = [["N", "K", "K"],
                 ["K", "K", "K"],
                 ["K", "K", None]]
        tour = ([0,0],[3,3])

        self.assertIsNotNone(check_tour(board, tour), msg)

    def test07_check_tour(self):
        msg = ("Non-existant tour")

        board = None
        tour = None
        self.assertFalse(check_tour(board, tour), msg)

    def test010_check_tour(self):
        msg = ("Non-existant tour")

        board = [[]]
        tour = []
        self.assertIsNone(find_tour(board, 0, 0), msg)

    def test08_check_tour(self):
        msg = ("Non-existant tour")

        board = None
        tour = []
        self.assertFalse(check_tour(board, tour), msg)

    def test09_check_tour(self):
        msg = ("Non-existant tour")

        board = None
        tour = []
        self.assertIsNone(find_tour(board, None, None), msg)

if __name__ == '__main__':
    unittest.main()
