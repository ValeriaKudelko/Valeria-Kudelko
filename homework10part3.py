"""
Homework.
"""
# Декоратор типов
# Напишите декоратор, который проверял бы тип параметров функции,
# конвертировал их если надо и складывал:
# @typed(type=str)
# def add(a, b):
#     return a + b
# add("3", 5) -> "35"
# add(5, 5) -> "55"
# add('a', 'b') -> 'ab’

# @typed(type=int)
# def add(a, b, с):
#     return a + b + с
# add(5, 6, 7) -> 18

# @typed(type=float)
# def add(a, b, с):
#     return a + b + с
# add(0.1, 0.2, 0.4) -> 0.7000000000000001


from functools import wraps


def typed(type):
    """
    Called function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            args = list(map(lambda arg: convert_val(arg, type), args))
            kwargs = {
                key: convert_val(value, type) for key, value in kwargs.items()
                }
            return func(*args, **kwargs)
        return wrapper
    return decorator


def convert_val(value, type):
    """
    Change value to the specified type.
    """
    try:
        return type(value)
    except (ValueError, TypeError):
        return value


@typed(type=str)
def add(a, b):
    """
    Add the lines.
    """
    return a + b


assert add("3", 5) == "35"
assert add(5, 5) == "55"
assert add('a', 'b') == 'ab'


@typed(type=int)
def add_one(a, b, e):
    """
    Add numbers.
    """
    return a + b + e


assert add_one(5, 6, 7) == 18


@typed(type=float)
def add_two(a, b, f):
    """
    Add floating point numbers.
    """
    return a + b + f


assert add_two(0.1, 0.2, 0.4) == 0.7000000000000001
