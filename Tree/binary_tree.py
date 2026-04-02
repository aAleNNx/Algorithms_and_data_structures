class Node:
    def __init__(self, key, data, right = None, left= None):
        self.key = key
        self.data = data
        self.right = right
        self.left = left

class BST:
    def __init__(self):
        self.root = None

    def search(self, key):
        return self.__search(key, self.root)

    def __search(self, key, node):
        if node is None:
            return None
        if key == node.key:
            return node.data
        elif key < node.key:
            return self.__search(key, node.left)
        else:
            return self.__search(key, node.right)

    def insert(self, key, data):
        self.root = self.__insert(key, data, self.root)

    def __insert(self, key, data, node):
        if node is None:
            return Node(key, data)
        if key < node.key:
            node.left = self.__insert(key, data, node.left)
        elif key > node.key:
            node.right = self.__insert(key, data, node.right)
        else:
            node.data = data
        return node

    def delete(self, key):
        self.root = self.__delete(key, self.root)

    def __delete(self, key, node):
        if node is None:
            return None
        
        if key < node.key:
            node.left = self.__delete(key, node.left)
        elif key > node.key:
            node.right = self.__delete(key, node.right)
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            next = node.right
            while next.left:
                next = next.left

            node.key = next.key
            node.data = next.data

            node.right = self.__delete(next.key, node.right)

        return node

    def print_as_list(self):
        result = []
        self.__ordering(result, self.root)
        print(result)

    def __ordering(self, result, node):
        if node:
            self.__ordering(result, node.left)
            result.append((node.key, node.data))
            self.__ordering(result, node.right)

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node is not None:
            self.__print_tree(node.right, lvl + 5)

            print()
            print(lvl * " ", node.key, node.data)

            self.__print_tree(node.left, lvl + 5)

    def height(self):
        return self.__height(self.root)

    def __height(self, node):
        if node is None:
            return 0

        return 1 + max(self.__height(node.left),
                       self.__height(node.right))
    

tree = BST()

data = {
    50:'A', 15:'B', 62:'C', 5:'D', 20:'E',
    58:'F', 91:'G', 3:'H', 8:'I', 37:'J',
    60:'K', 24:'L'
}

for k, v in data.items():
    tree.insert(k, v)

tree.print_tree()

tree.print_as_list()

print("\nSearch 24:", tree.search(24))

tree.insert(20, "AA")

tree.insert(6, "M")
tree.delete(62)
tree.insert(59, "N")
tree.insert(100, "P")
tree.delete(8)
tree.delete(15)
tree.insert(55, "R")
tree.delete(50)
tree.delete(5)
tree.delete(24)

print("\nHeight:", tree.height())

tree.print_as_list()

tree.print_tree()