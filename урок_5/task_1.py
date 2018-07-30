# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
#  Программа должна определить среднюю прибыль (за год для всех предприятий)
#  и вывести наименования предприятий, чья прибыль выше среднего
#  и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

companies = {}

num = int(input('Количество предприятий: '))
summa = 0
# name = []
for i in range(num):
    s = 0
    profit = 0
    name = input(f'Предприятие №{i + 1}: ')
    # name.append(nm)
    count = 1
    while count < 5:
        prft = int(input(f'Прибыль за {count} квартал: '))
        profit += prft
        count += 1
    companies[name] = profit
    s += profit
    print(f'Итого за год: {s}')

for key in companies:
    summa += companies[key]

average = summa / num
print(f'Средняя прибыль за год для всех предприятий: {round(average, 2)}')

good = {}
bad = {}
for key in companies:
    if companies[key] > average:
       good[key] = companies[key]
    else:
        bad[key] = companies[key]

print('Предприятия, чья прибыль выше среднего: ')
for key in good:
    print(f'{key} - {good[key]}')

print('Предприятия, чья прибыль ниже среднего: ')
for key in bad:
    print(f'{key} - {bad[key]}')