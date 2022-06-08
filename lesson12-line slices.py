# LINE SLICES

value = '12-08-2034'

print(value[6:10])
#####

# str[initial index:final index]
value = '01-12-9873'
print(value[1:2]) # '1'
print(value[3:5]) # '12'
###
value = 'Hexlet'
print(value[3:]) # 'let'
print(value[:4]) # 'Heal'
###
# negative index
value = 'Hexlet'
print(value[3:-1]) # 'el'
print(value[-5:3]) # 'ex'
###
value = 'Hexlet'
value[1:5:2]  # el
# 1:5 это 'exle'
# шаг 2 это каждый второй, то есть 'e' и 'l'

# Шаг может быть отрицательным, в таком случае он берется с конца. Из этого вытекает самый популярный способ
# использования шага - переворот строки:
value = 'Hexlet'
# Пропускаем обе границы
value[::-1]  # 'telxeH'

# LAB
# Task: Given var  'value = Hexlet'.
# It is necessary to extract from it and display the SLICE that will receive the substring 'xle'.
# This task can be done in different ways.

value = 'Hexlet'

print(value[2:5])
print(value[2:-1])
print(value[-4:5])









