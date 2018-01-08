"""
Дано целое число 1≤n≤10^3 и массив A[1…n] натуральных чисел, не превосходящих 2⋅10^9. Выведите максимальное 1≤k≤n, для 
которого найдётся подпоследовательность 1≤i1<i2<…<ik≤n длины k, в которой каждый элемент делится на предыдущий 
(формально: для  всех 1≤j<k, A[ij]|A[ij+1]).

Sample Input:
4
3 6 7 12

Sample Output:
3
"""


def max_LDS(A):
    D = [1] * len(A)
    for i in range(len(A)):
        for j in range(i):
            if A[i] % A[j] == 0 and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
    return max(D)


if __name__ == '__main__':
    _ = input()
    s = [int(i) for i in input().split()]
    print(max_LDS(s))
