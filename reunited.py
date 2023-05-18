import sqlite3
import json
import time
import ssl
import urllib.request, urllib.parse, urllib.error
import re


#Get dollar selling price
def get_dollar_venta():
    dolar_url = "https://mercados.ambito.com//dolar/informal/variacion"
    document = urllib.request.urlopen(dolar_url)
    text = document.read().decode()
    if document.getcode() != 200 :
        print("Error code=",document.getcode(), dolar_url)

    dolar = json.loads(text) #dolar pasa a ser un diccionario de python
    dolarbluehoy = dolar['venta']
    fechaact = dolar['fecha'][:10]
    return dolarbluehoy, fechaact, dolar_url

dolarbluehoy, fechaact, dolar_url = get_dollar_venta()

#Get ML name and price of the product
def get_ML_name_price(link):
    document = urllib.request.urlopen(link, None, 30)
    text = document.read().decode()
    if document.getcode() != 200 :
        print("Error code=",document.getcode(), link)

    articulo = re.findall('data-head-react="true"/><meta property="og:title" content="(.*?)"', text)
    articulo_str = ' '.join(articulo)
    precio_pos = articulo_str.find('$')
    precio = articulo_str[precio_pos+2:]
    nombre = articulo_str[:precio_pos-3]
    return precio, nombre

#print('-----------------BLOQUE UNO--------------------')
#print('Dolar Blue - Venta: ', 'USD' , dolarbluehoy )
#print('Fecha Actualización: ', fechaact)
#print('Fuente: ', dolar_url)
#print('------------------BLOQUE UNO---------------------')

#print('------------BLOQUE DOS------------------')
#Display options to user
opcion = input(
    f"1. Ingresar link ML \n"
    f"2. Ingresar datos manualmente \n"
    f"3. Consultar/editar base de datos \n"
    f">>>"
    )

if opcion == '1':
    url = input('Copie y pegue el link aquí: ')
    precio, nombre = get_ML_name_price(url)

    print('')
    print(nombre)
    print('Precio en pesos argentinos:', '$'+precio)

#print('-----------BLOQUE DOS----------------')

#BLOQUE TRES--------------------------
if opcion == '2':
        print('Estos son los registros actuales: ')
        #acá tirar la función de mostrar los items de la base de datos
        subopcion = input(
        f"1. Para incorporar un nuevo articulo \n"
        f"2. Para incorporar un nuevo precio \n"
        f"3. Para incorporar una entrada sin modificar datos \n"
        f">>>"
        )
        if subopcion == '1':
            nombre = input('Escriba el nombre del artículo: ')
            precio = input('Escriba el precio -sin signo $-: ')
            url = input('Registre el link donde se encuentra publicado: ')
            print('')
            print(nombre)
            print('Precio en pesos argentinos:', '$'+precio)

        if subopcion == '2':
            seleccion = input('Seleccione el número del artículo: ')
            #acá mostrar el nombre del articulo seleccionado y asignarlo a la variable nombre
            precio = input('Ingrese el nuevo precio: ')
            #acá ejecutar la función de almacenar en base de datos


if opcion == '3':
    print('Estos son los registros actuales: ')
    #acá tirar la función de mostrar los items de la base de datos
    subopcion = input(
    f"1. Consultar registros de algun producto \n"
    f"2. Remover producto del listado \n"
    f"3. Actualizar precios automáticamente (sólo para productos de ML) \n"
    f">>>"
    )
