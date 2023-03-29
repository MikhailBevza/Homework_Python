# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 1

# 1 2 1 2 2
# Вывод: 2
"""
import random
amount_of_elements = int(input('Введите количество элементов: '))

number = int(input('Введите число, которое необходимо проверить: '))

array_nums = [random.randint(1, amount_of_elements / 2) for i in range(amount_of_elements)]
print(array_nums)
"""

# count = 0
# for i in range(len(array_nums)):
#     if array_nums[i] == number:
#         count += 1
# if count != 0:
#     print(f'Число встречается {count} раз')
# else:
#     print('Такого числа нет')
"""
counter = array_nums.count(number)
if counter != 0:
    print(f'Число встречается {counter} раз')
else:
    print('Такого числа нет')
"""



