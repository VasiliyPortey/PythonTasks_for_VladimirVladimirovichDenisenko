import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter import filedialog

def calculate_clicked():  
    x = first_num.get()
    y = second_num.get()
    operat = operations.get()
    if operat=="+":
        s = int(x)+int(y)
        result.set(str(s))
    elif operat=="-":
        s = int(x)-int(y)
        result.set(str(s))
    elif operat=="*":
        s = int(x)*int(y)
        result.set(str(s))
    elif operat=="/":
        s = int(x)/int(y)
        result.set(str(s))
        
def otvet1_clicked():
        if check2.get()==1 or check3.get()==1:
            check2.set(0)
            check3.set(0)
        if check1.get()==1:
            str_otvet.set('Вы музыкант!')
        else:
            str_otvet.set('')

def otvet2_clicked():
        if check1.get()==1 or check3.get()==1:
            check1.set(0)
            check3.set(0)
        if check2.get()==1:
            str_otvet.set('Вы программист!')
        else:
            str_otvet.set('')
    
def otvet3_clicked():
        if check1.get()==1 or check2.get()==1:
            check1.set(0)
            check2.set(0)
        if check3.get()==1:
            str_otvet.set('Вы не музыкант и не программист(')
        else:
            str_otvet.set('')

def openfile():
    text.delete(1.0, END)
    file_name = filedialog.askopenfilename()
    f = open(file_name)
    s = f.read()
    text.insert(1.0, s)
    f.close()

main_window = tk.Tk()
main_window.title("Портей Василий Игоревич")  
main_window.geometry('310x400')

tabControl = ttk.Notebook(main_window)
tab1 = ttk.Frame(tabControl)  #вкладка калькултора
tabControl.add(tab1, text='Калькуляптор')

first_num = Entry(tab1, width=40) #поля для ввода чисел
second_num = Entry(tab1, width=10)
first_num.place(width=50, height=30, x=30, y=30)
second_num.place(width=50, height=30, x=150, y=30)

btn_calculate = Button(tab1, text="Посчитать", command=calculate_clicked) #кнопка, при нажатии на которую происходит вычисление
btn_calculate.place(x=85, y=120)

result = tk.StringVar()
result.set('Тут будет результат')
lbl_result = tk.Label(tab1, textvariable=result)
lbl_result.place(x=70, y=200)

operations = Combobox(tab1)   #выпадающий список для операций в блоке "калькуляптор"
operations['values'] = ('+', "-", "*", "/")
operations.place(width=40, x=95, y=30)

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Загадка')

zagadka = tk.Label(tab2, text="Что такое С#?")
zagadka.place(x=15, y=20)

#создаём чекбоксы (я думаю, тут бы лучше подошёл тот же комбобокс)
check1=IntVar()
check1.set(0)
check2=IntVar()
check2.set(0)
check3=IntVar()
check3.set(0)
otvet1 = Checkbutton(tab2, text = 'Нота между "До" и "Ре"', var=check1, command=otvet1_clicked)
otvet1.place(x=15, y=70)
otvet2 = Checkbutton(tab2, text = 'Язык программирования', var=check2, command=otvet2_clicked)
otvet2.place(x=15, y=120)
otvet3 = Checkbutton(tab2, text = 'Если честно, я не знаю(', var=check3, command=otvet3_clicked)
otvet3.place(x=15, y=170)

str_otvet = tk.StringVar()
str_otvet.set('')
lbl_otvet = tk.Label(tab2, textvariable=str_otvet)
lbl_otvet.place(x=15, y=270)

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Работа с тектом')

text = Text(tab3)
text.place(x=10,y=10, width=210, height=300)

btn_openfile = Button(tab3, text='Открыть файл', command=openfile)
btn_openfile.place(x=10, y=340)
                                  
tabControl.pack(expand=1, fill="y")

main_window.mainloop()