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

# a0 = [' ', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a1 = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = [a0, a1]
# for i in range(2, 11):
#     ai = []
#     for j in a1:
#         j = j * i
#         ai.append(j)
#     a.append(ai)
#
# # Этот код выводит таблицу умножения на экран.
# for row in a:
#     for elem in row:
#         print(elem, end=' ')
#     print()