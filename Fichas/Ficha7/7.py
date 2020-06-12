from Fichas.Ficha7.Queue import Queue
from Fichas.Ficha7.Stack import Stack


# Exercicio 7:
def merge(a, b):
    sa = Stack()
    sb = Stack()

    # Inserir os items de cada queue em stacks
    for i in a.items:
        sa.push(i)

    for j in b.items:
        sb.push(j)

    # Comparar os 2 stacks
    sc = Stack()
    while not sa.isEmpty() and not sb.isEmpty():
        if sa.peek() < sb.peek():
            tmp = sa.pop()
            sc.push(tmp)
            tmp = sb.pop()
            sc.push(tmp)
        elif sb.peek() < sa.peek():
            tmp = sb.pop()
            sc.push(tmp)
            tmp = sa.pop()
            sc.push(tmp)

    # Inverter o stack
    sd = Stack()
    while not sc.isEmpty():
        tmp = sc.pop()
        sd.push(tmp)

    # Inserir o stack temporario na queue final
    c = Queue()
    for y in sd.items:
        c.enqueue(y)

    return c


# Teste
a = Queue()
b = Queue()

items1 = [5, 10, 30, 45, 2]
for item_a in items1:
    a.enqueue(item_a)

items2 = [6, 11, 31, 42, 50]
for item_b in items2:
    b.enqueue(item_b)

print("a:", a.items)
print("b:", b.items)
print("c:", merge(a, b))
