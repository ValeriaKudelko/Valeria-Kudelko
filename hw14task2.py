"""
Homework.
"""
# Инженерный калькулятор.
# Напишите программу - инженерный калькулятор.
# Передусмотрите возможные ошибки и обработайте их.
# ~ - это предложение ввода.
# Базовые требования:
# Программа считает простые математические выражения:
# ~ 5 + 4 9
# Программа ожидает от пользователя ввода математического
# выражения и правильно его трактует:
# ~ 10 - 3 + 1 8
# ~ 2 ** 3 - 1 7


def calculate_expression(expression):
    """
    Evaluates a mathematical expression.
    """
    try:
        result = eval(expression)  # pylint: disable=eval-used
        return result
    except ZeroDivisionError:
        return "Нельзя делить на ноль!"
    except TypeError:
        return f"Ошибка: {str}"


while True:
    user_input = input("~ ")
    if user_input.lower() == "q":
        break
    print(calculate_expression(user_input))
