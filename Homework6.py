# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
"""
first_element = int(input('Введите первый элемент: '))
diff_elements = int(input('Введите разность элементов: '))
quantity_elements = int(input('Введите количество элементов: '))

array_nums = [first_element]

for i in range(1, quantity_elements):
    array_nums.append(array_nums[i - 1] + diff_elements)
print(array_nums)
"""

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
import random

quantity_elements = int(input('Введите количество элементов: '))
max_num = int(input('Введите максимальный элемент: '))
min_num = int(input('Введите минимальный элемент: '))

array_nums = [random.randint(-10, 10) for i in range(quantity_elements)]
print(array_nums)
count = 0
for i in range(len(array_nums)):
    if array_nums[i] >= min_num and array_nums[i] <= max_num:
        count += 1
        print(i, end = ' ') 
if count == 0:
    print('Нет чисел, который принадлежат заданному диапазону')
