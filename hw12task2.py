"""
Homework.
"""
# Конвертер валют.
# Расширьте функционал класса Bank из домашней работы #11.
# Добавьте новый класс Currency, который умеет конвертировать
# различные валюты(USD, EUR, ...) в заданную валюту.
# bank = Bank(..)
# vasya = Person('USD', 10)
# petya = Person('EUR', 5)
# Если валюта не задана, то конвертация происходит в BYN:
# assert bank.exchange_currency(vasya.currency, vasya.amount)
# == (32.69, "BYN"), <error message>
# assert bank.exchange_currency(petya.currency, petya.amount)
# == (35.20, "BYN"), <error message>
# Конвертация в заданную валюту:
# assert bank.exchange_currency(vasya.currency, vasya.amount, 'EUR')
# == (9.29, "EUR"), <error message>
# assert bank.exchange_currency(petya.currency, petya.amount, 'USD')
# == (10.76, "USD"), <error message>


class Currency:
    """
    Converts different currencies to a
    specified target currency (default: BYN).
    """
    def __init__(self):
        self.exchange_rates = {
            'USD': 3.19,
            'EUR': 3.42
        }

    def convert_to_byn(self, amount, source_currency):
        """
        Converts the given amount from the source currency to BYN.
        """
        exchange_rate = self.exchange_rates.get(source_currency, 1.0)
        converted_amount = amount * exchange_rate
        return converted_amount, "BYN"


class Deposit:
    """
    Displays the contribution by amount and term.
    """
    def __init__(self, amount, period, currency):
        self.amount = amount
        self.period = period
        self.currency = currency
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


class Person:
    """
    A person who has a certain amount of a certain currency.
    """
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount


class Bank:
    """
    A bank that offers currency exchange.
    """

    def __init__(self):
        self.currency_converter = Currency()

    def exchange_currency(self, source_currency, amount, target_currency='BYN'):  # noqa: 501
        """
        Converts the given amount from the source
        currency to the target currency, or to BYN if
        no target currency is specified.
        """
        if not target_currency:
            target_currency = 'BYN'

        converted_amount, converted_currency = self.currency_converter.convert_to_byn(amount, source_currency)  # noqa: E501
        target_exchange_rate = self.currency_converter.exchange_rates.get(target_currency, 1.0)  # noqa: E501
        final_amount = converted_amount / target_exchange_rate
        return final_amount, target_currency


bank = Bank()
vasya = Person('USD', 10)
petya = Person('EUR', 5)

amoun, currenc = bank.exchange_currency(vasya.currency, vasya.amount)
print(amoun, currenc)

amoun, currenc = bank.exchange_currency(petya.currency, petya.amount)
print(amoun, currenc)

amoun, currenc = bank.exchange_currency(vasya.currency, vasya.amount, 'EUR')
print(amoun, currenc)

amoun, currenc = bank.exchange_currency(petya.currency, petya.amount, 'USD')
print(amoun, currenc)

assert bank.exchange_currency(vasya.currency, vasya.amount) == (31.90, "BYN")
assert bank.exchange_currency(petya.currency, petya.amount) == (17.10, "BYN")
assert bank.exchange_currency(vasya.currency, vasya.amount, "EUR") == (9.29, "EUR"), "Conversion to EUR failed"  # noqa: E501
assert bank.exchange_currency(petya.currency, petya.amount, "USD") == (10.76, "USD"), "Conversion to USD failed"  # noqa: E501
