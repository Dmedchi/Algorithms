# Написать программу, которая генерирует в указанных пользователем границах:
# - случайное целое число;
# - случайное вещественное число
# - случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

answer = int(input('Нажмите соответствующую цифру для выбранной команды:\n'
                   '1 -  сгенерировать случайное целое число\n'
                   '2 - сгенерировать случайный символ\n'
                   '>> '))
if answer == 1:
    first = int(input('1 целое число: '))
    second = int(input('2 целое число: '))
    number = random.randint(first, second)
    print(f'Cлучайное целое число: {number}')

if answer == 2:
    one = input('Введите 1 символ  от "а" до "z": ')
    two = input('Введите символ  от "а" до "z": ')
    one = ord(one)
    two = ord(two)
    symbol = random.randint(one, two)
    symbol = chr(symbol)
    print(f'Cлучайный символ: {symbol}')


