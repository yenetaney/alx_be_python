class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

class Library:
    _books = []
    def add_books(self,book):
        self.book = book
        self._books.append(Book)
    def check_out_book(self, title):
        for book in self._books:
            if Book.title == title and not Book.is_checked_out:
                Book.is_checked_out = True
                print(f"Checked out: '{Book.title}' by '{Book.author}'")
                return
        print(f'Book not available: "{title}"')
     
    def return_book(self, title):
        for book in self._book:
            if Book.title == title and not Book.is_checked_out():
                Book.return_book()
                print(f"returned :{title}")
                return
        print(f"Book not found or not cheaked out :{title}")

    def list_available_books(self):
        print("Avaliable books: ")
        for book in self._books:
            if Book.is_checked_out():
                print(f"{Book.title} by {Book.author}")