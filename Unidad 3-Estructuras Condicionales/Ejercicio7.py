# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
# pantalla. 


frase = input("Ingrese una frase o palabra: ").lower() #convierte todo a minúscula para facilitar la comparacion
ultima_letra = frase[-1] #Analizamos la última letra de la frase/palabra ingresada
if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u": ##validacion de las vocales
    print(frase + "!") #frase = hola + "!" --> salida = hola!
else:
    print(frase) #frase = hola --> salida = hola
