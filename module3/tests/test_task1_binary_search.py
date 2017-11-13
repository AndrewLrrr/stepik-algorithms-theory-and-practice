import unittest

from module3.task1_binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test1(self):
        haystack = [1, 2, 3, 4, 5, 6]
        needles = [1, 6]
        expected = [1, 6]
        actual = []
        for needle in needles:
            actual.append(binary_search(needle, haystack))
        self.assertEqual(actual, expected)

    def test2(self):
        haystack = [1, 5, 8, 12, 13, 18, 20, 24, 30]
        needles = [8, 18, 12]
        expected = [3, 6, 4]
        actual = []
        for needle in needles:
            actual.append(binary_search(needle, haystack))
        self.assertEqual(actual, expected)

    def test3(self):
        haystack = [1, 5, 8, 12, 13, 18, 20, 24, 30, 45, 100, 150, 1000, 2000]
        needles = [8, 17, 45, 12, 1, 2, 3, 150, 1000, 24, 100, 150, 12, 2000, 30]
        expected = [3, -1, 10, 4, 1, -1, -1, 12, 13, 8, 11, 12, 4, 14, 9]
        actual = []
        for needle in needles:
            actual.append(binary_search(needle, haystack))
        self.assertEqual(actual, expected)

    def test4(self):
        self.assertEqual(-1, binary_search(8, []))
