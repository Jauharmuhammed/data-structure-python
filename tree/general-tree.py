class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 4 
        prefix = spaces + '|__' if self.parent else ''
        print(prefix, self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    

def build_product_tree():
    root = TreeNode('Electronics')

    laptop  = TreeNode('Laptop')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('HP'))
    laptop.add_child(TreeNode('Lenovo'))
    laptop.add_child(TreeNode('MSI'))

    mobile  = TreeNode('Mobile')
    mobile.add_child(TreeNode('iPhone'))
    mobile.add_child(TreeNode('Pixel'))
    mobile.add_child(TreeNode('Samsung'))
    mobile.add_child(TreeNode('OnePlus'))
    mobile.add_child(TreeNode('Nothing'))

    headphone = TreeNode('Headphone')
    headphone.add_child(TreeNode('Sony'))
    headphone.add_child(TreeNode('Sennheiser'))
    headphone.add_child(TreeNode('Airpods'))
    headphone.add_child(TreeNode('Beats'))

    root.add_child(laptop)
    root.add_child(headphone)
    root.add_child(mobile)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
