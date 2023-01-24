class Node:
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
                self.left = Node(val)

        if val > self.data:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = Node(val)

    
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


def height( node):
    if not node:
        return 0

    leftHeight = height(node.left)
    rightHeight = height(node.right)

    return max(leftHeight, rightHeight) + 1

        
def build_tree( arr):
    root = Node(arr[0])
    for i in range(1, len(arr)):
        root.add_child(arr[i])
    return root

if __name__ == '__main__':
    a = [2,45,2,65,1,5,7,8,4,5,5,334,33,4343,2,33,232]
    tree = build_tree(a)
    print(tree.in_order_traversal())
    print(height(tree))