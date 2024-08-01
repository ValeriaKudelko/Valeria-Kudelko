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


def engineering_calculator(expression):
    """
    Calculate a mathematical expression.
    """
    try:
        tokens = expression.split()
        numbers = []
        operators = []
        for token in tokens:
            if token.isdigit():
                numbers.append(int(token))
            elif token in ['+', '-', '*', '/', '**', '^']:
                operators.append(token)
            else:
                raise ValueError("Invalid token")

        i = 0
        while i < len(operators):
            if operators[i] in ['*', '**', '^']:
                if operators[i] == '*':
                    numbers[i] *= numbers[i + 1]
                elif operators[i] == '**' or operators[i] == '^':
                    numbers[i] **= numbers[i + 1]
                del numbers[i + 1]
                del operators[i]
            else:
                i += 1

        i = 0
        while i < len(operators):
            if operators[i] == '/':
                if numbers[i + 1] == 0:
                    raise ZeroDivisionError("Division by zero")
                numbers[i] /= numbers[i + 1]
                del numbers[i + 1]
                del operators[i]
            else:
                i += 1

        result = numbers[0]
        for num, op in zip(numbers[1:], operators):
            if op == '+':
                result += num
            elif op == '-':
                result -= num
        return result
    except ZeroDivisionError as e:
        return str(e)
    except ValueError as e:
        return str(e)


while True:
    user_input = input("~ ")
    if user_input.lower() == "exit":
        break

    conclusion = engineering_calculator(user_input)
    print(conclusion)
