# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# *Пример:*
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

float_numbers_list = [1.1, 1.2, 3.1, 5, 10.01]
new_list = []

for number in float_numbers_list:
    new_number = round(number % 1, 4)
    if new_number != 0:
        new_list.append(new_number)
difference = max(new_list) - min(new_list)

print('Разницу между максимальным и минимальным значением дробной части элементов:', difference)
