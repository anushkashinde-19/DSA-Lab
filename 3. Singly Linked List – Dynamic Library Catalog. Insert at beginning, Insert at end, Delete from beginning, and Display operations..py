class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def insert_beginning(self, book):
        new_node = Node(book)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, book):
        new_node = Node(book)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def delete_beginning(self):
        if self.head is None:
            print("Library Catalog is empty")
            return

        book = self.head.data
        self.head = self.head.next
        print("Deleted Book:", book)

    def display(self):
        if self.head is None:
            print("Library Catalog is empty")
            return

        temp = self.head

        print("Library Catalog:")

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


catalog = LL()

while True:
    print("\n1. Insert Book at Beginning")
    print("2. Insert Book at End")
    print("3. Delete Book from Beginning")
    print("4. Display Catalog")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        book = input("Enter book name: ")
        catalog.insert_beginning(book)

    elif ch == 2:
        book = input("Enter book name: ")
        catalog.insert_end(book)

    elif ch == 3:
        catalog.delete_beginning()

    elif ch == 4:
        catalog.display()

    elif ch == 5:
        break

    else:
        print("Invalid choice")