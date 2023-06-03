import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import math
import os


def precio_dolar_historico():
    clear()
    year_ini = 1913
    while year_ini not in range(1914,2024):
        try:
            year_ini= int(input('Desde: Tipea un año desde 1914 en adelante ==> '))
        except ValueError:
            print('Eso que fue?')

        if year_ini not in range(1914,2024):
            print('Debes elegir un año comprendido entre 1914 y 2020, vuelve a intentarlo')

    year_fin = year_ini - 1
    while year_fin not in range(year_ini,2024):
        try:
            year_fin= int(input('Hasta: Tipea un año desde el año que elegiste en el punto anterior en adelante ==> '))
        except ValueError:
            print('Eso que fue?')

        if year_fin not in range(year_ini,2024):
            print('Debes elegir un año comprendido entre 1914 y 2020, vuelve a intentarlo')


    df = pd.read_csv('./datasets/dolarPrecio.csv', sep=';') #leemos
    df = df.copy()#por sia
    df = df[(df['Year']>=int(year_ini)) & (df['Year']<=int(year_fin))]#filtramos
    #data = df.set_index('Year').T.to_dict()
    df_data= df.loc[:,'Ene':'Dic']#eliminamos columna year

    values = np.array(df_data, dtype='float16').reshape(-1) #haemos un array de una dimension de todos los datos
    
    for column in df_data.columns: #for para reemplazar todos los valoes de df_data por los valores del año
     df_data[column] = df['Year']

    labels = np.array(df_data, dtype='int').reshape(-1)

    fig, ax = plt.subplots()
    
    ax.plot(labels, values)
   
    plt.ylim(-1,600) 
    plt.xticks(range(year_ini, year_fin, 10))
    plt_name = 'Valor de Dolar Oficial desde ' + str(year_ini) + ' hasta ' + str(year_fin)
    plt.title(plt_name)
    plt.savefig('./charts/'+plt_name +'.jpg')
    plt.show()

    finalizar_programa()


def inflacion_mundial():
    clear()
    df_inflacion = pd.read_csv('./datasets/inflacionMundial.csv', skiprows=4) #con skiprow  no leemos las primeras 4 filas (la tabla comienza en la 5ta)
    df_inflacion = df_inflacion.drop(columns=['Unnamed: 67']) #pandas lee una ultima columna que realmente esta vacia
    countries = np.array(df_inflacion['Country Name'])


    array_country = []
    def elegir():
        country = 0
        while country not in countries:
            
            for i in range(0, len(countries)-1):
                print(str(i+1) + ' - ' + str(countries[i]) )
            
            print()
            print('Elige un Pais, o escribe su nombre')
            eleccion = input('Tipea el nombre de un pais (debe ser exactamente igual que en listado), o el numero que lo representa ==> ')
            if len(eleccion) in range(1,4):
                if int(eleccion) in range(0, len(countries)):
                    country = countries[int(eleccion)-1]
                    array_country.append(country)
                else:
                    print('Elige nuevamente, creo que te equivocaste')
                
            elif len(eleccion) > 4:
                if eleccion.capitalize() in countries:
                    country = eleccion.capitalize()
                    array_country.append(country)
                else:
                    print('Elige nuevamente, creo que te equivocaste')  
            
        return array_country

    paises = []
    otro = ''
    while otro != '2':
        paises = elegir()
        clear()
        for pais in paises:
            print(pais, end=', ')
        otro = input('\nQuieres elegir otro pais \n1 - Si \n2 - No \nTipea ==> ')
    
    df_inflacion2 = df_inflacion[df_inflacion['Country Name'].isin(paises)]
    df = df_inflacion2.iloc[:,4:].transpose()
    df.index = pd.to_numeric(df.index)

    df.columns = paises

    sns.relplot(data = df, kind='line')
    plt.ylim(-1,100)
    paises_titulo = (', '.join(map(str, paises)))
    plt.title('Inflación Historica: ' + paises_titulo)
    plt.savefig('./charts/'+'Inflación Historica: ' + paises_titulo +'.jpg')
    plt.show()
    clear()
    finalizar_programa()


