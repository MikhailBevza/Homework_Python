# Задача 2: Найдите сумму цифр трехзначного числа.
"""
num1 = int(input('Введите трехзначное число: '))
if num1 > 99 and num1 < 1000:
    sum = 0
    while num1 != 0:
        sum += num1 % 10
        num1 //= 10
    print('Сумма цифр =', sum)
else:
    print('Число должно быть трехзначным.')
"""

# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
"""
num1 = int(input('Введите количество журавликов: '))

if num1 % 6 == 0:
    amount_Petya = num1 // 6
    amount_Seryozha = amount_Petya
    amount_Katya = (amount_Petya + amount_Seryozha) * 2
    print('Петя', amount_Petya, ', Катя', amount_Katya, ', Сережа', amount_Seryozha)
else:
    print('Задача не имеет решения')
"""

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

num1 = int(input('Введите номер билета: '))

if num1 > 99999 and num1 < 1000000:
    first_part_ticket = num1 // 1000
    second_part_ticket = num1 % 1000
    first_sum = 0
    second_sum = 0
    while first_part_ticket != 0:
        first_sum += first_part_ticket % 10
        first_part_ticket //= 10
    while second_part_ticket != 0:
        second_sum += second_part_ticket % 10
        second_part_ticket //= 10
    if first_sum == second_sum:
        print('Билет счастливый!')
    else:
        print('Билет несчастливый')
else:
    print('Номер билета некорректный')
