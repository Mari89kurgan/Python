# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# *Пример:*
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

numbers_list = [2, 3, 4, 5, 6]
new_list = []

for i in range(len(numbers_list)//2):
    new_list.append(numbers_list[i] * numbers_list[-(i+1)])
if len(numbers_list) % 2 != 0:
    new_list.append(numbers_list[len(numbers_list)//2]**2)

print('Список:', new_list)
