"""Writing Python Code."""

# !1.Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'.
ann1 = 'www.my_site.com#about'.replace('#', '/')
print(ann1)


# !2.Напишите программу, которая добавляет ‘ing’ к словам.
s, v = "jump", "click"
d = s + 'ing', v + 'ing'
print(d)


# !3.В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou".
k = "Ivanou Ivan".split()
newk = " ".join([k[1], k[0]])
print(newk)


# !4.Напишите программу которая удаляет пробел в начале, в конце строки.
pe1 = " one two three "
print(pe1.strip())


# !5.Имена собственные всегда начинаются с заглавной буквы, за которой
#следуют строчные буквы. Исправьте данное имя собственное так, чтобы
#оно соответствовало этому утверждению "pARiS" >> "Paris"
cit = "pARiS"
print(cit.capitalize())
