import unittest
from module2.task6_priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def test_sift_up(self):
        pq = PriorityQueue()
        pq._h = [11, 5, 9, 3, 4, 8, 12]
        pq._sift_up(12, 6)
        self.assertEquals([12, 5, 11, 3, 4, 8, 9], pq._h)

    def test_sift_down(self):
        pq = PriorityQueue()
        pq._h = [3, 11, 9, 5, 4, 8]
        pq._sift_down(3, 0)
        self.assertEquals([11, 5, 9, 3, 4, 8], pq._h)

    def test_insert(self):
        pq = PriorityQueue()
        pq._h = [11, 5, 9, 3, 4, 8]
        pq.insert(12)
        self.assertEquals([12, 5, 11, 3, 4, 8, 9], pq._h)
        pq.insert(15)
        self.assertEquals([15, 12, 11, 5, 4, 8, 9, 3], pq._h)
        pq.insert(10)
        self.assertEquals([15, 12, 11, 10, 4, 8, 9, 3, 5], pq._h)

    def test_extract_max(self):
        pq = PriorityQueue()
        pq._h = [15, 12, 11, 10, 4, 8, 9, 3, 5]
        _max = pq.extract_max()
        self.assertEqual(15, _max)
        self.assertEquals([12, 10, 11, 5, 4, 8, 9, 3], pq._h)
        _max = pq.extract_max()
        self.assertEqual(12, _max)
        self.assertEquals([11, 10, 9, 5, 4, 8, 3], pq._h)

    def test_with_one_item(self):
        pq = PriorityQueue()
        pq.insert(1)
        self.assertEqual(1, pq.extract_max())
