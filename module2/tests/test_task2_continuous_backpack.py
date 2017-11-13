import unittest

from module2.task2_continuous_backpack import continuous_backpack


class TestContinuousBackpack(unittest.TestCase):
    def test1(self):
        stocks = [
            (60, 20),
            (100, 50),
            (120, 30),
        ]
        self.assertEqual(180.000, continuous_backpack(50, stocks))

    def test2(self):
        stocks = [
            (60, 20),
            (100, 50),
            (120, 30),
        ]
        self.assertEqual(200.000, continuous_backpack(60, stocks))

    def test3(self):
        stocks = [
            (70, 60),
        ]
        self.assertEqual(23.333, continuous_backpack(20, stocks))
