"""Writing Python Code."""

# 1.Перевести строку в список "Robin Singh" => ["Robin”, “Singh"].
zu1 = []
zu1 = list("Robin Singh")
print(zu1)
arr = "Robin Singh".split()
print(arr)


# !2."I love arrays they are my favorite" => ["I", "love", "arrays",
# "they", "are", "my", "favorite"].
convert_text = "I love arrays they are my favorite"
print(convert_text)
arr1 = convert_text.split()
print(arr1)


# !3.Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”.
name = ["Ivan", "Ivanou"]
print(name)
locations = "Minsk", "Belarus"
print(locations)
text_printing = "Привет, {} {}! Добро пожаловать в {} {}".format(*name, *locations)
print(text_printing)


# !4.Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку =>
# "I love arrays they are my favorite".
ml1 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(ml1)
make_with_line = " ".join(ml1)
print(make_with_line)


# !5.Создайте список из 10 элементов, вставьте на 3-ю позицию новое
# значение, удалите элемент из списка под индексом 6.
kt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
kt[2] = 8
print(kt)
del kt[6]
print(kt)
