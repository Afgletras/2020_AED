import random
import time


def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


# #################################### TESTE ######################################
def nearSorted(alist):
    n = len(alist)
    alist.sort()
    for l in range(n//3):
        alist[(n//2) + (l+1)], alist[n-(l+1)] = alist[n-(l+1)], alist[(n//2) + (l+1)]


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

    nearSorted(alist)
    print('Lista Quase-Ordenada:')
    print(alist)

    start = time.perf_counter()
    bubbleSort(alist)
    end = time.perf_counter()

    print('Lista Ordenada:')
    print(alist)

    benchmark = end-start
    benchmarkList.append(benchmark)
    print("Time: ", benchmark, "\n")

print("Tempos Benchmarking: ", benchmarkList)
avgTime = sum(benchmarkList) / len(benchmarkList)

print("Média dos Tempos de Benchmarking: ", avgTime.__round__(5))
