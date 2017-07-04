"""
По данным двум числам 1≤a,b≤2*10^9 найдите их наибольший общий делитель.

Sample Input 1:
18 35
Sample Output 1:
1

Sample Input 2:
14159572 63967072
Sample Output 2:
4

"""


def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(a % b, b) if a >= b else gcd(a, b % a)


if __name__ == '__main__':
    print(gcd(*map(int, input().split())))
