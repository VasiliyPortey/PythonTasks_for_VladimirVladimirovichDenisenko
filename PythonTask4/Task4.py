def second_number(a):
    b = int(input('Введите второе число В (оно должно быть больше/равно А): '))
    if b<a:
        print('ведённое число больше ', a, "! Попробуйте ещё раз.")
        return second_number(a)
    else:
        return b
    
a = int(input('Введите число А: '))
b = second_number(a)
s = ''
if a==b or (a==b-1):
    print('Между А и В нет других целых чисел(')
else:
    for i in range(a+1,b-1):
        s = s + str(i)+' '
    print('Числа между А и В:', s)