print('Задача №13. Списки')
print('Введите целое число, кроме ноля. Ноль завершит программу.')


def f_dig_list():
    dig_list = []
    while True:
        dig_int = int(input('?: '))
        if dig_int == 0:
            break
        dig_list.append(dig_int)
    return dig_list


num = f_dig_list()

print('Список чисел в порядке возрастания:')

for el in sorted(num):
    print(el)
