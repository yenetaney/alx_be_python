class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book({repr(self.title)}, {repr(self.author)})"

    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self,title: str, author: str, file_size:int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} [EBook, {self.file_size}MB]"

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count:int):
        super().__init__(title,author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} [PrintBook, {self.page_count} pages]"
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book:Book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)