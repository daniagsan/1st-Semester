from tkinter import *
import random
from tkinter import messagebox

ventana = Tk()
ventana.title("Memorama")
ventana.iconbitmap("G:/Mi unidad/TAREAS IDS/Metodología de la programación/Juego/Imágenes/juego-de-azar.ico")
ventana.geometry("460x450")

memorama = [1,1,2,2,3,3,4,4,5]
#random.shuffle(memorama)

tablero = Frame(ventana)
tablero.pack(pady=85)

clics = 0
respuestas = []
almacen_resp = {}

def clickeo(bt, posicion):
	global clics, respuestas, almacen_resp

	if bt["text"] == ' ' and clics < 2:
		bt["text"] = memorama[posicion]
		respuestas.append(posicion)
		almacen_resp[bt] = memorama[posicion]
		clics += 1
	
	if len(respuestas) == 2:
		if memorama[respuestas[0]] == memorama[respuestas[1]]:
			aviso.config(text= "¡MEMORIA!")
			for key in almacen_resp:
				key["state"] = "disabled"
		#else:
			# voltear cards
		clics = 0
		respuestas = []
		almacen_resp = {}

bt0 = Button(tablero, text=' ', font=('Helvetica'), height=3, width=6, command=lambda:clickeo(bt0,0))
bt1 = Button(tablero, text=' ', font=('Helvetica'), height=3, width=6, command=lambda:clickeo(bt1,1))
bt2 = Button(tablero, text=' ', font=('Helvetica'), height=3, width=6, command=lambda:clickeo(bt2,2))
bt3 = Button(tablero, text=' ', font=('Helvetica'), height=3, width=6, command=lambda:clickeo(bt3,3))
bt4 = Button(tablero, text=' ', font=('Helvetica'), height=3, width=6, command=lambda:clickeo(bt4,4))
bt5 = Button(tablero, text=' ', font=('Helvetica'), height=3, width=6, command=lambda:clickeo(bt5,5))
bt6 = Button(tablero, text=' ', font=('Helvetica'), height=3, width=6, command=lambda:clickeo(bt6,6))
bt7 = Button(tablero, text=' ', font=('Helvetica'), height=3, width=6, command=lambda:clickeo(bt7,7))
bt8 = Button(tablero, text=' ', font=('Helvetica'), height=3, width=6, command=lambda:clickeo(bt8,8))

bt0.grid(row=0, column=0)
bt1.grid(row=0, column=1)
bt2.grid(row=0, column=2)
bt3.grid(row=1, column=0)
bt4.grid(row=1, column=1)
bt5.grid(row=1, column=2)
bt6.grid(row=2, column=0)
bt7.grid(row=2, column=1)
bt8.grid(row=2, column=2)

aviso = Label(ventana, text="")
aviso.pack(pady=10)

ventana.mainloop()