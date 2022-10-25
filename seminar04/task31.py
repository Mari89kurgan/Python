# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Введите число: "))
divider = 2
list_number = []
old_number = number
while divider <= number:
    if number % divider == 0:
        list_number.append(divider)
        number //= divider
        divider = 2
    else:
        divider += 1
print(f"Простые множители числа {old_number} приведены в списке: {list_number}")
