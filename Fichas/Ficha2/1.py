import random

# O(n^2)
lista = [2, 5, 6, 9, 0, 2, 4, 3, 1, 9]
min = lista[0]
for i in range(len(lista)):
    if lista[i] < min:
        min = lista[i]

print("O(n^2) - O número mais pequeno da lista ", lista, "é ", min)


# O(n)
lista2 = []
for x in range(10):
   lista2.append(random.randint(0,9))

list.sort(lista2)
print("O(n) - O número mais pequeno da lista ", lista2, "é ", lista2[0])

