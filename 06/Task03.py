# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

lst = [x for x in range(10)]

odd = list(filter(lambda x: x % 2 != 0, lst))
print(odd, sum(odd))
