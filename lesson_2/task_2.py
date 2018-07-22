# 2.Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


number = list(input('>> '))

even_numbers = []
odd_numbers = []

for i in number:
    if int(i) % 2 == 0:
        even_numbers.append(int(i))
    else:
        odd_numbers.append(int(i))

print(f'Четные цифры {len(even_numbers)}: {even_numbers}')
print(f'Нечетные цифры {len(odd_numbers)}: {odd_numbers}')