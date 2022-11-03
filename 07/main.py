import controller as c

print('Выберите тип калькулятора:\n\t 1.Рациональный\n\t 2.Комплексный\n')

calc = input('Тип калькулятора № ')
if calc == '1':
    c.button_click_rac()

if calc == '2':
    c.button_click_complex()
1