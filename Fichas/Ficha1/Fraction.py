# Definição da função do gcd (maior divisor comum) (Tambem se pode importar gcd de math)
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


# Definição da classe da fração:
class Fraction:

    # Construtor
    def __init__(self, top, bottom):
        # Verifica se o numerador e denominador são do tipo int. Se não forem, levanta o erro ValueError()
        if not (type(top) is int and type(bottom) is int):
            raise ValueError()
        common = gcd(top, bottom)
        top = top // common
        bottom = bottom // common

        self.num = top
        self.den = bottom

    # Retorna o numerador
    def getNum(self):
        return self.num

    # Retorna o denominador
    def getDen(self):
        return self.den

    # Retorna o valor real da divisão
    def getReal(self):
        return self.num / self.den

    # Função que apresenta o resultado em string
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

# OPERAÇÕES

    # Adição (sem gcd)
    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    # Subtração
    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    # Multiplicação
    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    # Divisão
    def __truediv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        return Fraction(newnum, newden)

# COMPARAÇÕES:

    # Igual
    def __eq__(self, other):
        return self.getReal() == other.getReal()

    # Maior
    def __gt__(self, other):
        return self.getReal() > other.getReal()

    # Maior ou igual
    def __ge__(self, other):
        return self.getReal() >= other.getReal()
    # Menor
    def __lt__(self, other):
        return  self.getReal() < other.getReal()

    # Menor ou igual
    def __le__(self, other):
        return  self.getReal() <= other.getReal()

    # Diferente
    def __ne__(self, other):
        return self.getReal() != other.getReal()

    # Realiza a adição e atribui o valor final à fração
    def __iadd__(self, other):
        fraction = self + other
        return fraction

    # Realiza a adição, no entanto, caso alguma das frações seja do formato int, levanta um erro
    def __radd__(self, other):
        if type(other) is int:
            fraction = Fraction(other, 1)
            return fraction + self
        raise NotImplementedError()

    # Retorna algo que possa ser lido também pela máquina
    def __repr__(self):
        return 'Numerator: ' + str(self.num) + '\nDenominator: ' + str(self.den)


if __name__ == '__main__':

    f1 = Fraction(1, 2)
    f2 = Fraction(1, 4)

    print("f1 = ", f1)
    print("f2 = ", f2)

    # Operações
    print("f1 + f2 = ", f1 + f2)
    print("f1 - f2 = ", f1 - f2)
    print("f1 * f2 = ", f1 * f2)
    print("f1 / f2 = ", f1 / f2)

    # Comparações
    print("f1 = f2? ", f1 == f2)
    print("f1 > f2? ", f1 > f2)
    print("f1 >= f2? ", f1 >= f2)
    print("f1 < f2? ", f1 < f2)
    print("f1 <= f2? ", f1 <= f2)
    print("f1 != f2? ", f1 != f2)

    print("f1 numerator", f1.getNum())
    print("f1 denominator", f1.getDen())
    print("f1 Num Real", f1.getReal())

    f3 = Fraction(3,6)
    print("f3 = ", f3)

    print("f2 - f1 =", f2 - f1)

    print("f1 * f2 =", f1 * f2)
    print("f1 / f2 =", f1 / f2)

