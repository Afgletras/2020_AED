import random
import time


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


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
    quickSort(alist)
    end = time.perf_counter()

    print('Lista Ordenada:')
    print(alist)

    benchmark = end-start
    benchmarkList.append(benchmark)
    print("Time: ", benchmark, "\n")

print("Tempos Benchmarking: ", benchmarkList)
avgTime = sum(benchmarkList) / len(benchmarkList)

print("Média dos Tempos de Benchmarking: ", avgTime.__round__(5))
