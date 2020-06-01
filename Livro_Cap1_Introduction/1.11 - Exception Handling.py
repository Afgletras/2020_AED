# Existem dois tipos de erros ao escrever programas:

# Existe o erro de SYNTAX, em que houve um erro por parte do utilizador,
# ao não colocar um símbolo ou outro tipo de sinal.

# E existe o erro de EXCEPTION, que é contornável por parte do utilizador, colocando um try:


# Exemplo de código com erro (math):

# anumber = int(input("Please enter an integer: "))
# print(math.sqrt(anumber))

# Código correto:

import math
anumber = int(input("Please enter an integer: "))
try:
    print(math.sqrt(anumber))
except:
    print("Bad value for square root")
    print("Using absolute value instead")
    print(math.sqrt(abs(anumber)))

# É ainda possivel definirmos nós o Runtime Error:

if anumber < 0:
    raise RuntimeError ("You can't use a negative number")
else:
    print(math.sqrt(anumber))
