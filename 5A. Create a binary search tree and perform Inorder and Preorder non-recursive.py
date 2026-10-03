class Stack:
    def __init__(self):
        self.TOP = -1
        self.st = [0] * 100

    def push(self, x):
        if self.TOP == 99:
            print("Stack Overflow")
            return

        self.TOP = self.TOP + 1
        self.st[self.TOP] = x

    def pop(self):
        if self.TOP == -1:
            print("Stack Underflow")
            return

        x = self.st[self.TOP]
        self.TOP = self.TOP - 1
        return x


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, x):
    if root is None:
        return Node(x)

    if x < root.data:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)

    return root


root = None

n = int(input("Enter number of nodes: "))

for i in range(n):
    x = int(input("Enter data: "))
    root = insert(root, x)


def preorder(root):
    if root is None:
        return

    s1 = Stack()
    s1.push(root)

    while s1.TOP != -1:
        root = s1.pop()
        print(root.data, end=" ")

        if root.right is not None:
            s1.push(root.right)

        if root.left is not None:
            s1.push(root.left)


def inorder(root):
    s2 = Stack()

    while root is not None or s2.TOP != -1:

        while root is not None:
            s2.push(root)
            root = root.left

        root = s2.pop()
        print(root.data, end=" ")

        root = root.right


print("\nPreorder Traversal:")
preorder(root)

print("\nInorder Traversal:")
inorder(root)