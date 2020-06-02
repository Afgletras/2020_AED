# Função recursvia: Recebe uma lista e devolve outra lista que possui os mesmos elementos da primeira
# só que por ordem inversa

def invert(list):
    if len(list) == 0: #Caso base
        return []
    if len(list) == 1:
        return list[::]
    else:
        return list[-1:] + invert(list[:-1]) #Passo recursivo


lista = [1, 2, 3, 4, 5]
print("lista inicial: ", lista)
print("lista invertida: ", invert(lista))