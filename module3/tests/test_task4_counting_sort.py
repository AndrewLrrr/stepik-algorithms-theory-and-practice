import unittest

from module3.task4_counting_sort import counting_sort


class TestCountingSort(unittest.TestCase):
    def test1(self):
        self.assertEqual([2, 2, 3, 9, 9], counting_sort([2, 3, 9, 2, 9]))

    def test2(self):
        self.assertEqual([0, 0, 1, 2, 3, 10, 10], counting_sort([2, 3, 10, 0, 10, 1, 0]))

    def test3(self):
        self.assertEqual([0, 0, 1, 2, 3, 10, 10], counting_sort([0, 0, 1, 2, 3, 10, 10]))
