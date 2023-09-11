import tkinter as tk
from tkinter import *
import os 
from time import strftime

#estrutura do relógio
root = tk.Tk()
root.title('Relógio')
root.geometry('600x320')
#congelando janela
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(background = "dark green")

def get_saudacao():
    nome_usuario = os.getlogin()
    saudacao.config(text = 'Olá, ' + nome_usuario)

def get_data():
    data_atual = strftime('%a, %d %b, %Y')
    data.config(text=data_atual)

def get_horas():
    hora_atual = strftime('%H:%M:%S')
    horas.config(text = hora_atual)
    horas.after(1000, get_horas)

tela = tk.Canvas(root, width = 600, height = 60, bg = "dark green", bd = 0, highlightthickness=0, relief='ridge')
tela.pack()
saudacao = Label(root, bg = "dark green", fg = "white", font = ("arial", 16))
saudacao.pack()
data = Label(root, bg = "dark green", fg = "white", font = ("arial", 14))
data.pack(pady = 2)
horas = Label(root, bg = "dark green", fg = "white", font = ("arial", 64, 'bold'))
horas.pack(pady=2)

get_saudacao()
get_data()
get_horas()
root.mainloop()