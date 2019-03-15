import pandas as pd
import os
import matplotlib.pyplot as plt



def menor(datos):
    poz = 0
    buscaRango = 0
    busqueda = True
    salir = False
    while (busqueda):
        for dato in datos:
            if (dato>=-.19+(-1*buscaRango) and dato <=.21+buscaRango): #Establece un umbral en X y Y respcto a 0
                if((dato>=0 and datos[poz+1]<=0) or (dato<=0 and datos[poz+1]>=0)): #Valida que el soguiente dato no se ecuentre dentro del umbra, si se cumple rompe el ciclo y regresa valores para graficar
                    salir = True
                    break
            poz = poz +1
            
        if(salir==True):
            busqueda = False
        else:
            buscaRango = buscaRango + .3
            poz = 0
            
    return [dato,poz]

def leerArchivo(filename):  
    xls = pd.ExcelFile('PruebaEspecies.xlsx')
    especies = pd.read_excel(filename)
    NumEspecies = len(xls.sheet_names)
    #NumEspecies = 4
    """
    PASO 1: Agrupa todos los valores, de todas las especies del archivo de la hoja de cálculo. Se organiza para aplicar las operaciones necesarias 
    para obtener los datos que serán utilizados en subsecuentes operaciones
    """
    print("1")
    ciclo = 0
    for file in xls.sheet_names:
        print("2")
        ArchivoCSV = pd.read_excel('PruebaEspecies.xlsx',ciclo)
        A = (ArchivoCSV['Asc import'] + ArchivoCSV['Asc flow'] + ArchivoCSV['Asc export'] + ArchivoCSV['Asc resp']) * ArchivoCSV['Capacity'] / 100
        O = (ArchivoCSV['Ovh import'] + ArchivoCSV['Ovh flow'] + ArchivoCSV['Ovh export'] + ArchivoCSV['Ovh resp']) * ArchivoCSV['Capacity'] / 100
        C = A + O 
        Entropia = 1-(A/C)
        CB = ArchivoCSV["Catch"] / ArchivoCSV["Biomass"]
        BP = ArchivoCSV["Biomass"] / ArchivoCSV["Prod"]
        
        ArchivoCSV['AA'] = A
        ArchivoCSV['O'] = O
        ArchivoCSV['C'] = C
        ArchivoCSV['Entropia'] = Entropia
        ArchivoCSV['C/B'] = CB
        ArchivoCSV['B/P'] = BP
        ArchivoCSV['TL'] = especies.loc[ciclo+1][1]
        ArchivoCSV['X-Xmin'] = ""
        ArchivoCSV['Rent'] = ""
        ArchivoCSV['Group name'] = especies.loc[ciclo+1][0]
    
        if ciclo==0:
            temp = ArchivoCSV
            dim = len(temp)
                
        pos = 0
        while pos < 50 and ciclo!=0:        
            temp.loc[dim] = ArchivoCSV.loc[pos]
            pos = pos + 1
            dim = dim + 1
           
        print("3")
        if ciclo==len(xls.sheet_names)-(50-NumEspecies):
            break
        
        ciclo = ciclo + 1
        dim = len(temp)
    
    """
    PASO 2: Agregar la columna X-Xmin y Rent, para obtener los valores se utilizan los datos de la entropía que fueron generados en el PASO 1
    """
    print("4")
    Prom_ent= temp['Entropia'].min()
    temp['X-Xmin']  = temp['Entropia'] - Prom_ent
    Prom_XXmin = temp['X-Xmin'].max()
    temp['Rent'] = temp['X-Xmin'] / Prom_XXmin
    
    """
    PASO 3: Genera la la tabla de relación nivel trófico (TL) vs Tasa de cosecha (HR)
    """
    
    
    
    if (os.path.exists("Datos") == False):
        os.mkdir("Datos")
        
    ArchivoCSV=temp
    esp = 0
    while esp < NumEspecies:
        print("5")

        
        filtro = especies.loc[esp+1][0]
        l = ["Especies","TL"]
        c = 0
        for contador  in range(0,100,2):
            l.append(contador/100)
            c= c + 1
            
        list_especie = especies["Group name"][esp+1]
        list_trofico = especies["Trophic level"][esp+1]
    
        list_datos = ArchivoCSV['Rent'][ArchivoCSV['Group name'] == filtro] 
                      
        toL = list_datos.tolist()
        tolAvg = list_datos.mean()
        tolStd = list_datos.std()
        toL.insert(0, list_trofico)
        toL.insert(0, list_especie)    
        toL.append(tolAvg)
        toL.append(tolStd)
        l.extend(["avg","std"])
        
        if esp == 0:
            df2 = pd.DataFrame([toL] , columns=l)   
        else:
            df2.loc[esp] = toL
            
        esp = esp + 1
        
    """
    PASO 4: Genera la la tabla de relación nivel trófico (TL) vs Tasa de cosecha (HR) - FINALES
    """
    print("6")
    esp = 0
    while esp < NumEspecies:
        print("7")        
        filtro = especies.loc[esp+1][0]
        l = ["Especies","TL"]
        c = 0
        for contador  in range(0,100,2):
            l.append(contador/100)
            c= c + 1
            
        list_especie = especies["Group name"][esp+1]
        list_trofico = especies["Trophic level"][esp+1]
       
        d = (df2.loc[esp][2:52]-df2.loc[esp][-2])/df2.loc[esp][-1]     
        toL = d.tolist()
        
        toL.insert(0, list_trofico)
        toL.insert(0, list_especie)    
       
        if esp == 0:
            dfF = pd.DataFrame([toL] , columns=l)   
        else:
            dfF.loc[esp] = toL
            
        esp = esp + 1
        
    print("8")        
    df2.to_excel("Datos/" + "operaciones_HR.xlsx")
    dfF.to_excel("Datos/" + "HR_TL.xlsx")
    print("9")       
       
    Datos = []  #Se almacena cada reistro de cada especie para su procesamiento
    nEspecies = 0
    nEspecies2 = nEspecies + 1
    archivoXLS = dfF  #Leer el archivo que contiene 12 especies disponibles, se busca determinar la entropía con los valores en cada una       
    pos  = 0 # Posición del renglón para obtener el nombre y datos de la especie, PANDAS omite el primer rengón del archivo (A,B,C...), de lo contrario toma como posición 0 a (Groups name, , 0 , 0.02....)
    pos2 = pos + 1
    
    
    columnas = archivoXLS.columns #Obtiene el nomnre de las columnas del archivo de excel
    especies = columnas[0:1] #Obtiene valor de columna 1, nombre de las especies  'Especies'
    columnas = columnas[2:-2] #Obtiene los valores de columnas con Tase de Cosecchas (HR), aplica filtro a textos
    
    
    if (os.path.exists("Graph") == False):
        os.mkdir("Graph")
    
    while(nEspecies<NumEspecies): #Lectura de cada una de las especies para procesar y graficar datos 
        Nespecie = archivoXLS[nEspecies:nEspecies2][especies].values  #Obtiene el arreglo de especies, filtrando por 'Group name'
        Nespecie = Nespecie[0][0] #Extrae el valor del arreglo, tipo string
    
        
        HR = archivoXLS[pos:pos2][columnas].values  #Obtiene los valores de HR para cada especie
        ren,col = HR.shape  #Tamaño de los datos ren=1, col= 50  => 1 especie, 50 HR
    
        #Llenar arreglo para almacenar valores de cada HR de especie
        c = 0
        while (c<col):
            Datos.append(HR[0,c])
            c = c+1
            
        # Regresa posición del cambio de valores en HR.  Obtiene la posicón y valor de ubicación. 
        dato,poz = menor(Datos)
        
        
        #Grafíca especie 
        fig, ax = plt.subplots()
    
        ax.plot(columnas, Datos, 'go--',linewidth=.5,markersize=3, label='HR')
        ax.annotate('CAMBIO',xy=(columnas[poz+1],dato),xytext=(.6,.504),arrowprops=(dict(facecolor='black',arrowstyle='simple')))
        ax.annotate('XXX',xy=(columnas[poz+1],dato),xytext=(.3,.304),arrowprops=(dict(facecolor='red',arrowstyle='simple')))
     
        ax.set_facecolor('#eafff5')
        ax.tick_params(labelcolor='tab:red')
    
    
        plt.title(Nespecie)
        plt.xlabel("Tasa de cosecha")
        plt.ylabel("Cambio de entropía")
        fig.savefig("graph/" + Nespecie + '.png')
        plt.legend()
        plt.show()
        nEspecies = nEspecies + 1
        nEspecies2 = nEspecies + 1
        Datos = []
        pos = pos +1
        pos2 = pos2 + 1