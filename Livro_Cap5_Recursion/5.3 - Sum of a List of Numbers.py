import time
# Vamos supor que se quer calcular a soma de numeros de uma lista: [1, 3, 5, 7, 9]

# Função Iterativa
def listsum_iterative(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum
iterativeStart = time.perf_counter()
print(listsum_iterative([1, 3, 5, 7, 9]))
iterativeEnd = time.perf_counter()

iterativeTime = iterativeEnd-iterativeStart
print("Tempo Iterativa: " + str(iterativeTime))


# Imaginando que não havia ciclos for ou while, como fazer a mesma função?
# R: Podemos ir fazendo soma do resto da lista enquanto se retira numero a numero:

# listSum(numList) = first(numList) + listSum(rest(numList))

# Função Recursiva
def listsum_recursive(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum_recursive(numList[1:])

recursionStart = time.perf_counter()
print(listsum_recursive([1, 3, 5, 7, 9]))
recursionEnd = time.perf_counter()

recursionTime = recursionEnd-recursionStart
print("Tempo Recursão: " + str(recursionTime))

# Só para testar os tempos:
if recursionTime < iterativeTime:
    print("Algoritmo RECURSIVO é mais rápido")
else:
    print("Algoritmo ITERATIVO é mais rápido")

