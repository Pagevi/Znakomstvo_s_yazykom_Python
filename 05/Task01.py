# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

n = 2021
while n > 28:
    a = int(input('Игрок 1 взял конфет:'))
    if a > 28:
        print('Превышен лимит конфет за один ход. Игрок 1 берет заново')
    else:
        result = n - a
        print(result)
        if result <= 28:
            print('Игрок 2 победил')
            break
        b = int(input('Игрок 2 взял конфет:'))
        if b > 28:
            print('Превышен лимит конфет за один ход. Игрок 2 берет заново')
            b = int(input('Игрок 2 взял конфет:'))
            result = result - b
            n = result
            print(result)
        else:
            result = result - b
            n = result
            print(result)
            if result <= 28:
                print('Игрок 1 победил')
                break