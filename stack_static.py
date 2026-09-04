class Stack:
    def __init__(self):
        self.TOP = -1  #only top is defined coz the stack is empty
        self.st = [0] * 100

    def push(self, x):   #x is the element we want to insert
        if self.TOP == 99:
            print("Stack Overflow")
            return  #Exit the function because the stack is already full

        self.TOP = self.TOP + 1   #top becomes 0  (from -1 to 0)
        self.st[self.TOP] = x #top is 0th index and for next element its TOP=TOP+1 ie 1st index

    def pop(self):
        if self.TOP == -1:
            print("Stack Underflow")
            return

        self.st[self.TOP] = x  # First save the element #dont change positons its dif for push and pop
        self.TOP = self.TOP - 1   # Then remove it logically
        return x  # Give the deleted element back

    def peek(self):  #Only looks at TOP
        if self.TOP == -1:
            print("Stack is Empty")
        else:
            print("Top element:", self.st[self.TOP])

    def display(self):
        if self.TOP == -1:
            print("Stack is Empty")
        else:
            print("Stack elements:")
            for i in range(self.TOP, -1, -1):  #range(start, stop, step) The stop value is never included.
                print(self.st[i]) #range means looping through, we do this so that numbers to be displaced can be arranged in stack 

s = Stack() #stack object

while True: #while creates loop until user chooses exit
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        x = int(input("Enter element: "))  #this is written before s.push(x) coz we have to insert value 1st
        s.push(x)

    elif choice == 2:
        x = s.pop()
        if x is not None:
            print("Deleted element:", x)

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        break

    else:
        print("Invalid choice")