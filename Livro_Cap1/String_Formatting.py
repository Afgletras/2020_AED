# A formatted string is a template in wich words or spaces that will remain constant are combined with
# placeholders for variables that will be inserteed into the string.

aName = "André"
age = 24

# Um exemplo de output usual neste caso é:
print("STRING SIMPLES:")
print(aName, "is", age, "years old.")

# No entanto pode-se usar as formatted strings desta forma:
print("STRING FORMATADA:")
print("%s is %d years old." % (aName, age))

# O operador % é o operador de formatação. O lado esquerdo tem o local de formatação, e o lado direito tem
# os valores que vão ser alterados e formatados. Têm sempre que possuir o mesmo numero e a mesma ordem.

# Existem, no entanto, especificações para cada tipo de dados:
# %d, %i - Inteiros
# %u - Inteiros não associados
# %f - Float
# %c - Single char
# %s - String ou qualquer objeto que possa ser modificado pela função str do Python

# Exemplos

price = 24
item = "banana"

print("\nThe %s costs %d cents:")
print("The %s costs %d cents." % (item, price))

print("\nThe %+10s costs %5.2f cents:")
print("The %+10s costs %5.2f cents" % (item, price))

itemDict = {"item":"banana", "cost": 24}
print("\nThe %(item)s costs %(cost)7.1f cents:")
print("The %(item)s costs %(cost)7.1f cents" % itemDict)

