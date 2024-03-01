# Задача №4. Дата и время
# Напишите функцию для определения количества дней
# в конкретном месяце. Ваша функция должна принимать
# два параметра: номер месяца в виде целого числа
# в диапазоне от 1 до 12 и год, состоящий из четырех цифр.
#
# Убедитесь, что функция корректно обрабатывает февраль високосного года.
#
# Запросите у пользователя номер месяца и год и выведите
# на экран количество дней в указанном месяце.

def leap_year (year):
    # год, номер которого кратен 400, — високосный;
    if int(year)%400 == 0.0:
        return True
    # остальные годы, номер которых кратен 100, — невисокосные (например, годы 1700, 1800, 1900, 2100, 2200, 2300);
    if int(year)%100 == 0.0:
        return False
    # остальные годы, номер которых кратен 4, — високосные[5];
    if int(year)%4 == 0.0:
        return True
    # все остальные годы — невисокосные.
    return False

def num_days_mon(num_mon, year):
    list_days = [31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if num_mon == "2":
        if leap_year(year):
            return list_days[int(num_mon)-1][1]
        else:
            return list_days[int(num_mon)-1][0]
    return list_days[int(num_mon)-1]

while True:
    num_mon = input("Enter month: ")
    year = input("Enter year: ")
    print("Amount of days: ", num_days_mon(num_mon, year))
    if input("Сontinue (y/n)? ") != "y":
        break
