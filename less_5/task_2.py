# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например:
# пользователь ввёл A2 и C4F
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

x = input('Число №1: ')
y = input('Число №2: ')

x2 = int(x, 16)
y2 = int(y, 16)

summa = x2 + y2
mult = x2 * y2

summa2 = format(summa, 'x')
mult2 = format(mult, 'x')

print(f'сумма: {summa2} - {list(summa2)}\n'
      f'произведение: {mult2} - {list(mult2)}')


