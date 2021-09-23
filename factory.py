from tkinter import filedialog
import xml.etree.ElementTree as ET
from tkinter import messagebox

class process:

    def readMachine():
        machine = filedialog.askopenfilename(title = "Abrir maquina", filetypes = [('text files', '*.xml'),('All files', '*')])
        xml = ET.parse(machine)
        if xml.getroot().tag == 'Maquina':
            print(xml.getroot().tag)
        else:
            messagebox.showerror("Error", 'El archivo no es de tipo "Maquina"' )

    def readSimulation():
        machine = filedialog.askopenfilename(title = "Abrir maquina", filetypes = [('text files', '*.xml'),('All files', '*')])
        xml = ET.parse(machine)
        if xml.getroot().tag == 'Simulacion':
            print(xml.getroot().tag)
        else:
            messagebox.showerror("Error", 'El archivo no es de tipo "Maquina"' )

    