class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass





class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author}"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} has already borrowed the maximum number of books (3).")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"The book '{book.title}' is already borrowed.")

        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
        else:
            raise BookNotFoundException(f"{self.name} did not borrow the book '{book.title}'.")

    def __str__(self):
        borrowed_titles = ', '.join([book.title for book in self.borrowed_books]) or "None"
        return f"Member: {self.name}, Borrowed books: {borrowed_titles}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"The book '{title}' was not found in the library.")

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise Exception(f"Member '{member_name}' not found.")

        book = self.find_book(book_title)
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise Exception(f"Member '{member_name}' not found.")

        book = self.find_book(book_title)
        member.return_book(book)

# Testing the library system
library = Library()

# Add books
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

# Add members
library.add_member(Member("Alice"))
library.add_member(Member("Bob"))

# Borrow and return books
try:
    library.borrow_book("Alice", "1984")
    library.borrow_book("Alice", "The Great Gatsby")
    print(f"Alice successfully borrowed books.")
    
    library.borrow_book("Bob", "1984")  # This should raise BookAlreadyBorrowedException
except Exception as e:
    print(e)

try:
    library.return_book("Alice", "1984")
    print(f"Alice successfully returned '1984'.")
except Exception as e:
    print(e)

try:
    library.borrow_book("Bob", "1984")
    print(f"Bob successfully borrowed '1984'.")
except Exception as e:
    print(e)