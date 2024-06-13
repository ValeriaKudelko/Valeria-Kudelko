"""
Homework.
"""
# Вернуть число
# Создайте декоратор, который проверяет, является ли результат функции
# числом и выводит сообщение об ошибке, если это не так. Вот некоторые
# подсказки:
# Внутри декоратора, после вызова функции, проверьте тип результата с
# помощью функции isinstance().
# Если тип не является числом, выведите сообщение об ошибке с помощью
# функции print().


from functools import wraps


def check_numeric_result(func):
    """
    Сhecks whether the function result is number.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, (int, float)):
            print(f"Ошибка: {result} не является числом.")
        return result
    return wrapper


@check_numeric_result
def add_numbers(a, b):
    """
    Checking the result.
    """
    return a + b


assert add_numbers(1, 2)
assert add_numbers(1.5, 2.5)
assert add_numbers("a", "b")
