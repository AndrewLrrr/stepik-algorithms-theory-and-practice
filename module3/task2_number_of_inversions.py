"""
Первая строка содержит число 1≤n≤10^5, вторая — массив A[1…n], содержащий натуральные числа, не превосходящие 
10^9. Необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j]. (Такая пара элементов называется 
инверсией массива. Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности: например, в 
упорядоченном по неубыванию массиве инверсий нет вообще, а в массиве, упорядоченном по убыванию, инверсию образуют 
каждые два элемента.)

Sample Input:
5
2 3 9 2 9

Sample Output:
2
"""


def merge_sort_with_inversion(a):
    if len(a) == 1:
        return a, 0

    half = len(a) // 2
    l, i_1 = merge_sort_with_inversion(a[:half])
    r, i_2 = merge_sort_with_inversion(a[half:])
    inversion = i_1 + i_2

    res = []
    l_pointer = 0
    r_pointer = 0
    while True:
        if l_pointer < len(l) and r_pointer < len(r):
            if l[l_pointer] <= r[r_pointer]:
                v = l[l_pointer]
                l_pointer += 1
            else:
                v = r[r_pointer]
                r_pointer += 1
                inversion += len(l) - l_pointer
        elif l_pointer < len(l):
            v = l[l_pointer]
            l_pointer += 1
        elif r_pointer < len(r):
            v = r[r_pointer]
            r_pointer += 1
        else:
            break
        res.append(v)
    return res, inversion


def number_of_inversions(a):
    _, i = merge_sort_with_inversion(a)
    return i

if __name__ == '__main__':
    _ = input()
    a = [int(i) for i in input().split()]
    print(number_of_inversions(a))
