n = int(input('Введите число N: '))
i = 0
sum = 0
lst = []

while i <= n - 1:
    i = i + 1
    formula = (1 + (1 / i)) ** i
    sum = sum + formula
    lst.append(sum)
print(lst, 'сумма списка', round(sum, 2))