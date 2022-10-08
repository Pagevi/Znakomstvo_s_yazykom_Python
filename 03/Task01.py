# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import randint
lst = []
sum = 0

for i in range(randint(5, 10)):
    lst.append(randint(1, 100))
print(lst)

for i in range(len(lst)):
    if i % 2 == 1:
        sum += lst[i]
print(sum)