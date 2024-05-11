#!1.Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'.

a = 'www.my_site.com#about'
b = a.replace('#','/')
print(b)


#!2.Напишите программу, которая добавляет ‘ing’ к словам.

s, v = "jump", "click"
d = s +'ing', v + 'ing'
print(d)


#!3.В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou".

k = "Ivanou Ivan".split()
k[0], k[1] = k[1], k[0]
new_k = " ".join(k)
print(new_k)

             
#!4.Напишите программу которая удаляет пробел в начале, в конце строки.

pul = " one two three "
print(pul.lstrip())
print(pul.rstrip())


#!5.Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы. 
#Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению "pARiS" >> "Paris"

y = "pARiS"
print(y.capitalize())
