# A list is an ordered collection of zero or more references to Python data objects.
# Lists are written as comma-delimited values enclosed in square brackets.
# The empty list is simply [ ].

# Operações diretas de uma lista:
lista = [7, 5, 3, 1, 3, 5, 7]
print("LISTA: ", lista)

# Indexação
a = lista[2]
print("lista[2] - ", a)

# Concatenação
lista2 = [3, 2, 1]
print("LISTA: ", lista, "\nLISTA2: ", lista2)
b = lista + lista2
print("Lista + Lista2 - ", b)

# Repetição
c = lista * 2
print("Lista*2 -", c)

# Membro
d = 3 in lista
print("3 in lista? - ", d)

# Comprimento
e = len(lista)
print("Comprimento da lista - ", e)

# Slicing
f = lista[1:4]
print("Slicing [1:4] - ", f)