import unittest

from module2.task1_segments_cover import segments_cover


class TestSegmentsCover(unittest.TestCase):
    def test1(self):
        segments = [
            (1, 3),
            (2, 5),
            (3, 6)
        ]
        self.assertEqual([3], segments_cover(segments))

    def test2(self):
        segments = [
            (4, 7),
            (1, 3),
            (2, 5),
            (5, 6)
        ]
        self.assertEqual([3, 6], segments_cover(segments))

    def test3(self):
        segments = [
            (7, 8),
            (1, 2),
            (3, 4),
            (5, 6)
        ]
        self.assertEqual([2, 4, 6, 8], segments_cover(segments))

    def test4(self):
        segments = [
            (1, 1),
        ]
        self.assertEqual([1], segments_cover(segments))

    def test5(self):
        segments = [
            (8, 9),
            (1, 7),
            (3, 4),
            (5, 8),
            (1, 2),
        ]
        self.assertEqual([2, 4, 8], segments_cover(segments))
