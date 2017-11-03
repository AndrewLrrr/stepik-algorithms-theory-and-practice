"""
По данной непустой строке s длины не более 10^4, состоящей из строчных букв латинского алфавита, 
постройте оптимальный беспрефиксный код. В первой строке выведите количество различных букв k, 
встречающихся в строке, и размер получившейся закодированной строки. В следующих kk строках запишите 
коды букв в формате "letter: code". В последней строке выведите закодированную строку.

Sample Input 1:
a

Sample Output 1:
1 1
a: 0
0

Sample Input 2:
abacabad

Sample Output 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
"""

from collections import Counter
from collections import OrderedDict


class Node:
    def __init__(self, weight, key=None, left=None, right=None):
        self.weight = weight
        self.key = key
        self.left = left
        self.right = right


class PriorityQueue:
    list = []

    def insert(self, v, w):
        self.list.append((v, w))

    def extract_min(self):
        if self.is_empty():
            return None
        _min = min(self.list, key=lambda x: x[1])
        self.list.remove(_min)
        return _min[0]

    def is_empty(self):
        return not self.list


def get_weight(node):
    return node.weight if node is not None else 0


def post_order(node):
    def crawler(node, codes, code=''):
        if node is not None:
            codes = crawler(node.left, codes, code + '0')
            codes = crawler(node.right, codes, code + '1')
            if node.key is not None:
                codes[node.key] = code
        return codes
    return crawler(node, {})


def huffman(letters):
    q = PriorityQueue()
    for k, v in letters.items():
        q.insert(Node(v, k), v)
    while True:
        n1 = q.extract_min()
        n2 = q.extract_min()
        t = Node(get_weight(n1) + get_weight(n2), None, n1, n2)
        if q.is_empty() is True:
            break
        q.insert(t, t.weight)
    return post_order(t)


def main():
    string = input()
    codes = OrderedDict(sorted(huffman(Counter(string)).items(), key=lambda x: x[0]))
    code = ''.join([codes[l] for l in string])
    print(len(codes), len(code))
    print('\n'.join(k + ': ' + v for k, v in codes.items() if k != 'key'))
    print(code)


if __name__ == '__main__':
    main()
