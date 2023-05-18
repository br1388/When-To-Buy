#from getprice import *
#from getdolar import *

from getprice import nombre, precio, url
from getdolar import dolarbluehoy
from datetime import datetime
import sqlite3
import time
import ssl
import urllib.request, urllib.parse, urllib.error
import re

now = datetime.now().date()

def actualizacion():
    precio_convertido = precio.replace('.', '')

    #convertir dolar y precio en float y cortar decimales
    dolbluehoy = dolarbluehoy.replace(',' , '.')
    fldolbluehoy = float(dolbluehoy)
    precioUSDraw = float(precio_convertido) / float(fldolbluehoy)
    precioUSD = round(precioUSDraw, 2)

    #print(nombre)
    #print(precio_convertido)
    #print('Precio en USD: $' , precioUSD)
    #print(fldolbluehoy)
    #print(now)
    #print(url)

    conn = sqlite3.connect('whentobuy.sqlite') #se conecta a la base de datos
    cur = conn.cursor()


    cur.execute('''CREATE TABLE IF NOT EXISTS Articulos
        (id INTEGER PRIMARY KEY AUTOINCREMENT, articulo TEXT, precio FLOAT,
        precioUSD FLOAT, fldolbluehoy FLOAT, fecha DATE, url TEXT)''')

    #cur.execute('ALTER TABLE Articulos ADD LinkML INT NULL')

    cur.execute('''INSERT OR IGNORE INTO Articulos (articulo,precio,precioUSD,fldolbluehoy,fecha,url)
    VALUES ( ?,?,?,?,?,? )''', (nombre,precio_convertido, precioUSD, fldolbluehoy, now,url) )
    #cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( starturl, ) )
    #conn.commit()


if nombre is not None:
    #convertir el dato precio en número entero
    precio_convertido = precio.replace('.', '')

    #convertir dolar y precio en float y cortar decimales
    dolbluehoy = dolarbluehoy.replace(',' , '.')
    fldolbluehoy = float(dolbluehoy)
    precioUSDraw = float(precio_convertido) / float(fldolbluehoy)
    precioUSD = round(precioUSDraw, 2)

    #print(nombre)
    #print(precio_convertido)
    print('Precio en USD: $' , precioUSD)
    #print(fldolbluehoy)
    print(now)
    #print(url)

    conn = sqlite3.connect('whentobuy.sqlite') #se conecta a la base de datos
    cur = conn.cursor()


    cur.execute('''CREATE TABLE IF NOT EXISTS Articulos
        (id INTEGER PRIMARY KEY AUTOINCREMENT, articulo TEXT, precio FLOAT,
        precioUSD FLOAT, fldolbluehoy FLOAT, fecha DATE, url TEXT)''')

    #cur.execute('ALTER TABLE Articulos ADD LinkML INT NULL')

    cur.execute('''INSERT OR IGNORE INTO Articulos (articulo,precio,precioUSD,fldolbluehoy,fecha,url)
    VALUES ( ?,?,?,?,?,? )''', (nombre,precio_convertido, precioUSD, fldolbluehoy, now,url) )
    #cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( starturl, ) )
    conn.commit()

    def print_titles():
        if count == 0:
            print('Ítem: ', column)
        if count == 1:
            print('Precio: ', column)
        if count == 2:
            print('Precio en USD (Blue): USD' + str(column))
        if count == 3:
            print('Cotización dolar (Blue): USD' + str(column))
        if count == 4:
            print('Fecha: ', str(column))

    print('')
    print("Todos los registros: ")

    for row in cur.execute('SELECT * FROM Articulos WHERE articulo = ?', (nombre, )):
        count = 0
        print('')
        for column in row[1:6]:
            print_titles()
            count = count + 1

else:
        conn = sqlite3.connect('whentobuy.sqlite') #se conecta a la base de datos
        cur = conn.cursor()

        def print_titles():
            if count == 0:
                print('Ítem: ', column)
            if count == 1:
                print('Precio: ', column)
            if count == 2:
                print('Precio en USD (Blue): USD' + str(column))
            if count == 3:
                print('Cotización dolar (Blue): USD' + str(column))
            if count == 4:
                print('Fecha: ', str(column))

        for row in cur.execute('SELECT * FROM Articulos'):
            print(row[:2])
        print('')

        id = input('Que nro. de articulo quieres consultar? (presione R para remover) ')
        if id != 'R':
            articulo = cur.execute('SELECT articulo FROM Articulos WHERE id = ?', (int(id), ))
            articulo = cur.fetchone()
            print('')
            print('Registros del producto: ')
            for row in cur.execute('SELECT * FROM Articulos WHERE articulo = ?', (articulo[0], )):
                count = 0
                print('')
                for column in row[1:6]:
                    #print(column)
                    print_titles()
                    count = count + 1
            conn.commit()

        else:
            borrar = input('Seleccione el numero de articulo que quiere remover: ')
            #articulo = cur.execute('SELECT articulo FROM Articulos WHERE id = ?', (int(borrar), ))
            ver = cur.execute('SELECT articulo FROM Articulos WHERE id = ?', (int(borrar), ))
            ver = articulo = cur.fetchone()
            cur.execute('DELETE FROM Articulos WHERE articulo = ?', (articulo[0], ))
            print('Removido:', ver)
            conn.commit()

        print('')


        '''actualizar = input('Desea actualizar los articulos de ML automaticamente (y/n): ')
        if actualizar == 'y':
            for row in cur.execute('SELECT url FROM Articulos WHERE LinkML = ?', ('1', )):
                url2 = row[0]

                document = urllib.request.urlopen(url2, None, 30)
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

                actualizacion()
                print('funciono')
                time.sleep(5)
            conn.commit()'''
