import random
import time
from module4.task2_longest_not_increase_sequence import LNIS


def LNIS_naive(A):
    D = [1] * len(A)
    R = [-1] * len(A)
    for i in range(len(A)):
        for j in range(i):
            if A[i] <= A[j] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
                R[i] = j
    max_length_idx = D.index(max(D))
    l = []
    while True:
        l.append(max_length_idx + 1)
        max_length_idx = R[max_length_idx]
        if max_length_idx == -1:
            break
    return max(D), reversed(l)


random_list = random.sample(range(1, 15001), 15000)
print('Random list of {} elements has been generated.'.format(len(random_list)))
print()

start = time.time()
k, _ = LNIS_naive(random_list)
print('LNIS_naive work in', time.time()-start, 'seconds.')
print('LNIS_naive max sequence length is {}'.format(k))
print()

start = time.time()
k, _ = LNIS(random_list)
print('LNIS work in', time.time()-start, 'seconds.')
print('LNIS max sequence length is {}'.format(k))
