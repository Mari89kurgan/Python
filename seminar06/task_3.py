# *Реализуйте алгоритм перемешивания списка

from random import randint

test_list = [1, 2, 3, 4, 5]

new_list = list(sorted(test_list, key=lambda x: x * randint(-10, 10)))

print(new_list)
