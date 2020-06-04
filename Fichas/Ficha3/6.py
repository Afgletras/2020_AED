def factorial(n):
    if n is 0:
        return 1

    return n * factorial(n-1)

#def entry_pascalTriangle(i, j):


#def print_line_pascalTriangle(i):

# Funções que escrevem no ecrã o triangulo de Pascal
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
    n = int(input("Introduza o valor de n (número de linhas): "))
    print_pascal_triangle(n)


main()