import random
import time


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1


# #################################### TESTE ######################################
benchmarkList = []

# 5 Testes
for i in range(0, 5):

    alist = []
    for j in range(0, 5000):
        n = random.randint(0, 100)
        alist.append(n)

    print(i + 1, "º Teste:")
    print('Lista Original:')
    print(alist)

    start = time.perf_counter()
    mergeSort(alist)
    end = time.perf_counter()

    print('Lista Ordenada:')
    print(alist)

    benchmark = end-start
    benchmarkList.append(benchmark)
    print("Time: ", benchmark, "\n")

print("Tempos Benchmarking: ", benchmarkList)
avgTime = sum(benchmarkList) / len(benchmarkList)

print("Média dos Tempos de Benchmarking: ", avgTime.__round__(5))
