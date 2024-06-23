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


def parse_molecule(formula):
    """
    Parses a chemical formula and returns a
    dictionary of the atoms and their counts.
    """
    formula = formula.replace(" ", "")
    pattern = r"([A-Z][a-z]*)([0-9]*)"
    matches = re.findall(pattern, formula)
    atoms = {}
    for match in matches:
        atom = match[0]
        count = int(match[1]) if match[1] else 1
        atoms[atom] = atoms.get(atom, 0) + count
    return atoms


formulas = ["H2O", "Mg(OH)2", "K4[ON(SO3)2]2"]
for formul in formulas:
    atomy = parse_molecule(formul)
    print(f"{formul} -> {atomy}")
