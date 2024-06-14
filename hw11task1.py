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
    Сlass library.
    """
    def __init__(self, title, author, page_count, isbn):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.reserved = False

    def reserve(self):
        """
        Reservation.
        """
        self.reserved = True

    def unreserve(self):
        """
        Removed from reservation.
        """
        self.reserved = False

    def is_reserved(self):
        """
        In use by another reader.
        """
        return self.reserved


class User:
    """
    Class reader.
    """
    def __init__(self, name):
        self.name = name

    def borrow_book(self, book):
        """
        Book reservation.
        """
        if book.is_reserved():
            print(f"{self.name}, the book is already reserved.")
        else:
            print(f"{self.name} borrowed '{book.title}'.")
            book.reserve()

    def return_book(self, book):
        """
        Return of books.
        """
        print(f"{self.name} returned '{book.title}'.")
        book.unreserve()


book1 = Book("Mы", "Девид Николс", 292, "978-5-389-08539-8")
book2 = Book("Я", "Александр Потемкин", 249, "5-902377-10-2")
user1 = User("Mike")
user2 = User("Bob")
user1.borrow_book(book1)
user2.borrow_book(book1)
user2.borrow_book(book2)
user1.return_book(book1)
user2.return_book(book2)
