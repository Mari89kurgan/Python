# 16. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# Для n = 6: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44, 5: 2,49, 6: 2,52}

number = int(input('Введите число: '))
number_dict = {}
amount_key = 0

for i in range(1, number + 1):
    number_dict[i] = round((1 + 1 / i) ** i, 2)
    amount_key += number_dict[i]

print(f'Для числа {number} последовательности (1+1/n)^n словарь {number_dict}')
print(f'Сумма ключей равна {amount_key}')
