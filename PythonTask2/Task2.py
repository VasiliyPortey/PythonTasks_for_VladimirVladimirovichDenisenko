import math
x = 14.26
y = (-1.22)
z = 3.5*10**(-2)
#s = (2*math.cos(x-(2/3))/(1/2+(math.sin(y))**2))*((1+z**2)/(3-(z**2)/5) закомментировал, потому что почему-то не работало( наверное, скобка лишняя где-то
s = 2*math.cos(x-(2/3))*(1+((z**2)/3-(z**2)/5))/(1/2+math.sin(y)**2) 
print('Здравствуйте, Владимир Владимирович. Я выбрал самый первый номер из второго задания\nРезультат при х =', x, ', y=', y, ', z =', z, ', следующий:', s)