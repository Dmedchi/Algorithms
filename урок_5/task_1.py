# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
#  Программа должна определить среднюю прибыль (за год для всех предприятий)
#  и вывести наименования предприятий, чья прибыль выше среднего
#  и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

companies = {}

num = int(input('Количество предприятий: '))
summa = 0
for i in range(num):
    name = input(f'Предприятие №{i + 1}: ')
    profit = int(input('Прибыль: '))
    companies[name] = profit
    summa += profit
print(companies)

average = summa / num
print(f'\nСредняя прибыль за год для всех предприятий: {round(average, 2)}')

good = {}
bad = {}
for key in companies:
    if companies[key] > average:
       good[key] = companies[key]
    else:
        bad[key] = companies[key]

print('\nПредприятия, чья прибыль выше среднего: ')
for key in good:
    print(f'{key} - {good[key]}')

print('\nПредприятия, чья прибыль ниже среднего: ')
for key in bad:
    print(f'{key} - {bad[key]}')