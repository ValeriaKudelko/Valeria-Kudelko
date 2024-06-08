"""
Homework.
"""
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
