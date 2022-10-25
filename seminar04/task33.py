# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0

from random import randint

polynomial = ''
k = int(input('Задайте натуральную степень: '))

random_list = [randint(0, 10) for _ in range(k + 1)]

for index in range(k + 1):
    if index == k:
        if random_list[index] == 0:
            polynomial += ' = 0'
        else:
            polynomial += f'{random_list[index]} = 0'
        break
    elif index == k - 1:
        if random_list[index] > 0:
            polynomial += f'{random_list[index]}X'
    else:
        if random_list[index] > 1:
            polynomial += f'{random_list[index]}X**{len(random_list) - (index+1)}'
        else:
            polynomial += f'X**{len(random_list) - (index+1)}'
    if random_list[index + 1] == 0:
        continue
    polynomial += ' + '
print(polynomial)
with open('polynomial_file.txt', 'w', encoding='utf-8') as polynomial_file:
    polynomial_file.write(f'{polynomial}\n')

