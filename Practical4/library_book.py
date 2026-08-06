class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print("Book borrowed successfully.")
        else:
            print("Book is already borrowed.")

    def return_book(self):
        self.available = True
        print("Book returned successfully.")

    def display(self):
        print("\nBook Details")
        print("Title :", self.title)
        print("Author:", self.author)
        print("Year  :", self.year)
        print("Available:", self.available)


book = Book("Python Programming", "John", 2024)

book.display()

book.borrow()
book.display()

book.return_book()
book.display()