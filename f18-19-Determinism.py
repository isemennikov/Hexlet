# Variable Parameter Functions

# max(1, 10, 9, 4)  # 10

# print(max)

# LABS
# Calculate programmatically (and not in your head) the minimum number among 3, 10, 22, -3, 0 -
# and display it on the screen. Use the min() function, which works similar to max().

# print(min(3, 10, 22, -3, 0))

# L 19 Determinism
# LABS
# Task :В коде подключена функция random(). Она возвращает случайное число от 0 до 1 с большим количеством знаков
# после запятой. Но в реальных задачах бывает нужно получать случайные целые числа в заданном диапазоне.
#
# Реализуйте код, который печатает на экран случайное число в диапазоне от 1 до 10 включительно.
# Для этого вам понадобятся операции умножения, сложения, а также преобразование типов. random() возвращает float,
# а нам нужен int.
#
# Попробуйте решить это задание в одну строку.
#
# Подсказка
# random() возвращает число в диапазоне [0, 1). Такая запись обозначает, что 0 включается в диапазон, а 1 – нет.

from random import random

# number = (random()  * 7)
# number = round(int(number))

print(round(random() * int(8)))  # not correct
# corect print(int(random() * 10) + 1)