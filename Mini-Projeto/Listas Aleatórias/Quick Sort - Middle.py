import random
import time


def quickSort(x, l, r):
    left = l
    right = r
    p = x[l + (r - l) // 2] # pivot element in the middle
    while left <= right:
        while x[left] < p: left += 1
        while x[right] > p: right -= 1
        if left <= right: # swap
            x[left], x[right] = x[right], x[left]
            left += 1
            right -= 1
    if l < right: # sort left list
        quickSort(x, l, right)
    if left < r: # sort right list
        quickSort(x, left, r)
    return x


# #################################### TESTE ######################################
benchmarkList = []

# 5 Testes
for i in range(0, 5):

    alist = []
    for j in range(0, 50):
        n = random.randint(0, 100)
        alist.append(n)

    print(i + 1, "º Teste:")
    print('Lista Original:')
    print(alist)

    start = time.perf_counter()
    quickSort(alist, 0, len(alist)-1)
    end = time.perf_counter()

    print('Lista Ordenada:')
    print(alist)

    benchmark = end-start
    benchmarkList.append(benchmark)
    print("Time: ", benchmark, "\n")

print("Tempos Benchmarking: ", benchmarkList)
avgTime = sum(benchmarkList) / len(benchmarkList)

print("Média dos Tempos de Benchmarking: ", avgTime.__round__(5))
