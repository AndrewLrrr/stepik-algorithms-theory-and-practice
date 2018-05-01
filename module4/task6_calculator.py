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


def calculator(num):
    sequences = {(num,)}
    while num > 1:
        tmp = set()
        while len(sequences) > 0:
            seq = sequences.pop()
            n = seq[-1]
            a = n // 3 if n % 3 == 0 else None
            b = n // 2 if n % 2 == 0 else None
            c = n - 1
            r = set(filter(None, (a, b, c)))
            for j in r:
                new_seq = seq + (j,)
                if j == 1:
                    return tuple(reversed(new_seq))
                tmp.add(seq + (j,))
        sequences = tmp
    return sequences.pop()


if __name__ == '__main__':
    res = calculator(int(input()))
    print(len(res) - 1)
    print(*res)
