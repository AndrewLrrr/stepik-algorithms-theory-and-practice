import unittest

from module3.task2_number_of_inversions import number_of_inversions


class TestNumberOfInversions(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, number_of_inversions([2, 3, 9, 2, 9]))

    def test2(self):
        self.assertEqual(21, number_of_inversions([7, 6, 5, 4, 3, 2, 1]))

    def test3(self):
        self.assertEqual(1, number_of_inversions([1, 2, 3, 5, 4]))

    def test4(self):
        self.assertEqual(0, number_of_inversions([1, 2, 3, 4, 5]))
