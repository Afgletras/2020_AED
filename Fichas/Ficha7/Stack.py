class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def reverse(self):
        t = Stack()
        while not self.isEmpty():
            t.push(self.pop())

        self.items = t.items

    def remove(self, item):
        stack = Stack()
        while not self.isEmpty():
            i = self.pop()
            if item != i:
                stack.push(i)
        self.items = stack.items
        self.reverse()

    def __str__(self):
        string = '['
        for c in self.items:
            string += (str(c) + ', ')

        string += ']'
        string = string.replace(', ]', ']')
        return string
