# 7. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


x = int(input('Введите число x '))
y = int(input('Введите число y '))
z = int(input('Введите число z '))

left_part = not (x or y or z)
print(left_part)
right_part = not x and not y and not z
print(right_part)
if left_part == right_part:
    print("Выражение истинно")
else:
    print("Выражение ложно")
