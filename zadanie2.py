from math import *
print("Введите координаты трех вершин треугольника:")
x1, y1 = map(float, input("Введите любые 2 числа через пробел: ").split())
x2, y2 = map(float, input("Введите любые 2 числа через пробел: ").split())
x3, y3 = map(float, input("Введите любые 2 числа через пробел: ").split())

# Вычисляем длины сторон
a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
b = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
c = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

perimeter = (a + b + c)

# Площадь через полупериметр
s = perimeter / 2
S = sqrt(s * (s - a) * (s - b) * (s - c))

print(f"Координаты вершин: ({x1},{y1}), ({x2},{y2}), ({x3},{y3})")
print(f"Периметр: {perimeter:.2f}")
print(f"Площадь: {S:.2f}")
