import unittest

from module4.task4_knapsack import knapsack


class TestKnapsack(unittest.TestCase):
    def test1(self):
        self.assertEqual(9, knapsack(10, [1, 3, 8]))

    def test2(self):
        self.assertEqual(4, knapsack(10, [1, 1, 1, 1]))

    def test3(self):
        self.assertEqual(4, knapsack(4, [1, 1, 1, 1]))

    def test4(self):
        self.assertEqual(20, knapsack(20, [3, 6, 10, 11]))
