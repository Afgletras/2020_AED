from Fichas.Ficha7.Queue import Queue

class Stack:
    def __init__(self):
        self.q = Queue()

    def isEmpty(self):
        return self.q.isEmpty()

    def push(self, data):
        self.q.enqueue(data)

    def pop(self):
        for _ in range(self.q.size() - 1):
            dequeued = self.q.dequeue()
            self.q.enqueue(dequeued)
        return self.q.dequeue()

# Teste
s = Stack()

s.push(1)
s.push(5)
s.push(9)
print(s)
print(s.isEmpty())
s.pop()
s.pop()
print(s.isEmpty())
s.pop()
print(s.isEmpty())
