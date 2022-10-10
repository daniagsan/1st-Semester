from tkinter import *
import random
from tkinter import messagebox
import time

ventana = Tk()
ventana.title("Memorama")
#ventana.iconbitmap("G:/Mi unidad/TAREAS IDS/Metodología de la programación/Juego/Imágenes/juego-de-azar.ico")
ventana.geometry("500x500")

memorama = [1,1,2,2,3,3,4,4,5,5,6,6]
#random.shuffle(memorama)

tablero = Frame(ventana)
tablero.pack(pady=20)

clics = 0
respuestas = []
almacen_dict = {}
global ganador
ganador = 0

def vaciar():
	global clics, respuestas, almacen_dict
	
	aviso.config(text="")
	clics = 0
	respuestas = []
	almacen_dict = {}

def borrar():
	for key in almacen_dict:
		key["text"] = " "

def victoria():
	memoria_aviso.config(text = "WINNER DINNER CHICKEN DINNER")
	botones = [bt0,bt1,bt2,bt3,bt4,bt5,bt6,bt7,bt8,bt9,bt10,bt11]
	for button in botones:
		button.config(bg="yellow")

def clickeo(bt, posicion):
	global clics, respuestas, almacen_dict, ganador

	if bt["text"] == " " and clics < 2:
		bt["text"] = memorama[posicion]
		respuestas.append(posicion)
		almacen_dict[bt] = memorama[posicion]
		clics += 1
	
	if len(respuestas) == 2:
		if memorama[respuestas[0]] == memorama[respuestas[1]]:
			memoria_aviso.config(text = "¡MEMORIA!")
			for key in almacen_dict:
				key["state"] = "disabled"

			ganador += 1
			if ganador == 6:
				victoria()
		else:
			aviso.config(text = "¡ERROR!")
			messagebox.showinfo("¡Error!")
			borrar()
		vaciar()

bt0 = Button(tablero, text=" ", font=('Helvetica'), height=4, width=6, command=lambda:clickeo(bt0,0), relief = "groove")
bt1 = Button(tablero, text=" ", font=('Helvetica'), height=4, width=6, command=lambda:clickeo(bt1,1), relief = "groove")
bt2 = Button(tablero, text=" ", font=('Helvetica'), height=4, width=6, command=lambda:clickeo(bt2,2), relief = "groove")
bt3 = Button(tablero, text=" ", font=('Helvetica'), height=4, width=6, command=lambda:clickeo(bt3,3), relief = "groove")
bt4 = Button(tablero, text=" ", font=('Helvetica'), height=4, width=6, command=lambda:clickeo(bt4,4), relief = "groove")
bt5 = Button(tablero, text=" ", font=('Helvetica'), height=4, width=6, command=lambda:clickeo(bt5,5), relief = "groove")
bt6 = Button(tablero, text=" ", font=('Helvetica'), height=4, width=6, command=lambda:clickeo(bt6,6), relief = "groove")
bt7 = Button(tablero, text=" ", font=('Helvetica'), height=4, width=6, command=lambda:clickeo(bt7,7), relief = "groove")
bt8 = Button(tablero, text=" ", font=('Helvetica'), height=4, width=6, command=lambda:clickeo(bt8,8), relief = "groove")
bt9 = Button(tablero, text=" ", font=('Helvetica'), height=4, width=6, command=lambda:clickeo(bt9,9), relief = "groove")
bt10 = Button(tablero, text=" ", font=('Helvetica'), height=4, width=6, command=lambda:clickeo(bt10,10), relief = "groove")
bt11 = Button(tablero, text=" ", font=('Helvetica'), height=4, width=6, command=lambda:clickeo(bt11,11), relief = "groove")

bt0.grid(row=0, column=0)
bt1.grid(row=0, column=1)
bt2.grid(row=0, column=2)
bt3.grid(row=0, column=3)
bt4.grid(row=1, column=0)
bt5.grid(row=1, column=1)
bt6.grid(row=1, column=2)
bt7.grid(row=1, column=3)
bt8.grid(row=2, column=0)
bt9.grid(row=2, column=1)
bt10.grid(row=2, column=2)
bt11.grid(row=2, column=3)

aviso = Label(ventana, text="")
aviso.pack()

memoria_aviso = Label(ventana, text="")
memoria_aviso.pack()

ventana.mainloop()