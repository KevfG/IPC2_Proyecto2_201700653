from tkinter import *
from tkinter import messagebox
from factory import process

class mainWindow:

    def showInfo():
        messagebox.showinfo("Informacion", "Introduccion a la computacion y programacion 2 \nNombre: Kevyn Josué Girón Jiménez \nCarnet: 201700653 \nSeccion C")

    def wns():
        window = Tk()
        window.title("Proyecto 2")
        window.geometry("800x500")
        window.resizable(0,0)

        archivo = Button(window, text="Archivo", command = lambda: mainWindow.selectFile(window))
        reportes = Button(window, text="Reportes")
        ayuda = Button(window, text="Ayuda", command = lambda: mainWindow.showInfo())
        accion = Button(window, text="SmartWatch")

        lbl1 = Label(window, text = "Componentes necesarios")
        lbl2 = Label(window, text = "Texto de ejemplo", background = "gray")
        
        archivo.place(x = 0, y = 0, width = 100, height = 30)
        reportes.place(x = 100, y = 0, width = 100, height = 30)
        ayuda.place(x = 200, y = 0, width = 100, height = 30)
        accion.place(x = 100, y = 70, width = 150, height = 70)

        lbl1.place(x = 105, y = 160)
        lbl2.place(x = 105, y = 180, width = "150", height = "200")
        window.mainloop()

    def selectFile(w):
        w.destroy()
        window = Tk()
        window.title("Subir xml")
        window.geometry("400x200")
        window.resizable(0,0)

        archivo = Button(window, text="Cargar Maquina", command = lambda : process.readMachine())
        reportes = Button(window, text="Cargar simulacion", command = lambda : process.readSimulation())
        salir = Button(window, text="Salir", command = lambda : mainWindow.backMain(window))
        
        lbl1 = Label(window, text = " ")
        lbl2 = Label(window, text = " ")
        lbl3 = Label(window, text = " ")
        
        lbl1.pack()
        archivo.pack()
        lbl2.pack()
        reportes.pack()
        lbl3.pack()
        salir.pack()

        window.mainloop()

    def backMain(w):
        w.destroy()
        mainWindow.wns()

mainWindow.wns()