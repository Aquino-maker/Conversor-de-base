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

# Trabalhando no frame_baixo
base = ['Binário', 'Octal', 'Decimal', 'Hexadecimal']

combo = ttk.Combobox(frame_baixo, width=12, justify=CENTER, font='Ivy 12 bold')
combo['values'] = (base)
combo.place(x= 35, y=10)

entrada_valor = Entry(frame_baixo, width=9, justify=CENTER, font=('', 13), highlightthickness = 1, relief='solid')
entrada_valor.place(x=160, y=10)

bttn_converter = Button(frame_baixo, text='CONVERTER', relief=RAISED, overrelief=RIDGE , font=('Ivy 8 bold'), bg=co1, fg=co4)
bttn_converter.place(x=247, y=10)

label_binario = Label(frame_baixo, text='BINÁRIO', width=12, relief=FLAT, anchor='nw', font=('Verdana 13 bold'), bg=co5, fg=co4)
label_binario.place(x=35, y=60)
label_binario = Label(frame_baixo, text='', width=13, relief=FLAT, anchor='center', font=('Verdana 13 bold'), fg=co4)
label_binario.place(x=170, y=60)

label_octal = Label(frame_baixo, text='OCTAL', width=12, relief=FLAT, anchor='nw', font=('Verdana 13 bold'), bg=co5, fg=co4)
label_octal.place(x=35, y=100)
label_octal = Label(frame_baixo, text='', width=13, relief=FLAT, anchor='center', font=('Verdana 13 bold'), fg=co4)
label_octal.place(x=170, y=100)

label_hexa = Label(frame_baixo, text='HEXADECIMAL', width=13, relief=FLAT, anchor='nw', font=('Verdana 11 bold'), bg=co5, fg=co4)
label_hexa.place(x=35, y=140)
label_hexa = Label(frame_baixo, text='', width=13, relief=FLAT, anchor='center', font=('Verdana 13 bold'), fg=co4)
label_hexa.place(x=170, y=140)

label_decimal = Label(frame_baixo, text='DECIMAL', width=12, relief=FLAT, anchor='nw', font=('Verdana 13 bold'), bg=co5, fg=co4)
label_decimal.place(x=35, y=180)
label_decimal = Label(frame_baixo, text='', width=13, relief=FLAT, anchor='center', font=('Verdana 13 bold'), fg=co4)
label_decimal.place(x=170, y=180)





janela.mainloop()