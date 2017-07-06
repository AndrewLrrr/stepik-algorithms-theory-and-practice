"""
По данному числу 1≤n≤10^9 найдите максимальное число k, для которого n можно представитькак сумму
k различных натуральных слагаемых. Выведите в первой строке число k, во второй — k слагаемых.

Sample Input 1:
4

Sample Output 1:
2
1 3 

Sample Input 2:
6

Sample Output 2:
3
1 2 3
"""


def various_components(n):
    terms = []
    t = 1
    while True:
        rest = n - t
        if rest == 0:
            terms.append(t)
            break
        elif rest <= t:
            t += 1
            continue
        else:
            n = rest
            terms.append(t)
            t += 1
    return terms


def main():
    terms = various_components(int(input()))
    print(len(terms))
    print(*terms)


if __name__ == '__main__':
    main()
