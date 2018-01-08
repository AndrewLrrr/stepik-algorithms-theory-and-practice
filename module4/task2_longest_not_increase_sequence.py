"""
Дано целое число 1≤n≤10^5 и массив A[1…n], содержащий неотрицательные целые числа, не превосходящие 10^9. Найдите 
наибольшую невозрастающую подпоследовательность в A. В первой строке выведите её длину k, во второй — её индексы 
1≤i1<i2<…<ik≤n (таким образом, A[i1]≥A[i2]≥…≥A[in]).

Sample Input:
5
5 3 4 4 2

Sample Output:
4
1 3 4 5 
"""


def binary_idx_search(lst, x):
    l = 0
    r = len(lst)
    while r - l > 1:
        idx = (l + r) // 2
        if x > lst[idx]:
            r = idx
        else:
            l = idx
    return l + 1 if lst[l] >= x else l


def LNIS(A):
    n = len(A)
    D = [0] * n
    I = [-1] * n
    R = [-1] * n
    length = 1
    max_length_idx = 0
    D[0] = A[0]
    I[0] = 0
    for i in range(1, n):
        if A[i] > D[0]:
            D[0] = A[i]
            I[0] = i
        elif A[i] <= D[length-1]:
            D[length] = A[i]
            I[length] = i
            R[i] = I[length-1]
            length += 1
            max_length_idx = i
        else:
            idx = binary_idx_search(D, A[i])
            D[idx] = A[i]
            I[idx] = i
            R[i] = I[idx - 1] if idx > 0 else -1
    l = []
    while True:
        l.append(max_length_idx + 1)
        max_length_idx = R[max_length_idx]
        if max_length_idx == -1:
            break
    return length, reversed(l)


if __name__ == '__main__':
    _ = input()
    s = [int(i) for i in input().split()]
    k, l = LNIS(s)
    print(k)
    print(*l)
