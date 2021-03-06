import random
import time


def quickSort(alist, start, stop):
    if start < stop:
        # pivotindex is the index where the pivot lies in the alist
        pivotindex = partitionrand(alist, start, stop)

        # At this stage the alist is partially sorted around the pivot.
        # separately sorting the left half of the alist and the right half of the alist.
        quickSort(alist, start, pivotindex)
        quickSort(alist, pivotindex + 1, stop)

    # This function generates random pivot, swaps the first element with the pivot and calls the partition function.
def partitionrand(alist, start, stop):
    # Generating a random number between  
    # the starting index of the alist and  
    # the ending index of the alist. 
    randpivot = random.randrange(start, stop)

    # Swapping the starting element of the alist and the pivot
    alist[start], alist[randpivot] = alist[randpivot], alist[start]
    return partition(alist, start, stop)


def partition(alist, start, stop):
    pivot = start  # pivot 
    i = start - 1
    j = stop + 1
    while True:
        while True:
            i = i + 1
            if alist[i] >= alist[pivot]:
                break
        while True:
            j = j - 1
            if alist[j] <= alist[pivot]:
                break
        if i >= j:
            return j
        alist[i], alist[j] = alist[j], alist[i]


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
    for j in range(0, 5000):
        n = random.randint(0, 100)
        alist.append(n)

    print(i + 1, "º Teste:")
    print('Lista Original:')
    print(alist)

    nearSorted(alist)
    print('Lista Quase-Ordenada:')
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
