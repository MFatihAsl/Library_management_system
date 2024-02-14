class Library:
    def __init__(self):                           # constructor
        self.file = open("books.txt", "a+")
        print("Library created. Books file opened.")

    def __del__(self):                            # destructor
        self.file.close()
        print("Library destroyed. Books file closed.")

    def list_books(self):
        self.file.seek(0)
        book_list = self.file.read().splitlines()  # Add each line to a list using splitlines() method

        if not book_list:
            print("No books found.")
        else:
            print("List of Books:\n")
            for book_info in book_list:
                title, author, release_year, num_pages = book_info.split(',')
                print(f"BOOK:  {title}, AUTHOR:  {author}")

    def add_book(self):
        title = input("Enter the book title: ")    # Adding a new book
        author = input("Enter the author: ")
        release_year = input("Enter the release year: ")
        num_pages = input("Enter the number of pages: ")

        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print(f"Book '{title}' added successfully.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")

        self.file.seek(0)
        book_list = self.file.read().splitlines()   # Removing a book

        index_to_remove = -1
        for i, book_info in enumerate(book_list):
            if title_to_remove in book_info:
                index_to_remove = i
                break

        if index_to_remove != -1:
            del book_list[index_to_remove]

            self.file.seek(0)
            self.file.truncate()

            for book_info in book_list:
                self.file.write(book_info + '\n')

            print(f"Book '{title_to_remove}' removed successfully.")
        else:
            print(f"Book '{title_to_remove}' not found.")

lib = Library()


while True:
    print("\n*** MENU ***")
    print("1) List Books")        # Basic menu
    print("2) Add Book")
    print("3) Remove Book")
    print("0) Exit")

    user_input = input("Enter your choice (0-3): ")

    if user_input == "1":
        lib.list_books()
    elif user_input == "2":
        lib.add_book()
    elif user_input == "3":                # if - else blocks to check users input
        lib.remove_book()
    elif user_input == "0":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 0 and 3.")
