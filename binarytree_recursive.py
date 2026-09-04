class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def create():
    x=int(input("Enter data to create node (0 to stop): "))
    if x==0:
        return None
    root=Node(x)
    print("Enter left child of", x)
    root.left=create()
    print("Enter right child of", x)
    root.right=create()
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
        
root = create() #starts creation of tree
print("Preorder traversal:")
preorder(root)
print("\nInorder traversal:")
inorder(root)
print("\nPostorder traversal:")
postorder(root)
