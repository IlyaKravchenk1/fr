#случайное целое число;

import random

a = int(input('Введите начало диапазона\n'))
b = int(input('Введите конец диапазона\n'))

print(f"Случайное число из выбранного вами диапазона = {random.randint(a, b)}")

# случайное вещественное число;

a = float(a)
b = float(b)
num = random.uniform(a, b)

print(f"Случайное вещественное число из выбранного вами диапазона = {format(num, '.3f')}")