from validation import validate_isbn, validate_user_id, validate_name

def main_menu(library):
    while True:
        print("\nWelcome to the Library Management System!\n")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")

        choice = input("Select an option: ")

        if choice == '1':
            book_operations(library)
        elif choice == '2':
            user_operations(library)
        elif choice == '3':
            author_operations(library)
        elif choice == '4':
            genre_operations(library)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def book_operations(library):
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            borrow_book(library)
        elif choice == '3':
            return_book(library)
        elif choice == '4':
            search_book(library)
        elif choice == '5':
            library.display_all_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")
    pub_date = input("Enter publication date: ")
    genre = input("Enter genre: ")
    if not validate_isbn(isbn):
        print("Invalid ISBN format. Please try again.")
        return
    library.add_book(title, author, isbn, pub_date, genre)
    print(f"Book '{title}' added.")

def borrow_book(library):
    isbn = input("Enter book ISBN: ")
    if not validate_isbn(isbn):
        print("Invalid ISBN format. Please try again.")
        return
    user_id = input("Enter user ID: ")
    if not validate_user_id(user_id):
        print("Invalid user ID format. Please try again.")
        return
    if library.borrow_book(isbn, user_id):
        print("Book borrowed successfully.")
    else:
        print("Failed to borrow the book.")

def return_book(library):
    isbn = input("Enter book ISBN: ")
    if not validate_isbn(isbn):
        print("Invalid ISBN format. Please try again.")
        return
    user_id = input("Enter user ID: ")
    if not validate_user_id(user_id):
        print("Invalid user ID format. Please try again.")
        return
    if library.return_book(isbn, user_id):
        print("Book returned successfully.")
    else:
        print("Failed to return the book.")

def search_book(library):
    isbn = input("Enter book ISBN: ")
    if not validate_isbn(isbn):
        print("Invalid ISBN format. Please try again.")
        return
    book = library.find_book_by_isbn(isbn)
    if book:
        status = "Available" if book.available else "Borrowed"
        print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {status}")
    else:
        print("Book not found.")

def user_operations(library):
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == '1':
            add_user(library)
        elif choice == '2':
            view_user(library)
        elif choice == '3':
            library.display_all_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_user(library):
    name = input("Enter user name: ")
    if not validate_name(name):
        print("Invalid name format. Please try again.")
        return
    user_id = input("Enter library ID: ")
    if not validate_user_id(user_id):
        print("Invalid user ID format. Please try again.")
        return
    library.add_user(name, user_id)
    print(f"User '{name}' added.")

def view_user(library):
    user_id = input("Enter library ID: ")
    if not validate_user_id(user_id):
        print("Invalid user ID format. Please try again.")
        return
    user = library.find_user_by_id(user_id)
    if user:
        print(f"Name: {user.name}, Library ID: {user.library_id}")
    else:
        print("User not found.")

def author_operations(library):
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == '1':
            add_author(library)
        elif choice == '2':
            view_author(library)
        elif choice == '3':
            library.display_all_authors()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_author(library):
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")
    library.add_author(name, biography)
    print(f"Author '{name}' added.")

def view_author(library):
    name = input("Enter author name: ")
    for author in library.authors:
        if author.name == name:
            print(f"Name: {author.name}, Biography: {author.biography}")
            break
    else:
        print("Author not found.")

def genre_operations(library):
    while True:
        print("\nGenre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        print("4. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == '1':
            add_genre(library)
        elif choice == '2':
            view_genre(library)
        elif choice == '3':
            library.display_all_genres()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_genre(library):
    name = input("Enter genre name: ")
    description = input("Enter genre description: ")
    category = input("Enter genre category: ")
    library.add_genre(name, description, category)
    print(f"Genre '{name}' added.")

def view_genre(library):
    name = input("Enter genre name: ")
    for genre in library.genres:
        if genre.name == name:
            print(f"Name: {genre.name}, Description: {genre.description}, Category: {genre.category}")
            break
    else:
        print("Genre not found.")
