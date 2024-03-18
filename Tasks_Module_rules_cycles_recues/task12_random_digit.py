import random

print('Задача №12. Случайные числа')


def gen_rnd():
    list_num = random.sample(range(1,50), 6)
    list_num.sort()
    return ', '.join(str(el) for el in list_num)


num = gen_rnd()
print('Список номеров для билета:', num + '.')

# def generate_random_numbers():
#     numbers = random.sample(range(1, 50), 6)
#     numbers.sort()
#     return numbers
#
# numbers = generate_random_numbers()
# print(numbers)