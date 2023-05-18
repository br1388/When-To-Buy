
import urllib.request
import json

url = "https://mercados.ambito.com//dolar/informal/variacion"
document = urllib.request.urlopen(url)
text = document.read().decode()
if document.getcode() != 200 :
    print("Error code=",document.getcode(), url)


dolar = json.loads(text) #dolar pasa a ser un diccionario de python
dolarbluehoy = dolar['venta']
fechaact = dolar['fecha']
print('Dolar Blue - Venta: ', 'USD' , dolarbluehoy )
#print('Fecha Actualización: ', fechaact)
#print('Fuente: ', url)
