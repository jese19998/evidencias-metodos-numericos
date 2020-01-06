#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez
from tkinter import *

class MiPrimeraGUI:
    def __init__(self,master):
        self.master = master 
        master.title("Una GUI sencilla")
        
        self.etiqueta = Label(master, text=" Mi primera GUI")
        self.etiqueta.grid(row=0, column=0)
        
        self.boto_saludo = Button (master, text="Saludo", command=self.saludar)
        self.boto_saludo.grid(row=1, column=0)
        
        self.boto_saludo = Button(master, text="Despedirme", command=self.despedir)
        self.boto_saludo.grid(row=2, column=0)
        
        
        self.boto_cerrar= Button (master, text="Cerrar", command=master.quit)
        self.boto_cerrar.grid(row=3, column=1)
        
    def saludar(self):
        print('Saludos')
        
    def despedirme(self):
        print('adios')
        
    def darBuenos(self):
        print('Buenos Dias')
        
root = Tk()
mi_gui = MiPrimeraGUI(root)
root.mainloop()