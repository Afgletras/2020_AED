from Fichas.Ficha7.Stack import Stack

class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def isEmpty(self):
        return self.s1.isEmpty() and self.s2.isEmpty()

    def enqueue(self, item):
        self.s1.push(item)

    def dequeue(self):
        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                popped = self.s1.pop()
                self.s2.push(popped)
        return self.s2.pop()

if __name__ == '__main__':
    q = Queue()
    print(q.enqueue(1))
    print(q.enqueue(2))
    print(q.enqueue(3))
    print(q.isEmpty())

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.isEmpty())
