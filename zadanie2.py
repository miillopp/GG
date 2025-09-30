import math
print("Введите координаты трех вершин треугольника:")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
x3 = float(input("x3 = "))
y3 = float(input("y3 = "))

# Вычисляем длины сторон
a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

perimeter = (a + b + c)

# Площадь через полупериметр
s = perimeter / 2
S = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"Координаты вершин: ({x1},{y1}), ({x2},{y2}), ({x3},{y3})")
print(f"Периметр: {perimeter:.2f}")
print(f"Площадь: {S:.2f}")
