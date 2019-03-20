#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 13:54:00 2019

@author: administrador
"""

import prueba_ImportarClasesFunciones as Test
import tkinter as tk
import tkinter.filedialog as f
import pandas as pd
import os
import shutil



class App(tk.Tk):
    def __init__(self):
        try:
            shutil.rmtree("Datos")
        except:
            pass
 
        try:               
            shutil.rmtree("Graph")
        except:
            pass
        
        super().__init__()
        self.especiesFile = ""
        self.dir = os.getcwd()
        self.title("Relación HR y TL")
        self.configure(width=800, height=500)
        opciones = tk.LabelFrame(self, text="Opciones")
        opciones.place(x=10, y=10, height=450)
        self.cont = 1
 
        self.seccionGraf = tk.LabelFrame(self, text="Sección de gráficas")
        self.seccionGraf.place(x=200, y=10, height=450, width=550)
       
        self.btn_archivo  = tk.Button(opciones, text="Cargar archivo", command=self.cargaDatos)
        self.btn_archivo.pack(padx=11, pady=11)
       
        self.btn_archivo2  = tk.Button(opciones, text="Cargar especies", command=self.cargaDatos2)
        self.btn_archivo2.pack(padx=21, pady=21)

        
        self.btn_exportar = tk.Button(opciones, text="Gráficas/excel", command=self.muestraGraficas)
        self.btn_exportar.pack(padx=30, pady=50)
        
        self.btn_regresa = tk.Button(self.seccionGraf, text="<", state="disabled", command=self.regresaGraf)
        self.btn_regresa.place(x=10, y=400)       
        self.btn_siguiente = tk.Button(self.seccionGraf, text=">", command=self.siguienteGraf)
        self.btn_siguiente.place(x=500, y=400)  
        
        
        
    def cargaDatos(self):
               
        filetypes = (("Plain text files", "*.txt"),
                     ("Excel", "*.xls *.xlsx"),
                     ("All files", "*"))
        filename = f.askopenfilename(title="Open file", initialdir=".", filetypes=filetypes)
        if filename:
            xls = pd.ExcelFile(filename)
            NumEspecies = len(xls.sheet_names)
            Test.leerArchivo(filename,NumEspecies, self.especiesFile)

    def cargaDatos2(self):
        filetypes = (("Plain text files", "*.txt"),
                     ("Excel", "*.xls *.xlsx"),
                     ("All files", "*"))
        filename = f.askopenfilename(title="Open file", initialdir=".", filetypes=filetypes)
        if filename:
            print(filename)
            self.especiesFile = filename
            
        
                              
    def muestraGraficas(self):      
        if (os.path.exists("Graph") == False):
            os.mkdir("Graph")
        else:
            grafArray = os.listdir(path="Graph")
            grafLen = len(os.listdir(path="Graph")) - 1
            
        if(self.cont==1):
            self.btn_regresa['state'] = 'disabled'    
        elif(self.cont>1):
            self.btn_regresa['state'] = 'normal'   
 
        if(self.cont==grafLen):
            self.btn_siguiente['state'] = 'disabled'    
        elif(self.cont!=grafLen):
            self.btn_siguiente['state'] = 'normal'    
                                
        self.imagen = tk.PhotoImage(file=self.dir+"/Graph//"+grafArray[self.cont])
        tk.Label(self.seccionGraf, image=self.imagen).place(x=75, y=75) 
        
    def regresaGraf(self):
        self.cont = self.cont -1
        self.muestraGraficas()

    def siguienteGraf(self):      
        self.cont = self.cont + 1
        self.muestraGraficas()
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()