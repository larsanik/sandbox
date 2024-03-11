def task_7():
    print('Задача №7. Списки')
    # Изучите список:
    # my_list = [2, 4, 8].
    # Представьте его в обратном порядке двумя способами и
    # объясните, в чем между ними разница.

    # way 1
    print('way 1')
    my_list = [2, 4, 8]
    print(my_list)
    my_list.reverse()
    print(my_list)
    my_list = [2, 4, 8]

    # way 2
    print('way 2')
    my_list = [2, 4, 8]
    print(my_list)
    print(my_list[::-1])

def task_8():
    print('Задача №8. Списки')
    # Изучите список:
    # a = [1, 1, 2, 3, 5, 8, 34, 55, 89].
    # Напишите код: выведите все элементы списка, которые
    # меньше 5.

    a = [1, 1, 2, 3, 5, 8, 34, 55, 89]
    sample = []
    for i in a:
        if i < 5:
            sample.append(i)
            print(i)
    print(sample)

# task_7()
task_8()