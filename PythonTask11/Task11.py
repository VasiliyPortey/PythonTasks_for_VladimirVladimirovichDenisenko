import requests
import json
import tkinter as tk
from tkinter import *
from tkinter import ttk

def do_clicked():
    name_repos = profile_id.get()
    name_repos = 'https://api.github.com/users/' + name_repos
    r = requests.get(name_repos)
    s = json.loads(r.text)
    dannie = {'company':s.get("company"), 'created_at': s.get("created_at"), 'email': s.get("email"), 'id': s.get("id"), "Name": s.get("name"), 'url': s.get("url") }
    with open('Словарь с нужными значениями.txt', 'w') as file_vivod:
        file_vivod.write(str(dannie))

main_window = tk.Tk()
main_window.title("Портей Василий Игоревич")  
main_window.geometry('310x200')

lbl_response = tk.Label(main_window, text='Введите ID пользователя GitHub (осуществится\nзапрос по адресу "https://api.github.com/\nuresr/{введённый ID}, по номеру моей зачётки\nнужно ввести "dotnet"):')
lbl_response.pack()

profile_id = Entry(main_window)
profile_id.place(x=20, y=70, width=250)

btn_do = Button(main_window, text="Сделать запрос", width=20, command=do_clicked)
btn_do.place(x=70, y=100)

lbl_prim = tk.Label(main_window, text='Сохранится в файл "Словарь с\nнужными значениями"')
lbl_prim.pack(side=BOTTOM)

main_window.mainloop()
