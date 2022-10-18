# 14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = float(input('Введите число: '))
amount = 0

number_str = str(number).replace('.', '')
number_int = int(number_str)

while number_int != 0:
    amount += number_int % 10
    number_int //= 10

print(f'Сумма цифр вещественного числа {number} равна {amount}')
