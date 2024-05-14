from wallet import Wallet
from utils import save_transactions, load_transactions
from config.settings import TRANSACTIONS_FILE_NAME

def main() -> None:
    wallet = Wallet()
    load_transactions(wallet, TRANSACTIONS_FILE_NAME)
    while True:
        print("\nВыберите действие:")
        print("1. Внести средства")
        print("2. Снять средства")
        print("3. Проверить баланс")
        print("4. Вывести список транзакций")
        print("5. Редактировать транзакцию")
        print("6. Поиск по транзакциям")
        print("7. Сохранить данные в файл")
        print("8. Выйти")
        choice = input("Введите номер действия: ")

        if choice == '1':
            amount = float(input("Введите сумму для внесения: "))
            description = input("Введите описание: ")
            extra = input("Введите дополнительную информацию (опционально): ")
            wallet.deposit(amount, description, extra)
        elif choice == '2':
            amount = float(input("Введите сумму для снятия: "))
            description = input("Введите описание: ")
            extra = input("Введите дополнительную информацию (опционально): ")
            wallet.withdraw(amount, description, extra)
        elif choice == '3':
            wallet.check_balance()
        elif choice == '4':
            wallet.show_transactions()
        elif choice == '5':
            index = int(input("Введите индекс транзакции для редактирования: "))
            new_amount = float(input("Введите новую сумму: "))
            new_extra = input("Введите новую дополнительную информацию (опционально): ")
            wallet.edit_transaction(index, new_amount, new_extra)
        elif choice == '6':
            category = input("Введите категорию транзакции для поиска (Доход/Расход): ").capitalize()
            amount = float(input("Введите сумму транзакции для поиска (опционально): "))
            extra = input("Введите дополнительную информацию для поиска (опционально): ")
            wallet.search_transactions(category, amount, extra)
        elif choice == '7':
            save_transactions(wallet, TRANSACTIONS_FILE_NAME)
            print("Данные успешно сохранены в файл.")
        elif choice == '8':
            print("Спасибо за использование нашего кошелька. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
