"""
Дано целое число 1≤n≤40, необходимо вычислить n-е число Фибоначчи.

Sample Input:
3

Sample Output:
2

"""


def fib(n):
    a = 0
    b = 1
    while n != 0:
        a, b = b, a + b
        n -= 1
    return a


if __name__ == '__main__':
    print(fib(int(input())))
