"""
Homework.
"""
# Банковский вклад.
# Создайте класс вклад. Который содержит необходимые поля и методы,
# например сумма вклада и его срок. Пользователь делает вклад в размере
# N рублей сроком на R лет под 10% годовых (вклад с возможностью
# ежемесячной капитализации - это означает, что проценты прибавляются
# к сумме вклада ежемесячно). Написать класс Bank, метод deposit принимает
# аргументы N и R, и возвращает сумму, которая будет на счету пользователя.
# https://myfin.by/wiki/term/kapitalizaciya-procentov


class Deposit:
    """
    Displays the contribution by amount and term.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period
        self.rate = 0.1

    def calculate_interest(self):
        """
        Calculates monthly interest on deposits.
        """
        interest = self.amount * self.rate / 12
        return interest

    def apply_interest(self):
        """
        Adds the calculated interest to the deposit amount.
        """
        self.amount += self.calculate_interest()

    def get_total(self):
        """
        Interest capitalization and return of the final deposit amount.
        """
        for _ in range(self.period * 12):
            self.apply_interest()
        return self.amount


class Bank:
    """
    Displays bank.
    """
    def __init__(self):
        self.deposits = []

    def deposit(self, amount, period):
        """
        Displays the final deposit amount.
        """
        deposit = Deposit(amount, period)
        self.deposits.append(deposit)
        return deposit.get_total()


bank = Bank()
deposit_amount = bank.deposit(10000, 1)
print(f"Сумма на счету через 1 год: {deposit_amount}")
