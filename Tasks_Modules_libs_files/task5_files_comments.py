# Программа удаляет комментарии из файла источника и записывает код в указанный файл.
def del_comments(f_src, f_target):
    try:
        # открываем файлы
        with open(f_src, 'r', encoding='utf-8') as f:
            f_src_lines = f.readlines()
        ft = open(f_target, 'w', encoding='utf-8')
    except:
        # обрабатываем ошибки
        print('Произошла ошибка. Программа будет завершена.')
        exit(42)
    else:
        # выполняем код по удалению комментариев
        for el in f_src_lines:
            lin = el.split('#', 1)[0]  # TODO Этот кусок парсится неправильно. Если встречается # в коде, то режет код.
            if lin.strip() != '' or el.strip() == '':
                ft.write(lin)
        ft.close()


print('Программа удаляет комментарии из файла источника и записывает код в указанный файл.')
f_src = input('Введите наименование файла источника: ')
f_target = input('Введите наименование целевого файла: ')

del_comments(f_src, f_target)

