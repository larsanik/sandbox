import random

print('Задача №12. Случайные числа')

list_num = random.sample(range(1,50), 6)
list_num.sort()
print('Список номеров для билета:', ', '.join(str(el) for el in list_num) + '.')
