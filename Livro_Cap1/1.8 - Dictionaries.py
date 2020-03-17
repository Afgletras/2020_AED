# É uma coleção de pares de itens, em que a cada item corresponde uma chave

capitals = {'Iowa': 'DesMoines', 'Winsconsin':'Madison'}
print(capitals)

# Para adicionar mais items ao dicionário existe várias formas, a mais simples é:
capitals['Utah'] = 'SaltLakeCity'
print(capitals)
capitals['California'] = 'Sacramento'
print(capitals)
print("\n")

# Apresentar os resultados do dicionário com informação:
print("CAPITALS:")
for k in capitals:
    print(capitals[k], " is the capital of ", k)

print("\n")


# Operadores:

# [] - Retorna o valor da chave do item colocado:
print("[] - ", "Qual a capital do Utah? ", capitals["Utah"])

# in - Retorna True ou False no caso de conter o item indicado
print("in - ", "Iowa" in capitals)

# del - Elimina o item especificado
del capitals["Utah"]
print("del(UTAH) - ", capitals)

#-------------------------------------------- Métodos --------------------------------------------------

postalCode = {'Seixal':2840, 'FF':2865, "Lisboa":1500}

# keys - Retorna os itens que estão indicados no dicionario
print("Keys - ", postalCode.keys())

# values - Retorna os valores apenas das keys
print("Values - ", postalCode.values())

# items - Retorna os pares de valores do dicionário
print("Items - ", postalCode.items())

# get - Retorna o valor associado a determinado item
print("Get('Seixal') - ", postalCode.get("Seixal"))
print("Get ('Amora') - ", postalCode.get("Amora", "Não Existente"))
