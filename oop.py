class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title} | Author: {self.author}")

    def read_book(self):
        print(f"I am reading {self.title} by {self.author}.")

book1 = Book("Harry potter", "j.k. Rowling")
book2 = Book("Atomic habits", "james clear")

book1.read_book()
book2.read_book()
