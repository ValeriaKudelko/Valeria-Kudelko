"""Writing Python Code."""

# pylint: disable=invalid-name

# !1.Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'.
line1 = 'www.my_site.com#about'.replace('#', '/')
print(line1)


# !2.Напишите программу, которая добавляет ‘ing’ к словам.
s, v = "jump", "click"
d = s + 'ing', v + 'ing'
print(d)


# !3.В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou".
full_name = "Ivanou Ivan".split()
last_name = " ".join([full_name[1], full_name[0]])
print(last_name)


# !4.Напишите программу которая удаляет пробел в начале, в конце строки.
withoutSpaces = " one two three "
print(withoutSpaces.strip())


# !5.Имена собственные всегда начинаются с заглавной буквы, за которой
# следуют строчные буквы. Исправьте данное имя собственное так, чтобы
# оно соответствовало этому утверждению "pARiS" >> "Paris"
proper_name = "pARiS"
print(proper_name.capitalize())
