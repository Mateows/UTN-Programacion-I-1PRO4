#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde: 
# Las capitales sean las claves. 
# Los países sean los valores
diccionario_paises = {"Alemanía" : "Berlín",
                    "Australía" : "Canberra",
                    "Reino Unido" : "Londres",
                    "México" : "Ciudad de México",
                    "Perú" : "Lima",
                    "Brazil" : "Brasilia"
                    }

diccionario_paises_invertidos = {
                                }

for clave, valor in diccionario_paises.items():
    diccionario_paises_invertidos[valor] = clave

print(diccionario_paises_invertidos)