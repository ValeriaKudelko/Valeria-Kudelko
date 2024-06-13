"""
Homework.
"""
# Положительные аргументы функции
# Напишите декоратор @validate_arguments, который проверяет, что все
# аргументы функции являются положительными числами. Если встречается
# аргумент, не соответствующий этому условию, функция должна вывести
# сообщение об ошибке. Вот некоторые подсказки:
# Внутри декоратора, используйте цикл for для перебора аргументов функции.
# Используйте оператор if для проверки, является ли аргумент
# положительным числом.
# Если аргумент не соответствует условию, используйте оператор raise
# для вызова исключения ValueError.


from functools import wraps


def validate_arguments(func):
    """
    Checking conditions for positive numbers.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(f"{arg} не положительное число")
        return func(*args, **kwargs)
    return wrapper


@validate_arguments
def sum_numbers(a, b):
    """
    Sum of two numbers.
    """
    return a + b


assert sum_numbers(1, 2)
assert sum_numbers(1.5, 2.5)
assert sum_numbers(-1, 2)  # ValueError
