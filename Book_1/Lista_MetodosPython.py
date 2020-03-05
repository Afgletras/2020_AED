# Métodos do Python para as operações em listas

lista = [1, 2, 3, 4, 5]
print("LISTA: ", lista)

# append - introduz um item no fim da lista
lista.append(6)
print("Append(6) - ", lista)

# insert - insere um item na posicao i
lista.insert(0, 0)
print("Insert(0, 0) - ", lista)

# pop - remove o ultimo item da lista OU o item i da lista
lista.pop()
print("Pop() - ", lista)
lista.pop(0)
print("Pop(0) - ", lista)

# del - Elimina um elemento da lista numa posicao i
del lista[4]
print("Del[4] - ", lista)

#________________________________________________________________________________
lista_exemplo = [3, 6, 8, 9, 0, 1, 3]
print("\nLISTA: ", lista_exemplo)


# sort - Coloca uma lista por ordem crescente / alfabetica
lista_exemplo.sort()
print("Sort - ", lista_exemplo)

# reverse - Coloca uma lista por ordem decrescente
lista_exemplo.reverse()
print("Reverse - ", lista_exemplo)

# index - Retorna o index do elemento
print("Index(9) - ", lista_exemplo.index(9))

# count - Conta o numero de vezes que o elemento aparece na lista
print("Count(3) - ", lista_exemplo.count(3))

# remove - Remove a primeira ocorrência de um elemento
lista_exemplo.remove(0)
print("Remove(0) - ", lista_exemplo)


# range - cria valores por ordem crescente
a = list(range(10))
b = list(range(5, 10))

print("\nRANGE: ")
print("Lista (range(10)): ", a, "\nLista (range(5,10)): ", b)




