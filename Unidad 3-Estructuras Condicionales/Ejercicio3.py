#  Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

numero_par = int(input("Ingrese un número par: ")) #Entrada
if numero_par % 2 == 0: #Validacion de que sea un número par
    print("Ha ingresado un número par")
else: #Caso contrario
    print("Por favor, ingrese un número par")