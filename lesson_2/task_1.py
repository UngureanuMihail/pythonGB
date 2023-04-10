# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление
def int_to_hex(num):
    digits = "0123456789abcdef"
    x = (num % 16)
    rest = num // 16
    if rest == 0:
        return digits[x]
    return int_to_hex(rest) + digits[x]
