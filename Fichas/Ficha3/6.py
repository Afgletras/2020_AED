def factorial(n):
    if n is 0:
        return 1

    return n * factorial(n-1)

# Função que devolve o valor da formula de a(i,j)
def entry_pascalTriangle(row, column):
    if (column == 0) or (row == column):
        return 1
    else:
        print(int(factorial(row) / (factorial(column) * factorial(row - column))))

# Função que devolve apenas uma linha
def print_line_pascalTriangle(i):
    if i < 0:
        return
    else:
        line = []
        for j in range(i + 1):
            line.append(int(factorial(i) / (factorial(j) * factorial(i - j))))
    print(line)

# Função que escreve no ecrã o triangulo de Pascal
def print_pascal_triangle(n):
    if n < 0:
        return
    else:
        line = []
        for i in range(n + 1):
            line.append(int(factorial(n) / (factorial(i) * factorial(n - i))))
    print_pascal_triangle(n - 1)
    print(line)

def main():
    n = int(input("Introduza o valor de n: "))
    i = int(input("Introduza o número da linha: "))
    j = int(input("Introduza o número da coluna: "))

    print("Triângulo com ", n, " linhas:")
    print_pascal_triangle(n)

    print("Linha numero", n, "do triângulo:")
    print_line_pascalTriangle(n)

    print("Valor de a(", i, ",", j, "):")
    entry_pascalTriangle(i, j)

main()