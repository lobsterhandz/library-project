# user.py
class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = []

    def borrow(self, book):
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed {book.title}")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} has not borrowed {book.title}")

    def display_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s borrowed books:")
            for book in self.borrowed_books:
                print(f"- {book.title}")
        else:
            print(f"{self.name} has no borrowed books.")
