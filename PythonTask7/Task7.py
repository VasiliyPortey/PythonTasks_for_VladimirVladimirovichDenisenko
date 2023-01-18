import math
#Вариант 1 в задании

def ploshad_kv(x):
    return x**2
def ploshad_pr(x,y):
    return x*y
def ploshad_pr_tr(x,y):
    return x*y/2
def ploshad_kr(x):
    return math.pi*pow(x,2)

def go_calculate():
    type_of_figure = int(input('Выберите фигуру, выбрав соответствующую цифру: \n1 - квадрат, 2 - прямоугольник,\n3 - прямоугольный треугольник, 4 - круг: '))
    if type_of_figure==1:
        x = int(input('Введите длину стороны квадрата: '))
        print('Площадь квадрата равна ', ploshad_kv(x))
    elif type_of_figure==2:
        x = int(input('Введите длину прямоугольника: '))
        y = int(input('Введите ширину прямоугольника: '))
        print('Площадь прямоугольника равна ', ploshad_pr(x, y))
    elif type_of_figure==3:
        x = int(input('Введите длину первого катета: '))
        y = int(input('Введите длину второго катета: '))
        print('Площадь прямоугольного треугольника равна ', ploshad_pr_tr(x, y))
    elif type_of_figure==4:
        x = int(input('Введите длину радиуса круга: '))
        print('Площадь круга равна ', ploshad_kr(x))
    want_you = int(input('Если хотите повторить, введите 1, если нет, введите 0: '))
    if want_you==1:
        return go_calculate()
    elif want_you==0:
        print('Завершение работы...')
        return 0
        
go_calculate()

    
