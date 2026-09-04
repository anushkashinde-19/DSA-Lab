class Stack:
    def __init__(self):
        self.TOP = -1
        self.st = [0] * 100

    def push(self,x): #here stack stores nodes, not data.
        if self.TOP == 99:
            print("Stack Overflow")
            return

        self.TOP += 1
        self.st[self.TOP]=x

    def pop(self):
        if self.TOP == -1:
            print("Stack Underflow")
            return

        x = self.st[self.TOP]
        self.TOP -= 1
        return x

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def create():
    x=int(input("Enter data to create node(0 to stop):"))
    if x == 0:
        return None
    root = Node(x)

    print(f"Enter left of {x} :")
    root.left=create()
    print(f"Enter right of {x} :")
    root.right= create()
    return root

                                                                                                                                                                                                                                                 
root=create()

def preorder(root):
    s1= Stack()      # object of stack
    while root is not None:
        print(root.data)
        s1.push(root)
        root=root.left
    while s1.TOP != -1:  #not empty
        root = s1.pop()
        root = root.right
        while root is not None:
            print(root.data)
            s1.push(root)
            root= root.left

print("\nPreorder Traversal:")
preorder(root)

def inorder(root):
    s2= Stack()      # object of stack
    while root != None:
        s2.push(root)
        root=root.left
    while s2.TOP != -1:
        root=s2.pop()
        print(root.data)
        root=root.right
        while root != None:
            s2.push(root)
            root=root.left

print("\nInorder Traversal:")
inorder(root)