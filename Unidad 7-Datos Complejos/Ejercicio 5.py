#  5- Solicita al usuario una frase e imprime: 
# las palabras únicas (usando un set). 
#  Un diccionario con la cantidad de veces que aparece cada palabra. 


def validar_iteraciones(iteraciones): #Valido las iteraciones, solo pueden ser iteraciones positivas y enteras
    while True:
        if not iteraciones.isdigit():
            iteraciones = input("Ingresé un número válido que no sea negativo y/o contenga caracteres: ")
            continue
        return int(iteraciones)

def validar_frases(palabras): #Válido que las letras que vaya a ingresar el usuario no sean numeros
    while True:
        frase = input(f"Ingrese la palabra {palabras+1}: ")
        if not frase.isalpha():
            print("Error, ingrese una palabra válida: ")
        frase = str(frase)
        frases.append(frase) #Por cada iteracion voy generando una lista y la retorno al final
        return frases #<---Retorno de la lista completa


################################################CODIGO PRINCIPAL######################################################################
conteo_repetidas = {} #Inicializo una diccionario para contabilizar palabras repetidas o no
frases = []
iteraciones = validar_iteraciones(input("Ingresé la cantidad de palabras que desea ingresar: "))
for palabras in range(iteraciones):
    frases = validar_frases(palabras)

for palabra in frases: #Recorro mi lista con un for y añado un contador por cada palabra repetida
    if palabra in conteo_repetidas:
        conteo_repetidas[palabra] += 1 #Se suma +1 si la letra, por ejemplo "mundo" se repite más de 1 vez ["mundo", "mundo"] el contador diria (mundo aparece 2 veces)
    else:
        conteo_repetidas[palabra] = 1 #En el caso de que no se repita, solo pone que se encontro 1 vez/veces


#FINALIZACION#
lista_limpia= set(frases) #Paso la lista a un set para que quede limpia sin elementos repetidos
#Imprimo todo
print(f"Lista sin duplicados: {lista_limpia}")
for palabra, cantidad in conteo_repetidas.items():
    print(f"{palabra} aparece {cantidad} vez/veces")
