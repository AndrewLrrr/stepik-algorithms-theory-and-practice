import unittest

from module1.task2_the_last_digit_of_a_large_fibonacci_number import fib_digit


class TestFibDigit(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, fib_digit(3))

    def test2(self):
        self.assertEqual(1, fib_digit(8))

    def test3(self):
        self.assertEqual(4, fib_digit(12))

    def test4(self):
        self.assertEqual(1, fib_digit(19))

    def test5(self):
        self.assertEqual(2, fib_digit(875577))
