"""
Homework.
"""
# Files.
# Напишите программу, которая создает текстовый
# файл(если его нету) "students.txt". Запишите в файл
# список студентов, номер группы, их оценки. Каждый
# студент на новой строке. Откройте файл и прочитайте всю
# информацию из него. Напечатайте общее количество студентов,
# количество студентов для каждой группы и среднюю оценку для
# каждой группы. Допишите эту информацию в конец файла.
# Передусмотрите возможные ошибки и обработайте их.


try:
    with open("students.txt", "w") as file:
        file.write("Иван Иванов,1,9\n")
        file.write("Евгений Евгеньев,2,8\n")
        file.write("Олег Олегов,1,5\n")
        file.write("Павел Павлов,2,8\n")
        file.write("Александр Александров,3,2\n")
        file.write("Юрий Юрьев,3,8\n")

    with open("students.txt", "r") as file:
        lines = file.readlines()
        total_students = 0
        group_counts: dict[str, float] = {}
        group_averages: dict[str, float] = {}
        for line in lines:
            name, group, grade = line.split(",")
            total_students += 1
            group_counts[group] = group_counts.get(group, 0) + 1
            group_averages[group] = group_averages.get(group, 0) + int(grade)
        for group, count in group_counts.items():
            group_averages[group] /= count

        with open("students.txt", "a", encoding="utf-8") as file:
            file.write("\n")
            file.write(f"Всего студентов: {total_students}\n")
            for group, count in group_counts.items():
                file.write(f"Группа {group}: {count} студентов, средний балл: {group_averages[group]:.2f}\n")  # noqa: E501
except FileNotFoundError:
    print("Файл students.txt не найден.")
except PermissionError:
    print("Нет разрешения на запись файла students.txt.")
except ValueError:
    print("Одна из строк в файле students.txt недействительна.")
finally:
    if file:
        file.close()
