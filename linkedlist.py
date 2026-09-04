class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def create(self):
        n = int(input("Enter no. of nodes:"))
        if n <= 0:
            print("Enter valid no. of nodes.")
            return

        for i in range(1, n + 1):
            value = input(f"Enter value for node {i}:")
            self.insert(value)

    def insert(self, val):
        new_node = Node(val)

        if self.isEmpty():
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def display(self):
        if self.isEmpty():
            print("Linked List is empty...")
            return

        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

        print("None")

    def delete(self, val):
        if self.isEmpty():
            print("Nothing to delete...")
            return

        if self.head.data == val:
            self.head = self.head.next
            print(f"Node {val} is deleted...")
            return

        prev = self.head
        temp = self.head.next

        while temp is not None:
            if temp.data == val:
                prev.next = temp.next
                print(f"Node {val} is deleted...")
                return

            prev = temp
            temp = temp.next

        print(f"Node {val} not found...")


n = LL()

while True:
    ch = int(input("1 for create\n2 for insert\n3 for display\n4 for delete\nenter choice: "))

    if ch == 1:
        n.create()
    elif ch == 2:
        val = input("Enter value to insert:")
        n.insert(val)
    elif ch == 3:
        n.display()
    elif ch == 4:
        val = input("Enter value to delete:")
        n.delete(val)
    else:
        print("Invalid choice, try again.")