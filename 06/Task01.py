# Написать программу, которая будет принимать на вход число N и выводить числа от -N до N.

n = int(input('Введите число n: '))

lst = list(i for i in range(-n, n + 1))
print(lst)