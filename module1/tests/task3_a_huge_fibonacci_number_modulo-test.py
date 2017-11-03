import unittest

from module1.task3_a_huge_fibonacci_number_modulo import pisano_period
from module1.task3_a_huge_fibonacci_number_modulo import fib_mod


class TestPisanoPeriod(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, pisano_period(2))

    def test2(self):
        self.assertEqual(6, pisano_period(4))

    def test3(self):
        self.assertEqual(20, pisano_period(5))

    def test4(self):
        self.assertEqual(60, pisano_period(10))

    def test5(self):
        self.assertEqual(24, pisano_period(16))


class TestFibMod(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, fib_mod(10, 2))

    def test2(self):
        self.assertEqual(0, fib_mod(12, 3))

    def test3(self):
        self.assertEqual(2, fib_mod(875577, 10))
