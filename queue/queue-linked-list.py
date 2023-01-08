class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def display(self):
        if self.front is None: return
        itr = self.front
        liststr = ''
        while itr:
            liststr += str(itr.data)+' <-- ' if itr.next else str(itr.data)
            itr = itr.next
        print('\n',liststr)

    def enqueue(self, value):
        newNode = Node(value)
        if self.rear is None:
             self.front = self.rear = newNode
             return
        
        self.rear.next = newNode
        self.rear = newNode

    def dequeue(self):
        if self.front == None:
            return -1

        self.front = self.front.next

        if self.front is None:
            self.rear = None



queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

queue.display()

queue.dequeue()

queue.display()