# 9.Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

numbers = []

while True:
    num = int(input('>> '))
    if num == 0:
        break
    numbers.append(num)

num_max = 0
sum_max = 0

for num in numbers:
    mx = num
    s = 0
    while num > 0:
        s += num % 10
        num = num // 10
    if s > sum_max:
        sum_max = s
        num_max = mx

print(f'число {num_max} имеет наибольшую сумму: {sum_max}')


