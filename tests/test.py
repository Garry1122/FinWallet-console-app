import unittest
from src.wallet import Wallet


class TestWallet(unittest.TestCase):
    def setUp(self):
        self.wallet = Wallet()

    def test_deposit(self):
        self.wallet.deposit(1000, "Зарплата")
        self.assertEqual(self.wallet.balance, 1000)
        self.assertEqual(self.wallet.income, 1000)
        self.assertEqual(len(self.wallet.transactions), 1)

    def test_withdraw(self):
        self.wallet.deposit(1000, "Зарплата")
        self.wallet.withdraw(500, "Покупка")
        self.assertEqual(self.wallet.balance, 500)
        self.assertEqual(self.wallet.expense, 500)
        self.assertEqual(len(self.wallet.transactions), 2)

    def test_check_balance(self):
        self.wallet.deposit(1000, "Зарплата")
        self.wallet.withdraw(500, "Покупка")
        self.assertEqual(self.wallet.balance, 500)
        self.assertEqual(self.wallet.income, 1000)
        self.assertEqual(self.wallet.expense, 500)

    def test_edit_transaction(self):
        self.wallet.deposit(1000, "Зарплата")
        self.wallet.edit_transaction(1, 500)
        self.assertEqual(self.wallet.balance, 500)
        self.assertEqual(self.wallet.income, 500)
        self.assertEqual(self.wallet.transactions[0].amount, 500)

    def test_search_transactions(self):
        self.wallet.deposit(1000, "Зарплата")
        self.wallet.withdraw(500, "Покупка")
        transactions = self.wallet.search_transactions("Доход")
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0].amount, 1000)

if __name__ == "__main__":
    unittest.main()
