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
benchmarkList = []

# 20 Testes
for i in range(0, 5):

    alist = []
    for j in range(0, 200):
        n = random.randint(0, 100)
        alist.append(n)

    print(i, "º Teste:")
    print(alist)

    start = time.perf_counter()
    bubbleSort(alist)
    print(alist)
    end = time.perf_counter()

    benchmark = end-start
    benchmarkList.append(benchmark)
    print("Time: ", benchmark, "\n")

print("Benchmarking Times: ", benchmarkList)
avgTime = sum(benchmarkList) / len(benchmarkList)
print("Média dos Tempos de Benchmarking: ", avgTime)
