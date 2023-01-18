print('Номер 1 варианта 1 задания 8:\nСоздаём массив размерности 5х5 (введите числа поочереди, нажимая Enter):\n')
a=[]
for i in range(5):
    b=[]
    for j in range(5):
        b.append(int(input()))
    a.append(b)
print('Получился вот такой массив: ')
for i in range(5):
    for j in range(5):
        print(a[i][j], end = ' ')
    print()
print('Вычислим сумму и число положительных элементов матрицы, находящихся НАД главной диагональю.')
polozh_num=0
polozh_sum=0
for i in range(5):
    for j in range(5):
        if i<j and a[i][j]>0:
            polozh_num = polozh_num + 1
            polozh_sum = polozh_sum + a[i][j]
print('Сумма: ', polozh_sum, ' количество: ', polozh_num)
