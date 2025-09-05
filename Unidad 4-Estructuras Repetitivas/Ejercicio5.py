# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random ##biblioteca de Python para que la maquina seleccione una opcion al azar de una lista

numero_azar={ ##Una lista donde me guío por solo el valor numerico que tendra la lista
    "cero":0,
    "uno": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5,
    "seis": 6,
    "siete": 7,
    "ocho": 8,
    "nueve": 9
}
#variables
intentos = 0
eleccion_usuario = -1
maquina_seleccion = random.choice(list(numero_azar.values())) #Acá la maquina elegira una opcion al azar entre 0 y 9

while eleccion_usuario != maquina_seleccion: #Entra al bucle while, y va a salir cuando el número elegido sea igual al de la maquina, caso contrario seguira ejecutandose
    eleccion_usuario = int(input("Intente adivinar el numero elegido por la maquina entre el 0 y el 9\n"))
    intentos += 1 #Por cada intento fallido se le ira sumando un 1
print(f"Acerto!! Solo le costo un total de {intentos} intentos, enhorabuena")