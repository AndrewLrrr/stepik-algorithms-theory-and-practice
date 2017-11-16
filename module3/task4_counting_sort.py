"""
Первая строка содержит число 1≤n≤10^4, вторая — nn натуральных чисел, не превышающих 10. Выведите упорядоченную по 
неубыванию последовательность этих чисел.

Sample Input:
5
2 3 9 2 9

Sample Output:
2 2 3 9 9
"""


def counting_sort(l):
    c = [0] * (max(l) + 1)
    for k in l:
        c[k] += 1
    b = []
    for i, v in enumerate(c):
        b.extend([i] * v)
    return b


if __name__ == '__main__':
    _ = input()
    print(*counting_sort([int(i) for i in input().split()]))
