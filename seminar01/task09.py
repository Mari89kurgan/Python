# 9. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input("Введите четверть системы координат 1-4: "))

if number == 1:
    print("Данной четверти соответствует x>0 и y>0")
elif number == 2:
    print("Данной четверти соответствует x<0 и y>0")
elif number == 3:
    print("Данной четверти соответствует x<0 и y<0")
elif number == 4:
    print("Данной четверти соответствует x>0 и y<0")
else:
    print("Такой четверти координат нет")
