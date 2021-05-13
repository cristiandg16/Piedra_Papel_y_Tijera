from tkinter import *
import random

#Cremos el tablero
tablero = Tk()

#Establecemos las dimensiones del tablero
tablero.geometry("500x300")

#Establecemos el titulo de la GUI
tablero.title("Piedra, Papel o Tijera")

#Asignamos valores a cada elemento del juego
values = {
    "0":"Piedra",
    "1":"Papel",
    "2":"Tijera"
}

frame1 = Frame(tablero)
frame1.pack()

boton1 = Button(frame1,text = "Piedra",font = 10,width= 7,command=elije_piedra)

boton2 = Button(frame1,text = "Papel",font = 10,width= 7,command=elije_papel)

boton3 = Button(frame1,text = "Tijera",font = 10,width= 7,command=elije_tijera)

boton1.pack(side = LEFT, padx = 10)
boton2.pack(side = LEFT,padx = 10)
boton3.pack(padx = 10)

Button(tablero, text = "Reiniciar", font = 10, bg="red",command=reiniciar).pack(pady=20)



#Reinicio del juego
def reinicio():
    boton1["state"] = "active"
    boton2["state"] = "active"
    boton3["state"] = "active"

#Bloqueo de botones
def bloqueo():
    boton1["state"] = "disable"
    boton2["state"] = "disable"
    boton3["state"] = "disable"