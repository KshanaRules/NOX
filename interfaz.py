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
                
        self.archivo = tk.Frame(self, width=300, height=300, bg="", borderwidth=1,colormap="new")
        self.graficas = tk.Frame(self, width=300, height=300, bg="", borderwidth=1)
        
        self.archivo.pack(side=tk.LEFT)
        self.graficas.pack(side=tk.RIGHT)
        
        self.boton_archivo = tk.Button(self.archivo, text="Blue", fg="gray")
        self.boton_archivo.pack(side = tk.LEFT)
        
        self.image = tk.PhotoImage(file="Chanos.png")
        tk.Label(self.graficas, image=self.image).pack()
        
        



if __name__ == "__main__":
    app = App()
    app.mainloop()