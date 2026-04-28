# Library Management System

# Lists to store books
books = []
issued_books = []

# Function to add books

def add_books():

    total = int(input("How many books do you want to add? "))

    for i in range(total):

        name = input(f"Enter book {i+1} name: ")

        if name in books:
            print("Book already exists")

        else:
            books.append(name)
            print(f"{name} added successfully")

# Function to show books

def show_books():
    if len(books) == 0:
        print("No books available")
    else:
        print("\nAvailable Books:")
        for index, book in enumerate(books, start=1):
            print(f"{index}. {book}")

# Function to issue books

def issue_books():
    name = input("Enter the book name to issue: ")

    if name in books:
        books.remove(name)
        issued_books.append(name)
        print("Book issued successfully")
    else:
        print("Book is not available")


# Function to return books

def return_books():
    name = input("Enter the book name to return: ")

    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print("Book returned successfully")
    else:
        print("This book was not issued")

# Function to show issued books

def show_issued_books():
    if len(issued_books) == 0:
        print("No books are issued")
    else:
        print("\nIssued Books:")
        for index, book in enumerate(issued_books, start=1):
            print(f"{index}. {book}")

# Main library menu

def library_menu():
    while True:
        print("\n========== LIBRARY MENU ==========")
        print("1. Add Book")
        print("2. Show Available Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Show Issued Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_books()

        elif choice == "2":
            show_books()

        elif choice == "3":
            issue_books()

        elif choice == "4":
            return_books()

        elif choice == "5":
            show_issued_books()

        elif choice == "6":
            print("Thank you for using Library Management System")
            break

        else:
            print("Invalid choice. Please try again.")



library_menu()
