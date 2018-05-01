import unittest

from module4.task5_ladder import ladder


class TestKnapsack(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, ladder(map(int, '1 2'.split())))

    def test2(self):
        self.assertEqual(1, ladder(map(int, '2 -1'.split())))

    def test3(self):
        self.assertEqual(3, ladder(map(int, '-1 2 1'.split())))

    def test4(self):
        self.assertEqual(3, ladder(map(int, '-1 2 1 3 -3'.split())))

    def test5(self):
        self.assertEqual(7, ladder(map(int, '-1 2 1 3 -3 1'.split())))

    def test6(self):
        self.assertEqual(1, ladder(map(int, '1'.split())))

    def test7(self):
        self.assertEqual(1, ladder(map(int, '-1 1'.split())))

    def test8(self):
        self.assertEqual(-73, ladder(map(int, '-64 -16 -13 -9 -48'.split())))

    def test9(self):
        self.assertEqual(21, ladder(map(int, '3 4 10 10 0 -6 -10 0'.split())))
