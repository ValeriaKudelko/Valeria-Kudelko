"""
Unit tests.
"""
import logging
import unittest
from HW11.hw11task1 import User, Book

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment.
        """
        self.book1 = Book("Mы", "Девид Николс", 292, "978-5-389-08539-8")
        self.book2 = Book("Я", "Александр Потемкин", 249, "5-902377-10-2")
        self.user1 = User("Mike")
        self.user2 = User("Bob")

    def tearDown(self):
        """
        Completion at the end of the test.
        """
        del self.book1
        del self.book2
        del self.user1
        del self.user2

    def test_borrow_book(self):
        """
        Test the borrow_book method.
        """
        self.user1.borrow_book(self.book1)
        self.assertEqual(self.book1.borrowed_by, self.user1)
        self.user2.borrow_book(self.book1)
        self.assertEqual(self.book1.borrowed_by, self.user1)

    def test_return_book(self):
        """
        Test the return_book method.
        """
        self.user1.return_book(self.book1)
        self.user1.return_book(self.book1)
        self.assertIsNone(self.book1.borrowed_by)

    def test_reserve_book(self):
        """
        Test the reserve_book method.
        """
        self.user1.reserve_book(self.book1)
        self.assertTrue(self.book1.reserved)
        self.user2.reserve_book(self.book1)
        self.assertTrue(self.book1.reserved)


if __name__ == "__main__":
    unittest.main()
