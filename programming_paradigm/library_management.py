class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False
    
    def is_available(self):
        return not self.is_checked_out  


class Library:
    def __init__(self):
        self.books = []
  
    def add_book(self, book):
        self.books.append(book)
  
    def check_out_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    return f"{title} by {book.author} checked out successfully."
                else:
                    return f"{title} has already been checked out."
        return f"{title} is not in the library."
  
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    return f"{title} by {book.author} returned successfully."
                else:
                    return f"{title} was not checked out."
        return f"{title} is not in the library."
  
    def list_available_books(self):
        available_books = [book for book in self.books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No available books.")