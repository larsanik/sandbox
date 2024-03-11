print('Задача №10. Ввод значений')

var_a = int(input("Введите значение переменной A: "))
var_b = int(input("Введите значение переменной B: "))
var_c = int(input("Введите значение переменной C: "))

if var_a == var_b:
    var_c = var_a + var_b
    var_e = var_b + var_c
else:
    if var_b < var_c:
        var_a = var_a + var_b
        var_e = var_a + var_c
    else:
        var_b = var_c + var_b
        var_e = var_a + var_b

print(f"Результат: {var_e}")
