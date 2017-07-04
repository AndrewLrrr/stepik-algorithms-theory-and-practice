"""
Даны целые числа 1≤n≤10^18 и 2≤m≤10^5, необходимо найти остаток от деления n-го числа Фибоначчи на m.

Sample Input:
10 2

Sample Output:
1

"""


def pisano_period(m):
    a = 0
    b = 1
    counter = 0
    while True:
        a, b = b, (a + b) % m
        counter += 1
        if a == 0 and b == 1:
            return counter


def fib_mod(n, m):
    n = n % pisano_period(m)
    a = 0
    b = 1
    while n != 0:
        a, b = b, (a + b) % m
        n -= 1
    return a


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == '__main__':
    main()
