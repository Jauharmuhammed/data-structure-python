class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
    def add_child(self, val):
        if self.data == val:
            return

        if val < self.data:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = BinarySearchTreeNode(val)

        if val > self.data:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = BinarySearchTreeNode(val)


    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    
    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)


        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()

        elements.append(self.data)

        return elements

    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val < self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

        return False

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [4, 73, 29, 1, 0, 10023, 3, 56, 0, 393]
    root = build_tree(numbers)

    print(root.in_order_traversal())
    print(root.pre_order_traversal())
    print(root.post_order_traversal())

    print(root.search(99))

    print(root.find_min())