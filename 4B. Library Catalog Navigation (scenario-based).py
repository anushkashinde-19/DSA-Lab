class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    x = input("Enter book name (0 to stop): ")

    if x == "0":
        return None

    root = Node(x)

    print("Enter left child of", x)
    root.left = create()

    print("Enter right child of", x)
    root.right = create()

    return root


def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


root = create()

print("\nPreorder - Library Catalog:")
preorder(root)

print("\nInorder - Library Catalog:")
inorder(root)

print("\nPostorder - Library Catalog:")
postorder(root)