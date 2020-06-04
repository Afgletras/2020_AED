# Função recursiva que recebe uma lista e devolve o maior valor da lista
def max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = max(list[1:])
        return m if m > list[0] else list [0]

lista = [3, 5, 7, 10, 5, 78]
print("Lista: " + str(lista) + "\nMáximo: " + str(max(lista)))
