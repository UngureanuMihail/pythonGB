# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.  Дано a, b, c -
# стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух
# других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не
# существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.


# introduction of values
a = input('Introduce your first value a = ')
b = input('Introduce your second value b = ')
c = input('Introduce your third value c = ')

# logic control
if (a + b) > c and (a + c) > c and (b + c) > a:  # control if conditions are satisfacted
    print('This triangle can be real')
else:  # in other case message will be that is imposible to create that triangle
    print('Triangle is imposible to create')


# Function that help us to know that type of triangle is presented by knowing the sides lenght.
def triangle_type(a, b, c):
    if a == b == c:
        print('This is equilateral triangle')
    elif a == b or b == c or a == c:
        print('This is isosceles triangle')
    else:
        print('This is scalene triangle')
