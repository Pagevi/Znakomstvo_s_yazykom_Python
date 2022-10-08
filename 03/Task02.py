#  Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint

lst_size = int(input('Введите кол-во чисел в списке: '))
lst = []

for i in range(lst_size):
    lst.append(randint(1, 10))
print(lst)

ln = len(lst)
for i in range(ln):
    if i >= ln / 2:
        break
    print((lst[i] * lst[- i - 1]), end=' ')

