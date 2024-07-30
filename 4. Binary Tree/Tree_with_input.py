class Node:
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None
class Main:
    def __init__(self):
        self.root = None
    def build(self, L,i):
        if(i >= len(L) or L[i] == -1):
            return None
        root = Node(L[i])
        root.left = self.build(L, 2*i+1)
        root.right = self.build(L, 2*i+2)
        return root
        
    def preorder(self, root):
        if root == None:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
    
    def postorder(self, root):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)
        
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)
    
m = Main()
L = list(map(int, input().split()))
n = len(L)
i = 0
m.root = m.build(L, i)
print("Pre")
m.preorder(m.root)
print("Pos")
m.postorder(m.root)
print("ino")
m.inorder(m.root)