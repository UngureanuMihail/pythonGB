# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
from math import sqrt


def check_num_type(x):
    v = 2
    if 0 < x <= 100000:
        while v <= sqrt(x):
            if x % v == 0:  # until the remainder of the division is  0
                print("This number is composite")
                break
            v += 1  # plus 1 unit to v
        else:
            print("This number is prime")
    else:
        print('Error introduce number between 0 and 100000')
