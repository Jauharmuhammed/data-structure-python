class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    #traversing
    def printlist(self):  
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next

    # inserting at the beginning
    def insertBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    # inserting at the end
    def insertEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    # inserting an element inbetween
    def insertInBetween(self, node, data):
        if node is None:
            print('Invalid Position')
            return
        newNode = Node(data)
        newNode.next = node.next
        node.next = newNode

    # removin a node
    def remove(self, remove_item):
        val = self.head
        if val is not None and val == remove_item:
            self.head = val.next
            val = None
            return
        while val is not None:
            if val.data == remove_item:
                break
            prev = val
            val = val.next
        
        if val:
            prev.next = val.next
            val = None
            return

        

# initialization
list = SinglyLinkedList()
list.head = Node(10)
e2 = Node(20)
e3 = Node(30)

list.head.next = e2
e2.next = e3


# insert at the beginning
list.insertBeginning(5)
list.insertBeginning(1)

# insert at the end
list.insertEnd(100)
list.insertEnd(200)

# insert in between
list.insertInBetween(e2, 25)

# removing an item
list.remove(20)

# tarversing and printing each element of the linked list
list.printlist()