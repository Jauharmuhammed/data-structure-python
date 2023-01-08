class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None: return
        itr = self.head
        liststr = ''
        while itr:
            liststr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print('\n',liststr)

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def insertAtBeginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data)

    def insertList(self, data_list):
        for data in data_list:
            self.insertAtEnd(data)

    def deleteValue(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next

        print('The value does not match any element')
        
    def insertAfter(self, nodevalue, data):
        if self.head.data == nodevalue:
            self.head.next = Node(data, self.head.next)
            return
        
        itr = self.head
        while itr.next:
            if itr.data == nodevalue:
                itr.next = Node(data, itr.next)
                return
            itr = itr.next

    def insertBefore(self, nodevalue, data):
        if self.head.data == nodevalue:
            self.head = Node(data, self.head)
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == nodevalue:
                itr.next = Node(data, itr.next)
                return
            itr = itr.next

    def removeDuplicates(self):
        itr = self.head
        while itr.next:
            if itr.data == itr.next.data:
                itr.next = itr.next.next
            else:
                itr = itr.next
        


list = LinkedList()
list.insertAtBeginning(7)
list.insertAtBeginning(4)
# list.printList()

list.insertAtEnd(10)
list.insertAtEnd(31)
# list.printList()

list.insertList([101,102,7,103])
# list.printList()

list.deleteValue(7)
# list.printList()

list.insertAfter(7, 7)
# list.printList()

list.insertBefore(101, 100)
# list.printList()

list.insertBefore(4, 1)
list.printList()

list.reverse()
list.printList()

print('length : ', list.length())

sorted_list = LinkedList()
sorted_list.insertList([1,2,2,3,5,8,8,8,9,9])
sorted_list.printList()

sorted_list.removeDuplicates()
sorted_list.printList()

print('length : ', sorted_list.length())


