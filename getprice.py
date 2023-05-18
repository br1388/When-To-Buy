import sqlite3
import time
import ssl
import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


opcion = input('1. Ingresar link ML - 2. Ingresar manualmente - 3. Consultar Base de Datos: ')

if opcion == '3':
    nombre = None
    precio = None
    url = None
    

if opcion == '2':
    nombre = input('Escriba el nombre del artículo: ')
    precio = input('Escriba el precio: ')
    url = input('Copie y pegue el link aquí: ')
    print('')
    print(nombre)
    print('Precio en pesos argentinos:', '$'+precio)

if opcion == '1':
    url = input('Ingrese el link de ML: ')
    document = urllib.request.urlopen(url, None, 30, context=ctx)
    text = document.read().decode()
    if document.getcode() != 200 :
        print("Error code=",document.getcode(), url)

    articulo = re.findall('data-head-react="true"/><meta property="og:title" content="(.*?)"', text)
    articulo_str = ' '.join(articulo)
    precio_pos = articulo_str.find('$')
    precio = articulo_str[precio_pos+2:]
    nombre = articulo_str[:precio_pos-3]

    print('')
    print(nombre)
    print('Precio en pesos argentinos:', '$'+precio)
