import unittest

from module4.task2_longest_not_increase_sequence import LNIS


class TestLNIS(unittest.TestCase):
    def test1(self):
        k, l = LNIS((5, 3, 4, 4, 2,))
        self.assertEqual(4, k)
        self.assertEqual([1, 3, 4, 5], list(l))

    def test2(self):
        k, l = LNIS((56, 28, 14, 7, 6, 8, 1, 1, 1, 1,))
        self.assertEqual(9, k)
        self.assertEqual([1, 2, 3, 4, 5, 7, 8, 9, 10], list(l))

    def test3(self):
        k, l = LNIS((5, 3, 4, 6, 4, 2, 5, 0, 1, 0, 2,))
        self.assertEqual(6, k)
        self.assertEqual([1, 3, 5, 6, 9, 10], list(l))

    def test4(self):
        expected = []
        s = (70, 101, 12, 15, 4, 19, 22, 11, 7, 1002, 11, 20, 18, 45, 11, 1, 17, 700, 12, 11, 9)
        k, l = list(LNIS(s))
        for i in l:
            expected.append(s[i-1])
        self.assertEqual(8, k)
        self.assertEqual([101, 22, 20, 18, 17, 12, 11, 9], expected)

    def test5(self):
        k, l = LNIS((1,))
        self.assertEqual(1, k)
        self.assertEqual([1], list(l))
