print('\nНомер 2 варианта 1 задания 8:\nПусть будет матрица 6х5 (введите числа поочереди, нажимая Enter):\n')
a=[]
for i in range(5):
    b=[]
    for j in range(6):
        b.append(int(input()))
    a.append(b)
print('Получился вот такой массив: ')
for i in range(5):
    for j in range(6):
        print(a[i][j], end = ' ')
    print()
for i in range(5):
    max_num = a[i][0]
    min_num = a[i][5]
    first_num = a[i][0]
    last_num = a[i][5]
    index_j_max = 0
    index_j_min = 5
    for j in range(6):
        if a[i][j]>max_num:
            max_num=a[i][j]
            index_j_max = j
        if a[i][j]<min_num:
            min_num=a[i][j]
            index_j_min = j
    a[i][index_j_max]=first_num
    a[i][index_j_min]=last_num
    a[i][0]=max_num
    a[i][5]=min_num        
print('В результате получается такая матрица:\n')
for i in range(5):
    for j in range(6):
        print(a[i][j], end = ' ')
    print()
