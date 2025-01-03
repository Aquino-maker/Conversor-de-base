import tkinter
from tkinter import *
from tkinter import ttk

# Cores
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca / white
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = '#e89613'  # laranja

janela = Tk()
janela.title('Calculadora de conversão')
janela.geometry('400x310')
janela.configure(bg=co1)

style = ttk.Style()
style.theme_use('clam')
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=190)

janela.mainloop()