

def factorial(n):
    if n>1:
        return n*factorial(n-1)
    else:
        return n
        

def stepen(x, n, res):
    if n>1:
        res = res*x
        return stepen(x, n-1, res)
    elif n==1:
        return res
    elif n==0:
        return 1

print('Данная программа с помощью рекурсии посчитает результат выражения (x^n)/n! (ноль натуральным числом не считаем,\nхотя на всякий случай и такой вариант учёл(в функции степени, не факториала))')
x = int(input('Введите x: '))
x_mutable = x
n = int(input('Введите n: '))
otvet = stepen(x,n,x_mutable)/factorial(n)
print('Резултат = ', str(otvet))