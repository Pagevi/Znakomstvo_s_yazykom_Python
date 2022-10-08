# Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму

n = int(input('Введите число N: '))
sum = 0
lst = []

for i in range(1, n + 1):
    formula = (1 + (1 / i)) ** i
    sum = sum + formula
    lst.append(sum)
print(lst, 'сумма списка: ', round(sum, 2))