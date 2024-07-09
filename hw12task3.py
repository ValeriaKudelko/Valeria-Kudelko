"""
Homework.
"""
# Из молекулы в атомы *
# Напишите программу, которая обрабатывает строку
# - формулу молекулы, возвращает атомы из этой молекулы
# и их количество в виде словаря.
# Примеры:
# H2O -> {H: 2, O: 1}
# Mg(OH)2 -> {Mg: 1, O: 2, H: 2}
# K4[ON(SO3)2]2 -> {K: 4, O: 14, N: 2, S: 4}
# Замечания:
# Скобки в формулах могут быть круглыми, квадратными и
# фигурными. Скобки могут быть вложены друг в друга.
# Индекс после скобки означает количество раз, которое
# повторяется каждый атом внутри скобок.Индекс после скобки
# не обязателен. Если его нет, значит содержимое скобок
# повторяется 1 раз.


import re


def parse_molecule(formula):  # noqa: C901
    """
    Parses a chemical formula string and returns a
    dictionary with atoms and their counts.
    """
    def multiply_dict(d, factor):
        return {atom: count * factor for atom, count in d.items()}

    def merge_dicts(d1, d2):
        result = d1.copy()
        for atom, count in d2.items():
            if atom in result:
                result[atom] += count
            else:
                result[atom] = count
        return result

    def parse_group(group):
        group_dict = {}
        for match in re.finditer(r'([A-Z][a-z]*)(\d*)', group):
            atom, count = match.groups()
            count = int(count) if count else 1
            group_dict[atom] = count
        return group_dict

    stack = []
    current_group = {}
    i = 0

    while i < len(formula):
        char = formula[i]
        if char in ('(', '[', '{'):
            stack.append(current_group)
            current_group = {}
            i += 1
        elif char in (')', ']', '}'):
            factor = int(formula[i + 1]) if i + 1 < len(formula) and formula[i + 1].isdigit() else 1  # noqa: 501
            current_group = multiply_dict(current_group, factor)
            prev_group = stack.pop()
            current_group = merge_dicts(prev_group, current_group)
            i += 2
        else:
            group_match = re.match(r'([A-Z][a-z]*)(\d*)', formula[i:])
            if group_match:
                atom, count = group_match.groups()
                count = int(count) if count else 1
                current_group[atom] = count
                i += len(group_match.group())
            else:
                raise ValueError(f"Invalid character at position {i}: {char}")

    return current_group


print(parse_molecule("H2O"))
print(parse_molecule("Mg(OH)2"))
print(parse_molecule("K4[ON(SO3)2]2"))
