# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

test_list = [1, 1, 7, 5, 2, 2]
new_list = []

a = list(filter(lambda x: test_list.count(x) == 1, test_list))

print('Список неповторяющихся элементов исходной последовательности:', a)