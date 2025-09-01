# Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman 
# dos equipos de 6 integrantes cada uno, donde un integrante de cada equipo es el 
# “jefe” y los otros 5 son sus “oficiales”. La regla más importante del juego es que 
# sólo se comunicarán mediante un canal común, por lo que deben buscar la forma 
# de ocultar el contenido de sus mensajes. Uno de los equipos decide utilizar un 
# método antiguo de encriptación llamado “la cifra del césar”, que consiste en 
# correr cada letra del mensaje –considerando la posición de cada una en el 
# alfabeto– una determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 
# lugares, la palabra “ATAQUE” se transforma en “CVCSWG”. Cada día, el “jefe” del 
# equipo debe enviar un mensaje a cada uno de sus oficiales.  
# Escribir un programa que permita encriptar los 5 mensajes. El corrimiento 
# (cantidad de lugares que se correrán las letras) será dado por el usuario antes de 
# comenzar a encriptar. Los 5 mensajes usarán el mismo corrimiento. Nota: si el 
# alfabeto termina antes de poder correr la cantidad de lugares necesarios, se 
# vuelve a comenzar desde la letra “a”.  
# Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. 
# Utilizando el alfabeto español, de 27 letras, el siguiente cálculo matemático 
# permite volver a comenzar por el principio una vez que se llegó a la “z”: (índice de 
# la letra a correr+corrimiento)%27 Sólo se encriptarán las letras de los mensajes, 
# dejando al resto de caracteres sin modificación.

abecedario = "abcdefghijklmnñopqrstuvwxyz"

mensaje = ""
mensaje_clave = []
corrimiento = 0
letra = ""
indice = 0
indice_encriptado = 0
mensaje_encriptado = ""


corrimiento = int(input("Corrimiento que utilizara en cada mensaje\n"))

for i in range(5):
    mensaje = input(f"ingrese el mensaje nº{i+1}: ")
    mensaje_clave.append(mensaje)

##Acá no se separan el diccionario con los valores creadors
for mensaje in mensaje_clave:
    for letra in mensaje.lower():
        if letra in abecedario:
            indice = abecedario.index(letra)
            indice_encriptado = (indice + corrimiento)% len(abecedario)
            mensaje_encriptado += abecedario[indice]
        else:
            mensaje_encriptado += mensaje_encriptado + letra

print(mensaje_encriptado.upper()) ##Verificar porque TODAS las cadenas de texto no se separan





