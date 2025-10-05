
##Ejercicio clase 29/9/2025##
#MIS FUNCIONES PARA EL PROGRAMA PRINCIPAL!!!!!!
def pedir_letra(): ##Pide una letra al usuario cuando se llama la funcion
        while True:
            letra = input("Ingrese una letra: ").lower().strip()
            if len(letra) == 1 and letra.isalpha(): ##Pregunta si la letra es un caracter , y que ese caracter solo contenga 1 sola letra
                return letra  
            else:
                print("Entrada Invalida. Ingrese una sola letra(a-z)") #Caso de ingresar más de una letra y/o se ingresase un número se vuelve a llamar la funcion pedir_letra
                continue
    ###############################
#Variables
import random
mi_lista = ["miko", "inazuma", "fontaine", "sumeru"] #Puede modificar la lista con menos palabras!
#Lista para seleccion de la maquina para el ahorcado
seleccion_maquina = random.choice(mi_lista)
progreso =["_"]*len(seleccion_maquina)
#Intentos del usuario
intentos = 0
fallos_max = 6
#Palabras usadas por el usuario
usadas = set()
while intentos < fallos_max and "_" in progreso: #Pregunto ¿Mis intentos son menores a los fallos max, y el simbolo "_" se encuentra en el progreso?, como es True entra al bucle
    print("\nPalabra:", " ".join(progreso))
    print(f"Intentos restantes:{fallos_max-intentos}")#Por cada fallo se le ira restanto 1 a fallos_max
    print("Letras usadas: ", " ".join(usadas) if usadas else "-")#Va mostrando cada letra usada, por ejemplo "m-k-o"

    letra = pedir_letra() #Llamo a la funcion para pedir de entrada al usuario
    if letra in usadas: #Pregunto si una vez usada la letra vuelvo a repetirla ¿Qué pasa? El contador de intentos no se suma, nomás dice que la letra ya se ocupo
        print("Ya usaste esa letra.")
        continue

    usadas.add(letra)#Agrego la letra a mi lista de "usadas"

    if letra in seleccion_maquina: #Pregunto en un if-else ¿La letra se encontro en mi ahorcado?
        for i, l in enumerate(seleccion_maquina):
            if l == letra:
                progreso[i] = letra
                print("La letra está!") ##Este es el caso donde cualquier letra ingresada coincida con alguna letra de la seleccion de la maquina
    else:#Caso contrario, no se encontro la letra entonces el contador "intentos" se ira sumando hasta llegar al 6
        intentos += 1 
        print("La letra no se encontro")
#Una vez terminado el bucle while, preguntamos si el usuario gano o no
if "_" not in progreso:
    print(f"GANASTE LOCO BIEN AHI FELICIDADES ME SALVASTE !! Mi ahorcado era: {seleccion_maquina}")
else:
    print(f"Todo mal, perdiste. Mi ahorcado era: {seleccion_maquina} PD: Ahora toy muerto")







