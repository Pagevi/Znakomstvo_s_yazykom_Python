# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

x1 = int(input('Введите X первой точки: '))
y1 = int(input('Введите Y первой точки: '))

x2 = int(input('Введите X второй точки: '))
y2 = int(input('Введите Y второй точки: '))


result = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
print(round(result, 2))