# Binary Search Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Main:
    def __init__(self):
        self.root = None
        
    def build(self, root, key):
        if root is None:
            return Node(key)
        elif key < root.data:
            root.left = self.build(root.left, key)
        elif key > root.data:
            root.right = self.build(root.right, key)
        return root
    
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)


obj = Main()
keys = list(map(int, input().split())) 
for key in keys:
    obj.root = obj.build(obj.root, key)
    
print("Inorder traversal:")
obj.inorder(obj.root)
