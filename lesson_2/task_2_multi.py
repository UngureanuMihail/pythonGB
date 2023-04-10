# произведение* дробей

num1, den1 = map(int, list(input("Введите числитель и знаменатель через пробел: ").split(" ")))

# вторая дробь
num2, den2 = map(int, list(input("Введите числитель и знаменатель через пробел: ").split(" ")))

top_mult = num1 * num2
bot_mult = den1 * den2

print(num1, "/", den1, " * ", num2, "/", den2, " = ", top_mult, "/", bot_mult)

