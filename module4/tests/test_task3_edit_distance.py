import unittest

from module4.task3_edit_distance import edit_distance


class TestEditDistance(unittest.TestCase):
    def test1(self):
        self.assertEqual(0, edit_distance('ab', 'ab'))

    def test2(self):
        self.assertEqual(3, edit_distance('short', 'ports'))

    def test3(self):
        self.assertEqual(5, edit_distance('editing', 'distance'))
