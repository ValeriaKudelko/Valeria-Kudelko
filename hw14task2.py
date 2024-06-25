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


def engineering_calculator():
    """
    Calculate a mathematical expression.
    """
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '**': lambda x, y: x ** y
    }
    while True:
        try:
            user_input = input("~ ")
            if user_input.lower() == "exit":
                break
            tokens = user_input.split()
            if len(tokens) < 3 or len(tokens) % 2 == 0:
                raise ValueError("Invalid input")
            result = float(tokens[0])
            for i in range(1, len(tokens) - 1, 2):
                operator = tokens[i]
                operand = float(tokens[i + 1])
                if operator not in operators:
                    raise ValueError("Unknown operator")
                result = operators[operator](result, operand)
            print(f"{result}\n")
        except ValueError as e:
            print(f"Error: {e}\n")
        except ZeroDivisionError:
            print("Division by zero is not allowed.\n")


engineering_calculator()
