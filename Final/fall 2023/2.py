from abc import ABC, abstractmethod

# Abstract class
class LibraryItem(ABC):
    def __init__(self, title, author, publication_date):
        self.title = title
        self.author = author
        self.publication_date = publication_date

    @abstractmethod
    def display_details(self):
        pass

    def borrow(self):
        print(f"The item '{self.title}' has been borrowed.")

    def return_item(self):
        print(f"The item '{self.title}' has been returned.")


# Subclass: Book
class Book(LibraryItem):
    def __init__(self, title, author, publication_date, isbn):
        super().__init__(title, author, publication_date)
        self.isbn = isbn

    def display_details(self):
        print(f"Book Details:\nTitle: {self.title}\nAuthor: {self.author}\nPublication Date: {self.publication_date}\nISBN: {self.isbn}")


# Subclass: Magazine
class Magazine(LibraryItem):
    def __init__(self, title, author, publication_date, issue_no):
        super().__init__(title, author, publication_date)
        self.issue_no = issue_no

    def display_details(self):
        print(f"Magazine Details:\nTitle: {self.title}\nAuthor: {self.author}\nPublication Date: {self.publication_date}\nIssue No: {self.issue_no}")


# Creating objects and calling methods
library_item = LibraryItem  # Abstract class cannot be instantiated
book = Book("Python Programming", "John Doe", "2022-05-01", "1234567890")
magazine = Magazine("Tech World", "Jane Smith", "2023-06-15", "42")

# Display details
book.display_details()
book.borrow()
book.return_item()

print("\n")

magazine.display_details()
magazine.borrow()
magazine.return_item()
