import unittest

from module4.task6_calculator import calculator


class TestKnapsack(unittest.TestCase):
    def test1(self):
        self.assertEqual((1,), calculator(1))

    def test2(self):
        self.assertEqual((1, 2, 4, 5,), calculator(5))

    def test3(self):
        self.assertEqual((1, 3, 9, 10,), calculator(10))

    def test4(self):
        self.assertEqual((1, 2, 4, 8, 24, 25, 50, 100,), calculator(100))

    def test5(self):
        self.assertEqual((1,
                          2,
                          6,
                          7,
                          21,
                          22,
                          66,
                          198,
                          594,
                          1782,
                          5346,
                          16038,
                          16039,
                          32078,
                          96234,), calculator(96234))
