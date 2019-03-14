#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 13:54:00 2019

@author: administrador
"""


import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Relación HR y TL")
        self.configure(width=800, height=500)
        opciones = tk.LabelFrame(self, text="Opciones")
        opciones.place(x=10, y=10, height=450)

        seccionGraf = tk.LabelFrame(self, text="Sección de gráficas")
        seccionGraf.place(x=200, y=10, height=450, width=550)


        
        btn_archivo  = tk.Button(opciones, text="Cargar archivo")
        btn_archivo.pack(padx=11, pady=11)
        btn_exportar = tk.Button(opciones, text="Exportar a excel")
        btn_exportar.pack(padx=30, pady=50)
        
        self.imagen = tk.PhotoImage(file="Chanos.png")
        #tk.Label(seccionGraf, image=self.imagen).pack(padx=250, pady=100)       
        tk.Label(seccionGraf, image=self.imagen).place(x=75, y=75)       
        
if __name__ == "__main__":
    app = App()
    app.mainloop()