def precio_internacional_productos():
    clear()
    df = pd.read_csv('./datasets/indicePrecioProducto.csv')
    products = list(df.columns.values)
    products.pop(0)

    array_productos = []

    def elegir():
        product = ''
        while product not in products:
            
            for p in range(1, len(products)+1):
                print(str(p) + ' - ' + str(products[p-1].capitalize().replace('_',' ')))

            print('\n \n' + '***'*3 + "Elige una Opcion"+ '***'*3 + '\n')
            print('Elige un Producto, o escribe su nombre')
            eleccion = input('Tipea el nombre de un producto (debe ser exactamente igual que en listado), o el numero que lo representa ==> ')
            if len(eleccion) in range(1,3):
                try:
                    if int(eleccion) in range(1, len(products)+1):
                        product = products[int(eleccion)-1]
                        array_productos.append(product)
                    else:
                        print('Elige nuevamente, creo que te equivocaste')
                except ValueError:
                    print('¿Y eso que fue?')
            elif len(eleccion) > 2:
                product = eleccion.lower().replace(' ','_')
                if product in products:
                 array_productos.append(product)
                else:
                 print('Elige nuevamente, creo que te equivocaste')
                

        return array_productos

    productos_elegidos = []
    otro = ''
    while otro != '2':
        productos_elegidos = elegir()
        for producto in productos_elegidos:
            print(producto.capitalize().replace('_',' '), end=', ')
        otro = input('\nQuieres elegir otro producto \n1 - Si \n2 - No \nTipea ==> ')

    name_product = [producto.capitalize().replace('_',' ') for producto in productos_elegidos]
    name_product_str = (', '.join(map(str, name_product)))
    df2 = df[productos_elegidos]
    df2['Tiempo'] = df['indice_tiempo'].map(lambda x: str(x)[0:4])
    df2['Tiempo'] = df2['Tiempo'].astype('int')
    df3 = df2.set_index('Tiempo')
    clear()
    print('****'*3 + '\nAguardo un momento por favor, se esta generando su grafica\n' + '****'*3)
    sns.lineplot(data = df3)
    plt_name = 'Evolucion del Precio de '+ name_product_str
    plt.title(plt_name)
    plt.savefig('./charts/'+plt_name +'.jpg')

    plt.show()
    finalizar_programa()

def finalizar_programa():
    clear()
    print('\n \n')
    print('***'*2 + 'Se guardo la imagen en la carpeta charts' + '***'*2 + '\n')
    deseo = 0
    while deseo not in range(1,3):
        print('1 - Deseo volver al menu principal \n2 - Deseo Salir del programa')

        try:
            deseo = int(input('Tipee el numero de su eleccion ==> '))
        except ValueError:
            print('Eso que fue?')
        if deseo not in range(1,3):
            print('Debes elegir una opcion Valida, vuelve a intentarlo')

    if deseo == 1:
        menu()
    elif deseo ==2:
        clear()
        exit()




def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")




def menu():
    clear()
    print('*******'*10)
    print('*******'*10 + '\n')
    


    print('1 - Valor historico del dolar en Argentina \n')
    print('2 - Evolucion de la inflacion en uno o varios países \n')
    print('3 - Precio internacional de algun producto en el tiempo \n \n')
    print('4 - Salir del programa \n \n')
    
    eleccion = 0

    while eleccion not in range(1,5):
        try:
            eleccion = int(input('Escribe el numero de la opcion ==> '))
        except ValueError:
            print('Eso que fue?')

        if eleccion not in range(1,5):
            print('Debes elegir una opcion Valida, vuelve a intentarlo')
    
    match(eleccion):
        case 1:
            clear()
            precio_dolar_historico()
        case 2:
            clear()
            inflacion_mundial()
        case 3:
            clear()
            precio_internacional_productos()
            
        case 4:
            clear()
            exit()
        
    clear()

if __name__=='__main__':
    clear()
    menu()