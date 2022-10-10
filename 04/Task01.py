# Вычислить число c заданной точностью d
# Пример: при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

d = float(input('Введите чилсо d: '))
a = math.pi
b = int(a / d)
c = float(b * d)
print(f'{c}')
