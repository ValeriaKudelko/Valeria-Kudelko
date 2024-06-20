"""
Homework.
"""
# Колода карт.
# Напишите программу которая содержит список карт, умеет
# их перемешивать и позволяет пользователю достать карту
# из колоды по ее номеру. Всего в колоде 54 карты. Класс
# Card содержит спискок номеров карт и список мастей.
# class Card:
#     number_list = ...
#     mast_list = ...

#     def __init__(self):
#         ...

# class CardsDeck:
#     def __init__(self):
#         ...

# deck = CardsDeck()
# deck.shuffle()
# card_number = int(input('Выберите карту из колоды в 54 карты:'))
# card = deck.get(card_number)
# print(f'You card is: {card}')
# >> Hearts 10

# card_number = int(input('Выберите карту из колоды в 54 карты:'))
# card = deck.get(card_number)
# print(f'You card is: {card}')
# >> Diamonds 6


import random


class Card:
    """
    Contains a list of card numbers and a list of suits.
    """
    number_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']  # pylint: disable=line-too-long  # noqa: E501
    mast_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, number, mast):
        self.number = number
        self.mast = mast

    def __str__(self):
        return f"{self.mast} {self.number}"


class CardsDeck:
    """
    Contains an entire deck of cards.
    """
    def __init__(self):
        self.deck = [Card(number, mast) for number in Card.number_list for mast in Card.mast_list]  # pylint: disable=line-too-long  # noqa: E501

    def shuffle(self):
        """
        Shuffles the cards.
        """
        random.shuffle(self.deck)

    def get(self, card_number):
        """
        Output card.
        """
        if 1 <= card_number <= len(self.deck):
            return self.deck[card_number - 1]
        else:
            return "Joker"


deck = CardsDeck()
deck.shuffle()

card_number1 = int(input('Выберите карту из колоды в 54 карты: '))
card1 = deck.get(card_number1)
print(f'You card is: {card1}')

card_number2 = int(input('Выберите карту из колоды в 54 карты: '))
card2 = deck.get(card_number2)
print(f'You card is: {card2}')
