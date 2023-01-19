
def max_znachenie(stroka, max_znach, i):
    if int(stroka[i])>max_znach:
        max_znach=int(stroka[i])
    if i>0:
        i = i-1
        return max_znachenie(stroka, max_znach, i)
    else:
        return max_znach


print('Данная программа найдёт в сплошной последовательности натуральных чисел наибольшее и выведет его')
posled = input('Введите последовательность натуральных чисел без пробелов (по условию эта\nпоследовательность должна закончиться нулём): ')
max_znach = 0
kolvo = len(posled)
print('Максимальное число в последовательности - ', max_znachenie(posled, max_znach, kolvo-1))

