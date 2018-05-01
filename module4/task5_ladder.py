"""
Даны число 1≤n≤10^2 ступенек лестницы и целые числа −10^4≤a1,…,an≤10^4, которыми помечены ступеньки. Найдите 
максимальную сумму, которую можно получить, идя по лестнице снизу вверх (от нулевой до n-й ступеньки), каждый раз 
поднимаясь на одну или две ступеньки.

Sample Input 1:
2
1 2
Sample Output 1:
3

Sample Input 2:
2
2 -1
Sample Output 2:
1

Sample Input 3:
3
-1 2 1
Sample Output 3:
3
"""


def ladder(weights):
    prev1 = None
    prev2 = None
    for w in weights:
        if prev1 is None:
            prev1 = w
        elif prev2 is None:
            prev2 = max(prev1 + w, w)
        else:
            tmp = max(prev1 + w, prev2 + w)
            prev1 = prev2
            prev2 = tmp
    return prev2 if prev2 else prev1


if __name__ == '__main__':
    _ = int(input())
    print(ladder(map(int, input().split())))
