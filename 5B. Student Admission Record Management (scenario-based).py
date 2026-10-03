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

n = int(input("Enter number of students: "))

for i in range(n):
    admission_no = int(input("Enter admission number: "))
    root = insert(root, admission_no)


def preorder(root):
    if root is None:
        return

    s = Stack()
    s.push(root)

    while s.TOP != -1:
        root = s.pop()
        print(root.data, end=" ")

        if root.right is not None:
            s.push(root.right)

        if root.left is not None:
            s.push(root.left)


def inorder(root):
    s = Stack()

    while root is not None or s.TOP != -1:

        while root is not None:
            s.push(root)
            root = root.left

        root = s.pop()
        print(root.data, end=" ")

        root = root.right


print("\nPreorder Traversal:")
preorder(root)

print("\nInorder Traversal:")
inorder(root)