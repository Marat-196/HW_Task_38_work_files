from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f'в каком формате записать данные \n\n'
                    f'1 Вариант: \n'
                    f'{name}\n{surname}\n{phone}\n{address} \n\n'
                    f'2 Вариант: \n'
                    f'{name};{surname};{phone};{address} \n'
                    f'Выберите вариант: '))
    while var != 1 and var != 2:
        print('Неправильный ввод!')
        var = int(input('Введите число: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f'{name}\n{surname}\n{phone}\n{address} \n\n')
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f'{name};{surname};{phone};{address} \n')
            f.write('\n')


def print_data():
    print('Вывожу данные из 1 файла \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = list()
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i + 1]))
                j = i
        print(''.join(data_first_list))
    print('Вывожу данные из 2 файла \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        # data_second = f.readlines()
        # print(*data_second)
        for i in f.readlines():
            print(i.strip())


def edit_data():
    print('В каком файле вы хотите выполнить изменение данных?? \n1 - data_first_variant \n2 - data_second_variant')
    var = int(input('Введите число: '))
    while var != 1 and var != 2:
        print('Неправильный ввод!')
        var = int(input('Введите число: '))
    if var == 1:
        name = input('Введите имя для замены: ')
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            file = f.readlines()
            my_sp = list()
            for i in file:
                my_sp.append(i.strip())
            if name not in my_sp:
                print('Такого имени нет!')
            else:
                for i in range(len(my_sp)):
                    if my_sp[i] == name:
                        my_sp[i] = name_data()
                        my_sp[i + 1] = surname_data()
                        my_sp[i + 2] = phone_data()
                        my_sp[i + 3] = address_data()
                        break
                for i in range(len(my_sp)):
                    my_sp[i] = my_sp[i] + '\n'
                with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
                    for i in my_sp:
                        f.write(i)
    elif var == 2:
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


def delete_data():
    print('В каком файле вы хотите выполнить удаление данных?? \n1 - data_first_variant \n2 - data_second_variant')
    var = int(input('Введите число: '))
    while var != 1 and var != 2:
        print('Неправильный ввод!')
        var = int(input('Введите число: '))
    if var == 1:
        name = input('Введите имя для удаления: ')
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            file = f.readlines()
            my_sp = list()
            for i in range(len(file)):
                my_sp.append(file[i].strip())
            if name not in my_sp:
                print('Такого имени нет!')
            else:
                for i in range(len(my_sp)):
                    if name == my_sp[i]:
                        for _ in range(5):
                            del my_sp[i]
                        break
                for i in range(len(my_sp)):
                    my_sp[i] = my_sp[i] + '\n'
                with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
                    for i in my_sp:
                        f.write(i)
    elif var == 2:
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

