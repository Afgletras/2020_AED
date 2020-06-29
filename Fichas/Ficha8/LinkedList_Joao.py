from Fichas.Ficha8.Node import Node


class LinkedList:

    def __init__(self):
        self.head = None
        self.lenght=0

    def isEmpty(self):
        return self.head == None

    #def __str__(self):
    #   return str(self.head) + "->"

    def __repr__(self):
        return f"{self.head}" + "->"

    def add(self, item):
        temp = Node(item)

        temp.setNext(self.head)
        self.head = temp

    #def size(self):
    #
    #   current = self.head
    #   count = 0
    #   while current != None:
    #       count = count + 1
    #       current = current.getNext()
    #   return count


    #Exercício 1
    def size(self):
        return self.lenght

    def traversal(self):
        current = self.head
        while current != None:
            current = current.getNext()


    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found


    def remove(self,item):
        current = self.head
        previous = None
        found = False
        for current in item:
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



    def index(self,item):
        current = self.head
        while current != None:
            if current.data == item:
                return current.position
            else:
                current = current.next

        print ("item not present in list")

    def append(self,item):
        current = self.head
        if current:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(Node(item))
        else:
            self.head = Node(item)


    def insert(self,item,position):
        if position == 0:
            self.add(item)
        elif position > self.size():
            print("position index out of range")
        elif position == self.size():
            self.AppendNode(item)
        else:
            temp = Node(item, position)
            current = self.head
            previous = None
            while current.position != position:
                previous = current
                current = current.next
            previous.next = temp
            temp.next = current
            temp.back = previous
            current.back = temp
            current = self.head
            self.index_correct(current)

    def pop(self):
        prev = None
        node = self.head
        while node != None:
            prev = node
            node = node.get_next()
        if prev == None:
            self.head = node.get_next()
        else:
            prev.next = node.get_next()


    def pop(self, pos=None):
        if pos is None:
            pos = self.size()
        elif pos < 0 or pos >= self.size():
            raise ValueError("Position doesn't exist")

        current_pos = 0
        prev = None
        current = self.head
        while current.next and current_pos < pos:
            prev = current
            current = current.next
            current_pos += 1
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next
        return current.data

    def __str__(self):  # return string representation of a linked list
        current = self.head
        s = ""
        while current != None:
            s = s + str(current.getData())
            current = current.getNext()
            if current:
                s = s + " -> "
        return s

# Metodo para fazer a clonagem
# Usando o append()
def Clone(list1):
    list_copy =[]
    for item in list1: list_copy.append(item)
    return list_copy

#
# list1 = [4, 8, 2, 10, 15, 18]
# list2 = Clone(list1)
# print("Original List:", list1)
# print("Cloning:", list2)



def concatenate (a, b):
    a = lista1
    b = lista2
    for i in lista2:
        lista1.append(i)
    print ("Concatenated list using naive method : " + str(lista1))

#Dando 2 listas inicias
lista1 = [1, 4, 5, 6, 5]
lista2 = [3, 5, 7, 2, 5]

concatenate(lista1, lista2)

list = LinkedList()
print(list.add(12))
list.add(23)
list.add(24)
list.add(25)

print(list)

#print(list.pop())
#print(list.pop(1))
#print(list.pop())


