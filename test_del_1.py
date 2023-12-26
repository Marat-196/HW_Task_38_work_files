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
