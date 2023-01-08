# from collections import deque


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printlist(self):
        val = self.head
        while val is not None:
            print(val.data)
            val = val.next

    def insertBeginning(self, data):
        newNode = Node(data)
        self.head.prev = newNode
        newNode.next= self.head
        self.head = newNode

    # def insertEndWithoutTail(self, data):
    #     newNode = Node(data)
    #     if self.head is None:
    #         self.head = newNode
    #         return
    #     temp = self.head
    #     while temp.next:
    #         temp = temp.next
    #     temp.next = newNode

    def insertEnd(self, data):
        newNode = Node(data)
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

    def insertInbetween(self, node, data):
        if node is None:
            print('invalid position')
            return
        newNode = Node(data)
        newNode.next = node.next
        newNode.prev = node
        node.next = newNode

    def remove(self, remove_data):
        if self.head is not None and self.head.data == remove_data:
            newHead = self.head.next
            self.head.next = None
            self.head = newHead
            self.head.prev = None
            return
        if self.tail is None and self.tail.data == remove_data:
            newTail = self.tail.prev
            self.tail.prev = None
            newTail.next = None
            self.tail = newTail
            return
        temp = self.head
        while temp is not None:
            if temp.data == remove_data:
                break
            temp = temp.next
        if temp:
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            return





        

        
list = DoublyLinkedList()
list.head = Node(10)

e2 = Node(20)
e3 = Node(30)

list.head.next = e2
e2.prev = list.head
e2.next = e3
e3.prev = e2
 
list.tail = e3

list.insertBeginning(5)

list.insertEnd(80)
list.insertEnd(50)

list.insertInbetween(e2, 22)
list.insertInbetween(e2, 21)

list.remove(10)
list.remove(20)

list.printlist()




    

