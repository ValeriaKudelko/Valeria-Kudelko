"""Writing Python Code."""

# !1.Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'.
first_user = 'www.my_site.com#about'.replace('#', '/')
print(first_user)


# !2.Напишите программу, которая добавляет ‘ing’ к словам.
s, v = "jump", "click"
d = s + 'ing', v + 'ing'
print(d)


# !3.В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou".
full_name = "Ivanou Ivan".split()
change_name = " ".join([full_name[1], full_name[0]])
print(change_name)


# !4.Напишите программу которая удаляет пробел в начале, в конце строки.
f_line = " one two three "
print(f_line.strip())


# !5.Имена собственные всегда начинаются с заглавной буквы, за которой
# следуют строчные буквы. Исправьте данное имя собственное так, чтобы
# оно соответствовало этому утверждению "pARiS" >> "Paris"
sity = "pARiS"
print(sity.capitalize())
