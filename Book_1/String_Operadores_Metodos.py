#Strings are sequential collections of zero or more letters, numbers and other symbols.

string_ex = "david"
print("STRING: ", string_ex)

# index
print("Index[3] - ", string_ex[3])

# multiplicação
print("String x 2 - ", string_ex*2)

# length
print("Comprimento - ", len(string_ex))

#------------------------METODOS-----------------------------------

# capitalize - Coloca a primeira letra de uma string em maiuscula
print("Capitalize - ", string_ex.capitalize())

# upper - Coloca toda a string em letras maiusculas
print("Upper - ", string_ex.upper())

# center - Retorna uma string num espaço x
print("Center(20) - ", string_ex.center(20))

# count - Retorna o numero de ocorrecias na string
print("Count(d) - ", string_ex.count("d"))

# split - Separa a string na primeira ocorrencia indicada e coloca as duas numa lista
print("Split(v) - ", string_ex.split("v"))

