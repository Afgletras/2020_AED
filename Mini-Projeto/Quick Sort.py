import random
import time
import matplotlib.pyplot as plt

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

benchmarkList = []
# 20 Testes
for i in range(1, 21):

    alist = []
    for j in range(0, 200):
        n = random.randint(0, 200)
        alist.append(n)

    print(i, "º Teste:")
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

#plt.plot([1, 2, 3, 4])
#plt.ylabel('some numbers')
#plt.show()




