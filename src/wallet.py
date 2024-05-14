import datetime
from datetime import datetime
from typing import List, Optional
from src.transaction import Transaction

class Wallet:
    def __init__(self) -> None:
        self.balance: float = 0
        self.income: float = 0
        self.expense: float = 0
        self.transactions: List[Transaction] = []

    def deposit(self, amount: float, description: str, extra: Optional[str] = None) -> None:
        if amount > 0:
            self.balance += amount
            self.income += amount
            self.transactions.append(Transaction(datetime.now(), "Доход", amount, description, extra))
            print(f"Вы внесли {amount} руб. Ваш баланс: {self.balance} руб.")
        else:
            print("Неверная сумма для внесения.")

    def withdraw(self, amount: float, description: str, extra: Optional[str] = None) -> None:
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.expense += amount
            self.transactions.append(Transaction(datetime.now(), "Расход", amount, description, extra))
            print(f"Вы сняли {amount} руб. Ваш баланс: {self.balance} руб.")
        else:
            print("Недостаточно средств или неверная сумма для снятия.")

    def check_balance(self) -> None:
        print(f"Ваш текущий баланс: {self.balance} руб.")
        print(f"Ваши общие доходы: {self.income} руб.")
        print(f"Ваши общие расходы: {self.expense} руб.")

    def show_transactions(self) -> None:
        print("\n--- Список транзакций ---")
        for index, transaction in enumerate(self.transactions, start=1):
            print(f"{index}. {transaction}")

    def edit_transaction(self, index: int, new_amount: float, new_extra: Optional[str] = None) -> None:
        if 0 < index <= len(self.transactions):
            transaction = self.transactions[index - 1]
            if transaction.category == "Доход":
                self.balance -= transaction.amount
                self.balance += new_amount
                self.income -= transaction.amount
                self.income += new_amount
            elif transaction.category == "Расход":
                self.balance += transaction.amount
                self.balance -= new_amount
                self.expense -= transaction.amount
                self.expense += new_amount
            transaction.amount = new_amount
            transaction.extra = new_extra
            print("Транзакция успешно отредактирована.")
        else:
            print("Неверный индекс транзакции.")

    def search_transactions(self, category: Optional[str] = None, amount: Optional[float] = None,
                            extra: Optional[str] = None) -> List[Transaction]:
        transactions = []
        for transaction in self.transactions:
            if (category is None or transaction.category == category) and (
                    amount is None or transaction.amount == amount) and (extra is None or transaction.extra == extra):
                transactions.append(transaction)
        return transactions

