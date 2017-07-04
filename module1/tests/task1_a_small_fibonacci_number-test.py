import unittest
from module1.task1_a_small_fibonacci_number import fib


class TestFib(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, fib(3))

    def test2(self):
        self.assertEqual(5, fib(5))

    def test3(self):
        self.assertEqual(8, fib(6))

    def test4(self):
        self.assertEqual(21, fib(8))

