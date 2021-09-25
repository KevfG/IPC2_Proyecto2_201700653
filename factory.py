from tkinter import filedialog
import xml.etree.ElementTree as ET
from tkinter import messagebox

class machine:

    def __init__(self, cantidad, produccion, productos):
        self.cantidad = cantidad
        self.produccion = produccion
        self.productos = productos

class product:

    def __init__(self, nombre, elaboracion):
        self.nombre = nombre
        self.elaboracion = elaboracion

class lineas:

    def __init__(self, numero, cantidad, tiempo):
        self.numero = numero
        self.cantidad = cantidad
        self.tiempo = tiempo

class process:

    def readMachine():
        machine = filedialog.askopenfilename(title = "Abrir maquina", filetypes = [('text files', '*.xml'),('All files', '*')])
        xml = ET.parse(machine)
        if xml.getroot().tag == 'Maquina':
            #print(xml.getroot().tag)
            cantidad = 0
            lineas = None
            producto = None
            for i in xml.getroot():
                print(i)
                if i.tag == "CantidadLineasProduccion":
                    cantidad = int(i.text)
                    #print("cantidad de lineas: " + str(cantidad))
                if i.tag == "ListadoLineasProduccion":
                    numero = ""
                    cantidad_ = ""
                    tiempo = ""

                    for j in i:
                        for k in j:
                            if k.tag == "Numero":
                                #print("Numero: " + k.text.strip())
                                numero = k.text.strip() + "|" + numero
                            if k.tag == "CantidadComponentes":
                                #print("Cantidad: " + k.text.strip())
                                cantidad_ = k.text.strip() + "|" + cantidad_
                            if k.tag == "TiempoEnsamblaje":
                                #print("Tiempo: " + k.text.strip())
                                tiempo = k.text.strip() + "|" + tiempo

                if i.tag == "ListadoProductos":
                    nombre = ""
                    elaboracion = ""
                    for j in i:
                        if j.tag == "Producto":
                            for k in j:
                                if k.tag == "nombre":
                                    nombre = k.text.strip() + "|" + nombre
                                if k.tag == "elaboracion":
                                    elaboracion = k.text.strip() + "|" + elaboracion
                    print("Nombres: " + nombre)
                    print("Elaboracion: " + elaboracion)

                        
        else:
            messagebox.showerror("Error", 'El archivo no es de tipo "Maquina"' )

    def readSimulation():
        machine = filedialog.askopenfilename(title = "Abrir maquina", filetypes = [('text files', '*.xml'),('All files', '*')])
        xml = ET.parse(machine)
        if xml.getroot().tag == 'Simulacion':
            print(xml.getroot().tag)
        else:
            messagebox.showerror("Error", 'El archivo no es de tipo "Simulacion"' )

    