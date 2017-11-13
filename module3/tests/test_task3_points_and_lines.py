import unittest

from module3.task3_points_and_lines import SegmentsManager


class TestSegmentsManager(unittest.TestCase):
    def test1(self):
        s = SegmentsManager()
        for segment in [(0, 5), (7, 10)]:
            s.add(segment)
        points = [1, 6, 11]
        expected = [1, 0, 0]
        actual = [s.find(p) for p in points]
        self.assertEqual(expected, actual)

    def test2(self):
        s = SegmentsManager()
        for segment in [(1, 10), (2, 8), (4, 5)]:
            s.add(segment)
        points = [3, 9, 5, 4, 12]
        expected = [2, 1, 3, 3, 0]
        actual = [s.find(p) for p in points]
        self.assertEqual(expected, actual)

    def test3(self):
        s = SegmentsManager()
        for segment in [(0, 3), (1, 3), (2, 3), (3, 4), (3, 5), (3, 6)]:
            s.add(segment)
        points = [1, 2, 3, 4, 5, 6]
        expected = [2, 3, 6, 3, 2, 1]
        actual = [s.find(p) for p in points]
        self.assertEqual(expected, actual)

    def test4(self):
        s = SegmentsManager()
        for segment in [(6, 6), (2, 3), (2, 5), (3, 5), (2, 7), (5, 7), (3, 7)]:
            s.add(segment)
        points = [1, 2, 3, 5, 6, 7]
        expected = [0, 3, 5, 5, 4, 3]
        actual = [s.find(p) for p in points]
        self.assertEqual(expected, actual)
