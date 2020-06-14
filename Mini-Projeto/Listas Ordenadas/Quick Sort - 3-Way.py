import random
import time


def quickSort(alist):
    if len(alist) <= 1: 
        return alist
    pivot = alist[0]
    less, equal, greater = partition(alist, pivot)
    return quickSort(less) + equal + quickSort(greater)


def partition(alist, pivot):
    less, equal, greater = [], [], []
    for val in alist:
        if val < pivot: 
            less.append(val)
        if val == pivot: 
            equal.append(val)
        if val > pivot: 
            greater.append(val)
    return less, equal, greater


# #################################### TESTE ######################################

benchmarkList = []
# 5 Testes
for i in range(0, 5):

    alist = []
    for j in range(0, 200):
        n = random.randint(0, 100)
        alist.append(n)

    alist.sort()
    print(i+1, "º Teste:")
    print(alist)

    start = time.perf_counter()
    quickSort(alist)
    print(alist)
    end = time.perf_counter()

    benchmark = end-start
    benchmarkList.append(benchmark)
    print("Time: ", benchmark, "\n")

print("Benchmarking Times: ", benchmarkList)
avgTime = sum(benchmarkList) / len(benchmarkList)
print("Média dos Tempos de Benchmarking: ", avgTime)
