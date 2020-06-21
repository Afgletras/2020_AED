import random


# exer 1
def sequential_search(alist, value):
    for i in range(len(alist)):
        if alist[i] == value:
            return True
    return False
x=[15,18,2,19,18,0,8,14,19,14]
print(sequential_search(x,18))
# resposta: alínea D. Foram feitas 2 comparações pois, o valor a ser pesquisado é o segundo elemento da lista.


# exer 2
def sequential_search_orederedList(alist, value):
    for i in range(len(alist)):
        if alist[i] == value:
            return True
        elif alist[i] > value:
                break
    return False
a=[3,5,6,8,11,12,14,15,17,18]
print(sequential_search_orederedList(a,13))

# dúvida: em cada elemento são feitas 2 comparações, uma para verificar se o value é igual ao elemento i
# da lista e outra para verificar se o value é menor que o i da lista. Assim teríamos 14 comparações, que
# resultam de 7 * 2 comparações.


# exer 3
def binary_search(alist, value):
    if len(alist) == 1:
        return alist[0] == value
    mid = len(alist)//2
    if value == alist[mid]:
        return True
    elif value < alist[mid]:
        return binary_search(alist[:mid], value)
    else:
        return binary_search(alist[mid+1:], value)
b=[3,5,6,8,11,12,14,15,17,18]
print(sequential_search_orederedList(b,8))
# B

# exer 4
c= [3,5,6,8,11,12,14,15,17,18]
print(sequential_search_orederedList(c,16))
# D


# exer 5
def binarySearch_iterative(alist, item):

    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


def binarySearch_recursive(alist, item):

    if len(alist) == 0:
        return False

    # NÃO é necessário (mas pode-se deixar)
    # if len(alist) == 1:
    #     return alist[0] == item

    midpoint = len(alist) // 2
    if item == alist[midpoint]:
        return True
    else:
        if item < alist[midpoint]:
            return binarySearch_recursive(alist[:midpoint], item)
        else:
            return binarySearch_recursive(alist[midpoint + 1:], item)

d=[]
for i in range(500):
    d.append(random.randint(1,1000))

d.sort()
print(d)
print(binarySearch_iterative(d,20))
print(binarySearch_recursive(d,20))


#exer 6
def binarySearch_recursiveNoSlice(lista,inicio,fim, item):
    if len(lista) == 0:
        return False
    elif lista[0]>item:
        return False
    elif lista[0]==item:
        return True
    elif lista[fim]==item:
        return True
    elif lista[fim]<item:
        return False
    pontoMedio = (inicio+fim) // 2
    if item == lista[pontoMedio]:
        return True
    else:
        if item < lista[pontoMedio]:
            return binarySearch_recursiveNoSlice(lista,inicio,pontoMedio-1, item)
        else:
            return binarySearch_recursiveNoSlice(lista,pontoMedio+1,fim, item)


#6-a)
noSlice = []
for i in range(50):
    noSlice.append(random.randint(1,50))
# 6-b)
noSlice.append(10)

noSlice.sort()
print(noSlice)
print(binarySearch_recursiveNoSlice(noSlice,0,3,1))