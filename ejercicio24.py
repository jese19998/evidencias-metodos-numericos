#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez
from tkinter import *
 
class MiprimeraGUI:
    def __init__(self,master):
        self.master=master
        master.title("Una GUI sencilla")
        
        
        self.etiqueta=Label(master, text="Mi primera GUI")
        self.etiqueta.grid(row=0, column=0)
        
        self.boton_saludo=Button(master, text="saludo",command=self.saludar)
        self.boton_saludo.grid(row=1, column=0)
        
        self.boton_despedirce=Button(master, text="despedirce",command=self.despedirce)        
        self.boton_despedirce.grid(row=2, column=0)
        
        self.boton_cerrar=Button(master, text="cerrar", command=master.quit)
        self.boton_cerrar.grid(row=3, column=0)
        
    def saludar(self):
        print("saludos!")
    def despedirce(self):
        print("adios")

root=Tk()
mi_gui=MiprimeraGUI(root)
root.mainloop()