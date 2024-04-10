def concat_files(*args):
    for i in range(len(args)):
        try:
            with open(args[i], 'r', encoding='utf-8') as f:
                print(f)
        except:
            print(f'Файл {args[i]} не найден!')


concat_files('text1.txt', 'text2.txt', 'text3.txt', 'text4.txt')
