
"""
NAME: PRIYANSHI
DATE: 3/12/25
TITLE: Library Inventory Manager

"""



import logging
from library_manager.inventory import LibraryInventory
from library_manager.book import Book

# --- TASK 5: LOGGING CONFIGURATION ---
# This block MUST start at the far left margin (no indentation)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("library.log"), # Writes to file
        logging.StreamHandler()            # Prints to console
    ] # <--- Note the bracket and parenthesis end here
)

def menu():
    print("\n===== LIBRARY INVENTORY MANAGER =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

def main():
    inventory = LibraryInventory()

    while True:
        menu()
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                title = input("Title: ")
                author = input("Author: ")
                isbn = input("ISBN: ")

                inventory.add_book(Book(title, author, isbn))
                print("Book added successfully.")

            elif choice == "2":
                isbn = input("Enter ISBN to issue: ")
                book = inventory.search_by_isbn(isbn)

                if book and book.issue():
                    inventory.save_books()
                    print("Book issued.")
                else:
                    print("Book unavailable or not found.")

            elif choice == "3":
                isbn = input("Enter ISBN to return: ")
                book = inventory.search_by_isbn(isbn)

                if book:
                    book.return_book()
                    inventory.save_books()
                    print("Book returned.")
                else:
                    print("Book not found.")

            elif choice == "4":
                books = inventory.display_all()
                for b in books:
                    print(b)

            elif choice == "5":
                keyword = input("Enter title to search: ")
                results = inventory.search_by_title(keyword)

                if results:
                    for b in results:
                        print(b)
                else:
                    print("No book found.")

            elif choice == "6":
                print("Exiting program...")
                break

            else:
                print("Invalid option.")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()