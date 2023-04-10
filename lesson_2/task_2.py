# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
def fraction_summ(n1, n2):
    great = 0
    for i in range(1, int(min(n1, n2)) + 1):
        if n1 % i == 0 and n2 % i == 0:
            great = i
    return great


# первая дробь
num1, den1 = map(int, list(input("Введите числитель и знаменатель через пробел: ").split(" ")))

# вторая дроб
num2, den2 = map(int, list(input("Введите числитель и знаменатель через пробел: ").split(" ")))

last = (den1 * den2) // fraction_summ(den1, den2)

_sum = (num1 * last // den1) + (num2 * last // den2)

num3 = _sum // fraction_summ(_sum, last)

last = last // fraction_summ(_sum, last)

print(num1, "/", den1, " + ", num2, "/", den2, " = ", num3, "/", last)
