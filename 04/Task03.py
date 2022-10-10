# Задайте последовательность чисел.
# Напишите программу,которая выведет список неповторяющихся элементов исходной последовательности.

import random

lst1 = []
for i in range(10):
    lst1.append(random.randint(1, 10))
print(lst1)

lst2 = []
for i in lst1:
    if lst1.count(i) == 1:
        lst2.append(i)
print(lst2)
