import requests

#Logica del link


Ubicacion= str #Barrio, Ciudad, Departamento 
Tipo = str # Arriendo, Venta
Tipo_de_Inmueble = str #Apartamento, Casa, Lote, Apartaestudio, Finca

url='https://fincaraiz.com.co/finca-raiz/arriendos' if Tipo=="Arriendo" else "https://fincaraiz.com.co/finca-raiz/venta"

r = requests.get(url)
