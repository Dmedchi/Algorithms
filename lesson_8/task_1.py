# 1.Определение количества различных подстрок с использованием хеш-функции.
# Пусть дана строка S длиной N. Например, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib.
import hashlib

def s_subs(s, subs):
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()
    len_subs = len(subs)
    count = 0
    for i in range(len(s)):
        if h_subs == hashlib.sha1(s[i:i+len_subs].encode('utf-8')).hexdigest():
            count += 1
    return f'В строке "{s}" подстрока "{subs}" встречается {count} раз(a).'


s = input(('Строка: '))
subs = input(('Подстрока: '))

print(s_subs(s, subs))