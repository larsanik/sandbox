# Задача №3. Файлы: перенос данных

def transfer_files(file_1, file_2):
    with open(file_1, 'r', encoding='utf-8') as f:
        my_lines = f.readlines()

    out_file = open(file_2, 'w', encoding='utf-8')

    ln = 1
    for el in my_lines:
        out_file.write(str(ln) + ': ' + el)
        ln += 1
    //out_file.close()

    # TODO более годный вариант от Eduson
    #  with open(new_file_name, "w") as new_file:
    #     for index, line in enumerate(my_lines):
    #         new_file.write(f"{index + 1}: {line}")


file1 = input('Введте имя файла из которого будем читать строки: ')
file2 = input('Введте имя файла в который будем выаодить пронумерованные строки: ')
transfer_files(file1, file2)
