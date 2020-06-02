# Podemos criar uma função recursiva que transforme um número em string
# e que consiga transformar esse mesmo número em qualquer base:

# Para isso tem de se reduzir um número em digitos singulares,
# Depois converter esses numeros isolados para uma string,
# E concatenar essas strings de números para formar o resultado final.

# Em relação as bases, a função vai verificar se o numero é mais pequeno que a base.
# Caso não seja, faz a divisão do n pela base e retorna de novo a função (recursividade),
# Colocando o valor do resto da divisão em memória, para no fim atribuir os valores das strings.
# Quando o n for < base, ele atribui todos os restos das divisões à listra de strings para dar o numero final.

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]

print(toStr(1457, 16))