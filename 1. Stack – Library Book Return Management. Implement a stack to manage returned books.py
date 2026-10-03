stack = []

while True:
    print("\n--- Library Book Return Management ---")
    print("1. Return Book (Push)")
    print("2. Arrange Book (Pop)")
    print("3. Top Book (Peek)")
    print("4. Display Books")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        stack.append(book)
        print(book, "returned successfully.")

    elif choice == 2:
        if len(stack) == 0:
            print("No books to arrange.")
        else:
            book = stack.pop()
            print(book, "arranged on the shelf.")

    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Top Book:", stack[-1])

    elif choice == 4:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Books in Stack (Top to Bottom):")
            for i in range(len(stack) - 1, -1, -1):
                print(stack[i])

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid choice.")