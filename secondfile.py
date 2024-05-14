"""Writing Python Code."""

# 1.Перевести строку в список "Robin Singh" => ["Robin”, “Singh"].
zu1 = ["Robin Singh"]
print(zu1)


# !2."I love arrays they are my favorite" => ["I", "love", "arrays",
# "they", "are", "my", "favorite"].
big_line1 = "I love arrays they are my favorite"
print(big_line1)
arr1 = big_line1.split()
print(arr1)


# !3.Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”.
name = ["Ivan", "Ivanou"]
print(name)
locations = "Minsk", "Belarus"
print(locations)
status = "Привет, {} {}! Добро пожаловать в {} {}".format(*name, *locations)
print(status)


# !4.Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку =>
# "I love arrays they are my favorite".
ml1 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(ml1)
any_ml = " ".join(ml1)
print(any_ml)


# !5.Создайте список из 10 элементов, вставьте на 3-ю позицию новое
# значение, удалите элемент из списка под индексом 6.
kt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
kt[2] = 8
print(kt)
del kt[6]
print(kt)
