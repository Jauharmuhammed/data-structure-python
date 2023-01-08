class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def display(self):
        if self.top is None: return
        itr = self.top
        liststr = ''
        while itr:
            liststr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print('\n',liststr)

    
    def push(self, value):
        if self.top == None:
            self.top = Node(value)
            return

        self.top = Node(value, self.top)

    def pop(self):
        if self.top == None:
            return -1
        
        self.top = self.top.next

stack = Stack()
stack.push(1)
stack.push(78)
stack.push(778)
stack.push(23)

stack.display()

stack.pop()
stack.display()



