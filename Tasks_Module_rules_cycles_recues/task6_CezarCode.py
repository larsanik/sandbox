# Задача №6. Код Цезаря.

test_string = input("Enter phrase on english for Cesar coding: ")

list_symbol = [symbol for symbol in test_string]

list_upper_symbol = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C"]
list_lower_symbol = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c"]

i = 0

for smbl in list_symbol:
    if smbl.isalpha():
        #print(smbl, ' - буква')
        if smbl.isupper():
            # print(smbl, ' - большая')
            # print(list_upper_symbol.index(smbl), ' - индекс буквы')
            list_symbol[i] = list_upper_symbol[list_upper_symbol.index(smbl) + 3]
        else:
            # print(smbl, ' - маленькая')
            # print(list_lower_symbol.index(smbl), ' - индекс буквы')
            list_symbol[i] = list_lower_symbol[list_lower_symbol.index(smbl) + 3]
    i += 1

print(''.join(list_symbol))