import matplotlib.pyplot as plt
import numpy as np
import open_csv as ocsv
from os import system

def precio_dolar_historico(data):
    system("cls")
    year = 1913
    while year not in range(1914,2024):
        try:
            year= int(input('Tipea un año desde 1914 en adelante ==> '))
        except ValueError:
            print('Eso que fue?')

        if year not in range(1914,2024):
            print('Debes elegir un año comprendido entre 1914 y 2020, vuelve a intentarlo')


    data = list(filter(lambda x: int(x['Year']) > int(year), data)) #filtramos año de inicio si queremos

    labels=[]
    for item in data: #itema es cada diccionario dentro del array de datos
        label = [item['Year']for key in item] #genero una lista con el numero del año para cada key en cada diccioneario       
        label.pop()#elimino un elemento ya que la primer columna dle archivo no corresponde, solo lleva los años, de esta manera me quedan 12 veces repetido el mismo año (una vez por mes) 
        
        for x in label:#label es un array con los años reemplazando a los meses, con esto busco eliminar el formato de lista de listas, y solo queda una lista con todos los valors
            labels.append(int(x)) #transformo en int para evitar problemas al graficar

    values=[]
    for item in data:
        item.pop('Year')
        for x in item.values():
            if x != '':
                values.append(float(x))
            else:
                values.append(0)
    fig, ax = plt.subplots()
    
    ax.plot(labels, values)
   
    plt.ylim(-1,600) 
    plt.xticks(range(year, 2023, 10))
    plt.title('Valor de Dolar Oficial desde ' + str(year))
    plt.show()

    finalizar_programa()


def inflacion_mundial(data):
    system("cls")
    countries = [item['Country Name'] for item in data]
    print(len(countries))
    country = 9
    while country not in countries:
        print('Elige un Pais, o escribe su nombre')
        for i in range(0, len(countries)-1):
            print(str(i+1) + ' - ' + countries[i] )

        eleccion = input('Tipea el nombre de un pais (debe ser exactamente igual que en listado), o el numero que lo representa ==> ')
        if len(eleccion) in range(1,4):
            if int(eleccion) in range(0, len(countries)):
                country = countries[int(eleccion)-1]
            else:
                print('Elige nuevamente, creo que te equivocaste')
            
        elif len(eleccion) > 4:
            country = eleccion.capitalize()

    data_country = list(filter(lambda item: item['Country Name'] == country, data))

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
    plt.title('Inflación Historica de '+ country)
    plt.show()
    system("cls")
    finalizar_programa()


def precio_internacional_productos(data):
    system("cls")
    products = [key for key in data[0]]
    products.pop(0)
    products
    
    print('\n \n' + '***'*3 + "Elige una Opcion"+ '***'*3 + '\n')

    product = ''
    while product not in products:
        print('Elige un Producto, o escribe su nombre')
        for p in range(0, len(products)):
            print(str(p+1) + ' - ' + str(products[p].capitalize().replace('_',' ')))

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


    system("cls")

    name_product = product.capitalize().replace('_',' ')

    
    #aca dividir en dos cosas label las fechas y values los valores del trigo
    labels_fecha = [item['indice_tiempo'] for item in data]
    labels = list(map(lambda x: int(x[0:4]),labels_fecha))
    
    values = [float(item[product]) if item[product]!='' else 0 for item in data ]
  
    fig, ax = plt.subplots()    
    ax.plot(labels, values) 
    plt.xticks(range(1980, 2017, 10))
    plt.title('Evolucion del Precio de '+ name_product)
    plt.show()
    finalizar_programa()

def finalizar_programa():
    system("cls")
    print('\n \n')
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
        system("cls")
        exit()

def menu():
    system("cls")
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
            system("cls")
            precio_dolar_historico(ocsv.read_csv('.datasets/dolarPrecio.csv',';'))
        case 2:
            system("cls")
            inflacion_mundial(ocsv.read_csv('./datasets/inflacionMundial.csv',','))
        case 3:
            system("cls")
            precio_internacional_productos(ocsv.read_csv('./datasets/indicePrecioProducto.csv',','))
            
        case 4:
            system("cls")
            exit()
        
    system("cls")

if __name__=='__main__':
    system("cls")
    menu()