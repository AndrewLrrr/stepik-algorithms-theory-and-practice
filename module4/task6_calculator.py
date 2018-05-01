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

# 1 -> {2, 3} # s = 1
# 2 -> 3, 4, 6 # s = 1, 2 | 3 -> 4, 6, 9 | s = 1, 3
# 3 -> 4, 6, 9, # (1, 2, 3,) | 5, 8, 12 # (1, 2, 4,) | 7, 12, 18 # (1, 2, 6,) \
#      5, 8, 12 # (1, 3, 4,) | 7, 12, 18 # (1, 3, 6,) | 10, 18, 27 # (1, 3, 9,)


def calculator(num):
    mem = dict()
    sequences = {(1,)}
    while num > 1:
        tmp = set()
        while len(sequences) > 0:
            seq = sequences.pop()
            n = seq[-1]
            if n not in mem:
                r = {n * 3, n * 2, n + 1}
                mem[n] = r
            else:
                r = mem[n]
            for j in r:
                new_seq = seq + (j,)
                if j == num:
                    return new_seq
                tmp.add(seq + (j,))
        sequences = tmp
    return sequences.pop()


if __name__ == '__main__':
    res = calculator(int(input()))
    print(len(res) - 1)
    print(*res)
