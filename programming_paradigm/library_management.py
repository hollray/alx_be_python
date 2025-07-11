# library_management.py

class Book:
    """Represents a book in the library with title, author, and checkout status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Already checked out

    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Not checked out

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of Book objects."""

    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Adds a new book to the library."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Error: Only Book objects can be added to the library.")

    def _find_book(self, title):
        """Helper method to find a book by title."""
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        """Checks out a book by its title."""
        book = self._find_book(title)
        if book:
            if book.check_out():
                print(f"'{title}' has been checked out.")
            else:
                print(f"'{title}' is already checked out.")
        else:
            print(f"Book with title '{title}' not found in the library.")

    def return_book(self, title):
        """Returns a book by its title."""
        book = self._find_book(title)
        if book:
            if book.return_book():
                print(f"'{title}' has been returned.")
            else:
                print(f"'{title}' was not checked out.")
        else:
            print(f"Book with title '{title}' not found in the library.")

    def list_available_books(self):
        """Lists all currently available books in the library."""
        available_found = False
        for book in self._books:
            if book.is_available():
                print(book)
                available_found = True
        if not available_found:
            print("No books are currently available.")
