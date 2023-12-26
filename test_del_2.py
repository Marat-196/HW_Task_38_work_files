
name = input('Введите имя для удаления: ')
with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
    file = f.readlines()
    my_sp = list()
    lst = list()
    my_list = list()
    for i in range(len(file)):
        my_sp.append(file[i].strip().split(';'))
    for i in range(len(my_sp)):
        lst.append(my_sp[i][0])
    if name not in lst:
        print('Такого имени нет!')
    else:
        for i in range(len(my_sp)):
            if name == my_sp[i][0]:
                del my_sp[i]
                break
        for i in range(len(my_sp)):
            my_list.append(';'.join(my_sp[i]) + '\n')
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(my_list)

