import bisect
import random
import time

from module3.task3_points_and_lines import SegmentsManager


class SegmentsManagerBisect:
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
    pairs = [(random.randrange(1000), random.randrange(1000)) for _ in range(20000)]
    points = [random.randrange(1000) for _ in range(20000)]

    print('Start SegmentsManagerBisect...')
    start1 = time.time()
    smb = SegmentsManagerBisect()
    res_smb = []
    for pair in pairs:
        smb.add(pair)
    print('SegmentsManagerBisect add pairs in', time.time() - start1, 'seconds.')
    start2 = time.time()
    for p in points:
        res_smb.append(smb.find(p))
    print('SegmentsManagerBisect find points in', time.time() - start2, 'seconds.')
    print('SegmentsManagerBisect work in', time.time() - start1, 'seconds.')

    print()

    print('Start SegmentsManager...')
    start1 = time.time()
    sm = SegmentsManager()
    res_sm = []
    for pair in pairs:
        sm.add(pair)
    print('SegmentsManager add pairs in', time.time() - start1, 'seconds.')
    start2 = time.time()
    for p in points:
        res_sm.append(sm.find(p))
    print('SegmentsManager find points in', time.time() - start2, 'seconds.')
    print('SegmentsManager work in', time.time() - start1, 'seconds.')

    print()

    print('Are results correct?', 'Yes' if res_smb == res_sm else 'No')
