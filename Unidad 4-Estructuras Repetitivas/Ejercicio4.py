# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

opcion = int(input("Desea sumar numeros en secuencia? [0]No/[1]Sí\n"))
numero = 0
suma = 0
while opcion != 0:
    numero=int(input("Ingrese el número a sumar\n"))
    suma += numero ##Por cada iteracion que realice el bucle en caso de que se ingrease un sí como respuesta
    opcion=int(input("Desea seguir sumando? [0]No/[1]Sí\n")) #Condicion de salida

print(f"Suma acumulada = {suma}") ##Valor esperado si se ingrease 3(tres) veces el número 7  y ingrease el valor 0 para salir == 21