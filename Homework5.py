#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))

def exponentiation(a, b):
    if b == 0:
        return 1
    if b < 0:
        return 1 / exponentiation(a, -b)
    return a * exponentiation(a, b - 1)

exp_nums = exponentiation(num_1, num_2)
print(f'A = {num_1}; B = {num_2} -> {exp_nums}')

#Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
"""
num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))

def sum_nums(a, b):
    if a == 0:
        return b
    return sum_nums(a - 1, b + 1)

if num_1 >= 0 and num_2 >= 0:
    print(f'Сумма элементов = {sum_nums(num_1, num_2)}')
else:
    print('Числа должны быть неотрицательными')
"""
