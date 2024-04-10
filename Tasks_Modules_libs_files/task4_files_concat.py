def concat_files(*args):
    if args != ():
        rc = open('res.txt', 'w', encoding='utf-8')
        rc.close()
        r = open('res.txt', 'a', encoding='utf-8')
        for i in range(len(args)):
            try:
                with open(args[i], 'r', encoding='utf-8') as f:
                    fr = f.read()
                    r.write(fr)
                    r.write('\n')
            except:
                print(f'Файл {args[i]} не найден!')
        r.close()
    else:
        print('Ошибка! Программа запущена без аргументов!')


concat_files('text3.txt', 'text2.txt', 'text1.txt', 'text4.txt')
# concat_files()
