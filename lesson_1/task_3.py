# 3. По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки.

print('Ведите координаты для точки А: ')
x1 = int(input('\tx1: '))
y1 = int(input('\ty1: '))
print('Ведите координаты для точки B: ')
x2 = int(input('\tx2: '))
y2 = int(input('\ty2: '))

# Общее уравнение прямой : y = kx + b
k = (y1 - y2)/(x1 - x2)
b = y2 - k*x2
print(f'Уравнение прямой, проходящей через точки A и В: y = {k}x + {b}')
