# Изучите алгоритм и напишите код, который выведет у (см. for_task5_cycles.png).

x = 10
y = 0

while x != 5:
    y = y + 2*y -3
    x = x-1

if x == y:
    x = x-y
    y = y+x
else:
    x = x+y
    y = y-x

print(f"y = {y}")
