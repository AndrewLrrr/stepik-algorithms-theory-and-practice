"""
Первая строка входа содержит число операций 1≤n≤10^5. Каждая из последующих n строк задают операцию одного 
из следующих двух типов:

Insert x, где 0≤x≤10^9 — целое число;
ExtractMax.
Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает максимальное число и выводит его.

Sample Input:
6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax

Sample Output:
200
500
"""


class PriorityQueue(list):
    def append(self, n):
        super().append(n)
        self._sift_up(n, self._last_idx())

    def extract_max(self):
        self._swap(0, self._last_idx())
        _max = self.pop()
        if len(self) > 0:
            self._sift_down(self[0], 0)
        return _max

    def _safe_value(self, i):
        try:
            return self[i]
        except IndexError:
            return -float("inf")

    def _swap(self, i, j):
        self[i], self[j] = self[j], self[i]

    def _next(self, i):
        r_i = self._right_child(i)
        l_i = self._left_child(i)
        return r_i if self._safe_value(r_i) > self._safe_value(l_i) else l_i

    def _last_idx(self):
        return len(self) - 1

    def _sift_up(self, n, i):
        j = self._parent(i)
        if j >= 0 and self[j] < n:
            self._swap(i, j)
            self._sift_up(n, j)

    def _sift_down(self, n, i):
        j = self._next(i)
        if j <= self._last_idx() and self[j] > n:
            self._swap(i, j)
            self._sift_down(n, j)

    @staticmethod
    def _parent(i):
        return (i + 1) // 2 - 1

    @staticmethod
    def _right_child(i):
        return (i + 1) * 2

    @staticmethod
    def _left_child(i):
        return (i + 1) * 2 - 1


def main():
    total = int(input())
    pq = PriorityQueue()
    for i in range(total):
        command = input()
        if command.startswith('Insert'):
            _, n = command.split()
            pq.append(int(n))
        elif command.startswith('ExtractMax'):
            print(pq.extract_max())


if __name__ == '__main__':
    main()
