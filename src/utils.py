from datetime import datetime
from transaction import Transaction
from wallet import Wallet

def save_transactions(wallet: Wallet, file_name: str) -> None:
    with open(file_name, "w") as file:
        for transaction in wallet.transactions:
            file.write(f"Дата: {transaction.date}\nКатегория: {transaction.category}\nСумма: {transaction.amount}\nОписание: {transaction.description}\nДополнительно: {transaction.extra}\n\n")


def load_transactions(wallet: Wallet, file_name: str) -> None:
    with open(file_name, "r") as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            date = datetime.strptime(lines[i].strip(), "Дата: %Y-%m-%d %H:%M:%S.%f")
            category = lines[i+1].split(":")[1].strip()
            amount = float(lines[i+2].split(":")[1].strip())
            description = lines[i+3].split(":")[1].strip()
            extra = lines[i+4].split(":")[1].strip() if lines[i+4].split(":")[1].strip() != 'None' else None
            wallet.transactions.append(Transaction(date, category, amount, description, extra))
            i += 6
