"""Homework."""
# Строки с заданным символом.
# Напишите программу, которая бы работала следующим образом
# - находила символ "#" и если этот символ найден - удаляла
# предыдущий символ из строки. Ваша задача обработать строки с "#" символом.
# Примеры:
# "a#bc#d" ==>  "bd"
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""


def delete_character(string):
    """
    Removes the previous character if the current character is "#".
    """
    result = []
    assert (result) != 0
    for i in string:
        if i == "#" and result:
            result.pop()
        else:
            result.append(i)
    return "".join(result)


assert delete_character("a#bc#d")  # True
assert delete_character("abc#d##c")  # True
# assert delete_character("abc##d######")  # AssertionError
assert delete_character("#######")  # True
# assert delete_character("")  # AssertionError
