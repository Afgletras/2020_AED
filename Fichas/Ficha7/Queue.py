class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    # Representação da fila ao realizar um print
    def __str__(self):
        string = '['
        for c in self.items:
            string += (str(c) + ', ')

        string += ']'
        string = string.replace(', ]', ']')
        return string