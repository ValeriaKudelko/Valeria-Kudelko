"""Writing Python Code."""

# !1.Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'.
Sq = 'www.my_site.com#about'.replace('#', '/')
print(Sq)


# !2.Напишите программу, которая добавляет ‘ing’ к словам.
s, v = "jump", "click"
d = s + 'ing', v + 'ing'
print(d)


# !3.В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou".
full_name = "Ivanou Ivan".split()
k_2 = " ".join([full_name[1], full_name[0]])
print(k_2)


# !4.Напишите программу которая удаляет пробел в начале, в конце строки.
Tr_1 = " one two three "
print(Tr_1.strip())


# !5.Имена собственные всегда начинаются с заглавной буквы, за которой
# следуют строчные буквы. Исправьте данное имя собственное так, чтобы
# оно соответствовало этому утверждению "pARiS" >> "Paris"
c_2 = "pARiS"
print(c_2.capitalize())
