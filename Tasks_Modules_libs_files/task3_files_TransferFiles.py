# Задача №3. Файлы: перенос данных

def transfer_files(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f:
        my_lines = f.readlines()

    out_file = open(file2, 'w', encoding='utf-8')
    
    ln = 1
    for el in my_lines:
        out_file.write(str(ln) + ': ' + el)
        ln += 1
    out_file.close()


file1 = input('Введте имя файла из которого будем читать строки: ')
file2 = input('Введте имя файла в который будем выаодить пронумерованные строки: ')
transfer_files(file1, file2)