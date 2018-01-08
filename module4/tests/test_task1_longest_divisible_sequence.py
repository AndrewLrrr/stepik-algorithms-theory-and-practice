import unittest

from module4.task1_longest_divisible_sequence import max_LDS


class TestLDS(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, max_LDS((3, 6, 7, 12,)))

    def test2(self):
        self.assertEqual(1, max_LDS((12, 6, 7, 3,)))

    def test3(self):
        self.assertEqual(4, max_LDS((2, 4, 8, 4, 12)))

    def test4(self):
        self.assertEqual(6, max_LDS((2, 4, 8, 4, 12, 24, 48)))

    def test5(self):
        self.assertEqual(4, max_LDS((1, 1, 1, 1)))

    def test6(self):
        self.assertEqual(8, max_LDS((1, 1, 1, 1, 3, 6, 7, 14, 28, 56)))

    def test7(self):
        self.assertEqual(10, max_LDS((1, 2, 2, 2, 3, 6, 7, 12, 24, 48, 4, 28, 24, 8, 48, 96, 56, 48, 16, 100, 16, 102)))
