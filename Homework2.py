# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random


number_of_coins = int(input('Введите количество монет: '))
coins = list()
count_0 = 0
count_1 = 0

for i in range(number_of_coins):
    coins.append(random.randint(0, 1))
print(coins)

for i in range(number_of_coins):
    if coins[i] == 0:
        count_0 += 1
    else:
        count_1 += 1

if count_1 == 0 or count_0 == 0:
    print('Монетки переворачивать не нужно')
elif count_0 <= count_1:
    print(f'Необходимо перевернуть {count_0} монетки')
else:
    print(f'Необходимо перевернуть {count_1} монетки')

