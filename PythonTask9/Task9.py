a = []
with open('PorteyVasiliy_ZIT21_vvod.txt', 'r') as file_vvod:
    for line in file_vvod:
        stroka = line.strip()
        massiv_str = stroka.split(' ')
        b = list(map(int, massiv_str))
        a.append(b)
print('В файле лежит вот такая матрица 6х5:')
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
with open('PorteyVasiliy_ZIT21_vivod.txt', 'w') as file_vivod:
    for i in range(5):
        stroka = ''
        for j in range(6):
            stroka = stroka + str(a[i][j]) + ' '
            print(a[i][j], end = ' ')
        stroka = stroka + '\n'
        file_vivod.write(stroka)
        print()
print('Запись в файл "PorteyVasiliy_ZIT21_vivod.txt завершена!')
