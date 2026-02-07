# Library Management System

books = []
issued_books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    quantity = int(input("Enter quantity: "))
    books.append({"title": title, "author": author, "quantity": quantity})
    print(f"{title} added successfully!")

def display_books():
    print("\nAvailable Books:")
    for book in books:
        print(f"{book['title']} by {book['author']} - Quantity: {book['quantity']}")

def issue_book():
    title = input("Enter book title to issue: ")
    for book in books:
        if book['title'].lower() == title.lower() and book['quantity'] > 0:
            book['quantity'] -= 1
            issued_books.append(book)
            print(f"{title} has been issued.")
            return
    print("Book not available!")

def return_book():
    title = input("Enter book title to return: ")
    for book in issued_books:
        if book['title'].lower() == title.lower():
            book['quantity'] += 1
            issued_books.remove(book)
            print(f"{title} has been returned.")
            return
    print("This book was not issued.")

# Menu
while True:
    print("\n1. Add Book\n2. Display Books\n3. Issue Book\n4. Return Book\n5. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        add_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        issue_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        break
    else:
        print("Invalid choice!")