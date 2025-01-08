import tkinter
from tkinter import *
from tkinter import ttk

# Cores
co0 = "#444466"  # Black
co1 = "#feffff"  # White
co2 = "#1E90FF"  # Blue
co3 = "#38576b"  # valor
co4 = "#403d3d"  # Word
co5 = '#7FFF00'  # Green

janela = Tk()
janela.title('Calculadora de conversão')
janela.geometry('400x310')
janela.configure(bg=co2)

style = ttk.Style()
style.theme_use('clam')
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=200)

# Dividindo a Janela em dois frames

frame_cima = Frame(janela, width=400, height=60, bg=co1, pady=0, padx=0)
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=400, height=300, bg=co1, pady=12, padx=20)
frame_baixo.grid(row=2, column=0, sticky=NW)

# Trabalhando no frame_cima
app_nome = Label(frame_cima, text='Conversor de base númerica', relief=FLAT, anchor='center', font=('System 20'), bg=co2, fg=co1)
app_nome.place(x=10, y=15)



janela.mainloop()