from data_create import name_data, surname_data, phone_data, address_data

name = input('Введите имя для замены: ')
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
                my_sp[i][0] = name_data()
                my_sp[i][1] = surname_data()
                my_sp[i][2] = phone_data()
                my_sp[i][3] = address_data()
                break
        for i in range(len(my_sp)):
            my_list.append(';'.join(my_sp[i]) + '\n')
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.writelines(my_list)
