from user import User
class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.genres = []

    def add_book(self, title, author, isbn, pub_date, genre):
        new_book = Book(title, author, isbn, pub_date, genre)
        self.books.append(new_book)

    def borrow_book(self, isbn, user_id):
        book = self.find_book_by_isbn(isbn)
        user = self.find_user_by_id(user_id)
        if book and user and book.available:
            book.borrow()
            user.borrow(book)
            return True
        return False

    def return_book(self, isbn, user_id):
        book = self.find_book_by_isbn(isbn)
        user = self.find_user_by_id(user_id)
        if book and user:
            book.return_book()
            user.return_book(book)
            return True
        return False

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all_books(self):
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {status}")

    # User operations
    def add_user(self, name, library_id):
        user = User(name, library_id)
        self.users.append(user)
        return user

    def find_user_by_id(self, library_id):
        for user in self.users:
            if user.library_id == library_id:
                return user
        return None

    def display_all_users(self):
        for user in self.users:
            print(f"Name: {user.name}, Library ID: {user.library_id}")

    # Author operations
    def add_author(self, name, biography):
        author = Author(name, biography)
        self.authors.append(author)
        return author

    def display_all_authors(self):
        for author in self.authors:
            print(f"Name: {author.name}, Biography: {author.biography}")

    # Genre operations
    def add_genre(self, name, description, category):
        genre = Genre(name, description, category)
        self.genres.append(genre)
        return genre

    def display_all_genres(self):
        for genre in self.genres:
            print(f"Name: {genre.name}, Description: {genre.description}, Category: {genre.category}")

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    # Getters and setters
    @property
    def name(self):
        return self.__name

    @property
    def biography(self):
        return self.__biography

class Book:
    def __init__(self, title, author, isbn, pub_date, genre):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__pub_date = pub_date
        self.__genre = genre
        self.__available = True

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    @property
    def available(self):
        return self.__available

    def borrow(self):
        if self.__available:
            self.__available = False
            print(f"Book '{self.__title}' is now borrowed.")
        else:
            print(f"Book '{self.__title}' is already borrowed.")

    def return_book(self):
        if not self.__available:
            self.__available = True
            print(f"Book '{self.__title}' is now returned.")
        else:
            print(f"Book '{self.__title}' was not borrowed.")

class Genre:
    def __init__(self, name, description, category):
        self.__name = name
        self.__description = description
        self.__category = category

    # Getters and setters
    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def category(self):
        return self.__category