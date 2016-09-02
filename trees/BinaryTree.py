__author__ = 'arunsasidharan'


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        if self.root is not None:
            if self.root.value == find_val:
                return True
            else:
                return self.preorder_search(self.root, find_val)

    def preorder_search(self, start, find_val):
        if start is not None:
            if start.value == find_val:
                return True
            elif self.preorder_search(start.left, find_val):
                return True
            elif self.preorder_search(start.right, find_val):
                return True
            else:
                return False

    def print_tree(self):
        return self.preorder_print(tree.root)

    def preorder_print(self, start):
        if start is not None:
            print(start.value)
            self.preorder_print(start.left)
            self.preorder_print(start.right)


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(2)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()