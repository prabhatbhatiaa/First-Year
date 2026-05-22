# Task 4: Menu-Driven Command Line Interface

from library_manager.inventory import LibraryInventory
from library_manager.book import Book

def main():
    library = LibraryInventory()
    while True:
        print("\n === Library Inventory Manager ===")
        print("1. Add New Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search for Book")
        print("6. Exit")
        ch = input("Enter your choice: ")

        if ch == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN number: ")
            new_book = Book(title, author, isbn)
            library.add_book(new_book)
            print("Book added successfully")

        elif ch == "2":
            isbn = input("Enter ISBN of book: ")
            book = library.search_by_isbn(isbn)
            if book is None:
                print("No book found with given ISBN")
            else:
                if book.issue():
                    library.save_catalog()
                    print("Book issued successfully.")
                else:
                    print("This book is already issued.")

        elif ch == "3":
            isbn = input("Enter ISBN of book: ")
            book = library.search_by_isbn(isbn)
            if book is None:
                print("No book found with given ISBN.")
            else:
                if book.return_book():
                    library.save_catalog()
                    print("Book returned successfully.")
                else:
                    print("This book was not issued.")

        elif ch == "4":
            books = library.display_all()
            if not books:
                print("No books in the catalog yet.")
            else:
                print("\n >>> All Books")
                for book in books:
                    print(book)

        elif ch == "5":
            title = input("Enter title to search: ")
            matches = library.search_by_title(title)
            if not matches:
                print("No books found with that title.")
            else:
                print("\n >>> Search Results")
                for book in matches:
                    print(book)

        elif ch == "6":
            print("PROGRAM END")
            break

        else:
            print("Incorrect choice. Retry")

if __name__ == "__main__":
    main()
