"""
В первой строке задано два целых числа 1≤n≤50000 и 1≤m≤50000 — количество отрезков и точек на прямой, соответственно. 
Следующие n строк содержат по два целых числа ai и bi (ai≤bi) — координаты концов отрезков. Последняя строка содержит 
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


def bisect_left(a, n):
    l = 0
    r = len(a) - 1
    while l <= r:
        idx = (l + r) // 2
        v = a[idx]
        if n > v:
            l = idx + 1
        else:
            r = idx - 1
    return l


def bisect_right(a, n):
    l = 0
    r = len(a) - 1
    while l <= r:
        idx = (l + r) // 2
        v = a[idx]
        if n < v:
            r = idx - 1
        else:
            l = idx + 1
    return l


def insort(a, n):
    low = bisect_right(a, n)
    a.insert(low, n)
    return a


class SegmentsManager:
    def __init__(self):
        self._opening = []
        self._ending = []

    def add(self, segment):
        start, finish = segment
        insort(self._opening, start)
        insort(self._ending, finish)

    def find(self, point):
        i1 = bisect_right(self._opening, point)
        i2 = bisect_left(self._ending, point)
        return i1 - i2


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
