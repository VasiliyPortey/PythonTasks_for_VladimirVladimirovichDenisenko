#задание из файла "3 ПР"
x1 = int(input('Введите 1-е число:'))
x2 = int(input('Введите 2-е число:'))
x3 = int(input('Введите 3-е число:'))
s=''
if 1<=x1<=3:
    s= s + str(x1) + ' '
if 1<=x2<=3:
    s= s + str(x2) + ' '
if 1<=x3<=3:
    s= s + str(x3) + ' '
print('Выбираем из введённых чисел те, которые входят в интервал от 1 до 3\nЭто числа: ', s)