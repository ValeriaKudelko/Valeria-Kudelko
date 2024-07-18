"""
Unit tests.
"""
import logging
import unittest
from HW11.hw11task2 import Bank, Deposit

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestDeposit(unittest.TestCase):
    """
    Test case for the Deposit class.
    """
    def setUp(self):
        """
        Set up the test environment.
        """
        logger.info("Setting up test for Deposit class")
        self.deposit = Deposit(10000, 1)

    def tearDown(self):
        """
        Completion at the end of the test.
        """
        logger.info("Tearing down test for Deposit class")
        del self.deposit

    def test_calculate_interest(self):
        """
        Test the calculate_interest method of the Deposit class.
        """
        logger.info("Testing calculate_interest method")
        interest = self.deposit.calculate_interest()
        self.assertAlmostEqual(interest, 83.33, places=2)

    def test_apply_interest(self):
        """
        Test the apply_interest method of the Deposit class.
        """
        logger.info("Testing apply_interest method")
        initial_amount = self.deposit.amount
        self.deposit.apply_interest()
        self.assertGreater(self.deposit.amount, initial_amount)

    def test_get_total(self):
        """
        Test the get_total method of the Deposit class.
        """
        logger.info("Testing get_total method")
        total_amount = self.deposit.get_total()
        self.assertGreaterEqual(total_amount, self.deposit.amount)


class TestBank(unittest.TestCase):
    """
    Test case for the Bank class.
    """
    def setUp(self):
        """
        Set up the test environment.
        """
        logger.info("Setting up test for Bank class")
        self.bank = Bank()

    def tearDown(self):
        """
        Completion at the end of the test.
        """
        logger.info("Tearing down test for Bank class")
        del self.bank

    def test_deposit(self):
        """
        Test the deposit method of the Bank class.
        """
        logger.info("Testing deposit method")
        deposit_amount = self.bank.deposit(10000, 1)
        self.assertGreaterEqual(deposit_amount, 10000)


if __name__ == "__main__":
    unittest.main()
