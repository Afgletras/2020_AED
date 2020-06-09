from Stack import Stack

# Exercicio 1:
m = Stack()
m.push('x')
m.push('y')
m.pop()
m.push('z')
m.peek
# print(m)
# Resposta: C. 'z'


# Exercicio 2:
# s = Stack()
# s.push('x')
# s.push('y')
# s.push('z')
# while not s.isEmpty():
#     s.pop()
#     s.pop()

# Resposta: C. Ocorrerá um erro


# Exercicio 3:
# Resposta: A implementação alternativa, uma vez que possui o pop(0) e o insert(), possuem ambos complexidade O(n), e
#           portanto a implementação alternativa tem complexidade maior do que a implementação normal, sendo assim a
#           normal mais eficiente.

# Exercicio 4:
# Resposta: Este método serve para apresentar os elementos da pilha de forma mais representativa e vertical.


# Exercicio 5:
def transfer(s, t):
    while not s.isEmpty():
        t.push(s.pop())
    return t

def test_transfer():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack)
    newStack = transfer(stack, Stack())
    print(newStack)


print("Função transfer:")
test_transfer()
print("\n")


# Exercicio 6:
def rev_string(mystr):
    stack = Stack()
    for c in mystr:
        stack.push(c)
    stack.reverse()
    return stack

def test_rev_string():
    string = 'AndreLetras'
    print(string)
    print(''.join(rev_string(string).items))


print("Função rev_string:")
test_rev_string()
print("\n")


# Exercicio 7:
def test_remove():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack)
    stack.remove(3)
    print(stack)


print("Função remove:")
test_remove()
print("\n")


# Exercicio 8:
def findDuplicateParenthesis(string):
    stack = Stack()

    for ch in string:
        if ch == ')':
            top = stack.pop()
            elementsInside = 0
            while top != '(':
                elementsInside += 1
                top = stack.pop()
                print(stack)

            if elementsInside < 1:
                return True

        else:
            stack.push(ch)
            print(stack)

    return False

def test_findDuplicateParenthesis():
    string = "((x+y))+z"

    if findDuplicateParenthesis(string) == True:
        print("Found duplicate parenthesis")
    else:
        print("No duplicate parenthesis found")

print("Função de encontrar parentesis duplicados:")
test_findDuplicateParenthesis()
