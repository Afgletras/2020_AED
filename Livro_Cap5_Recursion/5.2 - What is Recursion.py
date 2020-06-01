# A recursão é um método de resolver problemas que envolva partir o problema em pequenas
# partes do mesmo problema até chegar à versão trivial do mesmo.

# Três leis da recursão:
# 1 - Tem de ter uma condição de paragem;
# 2 - Tem de se mover ao longo do caso básico;
# 3 - Tem que se chamar a si próprio recursivamente.

# Exemplo:
# Escrever uma expressão recursiva para representar o resultado de fatoriais (!).
def factorial_recursive(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

print(factorial_recursive(4))


# Solução iterativa:
def factorial_iterative(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

print(factorial_iterative(4))