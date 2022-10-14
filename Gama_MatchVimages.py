from email.mime import image
from tkinter import *
from tkinter import messagebox
from tkinter import Menu
from PIL import ImageTk,Image
import random
import time
import pygame

pygame.init()
pygame.mixer.init()

ventana = Tk()
ventana.title("Memorama")
ventana.iconbitmap("")
ventana.geometry("500x500")
tablero = Frame(ventana)
tablero.pack()

memorama = [1,1,2,2,3,3,4,4,5,5,6,6]
random.shuffle(memorama)

clics = 0
respuestas = []
almacen_dict = {}
global ganador
ganador = 0


def reiniciar():
	global memorama, ganador
	ganador = 0
	

	memoria_aviso.config(text = "")

	memorama = [1,1,2,2,3,3,4,4,5,5,6,6]
	random.shuffle(memorama)

	botones = [bt0,bt1,bt2,bt3,bt4,bt5,bt6,bt7,bt8,bt9,bt10,bt11]
	for button in botones:
		button.config(text=" ", bg="SystemButtonFace", state="normal")
	

def vaciar():
	global clics, respuestas, almacen_dict, error
	
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
	global clics, respuestas, almacen_dict, ganador, error

	if bt["text"] == " " and clics < 2:
		bt["text"] = memorama[posicion]
		respuestas.append(posicion)
		almacen_dict[bt] = memorama[posicion]
		clics += 1
	
	if len(respuestas) == 2:
		if memorama[respuestas[0]] == memorama[respuestas[1]]:
		
			for key in almacen_dict:
				key.config(bg="magenta")
				key["state"] = "disabled"
			memoria_aviso.config(text = "")
			ganador += 1

			if ganador == 6:
				victoria()

		else:
			messagebox.showinfo("Error!")
			borrar()
		vaciar()



img= Image.open("C:\\Users\\Braya\\Downloads\\Manzana.jpeg")
resized=img.resize((240,160), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resized)

img2= Image.open("C:\\Users\\Braya\\Downloads\\Sandia.jpeg")
resized=img2.resize((240,160), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(resized)

img3= Image.open("C:\\Users\\Braya\\Downloads\\Naranja.jpeg")
resized=img3.resize((240,160), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(resized)

img4= Image.open("C:\\Users\\Braya\\Downloads\\Platano.jpeg")
resized=img4.resize((240,160), Image.ANTIALIAS)
img4 = ImageTk.PhotoImage(resized)

img5= Image.open("C:\\Users\\Braya\\Downloads\\Pina.jpeg")
resized=img5.resize((240,160), Image.ANTIALIAS)
img5 = ImageTk.PhotoImage(resized)

img6= Image.open("C:\\Users\\Braya\\Downloads\\Queso.jpeg")
resized=img6.resize((240,160), Image.ANTIALIAS)
img6 = ImageTk.PhotoImage(resized)

bt0 = Button(tablero, text=" ", font=('Helvetica'), height=160, width=240, command=lambda:clickeo(bt0,0), relief = "groove", image=img) 
bt1 = Button(tablero, text=" ", font=('Helvetica'), height=160, width=240, command=lambda:clickeo(bt1,1), relief = "groove", image=img)
bt2 = Button(tablero, text=" ", font=('Helvetica'), height=160, width=240, command=lambda:clickeo(bt2,2), relief = "groove", image=img2)
bt3 = Button(tablero, text=" ", font=('Helvetica'), height=160, width=240, command=lambda:clickeo(bt3,3), relief = "groove", image=img2)
bt4 = Button(tablero, text=" ", font=('Helvetica'), height=160, width=240, command=lambda:clickeo(bt4,4), relief = "groove", image=img3)
bt5 = Button(tablero, text=" ", font=('Helvetica'), height=160, width=240, command=lambda:clickeo(bt5,5), relief = "groove", image=img3)
bt6 = Button(tablero, text=" ", font=('Helvetica'), height=160, width=240, command=lambda:clickeo(bt6,6), relief = "groove", image=img4)
bt7 = Button(tablero, text=" ", font=('Helvetica'), height=160, width=240, command=lambda:clickeo(bt7,7), relief = "groove", image=img4)
bt8 = Button(tablero, text=" ", font=('Helvetica'), height=160, width=240, command=lambda:clickeo(bt8,8), relief = "groove", image=img5)
bt9 = Button(tablero, text=" ", font=('Helvetica'), height=160, width=240, command=lambda:clickeo(bt9,9), relief = "groove", image=img5)
bt10 = Button(tablero, text=" ", font=('Helvetica'), height=160, width=240, command=lambda:clickeo(bt10,10), relief = "groove", image=img6)
bt11 = Button(tablero, text=" ", font=('Helvetica'), height=160, width=240, command=lambda:clickeo(bt11,11), relief = "groove", image=img6)

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

menu_ctrl = Menu(ventana)
ventana.config(menu = menu_ctrl)

menuprincipal = Menu(menu_ctrl, tearoff = False)
menu_ctrl.add_cascade(label = "Opciones", menu = menuprincipal)
menuprincipal.add_command(label = "Nueva Partida", command = reiniciar)
menuprincipal.add_command(label = "Salir", command = ventana.quit)

ventana.mainloop()