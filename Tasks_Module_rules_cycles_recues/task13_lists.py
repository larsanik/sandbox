print('Задача №13. Списки')
print('Введите целое число, кроме ноля. Ноль завершит программу.')

dig_list = []

while True:
    dig_int = input('?: ')
    if dig_int == "0":
        break
    dig_list.append(dig_int)

dig_list.sort()

print('Список чисел в порядке возрастания:')

for el in dig_list:
    print(el)

