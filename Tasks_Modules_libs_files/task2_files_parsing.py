# Задача №2. Файлы: парсинг

# функция которая делает всю работу
def long_word(namefile, encoding):
    # открываем файл, записываем содержимое в переменную и создаем список из слов
    with open(namefile, 'r', encoding=encoding) as f:
        data = f.read()
    words_list = data.split()

    # находим самое длинное слово
    max_long = 0

    for el in words_list:
        if max_long < len(el):
            max_long = len(el)

    # создаем список самых длинных слов
    list_long_words = []

    for el in words_list:
        if len(el) == max_long:
            list_long_words.append(el)

    # возвращаем результаты
    return max_long, list_long_words

# вызов функции
res = long_word('text.txt', 'utf-8')

# вывод результатов в консоль
print('Max long = ', res[0])
print('List long words = ', res[1])
