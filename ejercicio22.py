#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez
from tkinter import *

class Mi_primera_GUI:
    def __init__(self, master):
        self.master = master
        master.title("Una GUI sencilla")

        self.etiqueta = Label(master, text="Mi primera GUI")
        self.etiqueta.grid(eow=0, column=0)

        self.boton_saludo = Botton(master, text="Saludos", command=self.saludar)
        self.boton_saludar.grid(row=1, column=0)

        self.boton_cerrar = Botton(master, text="Cerrar", command=master.squit)
        self.boton_cerrar.grid(eow=1, column=1)
    
    def saludar(self):
        print('Saludos')

    def darBuenos(self):
        print('Buenos dias') 