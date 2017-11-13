"""
В первой строке задано два целых числа 1≤n≤50000 и 1≤m≤50000 — количество отрезков и точек на прямой, соответственно. 
Следующие nn строк содержат по два целых числа ai и bi (ai≤bi) — координаты концов отрезков. Последняя строка содержит 
m целых чисел — координаты точек. Все координаты не превышают 10^8 по модулю. Точка считается принадлежащей отрезку, 
если она находится внутри него или на границе. Для каждой точки в порядке появления во вводе выведите, скольким 
отрезкам она принадлежит.

Sample Input:
2 3
0 5
7 10
1 6 11

Sample Output:
1 0 0
"""

import bisect


class SegmentsManager:
    def __init__(self):
        self._opening = []
        self._ending = []

    def add(self, segment):
        start, finish = segment
        self._add_open_point(start)
        self._add_end_point(finish)

    def find(self, point):
        i1 = self._find_open_point(point)
        i2 = self._find_end_point(point)
        return i1 - i2

    def _add_open_point(self, point):
        bisect.insort(self._opening, point)

    def _add_end_point(self, point):
        bisect.insort_left(self._ending, point)

    def _find_open_point(self, point):
        return bisect.bisect(self._opening, point)

    def _find_end_point(self, point):
        return bisect.bisect_left(self._ending, point)


if __name__ == '__main__':
    sm = SegmentsManager()
    res = []
    s, _ = [int(i) for i in input().split()]
    for i in range(s):
        sm.add(tuple(int(i) for i in input().split()))
    points = tuple(int(i) for i in input().split())
    for p in points:
        res.append(sm.find(p))
    print(*res)
