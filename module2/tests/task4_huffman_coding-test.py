import unittest
from module2.task4_huffman_coding import huffman
from collections import Counter
from collections import OrderedDict


class TestHuffman(unittest.TestCase):
    def test1(self):
        string = 'a'
        codes = {
            'a': '0',
        }
        self.assertEquals(codes, huffman(self.str_to_ordered_letters(string)))

    def test2(self):
        string = 'abacabad'
        codes = {
            'a': '0',
            'b': '10',
            'c': '110',
            'd': '111'
        }
        self.assertEquals(codes, huffman(self.str_to_ordered_letters(string)))

    def test3(self):
        string = 'acceptance'
        codes = {
            'a': '111',
            'c': '10',
            'e': '00',
            'n': '010',
            'p': '011',
            't': '110'
        }
        self.assertEquals(codes, huffman(self.str_to_ordered_letters(string)))

    @staticmethod
    def str_to_ordered_letters(string):
        return OrderedDict(sorted(Counter(string).items(), key=lambda x: x[0]))
