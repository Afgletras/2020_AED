# Exemplo de função de colcoar numero ao quadrado:0
def square(n):
    return n**2

# Exemplo de função para raiz quadrada:
def squareroot(n):
    root = n/2

    for k in range(20):
        root = (1/2)*(root + (n / root))

    return root


# Chamar as funções:
print("n ao quadrado: ", square(5))
print("Raíz quadrada de n: ", squareroot(4))

