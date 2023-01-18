print('Номер 1 из варианта 1:')
stroka = input('Введите несколько целых чисел через пробел:')
massiv_str = stroka.split(' ')
print('Вы ввели числа: ', massiv_str)
massiv_int = list(map(int, massiv_str))
max_num = massiv_int[0] #объявляю переменную, в которую буду записывать максимальное число
for i in range(0,len(massiv_int)):
    if massiv_int[i]>max_num:
        max_num = massiv_int[i]
print('Максимальное число из введённых Вами: ', max_num)
s = ' '
for i in range(0,len(massiv_int)):
    if i<=len(massiv_int):
        #print(massiv_int[len(massiv_int)-i-1], ' ')
        s = s + str(massiv_int[len(massiv_int)-i-1]) + ' '
print('Теперь выводим список в обратном порядке: ', s)
print('Номер 2 из варианта 1 (возьмём просто тот же список):')
s = ' '
srednee_arif = 0
for i in range(0,len(massiv_int)):
    srednee_arif = srednee_arif + massiv_int[i]
srednee_arif = srednee_arif/len(massiv_int)
print('Среднее арифметическое введённых Вами чисел: ', srednee_arif)
for i in range(0,len(massiv_int)):
    if massiv_int[i]==0:
        massiv_int[i] = srednee_arif
    s = s + str(massiv_int[i]) + ' '
print('Вот такой список в итоге получился:', s)