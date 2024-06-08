"""
Homework.
"""
# Подсчет количества букв.
# На вход подается строка, например, "cccbba" результат работы программы -
# строка “c3b2a".
# Примеры для проверки работоспособности:
# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"


def letter_counting(string_one: str) -> str:
    """
    Counting duplicate characters.
    """
    result_one = []
    count = 1
    for k in range(1, len(string_one) + 1):
        if k < len(string_one) and string_one[k] == string_one[k - 1]:
            count += 1
        else:
            if count > 1:
                result_one.append(string_one[k - 1] + str(count))
            else:
                result_one.append(string_one[k - 1])
            count = 1
    return ''.join(result_one)


assert letter_counting("cccbba") == "c3b2a"
assert letter_counting("abeehhhhhccced") == "abe2h5c3ed"
assert letter_counting("aaabbceedd") == "a3b2ce2d2"
assert letter_counting("abcde") == "abcde"
assert letter_counting("aaabbdefffff") == "a3b2def5"
