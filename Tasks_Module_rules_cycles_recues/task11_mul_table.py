print('Задача №11. Упорядоченный вывод данных')

def spc(dig):
    if dig > 99:
        return " "
    if dig > 9:
        return "  "
    return "   "

print("     ", end="")

for name_col in range(1,11):
    print(name_col, spc(name_col), end="")
print()
print()

for row in range(1,11):
    print(row, spc(row), end="")
    for col in range(1,11):
        vol = row*col
        print(vol, spc(vol) , end="")
    print()