from Fichas.Ficha7.Queue import Queue


def generateBinaryQueue(n):

    q = Queue()
    q.enqueue("1")

    while n > 0:
        n -= 1

        s1 = q.dequeue()
        print(s1)

        s2 = s1

        q.enqueue(s1 + "0")
        q.enqueue(s2 + "1")


generateBinaryQueue(16)
