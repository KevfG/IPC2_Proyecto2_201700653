from tkinter import messagebox
from tkinter.filedialog import test
from typing import Text

class nodo:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class listaEnlazada:
    # ----------------------------------Lo principal en la lista---------------------------------
    def __init__(self):
        self.head = None

    def insertar(self, nuevo):
        #messagebox.showinfo("a", "si sirve")
        if not self.head:
            self.head = nodo(data=nuevo)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = nodo(data=nuevo)

    def print(self, tabla):
        aux = self.head
        t = 0
        while aux != None:
            print(aux.data.nombre)
            y = (t, aux.data.nombre, aux.data.elaboracion)
            tabla.insert("", 0, values = y)
            aux = aux.next
# -------------------------------------------Fin--------------------------------------------------