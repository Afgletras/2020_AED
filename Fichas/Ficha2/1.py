import random

# O(n^2)
lista = []
for x in range(10):
   lista.append(random.randint(0,9))
   min = lista[0]
   for i in range(len(lista)):
       if lista[i] < min:
           min = lista[i]

print("O número mais pequeno da lista ", lista, "é ", min)

# O(n)
lista2 = [1, 4, 7, 9, 3, 2, 8, 0]
min2 = lista2[0]
for i in range(len(lista2)):
    if lista2[i] < min2:
        min2 = lista2[i]

print("O número mais pequeno da lista ", lista2, "é ", min2)