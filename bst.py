## Grant Gasser and Udacity
## 8/1/2019
## Binary Search Tree

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        elif current.value > new_val:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def print_tree(self):
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current.value == find_val:
            return True

        else:
            if current.value < find_val:
                if current.right:
                    self.search_helper(current.right, find_val)
                else:
                    return False
            elif current_value > find_val:
                if current.left:
                    self.search_helper(current.left, find_val)
                else:
                    return False

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print(tree.print_tree())

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
