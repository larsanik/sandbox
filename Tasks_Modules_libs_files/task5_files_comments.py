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
            ft.write(el.split('#', 1)[0])
            print(el)
            print(el.split('#', 1)[0])
            ...
        ft.close()


print('Программа удаляет комментарии из файла источника и записывает код в указанный файл.')
# f_src = input('Введите наименование файла источника: ')
# f_target = input('Введите наименование целевого файла: ')

# del_comments(f_src, f_target)
del_comments('task5_files_comments.py', 'no_comments.py')
