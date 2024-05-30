"""
Homework
"""
# Быки и коровы.
# В классическом варианте игра рассчитана на двух игроков. Каждый
# из игроков задумывает и записывает тайное 4-значное число с неповторяющимися
# цифрами. Игрок, который начинает игру по жребию, делает первую попытку
# отгадать число. Попытка — это 4-значное число с неповторяющимися цифрами,
# сообщаемое противнику. Противник сообщает в ответ, сколько цифр угадано без
# совпадения с их позициями в тайном числе (то есть количество коров) и сколько
# угадано вплоть до позиции в тайном числе (то есть количество быков). При игре
# против компьютера игрок вводит комбинации одну за другой, пока не отгадает
# всю последовательность. Ваша задача реализовать программу, против которой
# можно сыграть в "Быки и коровы"
# Пример:
# Загадано
# 2310
# Две коровы, один бык
# 3219
# Вы выиграли!

# pylint: disable=invalid-name

import random


def generate_secret_number():
    """
    Game with user.
    """
    digits = [str(i) for i in range(10)]
    random.shuffle(digits)
    return ''.join(digits[:4])


def check_guess(secret, guess):
    """
    Check the combination and return the number of cows and bulls.
    """
    bulls = 0
    cows = 0
    for n in range(4):
        if guess[n] == secret[n]:
            bulls += 1
        elif guess[n] in secret:
            cows += 1
    return bulls, cows


def main():
    """
    Game loop
    """
    secret_number = generate_secret_number()
    print("Я загадал 4-х значное число. Попробуйте отгадать его!")
    attempts = 0
    while True:
        guess = input("Введите вашу догадку: ")
        attempts += 1

        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) < 4:
            print("Введите 4-х значное число с неповторяющимися цифрами.")
            continue

        bulls, cows = check_guess(secret_number, guess)
        print(f"Быков: {bulls}, коров: {cows}")

        if bulls == 4:
            print(f"Вы отгадали число {secret_number} за {attempts} попыток.")
            break


main()

# Пирамида.
# Мы можем визуализировать художественную пирамиду ASCII с N уровнями,
# напечатав N рядов звездочек, где верхний ряд имеет одну звездочку в центре,
# а каждый последующий ряд имеет две дополнительные звездочки с каждой стороны.
# Вот как это выглядит, когда N равно 3.
#   *
#  ***
# *****
# Вот как это выглядит, когда N равно 5.
#     *
#    ***
#   *****
#  *******
# *********
# Необходимо написать программу, которая генерирует такую пирамиду пирамиду
# со значением N,равным 10.


def print_art_pyramid(n):
    """
    Pyramid seal.
    """
    for k in range(1, n+1):
        spaces = n - k
        print(" " * spaces, end="")
        print("*" * (2 * k - 1))


print_art_pyramid(10)


# Статуи.
# Вы получили в подарок на день рождения статуи разных размеров,
# каждая статуя имеет неотрицательный целочисленный размер. Поскольку Вам
# нравится доводить вещи до совершенства, то необходимо расположить их от
# меньшего к большему, чтобы каждая статуя была больше предыдущей ровно
# на 1. Для этого Вам могут понадобиться дополнительные статуи.
# Определите количество отсутствующих статуй.
# Пример:
# Для статуй = [6, 2, 3, 8] результат должен быть = 3. Иными словами,
# у Вас отсутствуют статуи размеров 4, 5 и 7.

def find_missing_statues(statues):
    """
    Finding the number of missing statues.
    """
    min_size = min(statues)
    max_size = max(statues)
    missing_count = max_size - min_size - len(statues) + 1
    return missing_count


quantity_statues = [6, 2, 3, 8]
result = find_missing_statues(quantity_statues)
print(result)
