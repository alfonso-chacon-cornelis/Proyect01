import tkinter as tk
from tkinter import messagebox
from tkinter import BOTH
from tkinter.ttk import Combobox
from functools import partial
from random import randint
import time
from tkinter import *
white = "#FFFFFF"
black = "#000000"
class App:
    def __init__(self, master):
        # Configuración de la ventana
        master.title("Algoritmo Quine.McCluskey")
        master.geometry("1320x800")
        master.configure(bg="gray25")
        master.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.data_with_parity = []
        Fibonacci = Toplevel()
        Fibonacci.title("Tarea Corta 1: Fibonacci")
        Fibonacci.geometry("910x600")
        Fibonacci.withdraw()
    
        Fibonacci.resizable(False, False)

        # Scroll
        self.canvasScroll = tk.Canvas(master, bg="gray25")
        self.canvasScroll.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.scrollBar = tk.Scrollbar(master, command=self.canvasScroll.yview)
        self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvasScroll.config(yscrollcommand=self.scrollBar.set)

        # Frames para dividir la interfaz en secciones

        self.mainFrame = tk.Frame(self.canvasScroll, bg="gray25")

        self.basesFrame = tk.Frame(self.mainFrame, bg="gray15")
        self.basesFrame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)


        self.parityFrame = tk.Frame(self.mainFrame, bg="gray15")
        self.parityFrame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)


        self.canvasScroll.create_window((0, 0), window=self.mainFrame, anchor="nw")
        self.mainFrame.bind(
            "<Configure>",
            lambda e: self.canvasScroll.configure(
                scrollregion=self.canvasScroll.bbox("all")
            ),
        )
        self.mainFrame.bind_all(
            "<MouseWheel>",
            lambda e: self.canvasScroll.yview_scroll(
                int(-1 * (e.delta / 120)), "units"
            ),
        )

        # Labels
        self.label1 = tk.Label(
            self.basesFrame,
            text="Ingrese las Variables separadas por un espacio",
            bg="gray15",
            fg="cyan",
            font=("Arial Black", 12),
        ).grid(row=0, column=0, padx=5, sticky=tk.W)




       # Entry
        entry = tk.Entry(
            self.basesFrame, bg="gray15", fg="gray70", font=("Arial Black", 12)
        )
        entry.grid(row=0, column=1, sticky=tk.W)
        
       


        # Funcion del boton update
        def update_button():
            input = entry.get()
            print("\si")
            #valor = tk.Label(mostrar)
            
        self.update = tk.Button(
            self.basesFrame,
            text="ACEPTAR",
            bg="gray25",
            fg="cyan",
            font=("Arial Black", 10, "bold"),
            command=update_button,
        )
        self.update.grid(row=1, column=2, padx=10, sticky=tk.W)
        


    def on_closing(self):
        root.destroy()


# Inicializa la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

