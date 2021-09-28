from tkinter import *
from tkinter import messagebox
from factory import process
from tkinter import ttk
window = Tk()

class mainWindow:

    def showInfo():
        messagebox.showinfo("Informacion", "Introduccion a la computacion y programacion 2 \nNombre: Kevyn Josué Girón Jiménez \nCarnet: 201700653 \nSeccion C")

    def wns():
        window.title("Proyecto 2")
        window.geometry("1000x500")
        window.resizable(0,0)

        tabla = ttk.Treeview(window, columns = ('#1', '#2', '#3'))
        tabla['show'] = 'headings'
        tabla.heading("#1", text = "tiempo")
        tabla.heading("#2", text = "Linea 1")
        tabla.heading("#3", text = "Linea 2")

        archivo = Button(window, text="Archivo", command = lambda: mainWindow.selectFile(window, tabla))
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

        tabla.place(x = 285, y = 160)

        window.mainloop()

    def selectFile(w, tabla):
        #w.destroy()
        win = Tk()
        win.title("Subir xml")
        win.geometry("400x200")
        win.resizable(0,0)

        archivo = Button(win, text="Cargar Maquina", command = lambda : process.readMachine(tabla))
        reportes = Button(win, text="Cargar simulacion", command = lambda : process.readSimulation())
        salir = Button(win, text="Salir", command = lambda : win.destroy())
        
        lbl1 = Label(win, text = " ")
        lbl2 = Label(win, text = " ")
        lbl3 = Label(win, text = " ")
        
        lbl1.pack()
        archivo.pack()
        lbl2.pack()
        reportes.pack()
        lbl3.pack()
        salir.pack()

        window.mainloop()

mainWindow.wns()