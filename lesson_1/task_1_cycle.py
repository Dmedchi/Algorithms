# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

n = int(input('Введите трехзначное число: '))
if 99 < n < 1000:
    summa = 0
    mult = 1
    while n > 0:
        summa += n % 10
        mult *= n % 10
        n = n // 10
    print(f'Сумма: {summa}')
    print(f'Произведение: {mult}')
else:
    print('Неверный ввод.')

