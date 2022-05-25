from vista import *
from tkinter import Tk

class Controlador:
    def __init__(self, root_w):
        self.root=root_w
        self.objeto_vista=Ventana(self.root)

if __name__=="__main__":
    root = Tk()
    
    mi_app=Controlador(root)


    root.mainloop()