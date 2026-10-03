class Queue:
    def __init__(self):
        self.FRONT = -1
        self.REAR = -1
        self.q = []

    def enqueue(self, customer):
        self.q.append(customer)
        self.REAR = self.REAR + 1

        if self.FRONT == -1:
            self.FRONT = 0

    def dequeue(self):
        if self.FRONT == -1:
            print("Queue Underflow")
            return

        customer = self.q[self.FRONT]
        self.FRONT = self.FRONT + 1

        if self.FRONT > self.REAR:
            self.FRONT = -1
            self.REAR = -1
            self.q.clear()

        return customer

    def display(self):
        if self.FRONT == -1:
            print("Queue is Empty")
        else:
            for i in range(self.FRONT, self.REAR + 1):
                print(self.q[i], end=" ")
            print()


q = Queue()

while True:
    print("\n1. Book Ticket (Enqueue)")
    print("2. Serve Customer (Dequeue)")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        customer = input("Enter customer name: ")
        q.enqueue(customer)
        print(customer, "added to the queue.")

    elif choice == 2:
        customer = q.dequeue()
        if customer is not None:
            print("Ticket booked for:", customer)

    elif choice == 3:
        q.display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")