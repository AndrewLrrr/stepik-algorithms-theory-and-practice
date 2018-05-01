"""
У вас есть примитивный калькулятор, который умеет выполнять всего три операции с текущим числом x: заменить x на 2x, 3x 
или x+1. По данному целому числу 1≤n≤10^5 определите минимальное число операций k, необходимое, чтобы получить n из 1. 
Выведите k и последовательность промежуточных чисел.

Sample Input 1:
1
Sample Output 1:
0
1

Sample Input 2:
5
Sample Output 2:
3
1 2 4 5

Sample Input 3:
96234
Sample Output 3:
14
1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234 
"""

# 6 ->  6 - 1, 6 / 2, 6 / 3 -> 5, 3, 3
# 5 -> 5 - 1, 5 / 2, 5 / 3 -> 4
# 3 -> 3 - 1, 3 / 2, 3 / 3 -> 2, 1!
# 2 -> 2 - 1, 2 / 2, 2 / 3 -> 1, 1!

# 7
# 0 -> (7 - 1) | (7 / 2) | (7 / 3) -> 6
# 1 -> (6 - 1) | (6 / 2) | (6 / 3) -> 5, 3, 2
# 2 -> (5 - 1) | (5 / 2) | (5 / 3) | (3 - 1) | (3 / 2) | (3 / 3) | (2 - 1) | (2 / 2) | (2 / 3)
# 3 -> 6 | 2 1 | 1 1
# res = 1 3 6 7 | 1 2 6 7

# 10 -> 1, 3, 9, 10
# 0 -> (10 - 1) | (10 / 2) | (10 / 3) -> 9 5
# 1 -> (9 - 1) | (9 / 2) | (9 / 3) -> 8, 3 | (5 - 1) | (5 / 2) | (5 / 3) -> 4
# 2 -> (8 - 1) | (8 / 2) | (8 / 3) -> 7, 4 | (3 - 1) | (3 / 2) | (3 / 3) -> 2, 1 | (4 - 1) | (4 / 2) | (4 / 3) | 3, 2
# 3 -> 6 | 2 1 | 1 1
#        10
#        |  \
#        5   9 ----- 3 - 1
#         \   \      |
#          4   8     2
#          |   |     |\
#          2   4     1 1
#          |\
#          1 1
import sys

sys.setrecursionlimit(20000)


def calculator(num):
    mem = dict()

    def path_crawler(n):
        if n == 1:
            return tuple()
        if n in mem:
            return mem[n]
        else:
            a = n // 3 if n % 3 == 0 else None
            b = n // 2 if n % 2 == 0 else None
            c = n - 1
            res = []
            if a:
                r = path_crawler(a)
                r += (a,)
                res.append(r)
            if b:
                r = path_crawler(b)
                r += (b,)
                res.append(r)
            r = path_crawler(c)
            r += (c,)
            res.append(r)
            res = sorted(res, key=lambda x: len(x))[0]
            mem[n] = res
            return res
    path = path_crawler(num) + (num,)

    return path
