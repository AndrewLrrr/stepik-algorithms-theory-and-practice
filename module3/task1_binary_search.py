"""
В первой строке даны целое число 1≤n≤10^5 и массив A[1…n] из n различных натуральных чисел, не превышающих 10^9, 
в порядке возрастания, во второй — целое число 1≤k≤10^5 и k натуральных чисел b1,…,bk, не превышающих 10^9. 
Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n, для которого A[j]=bi, или −1, если 
такого j нет.

Sample Input:
5 1 5 8 12 13
5 8 1 23 1 11

Sample Output:
3 1 -1 1 -1
"""


def binary_search(x, lst):
    l = 0
    r = len(lst)
    while r - l > 1:
        idx = (l + r) // 2
        if x < lst[idx]:
            r = idx
        else:
            l = idx
    return l + 1 if r > 0 and lst[l] == x else -1


def main():
    _, *haystack = [int(i) for i in input().split()]
    _, *needles = [int(i) for i in input().split()]
    for needle in needles:
        print(binary_search(needle, haystack), end=' ')


if __name__ == '__main__':
    main()
