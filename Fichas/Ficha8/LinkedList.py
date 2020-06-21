from Fichas.Ficha8.Node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.lenght=0

    def isEmpty(self):
        self.head = None

    def add(self, item):
        temp = Node(item)

        temp.setNext(self.head)
        self.head = temp

    def traversal(self):
        current = self.head
        while current != None:
            current = current.getNext()

    # def size(self):
    #     current=self.head
    #     count=0
    #     while current!=None:
    #         count+=1
    #         current=current.getNext()
    #     return count

    # ficha 8, exer 1:
    def size(self):
        return self.lenght

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def __str__(self):  # return string representation of a linked list
        current = self.head
        s = ""
        while current != None:
            s = s + str(current.getData())
            current = current.getNext()
            if current:
                s = s + " -> "
        return s

# lista=LinkedList()
# print(lista)
#
# lista.add(17)
# print(lista)
#
# lista.add(93)
# print(lista)
#
# lista.add(26)
# print(lista)
#
# print(lista.search(93))
# lista.remove(93)
# print(lista)
