import random
import time


# Function to do Quick sort
def quickSort(alist, low, high):
    if low < high:
        # partitioning index, alist[p] is now at right place
        pi = partition(alist, low, high)

        # Separately sort elements before partition and after partition
        quickSort(alist, low, pi - 1)
        quickSort(alist, pi + 1, high)


# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# alist, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(alist, low, high):
    i = (low - 1)  # index of smaller element
    pivot = alist[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if alist[j] < pivot:
            # increment index of smaller element
            i = i + 1
            alist[i], alist[j] = alist[j], alist[i]

    alist[i + 1], alist[high] = alist[high], alist[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# alist[] --> arraylist to be sorted,
# low  --> Starting index,
# high  --> Ending index


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
