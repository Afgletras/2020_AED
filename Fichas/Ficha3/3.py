# Função recursiva que recebe um numero inteiro e é escrito na base binária:

#Regra geral para qualauer base:
def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]

print("1457: " + toStr(1457, 2))
print("128: " + toStr(128, 2))