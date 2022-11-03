import logger as log


def calculator(a, b):
    point = input('\tВведите знак: ')
    if point == '+':
        result = a + b
        print(result)
        log.logger(f'{a}+{b}={result}')
    elif point == '-':
        result = a - b
        print(result)
        log.logger(f'{a}-{b}={result}')
    elif point == '*':
        result = a * b
        print(result)
        log.logger(f'{a}*{b}={result}')
    elif point == '/':
        if b == 0:
            print('На 0 делить нельзя')
        else:
            result = a / b
            print(result)
            log.logger(f'{a}/{b}={result}')
