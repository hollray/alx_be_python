# library_system.py

class Book:
    """
    Base class representing a general book.
    """

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class EBook(Book):
    """
    Derived class representing an electronic book.
    Inherits from Book and includes file_size.
    """

    def __init__(self, title: str, author: str, file_size: int):
        # Call the base class (Book) constructor
        super().__init__(title, author)
        # Unique attribute for EBook
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author} ({self.file_size} KB)"


class PrintBook(Book):
    """
    Derived class representing a physical print book.
    Inherits from Book and includes page_count.
    """

    def __init__(self, title: str, author: str, page_count: int):
        # Call the base class (Book) constructor
        super().__init__(title, author)
        # Unique attribute for PrintBook
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author} ({self.page_count} pages)"


class Library:
    """
    Manages a collection of books (composition).
    """

    def __init__(self):
        # List to store instances of various book types
        self.books = []

    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook instance to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print(
                f"Error: Invalid object type. Cannot add {type(book)} to the library.")

    def list_books(self):
        """Prints details of each book in the library."""
        if not self.books:
            print("The library is currently empty.")
            return

        print("--- Library Inventory ---")
        for book in self.books:
            # Polymorphism in action: calling __str__ on the specific book type
            print(book)
        print("-------------------------")
