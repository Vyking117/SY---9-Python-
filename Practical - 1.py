# Library Management System using OOP

class Book:

    def __init__(self, book_id, book_title, book_author, book_genre,
                 article_id, article_title, article_author, article_genre):

        self.book_id = book_id
        self.book_title = book_title
        self.book_author = book_author
        self.book_genre = book_genre
        self.book_borrowed = False

        self.article_id = article_id
        self.article_title = article_title
        self.article_author = article_author
        self.article_genre = article_genre
        self.article_borrowed = False

    def display(self):

        status_book = "Borrowed" if self.book_borrowed else "Available"
        status_article = "Borrowed" if self.article_borrowed else "Available"

        print("\n------ Book Details ------")
        print("Book ID:", self.book_id)
        print("Title:", self.book_title)
        print("Author:", self.book_author)
        print("Genre:", self.book_genre)
        print("Status:", status_book)

        print("\n------ Article Details ------")
        print("Article ID:", self.article_id)
        print("Title:", self.article_title)
        print("Author:", self.article_author)
        print("Genre:", self.article_genre)
        print("Status:", status_article)


class Patron:

    def __init__(self, patron_id, name, contact_no):

        self.patron_id = patron_id
        self.name = name
        self.contact_no = contact_no
        self.borrowed_books = []
        self.borrowed_articles = []

    def display(self):

        print("\nPatron ID:", self.patron_id)
        print("Name:", self.name)
        print("Contact No:", self.contact_no)
        print("Borrowed Books:", self.borrowed_books)
        print("Borrowed Articles:", self.borrowed_articles)


class Library:

    def __init__(self):

        self.books = {}
        self.patrons = {}

    def add_book(self, book):

        self.books[book.book_id] = book
        print("Book and Article added successfully.")

    def register_patron(self, patron):

        self.patrons[patron.patron_id] = patron
        print("Patron Registered Successfully.")

    def borrow_book(self, patron_id, book_id):

        if patron_id not in self.patrons:
            print("Patron Not Found")
            return

        if book_id not in self.books:
            print("Book Not Found")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.book_borrowed:
            print("Book Already Borrowed")
        else:
            book.book_borrowed = True
            patron.borrowed_books.append(book.book_title)
            print("Book Borrowed Successfully")

    def return_book(self, patron_id, book_id):

        if patron_id not in self.patrons or book_id not in self.books:
            print("Invalid ID")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.book_title in patron.borrowed_books:

            book.book_borrowed = False
            patron.borrowed_books.remove(book.book_title)
            print("Book Returned Successfully")

        else:
            print("Book was not borrowed")

    def borrow_article(self, patron_id, book_id):

        if patron_id not in self.patrons:
            print("Patron Not Found")
            return

        if book_id not in self.books:
            print("Book Not Found")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.article_borrowed:
            print("Article Already Borrowed")
        else:
            book.article_borrowed = True
            patron.borrowed_articles.append(book.article_title)
            print("Article Borrowed Successfully")

    def return_article(self, patron_id, book_id):

        if patron_id not in self.patrons or book_id not in self.books:
            print("Invalid ID")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.article_title in patron.borrowed_articles:

            patron.borrowed_articles.remove(book.article_title)
            book.article_borrowed = False
            print("Article Returned Successfully")

        else:
            print("Article was not borrowed")

    def display_books(self):

        print("\n========== Library ==========")

        for book in self.books.values():
            book.display()

    def display_patrons(self):

        print("\n========== Patrons ==========")

        for patron in self.patrons.values():
            patron.display()


# Main Program

library = Library()

while True:

    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book & Article")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Borrow Article")
    print("6. Return Article")
    print("7. Display Books & Articles")
    print("8. Display Patrons")
    print("9. Exit")

    choice = input("Enter your Choice: ")

    if choice == "1":

        book_id = input("Enter Book ID: ")
        book_title = input("Enter Book Title: ")
        book_author = input("Enter Book Author: ")
        book_genre = input("Enter Book Genre: ")

        article_id = input("Enter Article ID: ")
        article_title = input("Enter Article Title: ")
        article_author = input("Enter Article Author: ")
        article_genre = input("Enter Article Genre: ")

        library.add_book(Book(book_id, book_title, book_author, book_genre,
                              article_id, article_title, article_author, article_genre))

    elif choice == "2":

        patron_id = input("Enter Patron ID: ")
        name = input("Enter Name: ")
        contact_no = input("Enter Contact Number: ")

        library.register_patron(Patron(patron_id, name, contact_no))

    elif choice == "3":

        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")

        library.borrow_book(patron_id, book_id)

    elif choice == "4":

        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")

        library.return_book(patron_id, book_id)

    elif choice == "5":

        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")

        library.borrow_article(patron_id, book_id)

    elif choice == "6":

        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")

        library.return_article(patron_id, book_id)

    elif choice == "7":

        library.display_books()

    elif choice == "8":

        library.display_patrons()

    elif choice == "9":

        print("Thank You!")
        break

    else:

        print("Invalid Choice")