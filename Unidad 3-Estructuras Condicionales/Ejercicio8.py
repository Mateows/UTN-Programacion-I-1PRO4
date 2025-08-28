# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas. 

nombre =input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 para mayusculas, 2 para minusculas ó 3 para la primera letra en mayuscula"))

if opcion == 1:
    print(nombre.upper())#nombre = "mateo" --> salida esperada "MATEO"
elif opcion == 2:
    print(nombre.lower())# nombre = "MatEO" --> salida esperada "mateo"
elif opcion == 3:
    print(nombre.capitalize()) #Esta funcion es igual a la de title() nombre = "mateo" --> salida esperada "Mateo"
else:
    print("Opcion no valida") #El usuario ingresa un número no correspondiente al 1, 2 ó 3