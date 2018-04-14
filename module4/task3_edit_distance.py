"""
Вычислите расстояние редактирования (расстояние Левенштейна) двух данных непустых строк длины не более 10^2, содержащих 
строчные буквы латинского алфавита.

Sample Input 1:
ab
ab

Sample Output 1:
0

Sample Input 2:
short
ports

Sample Output 2:
3
"""


def edit_distance(a, b):
    d = []
    n, m = len(a) + 1, len(b) + 1
    for j in range(n):
        d.append([0] * m)
        d[j][0] = j
    for i in range(m):
        d[0][i] = i
    for i in range(1, n):
        for j in range(1, m):
            d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + diff(a[i-1], b[j-1]))
    return d[n-1][m-1]


def diff(a, b):
    return 1 if a != b else 0


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    print(edit_distance(s1, s2))
