"""
Homework.
"""
# Библиотека.
# Создайте класс book с именем книги, автором, кол-м страниц,
# ISBN, флагом, зарезервирована ли книги или нет. Создайте
# класс пользователь который может брать книгу, возвращать,
# бронировать. Если другой пользователь хочет взять зарезервированную
# книгу(или которую уже кто-то читает - надо ему про это сказать).


class Book:
    """
    Class library.
    """
    def __init__(self, title, author,
                 pages, isbn, reserved=False, borrowed_by=None):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved
        self.borrowed_by = borrowed_by


class User:
    """
    Class reader.
    """
    def __init__(self, name):
        self.name = name
        self.books = []

    def borrow_book(self, book):
        """
        Takes books.
        """
        if book.borrowed_by is not None:
            print(f"Книгу '{book.title}' взял {book.borrowed_by.name}.")
        else:
            book.borrowed_by = self
            self.books.append(book)
            print(f"{self.name} взял книгу '{book.title}'.")

    def return_book(self, book):
        """
        Return of books.
        """
        if book in self.books:
            book.borrowed_by = None
            self.books.remove(book)
            print(f"{self.name} вернул книгу '{book.title}'.")
        else:
            print(f"{self.name} не брал книгу '{book.title}'.")

    def reserve_book(self, book):
        """
        Book reservation.
        """
        if book.reserved:
            print(f"Книга '{book.title}' зарезервирована другим читателем.")
        else:
            book.reserved = True
            book.reserved_by = self
            print(f"{self.name} зарезервировал книгу '{book.title}'.")


book1 = Book("Mы", "Девид Николс", 292, "978-5-389-08539-8")
book2 = Book("Я", "Александр Потемкин", 249, "5-902377-10-2")
user1 = User("Mike")
user2 = User("Bob")

user1.reserve_book(book1)
user1.borrow_book(book1)
user2.borrow_book(book1)
user2.reserve_book(book1)
user2.borrow_book(book1)
user1.return_book(book1)
user2.return_book(book1)
user2.borrow_book(book1)
user2.return_book(book1)
