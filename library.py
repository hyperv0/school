# Library Management System

# Welcome message
print("Welcome to the Library Management System!")

# Initialize library as an empty list
library = []

# Main menu loop
while True:
    # Display menu options
    print("\nMain Menu:")
    print("1. Add a New Book")
    print("2. View All Books")
    print("3. Search for a Book")
    print("4. Remove a Book")
    print("5. Exit")

    # Get user choice
    choice = input("Enter your choice (1-5): ").strip()

    # Option 1: Add a New Book
    if choice == "1":
        book = input("Enter the title of the book to add: ").strip()
        if book:
            library.append(book)
            print(f'"{book}" has been added to the library.')
        else:
            print("Book title cannot be empty.")

    # Option 2: View All Books
    elif choice == "2":
        if library:
            print("\nList of Books in the Library:")
            for idx, book in enumerate(library, 1):
                print(f"{idx}. {book}")
        else:
            print("The library is currently empty.")

    # Option 3: Search for a Book
    elif choice == "3":
        search = input("Enter the title of the book to search for: ").strip()
        if search in library:
            print(f'"{search}" is available in the library.')
        else:
            print(f'"{search}" is not found in the library.')

    # Option 4: Remove a Book
    elif choice == "4":
        remove = input("Enter the title of the book to remove: ").strip()
        if remove in library:
            library.remove(remove)
            print(f'"{remove}" has been removed from the library.')
        else:
            print(f'"{remove}" is not found in the library.')

    # Option 5: Exit
    elif choice == "5":
        print("Thank you for using the Library Management System. Goodbye!")
        break

    # Invalid Input
    else:
        print("Invalid choice. Please try again.")
 
