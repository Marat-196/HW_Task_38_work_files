from data_create import name_data, surname_data, phone_data, address_data

name = input('Введите имя для замены: ')
with open('data_first_variant.csv', 'r+', encoding='utf-8') as f:
    file = f.readlines()
    print(file)
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
        print(my_sp)
        with open('data_first_variant.csv', 'w+', encoding='utf-8') as f:
            for i in my_sp:
                f.write(i)
