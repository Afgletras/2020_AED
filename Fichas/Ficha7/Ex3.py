class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)  # O(1)

    def dequeue(self):
        return self.items.pop(len(self.items) - 1)  # O(n)

    # Resposta: Em termos de complexidade é igual à implementação normal, uma vez que o insert tem complexidade O(n),
    # no entanto o pop(i) tem complexidade O(n) também, logo acaba por ser igual.


    def size(self):
        return len(self.items)

    # Representação da fila ao realizar um print
    def __str__(self):
        string = ""
        for item in self.items:
            string = string + str(item) + " "
        return string