# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def check_num_type(x):
    v = 2
    if x % v != 0:  # until the remainder of the division is not 0
        v += 1  # plus 1 unit to v
    if v == x:  # in case if v number is equal by checked one this number prime
        print('This number is prime')
    else:
        print('This number is composite')  # in other case this is composite number


check_num_type(4)  # composite number test
check_num_type(2)  # prime number test
