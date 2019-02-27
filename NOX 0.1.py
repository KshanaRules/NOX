import pandas as pd
import matplotlib.pyplot as plt


def menor(datos):
    poz = 0
    for dato in datos:
        if (dato>=-.19 and dato <=.21): #Establece un umbral en X y Y respcto a 0
            if((dato>=0 and datos[poz+1]<=0) or (dato<=0 and datos[poz+1]>=0)): #Valida que el soguiente dato no se ecuentre dentro del umbra, si se cumple rompe el ciclo y regresa valores para graficar
                break
        poz = poz +1
    return [dato,poz]


Datos = []  #Se almacena cada reistro de cada especie para su procesamiento
nEspecies = 0
nEspecies2 = nEspecies + 1
archivoXLS = pd.read_excel('datos.xlsx')  #Leer el archivo que contiene 12 especies disponibles, se busca determinar la entropía con los valores en cada una       

pos  = 16 # Posición del renglón para obtener el nombre y datos de la especie, PANDAS omite el primer rengón del archivo (A,B,C...), de lo contrario toma como posición 0 a (Groups name, , 0 , 0.02....)
pos2 = pos + 1


columnas = archivoXLS.columns #Obtiene el nomnre de las columnas del archivo de excel
especies = columnas[0:1] #Obtiene valor de columna 1, nombre de las especies  'Group name'
columnas = columnas[2:-2] #Obtiene los valores de columnas con Tase de Cosecchas (HR), aplica filtro a textos


while(nEspecies<12): #Lectura de cada una de las especies para procesar y graficar datos 
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
    
    ax.set_facecolor('#eafff5')
    ax.tick_params(labelcolor='tab:red')


    plt.title(Nespecie)
    plt.xlabel("Tasa de cosecha")
    plt.ylabel("Cambio de entropía")
    fig.savefig(Nespecie + '.png')
    plt.legend()
    plt.show()
    nEspecies = nEspecies + 1
    nEspecies2 = nEspecies + 1
    Datos = []
    pos = pos +1
    pos2 = pos2 + 1
