import unittest

from module2.task5_huffman_decoding import huffman_decode


class TestHuffmanDecode(unittest.TestCase):
    def test1(self):
        codes = {
            '0': 'a',
        }
        self.assertEqual('a', huffman_decode('0', codes))

    def test2(self):
        codes = {
            '0': 'a',
            '10': 'b',
            '110': 'c',
            '111': 'd',
        }
        self.assertEqual('abacabad', huffman_decode('01001100100111', codes))

    def test3(self):
        codes = {
            '1110': 'a',
            '001': 'c',
            '10': 'i',
            '1101': 'n',
            '011': 'o',
            '1100': 'q',
            '000': 's',
            '1111': 't',
            '010': 'u',
        }
        self.assertEqual('acquisition', huffman_decode('1110001110001010000101111100111101', codes))

