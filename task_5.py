# 5. Пользователь вводит две буквы.
# Определить:
# - на каких местах алфавита они стоят
# - сколько между ними находится букв.

first_letter = input('1-ая буква: ')
second_letter = input('2-ая буква: ')

first = ord(first_letter)
second = ord(second_letter)
a = ord('a')

place_first = (first - a) + 1
place_second = (second - a) + 1
num_letters = abs(place_first - place_second) - 1

print(f'Позиция буквы {first_letter}: {place_first}\n'
      f'Позиция буквы {second_letter}: {place_second}\n'
      f'Между ними букв: {num_letters}')


