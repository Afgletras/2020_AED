import random
import time


def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum-1

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

def insertionSort(alist):
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)




benchmarkList = []

for i in range(0, 5):

    list = []
    for j in range(0,200):
        n = random.randint(0, 100)
        list.append(n)

    print(i + 1, "º Teste:")
    print('Lista Original:')
    print(list)
    #print('Lista ordenada decrescente:')
    #list.sort(reverse=True)
    print(list)

    start = time.perf_counter()

    shortBubbleSort(list)
    #selectionSort(list)
    #insertionSort(list)
    #mergeSort(list)

    end = time.perf_counter()

    print('Lista Ordenada:')
    print(list)

    benchmark = end-start
    benchmarkList.append(benchmark)
    print("Time: ", benchmark, "\n")

print("Tempos Benchmarking: ", benchmarkList)
avgTime = sum(benchmarkList) / len(benchmarkList)

print("Média dos Tempos de Benchmarking: ", avgTime.__round__(5))






# Exercício 4
# Já ordenada (crescente)

#shortBubbleSort - 0.00134(100), 0.00509(200), 03632(500)

#selectionsort - 0.00057(100), 0.0024(200), 0.1485(500)

#insertionSort - 0.00057(100), 0.00239(200), 0.01803(500)

#mergeSort - 0.00672(100), 0.01308(200), 0.0309(500)


# Existem grandes diferenças de tempo ao correr o shortBubbleSort numa lista ordenada e numa não ordenada, visto que, o algoritmo só vai percorrer a lista uma única vez.
# No selectionSort tivemos tempos idênticos.
# No InsertionSort tivemos uma diferança nos tempos, demorou aproximadamente um terço do tempo numa lista ordenada em comparação a uma lista desordenada.
# No mergeSort tivemos tempos muitos idênticos, visto que o processo é mesmo. Apenas tivemos um decréscimo de tempo numa lista ordenada devido às trocas que não foram precisas de ser feitas mas sendo que a comparação só é feita após a divisão em pequenos grupos, os tempos são bastante similares#Exercício 5



#Exercício 5
#Já ordenada (Descrescente)

# #shortBubbleSort - 0.00192(100). 0.00763(200), 0.04857 (500)

# #selectionsort - 0.00059(100), 0.00228(200), 0.01465(500)

# #insertionSort - 0.00121(100), 0.0048 (200), 0.03163(500)

# #mergeSort - 0.00641(100), 0.01237(200), 0.03301(500)


# ShortBubblesort tivemos um ligeiro aumento de tempo

# SelectionSort tivemos tempos idênticos

# InsertionSort demorou o dobro do tempo numa lista ordenada de forma decrescente

# MergeSort também com tempos muitos idênticos
