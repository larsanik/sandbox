# Задача №6. Код Цезаря.

test_string = 'Hello world!'

list_symbol = [symbol for symbol in test_string]

list_upper_symbol = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C"]
list_lower_symbol = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c"]

print(list_symbol)
for smbl in list_symbol:
    if smbl.isalpha():
        print(smbl, ' - буква')
        if smbl.isupper():
            print(smbl, ' - большая')
