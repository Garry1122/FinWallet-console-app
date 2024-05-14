from datetime import datetime
from typing import Optional

class Transaction:
    def __init__(self, date: datetime, category: str, amount: float, description: str, extra: Optional[str] = None) -> None:
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description
        self.extra = extra

    def __str__(self) -> str:
        return f"Дата: {self.date}\nКатегория: {self.category}\nСумма: {self.amount}\nОписание: {self.description}\nДополнительно: {self.extra}\n"
