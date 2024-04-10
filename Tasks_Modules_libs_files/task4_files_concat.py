def concat_files(*args):
    for i in range(len(args)):
        print(args[i])


concat_files('text1.txt', 'text2.txt', 'text3.txt', 'text4.txt')
