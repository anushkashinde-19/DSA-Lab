class Queue:
    def __init__(self):
        self.FRONT = -1
        self.REAR = -1
        self.q = [0] * 100

    def enqueue(self, x):
        if self.REAR == 99:
            print("Queue Overflow")
            return

        if self.FRONT == -1:
            self.FRONT = 0

        self.REAR = self.REAR + 1
        self.q[self.REAR] = x

    def dequeue(self):
        if self.FRONT == -1 or self.FRONT > self.REAR:
            print("Queue Underflow")
            return

        x = self.q[self.FRONT]
        self.FRONT = self.FRONT + 1

        if self.FRONT > self.REAR:
            self.FRONT = -1
            self.REAR = -1

        return x

    def display(self):
        if self.FRONT == -1:
            print("Queue is Empty")
        else:
            print("Queue elements:")
            for i in range(self.FRONT, self.REAR + 1):
                print(self.q[i], end=" ")
            print()


q = Queue()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        x = int(input("Enter element: "))
        q.enqueue(x)

    elif choice == 2:
        x = q.dequeue()
        if x is not None:
            print("Deleted element:", x)

    elif choice == 3:
        q.display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")