"""
Homework
"""
# Последовательность.
# Дана последовательность целых чисел в виде массива. Определите,
# можно ли получить строго возрастающую последовательность, удалив
# из массива не более одного элемента.
# Примечание: последовательность a0, a1, ..., an считается строго возрастающей,
# если a0 < a1 < ... < an. Последовательность, содержащая только один элемент,
# также считается строго возрастающей.
# Примеры
# Для последовательности = [1, 3, 2, 1], вывод должен быть решение = False.
# В этом массиве нет ни одного элемента, который можно было бы удалить,
# чтобы получить строго возрастающую последовательность.
# Для последовательности = [1, 3, 2] вывод должен быть = True.
# Вы можете удалить 3 из массива, чтобы получить строго возрастающую
# последовательность [1, 2]. Альтернативно можно убрать 2, чтобы получить
# строго возрастающую последовательность [1, 3].
# solution([1, 2, 3])
# solution([1, 2, 1, 2])
# solution([1, 3, 2, 1])
# solution([1, 2, 3, 4, 5, 3, 5, 6])
# solution([40, 50, 60, 10, 20, 30])

# pylint: disable=invalid-name


def solution(nums):
    """
    Checks whether a strictly increasing sequence can be obtained,
    removing at most one element from the array.
    """
    def is_increasing(nums):
        """
        Is the array of numbers increasing.
        """
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                return False
        return True

    for i in range(len(nums)):
        temp = nums[:i] + nums[i+1:]
        if is_increasing(temp):
            return True
    return False


print(solution([1, 2, 3]))
print(solution([1, 2, 1, 2]))
print(solution([1, 3, 2, 1]))
print(solution([1, 2, 3, 4, 5, 3, 5, 6]))
print(solution([40, 50, 60, 10, 20, 30]))


# Число напротив.
# Рассмотрим целые числа от 0 до n-1, записанные по окружности так,
# чтобы расстояние между любыми двумя соседними числами было одинаковым
# (обратите внимание, что 0 и n-1 тоже являются соседними).Учитывая n и
# first_number, найдите число, которое написано в радиально противоположной
# позиции от first_number. Вывести результат на экран.
# Примеры
# Для n = 10 и first_number = 2 вывод должен быть (n, first_number) = 7.

n = 10
first_number = 2
opposite_number = (first_number + n // 2) % n
print(opposite_number)


# Validate.
# Ваша задача написать программу, принимающее число - номер кредитной
# карты(число может быть четным или не четным). И проверяющей может ли
# такая карта существовать. Предусмотреть защиту от ввода букв, пустой
# строки и т.д. Примечания Алгоритм Луна.
# Примеры
# validate(4561261212345464) #=> False
# validate(4561261212345467) #=> True


def is_valid_credit_card(card_number):
    """
    Is the credit card number valid with
    using the Luhn algorithm.
    """
    if not card_number:
        return False
    try:
        card_number = int(card_number)
        if card_number <= 0:
            return False
    except ValueError:
        return False

    digits = [int(digit) for digit in str(card_number)]
    al = sum(digits[-1::-2] + [sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    return al % 10 == 0


number_from_the_card = input("Введите номер кредитной карты: ")
if is_valid_credit_card(number_from_the_card):
    print("Номер карты соответствует.")
else:
    print("Номер карты не соответствует.")
