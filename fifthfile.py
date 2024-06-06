"""
Homework.
"""
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
    for i in string:
        if i == "#" and result:
            result.pop()
        else:
            result.append(i)
    return "".join(result)


print(delete_character("a#bc#d"))
print(delete_character("abc#d##c"))
print(delete_character("abc##d######"))
print(delete_character("#######"))
print(delete_character(""))


# Свечи.
# Когда свеча догорает, остается остаток. Остатки можно объединить, чтобы
# создать новую свечу, которая при догорании, в свою очередь, оставит еще
# один остаток. У вас есть количество свечей. Какое общее количество свечей
# вы можете сжечь, если предположить, что вы создадите новые свечи, как только
# у вас останется достаточно остатков?
# Пример Если у Вас 5(candles_number) свечей, и из 2х(make_new) остатков вы
# можете сделать 1 новую свечу, то ответе будет: 9.
# По шагам, чтобы сжечь 9 свечей:
# сожгите 5 свечей, получите 5 остатков;
# создайте еще 2 свечи, используя 4 остатка (остался 1);
# сожгите 2 свечи, в итоге останется 3 остатка;
# создайте еще одну свечу, используя 2 остатка (остался 1);
# сожгите созданную свечу, что даст еще один остаток (всего 2 остатка);
# создать свечу из оставшихся остатков;
# зажгите последнюю свечу.
# Таким образом, можно сжечь 5+2+1+1=9 свечей, что и является ответом.
# Проверка работоспособности:
# assert solution(5, 2) == 9
# assert solution(1, 2) == 1
# assert solution(15, 5) == 18
# assert solution(12, 2) == 23
# assert solution(6, 4) == 7
# assert solution(13, 5) == 16
# assert solution(2, 3) == 2


def solution(candles_number: int, make_new: int) -> int:
    """
    Calculates the total number of candles that can
    be burned by combining the remainder.
    """
    total_number_of_candles = candles_number
    remaining = candles_number
    while remaining >= make_new:
        new_candles = remaining // make_new
        total_number_of_candles += new_candles
        remaining = remaining % make_new + new_candles
    return total_number_of_candles


assert solution(5, 2) == 9  # True
assert solution(1, 2) == 1  # True
assert solution(15, 5) == 18  # True
assert solution(12, 2) == 23  # True
assert solution(6, 4) == 7  # True
assert solution(13, 5) == 16  # True
assert solution(2, 3) == 2  # True


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


# Example: "abcde" == "abcde"
string_exam = "abcde"  # pylint: disable=C0103
conclusion = letter_counting(string_exam)  # pylint: disable=C0103
print(f"'{string_exam}' == '{conclusion}'")  # pylint: disable=C0103
