# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# Для n = 6: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44, 5: 2,49, 6: 2,52}

number = int(input('Введите число: '))

number_dict = {i: round((1 + 1 / i) ** i, 2) for i in range(1, number + 1)}
amount_key = sum(map(lambda x: number_dict[x], number_dict))

print(f'Для числа {number} последовательности (1+1/n)^n словарь {number_dict}')
print(f'Сумма ключей равна {amount_key}')
