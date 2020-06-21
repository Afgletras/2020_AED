from AED.Node import Node


class Stack:

    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

a_stack = Stack()


s = Stack()


s.push(13)
s.push(14)
s.push(12)

print(s.pop())
print(s.pop())
print(s.pop())


#print(s.peek())