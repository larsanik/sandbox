print('Задача №14. Рекурсии')
# Напишите программу, которая будет складывать числа,
# введенные пользователем.
# Сигнал к окончанию ввода — пустая строка.
# Отобразите на экране сумму значений. Если пользователь сразу же пропустил ввод, выведите 0.0. Решите эту
# задачу с использованием рекурсии. В вашей программе
# не должны присутствовать циклы.
# Важно: запросите одно число у пользователя в теле
# вашей рекурсивной функции. После этого должно быть
# принято решение, производить ли еще один рекурсивный вызов.
# Ваша функция не должна принимать аргументов, а возвращать будет числовое значение.

d = 0.0


def rec():
    global d
    val = input('digit: ')
    if val == '':
        print(d)
        return d
    d = d + float(val)
    rec()


rec()
