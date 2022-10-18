# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на введенных пользователем позициях.

import random

number = int(input('Введите число: '))
number_list = []
multiplication = 1

for i in range(-number, number + 1):
    number_list.append(random.randint(-number, number))

for number in number_list:
    multiplication *= number

print(f'Список из N элементов, заполненных числами из промежутка [-N, N]: {number_list}')
print(f'Произведение элементов: {multiplication}')

