class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

class Library:
    def __init__(self):
        self._books = []
    def add_books(self,book):
        self.book = book
        self._books.append(book)
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_checked_out:
                book.is_checked_out = True
                print(f"Checked out: '{book.title}' by '{book.author}'")
                return
        print(f'Book not available: "{title}"')
     
    def return_book(self, title):
        for book in self._book:
            if book.title == title and not book.is_checked_out():
                book.return_book()
                print(f"returned :{title}")
                return
        print(f"Book not found or not cheaked out :{title}")

    def list_available_books(self):
        print("Avaliable books: ")
        for book in self._books:
            if book.is_checked_out():
                print(f"{book.title} by {book.author}")