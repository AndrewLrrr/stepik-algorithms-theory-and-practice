import unittest
from module2.task3_various_components import various_components


class TestVariousComponents(unittest.TestCase):
    def test1(self):
        self.assertEquals([1, 3], various_components(4))

    def test2(self):
        self.assertEquals([1, 4], various_components(5))

    def test3(self):
        self.assertEquals([1, 2, 3], various_components(6))

    def test4(self):
        self.assertEquals([1, 2, 3, 4, 5, 6], various_components(21))
