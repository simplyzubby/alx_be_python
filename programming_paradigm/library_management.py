class Book:
     def __init__(self, title, author):
        self.title = title          # Public attribute
        self.author = author        # Public attribute
        self._is_checked_out = False  
     def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

     def return_book(self):
        """Return the book (mark as available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

     def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only Book instances can be added.")

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f'Book "{title}" has been checked out.'
        return f'Book "{title}" is not available.'

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f'Book "{title}" has been returned.'
        return f'Book "{title}" was not checked out.'

    def list_available_books(self):
        """Return a list of available books."""
        available = [f'{book.title} by {book.author}' for book in self._books if book.is_available()]
        return available