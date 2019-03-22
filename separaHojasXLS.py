#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:54:01 2019

@author: administrador
"""

import pandas as pd

datos = pd.read_excel("PruebaEspecies.xlsx")
xls = pd.ExcelFile("PruebaEspecies.xlsx")
NumEspecies = len(xls.sheet_names) 


ciclo = 0
for file in xls.sheet_names:
    ArchivoCSV = pd.read_excel("PruebaEspecies.xlsx",ciclo)
    ArchivoCSV = ArchivoCSV[0:50]
    ArchivoCSV.to_excel('DatosXLS/' + 'Group' +  str(ciclo+1) + '.xlsx')
    ciclo = ciclo + 1




