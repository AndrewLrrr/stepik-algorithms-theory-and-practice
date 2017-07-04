import unittest
from module1.task4_the_greatest_common_divisor import gcd


class TestGcd(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, gcd(18, 35))

    def test2(self):
        self.assertEqual(10000, gcd(20000, 10000))

    def test3(self):
        self.assertEqual(10000, gcd(10000, 20000))

    def test4(self):
        self.assertEqual(5000, gcd(10000, 15000))

    def test5(self):
        self.assertEqual(5000, gcd(15000, 10000))

    def test6(self):
        self.assertEqual(4, gcd(14159572, 63967072))
