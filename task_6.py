# Пользователь вводит номер буквы в алфавите.
# Определить, какая это буква.

number = int(input('Введите номер буквы в алфавите: '))

if 1 <= number <= 26:
    a = ord('a')
    place_letter = (a + number) - 1
    letter = chr(place_letter)
    print(f'Это буква: {letter}')
else:
    print('Неверный ввод.')
