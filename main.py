import matplotlib.pyplot as plt
import pandas as pd
import math
import os


def precio_dolar_historico():
    clear()
    year = 1913
    while year not in range(1914,2024):
        try:
            year= int(input('Tipea un año desde 1914 en adelante ==> '))
        except ValueError:
            print('Eso que fue?')

        if year not in range(1914,2024):
            print('Debes elegir un año comprendido entre 1914 y 2020, vuelve a intentarlo')


    df = pd.read_csv('./datasets/dolarPrecio.csv', sep=';')
    df = df[df['Year']>int(year)]
    data = df.set_index('Year').T.to_dict()

    labels = []
    for key in data.keys():
        for i in data[key].keys():
            labels.append(key)

    values= []
    for item in data.values():
        for x in item.values():
            if math.isnan(x):
                values.append(0)
            else:
                values.append(x)


    fig, ax = plt.subplots()
    
    ax.plot(labels, values)
   
    plt.ylim(-1,600) 
    plt.xticks(range(year, 2023, 10))
    plt_name = 'Valor de Dolar Oficial desde ' + str(year)
    plt.title(plt_name)
    plt.savefig('./charts/'+plt_name +'.jpg')
    plt.show()

    finalizar_programa()


def inflacion_mundial():
    clear()
    df = pd.read_csv('./datasets/inflacionMundial.csv', skiprows=4) #con skiprow  no leemos las primeras 4 filas (la tabla comienza en la 5ta)
    df_dict = df.to_dict('records')


    countries = [item['Country Name'] for item in df_dict]

    country = 9
    while country not in countries:
        
        for i in range(0, len(countries)-1):
            print(str(i+1) + ' - ' + str(countries[i]) )
        
        print()
        print('Elige un Pais, o escribe su nombre')
        eleccion = input('Tipea el nombre de un pais (debe ser exactamente igual que en listado), o el numero que lo representa ==> ')
        if len(eleccion) in range(1,4):
            if int(eleccion) in range(0, len(countries)):
                country = countries[int(eleccion)-1]
            else:
                print('Elige nuevamente, creo que te equivocaste')
            
        elif len(eleccion) > 4:
            country = eleccion.capitalize()


    df = df[df['Country Name'] == country]
    df = df.drop(columns=['Unnamed: 67']) #pandas lee una ultima columna que realmente esta vacia
    data_country = df.to_dict('records')

    labels = [key for key in data_country[0].keys()]
    del labels[0:4:1]
    del labels[len(labels)-1]
    labels = [int(label)  if label!='' else 0 for label in labels]

    values = [values for values in data_country[0].values()]
    del values[0:4:1]
    del values[len(values)-1]
    
    values = [float(value)  if value!='' else 0 for value in values]

   
    fig, ax = plt.subplots()    
    ax.plot(labels, values) 
    plt.ylim(-1,150)
    plt.xticks(range(1960, 2023, 10))
    plt_name = 'Inflación Historica de '+ country
    plt.title(plt_name)
    plt.savefig('./charts/'+plt_name +'.jpg')
    plt.show()
    clear()
    finalizar_programa()


def precio_internacional_productos():
    clear()
    df = pd.read_csv('./datasets/indicePrecioProducto.csv')
    products = list(df.columns.values)
    products.pop(0)

    product = ''
    while product not in products:
        
        for p in range(0, len(products)):
            print(str(p+1) + ' - ' + str(products[p].capitalize().replace('_',' ')))

        print('\n \n' + '***'*3 + "Elige una Opcion"+ '***'*3 + '\n')
        print('Elige un Producto, o escribe su nombre')
        eleccion = input('Tipea el nombre de un producto (debe ser exactamente igual que en listado), o el numero que lo representa ==> ')
        if len(eleccion) in range(1,3):
            try:
                if int(eleccion) in range(0, len(products)):
                    product = products[int(eleccion)-1]
                else:
                    print('Elige nuevamente, creo que te equivocaste')
            except ValueError:
                print('¿Y eso que fue?')
        elif len(eleccion) > 2:
            product = eleccion.lower().replace(' ','_')

    clear()

    name_product = product.capitalize().replace('_',' ')

    labels_fecha = list(df['indice_tiempo'].values)
    labels = list(map(lambda x: int(x[0:4]),labels_fecha))
    values = list(df[product])


    fig, ax = plt.subplots()    
    ax.plot(labels, values) 
    plt.xticks(range(1980, 2017, 10))
    plt_name = 'Evolucion del Precio de '+ name_product
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
    print('2 - Evolucion de la inflacion en algún pais en Especial \n')
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