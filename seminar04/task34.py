# 34. *Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# 2x² + 4x + 5 = 0 и x² + 5x + 3 = 0 => 3x² + 9x + 8 = 0

with open('test_1.txt', 'r', encoding='utf-8') as test_1:
    test_1 = test_1.read().split(' ')

with open('test_2.txt', 'r', encoding='utf-8') as test_2:
    test_2 = test_2.read().split(' ')

new_list = test_1 + test_2

number_1 = 0
number_2 = 0
number_3 = 0

for i in new_list:
    if i.isdigit():
        number_3 += int(i)
    elif i.count('X**2') > 0:
        i = i.replace('X**2', '')
        number_1 += int(i)
    elif i.count('X') > 0:
        i = i.replace('X', '')
        number_2 += int(i)

with open('new_polynomial_file.txt', 'w', encoding='utf-8') as polynomial_file:
    polynomial_file.write(f'{number_1}X**2 + {number_2}X + {number_3} = 0')
