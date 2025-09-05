# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
numero = 0
suma = 0
media = 0

#Variables para probar con distintos limites de iteracion
##alcance= 0
##alcance = int(input("Ingrese la cantida de numerros que desea ingresar\n"))

for i in range (10): #Se cambia el bucle por "for i in range (alcance)" para iterar las veces que desee el usuario
    numero=int(input(f"Ingrese el número Nº{i+1}\n"))
    suma += numero
    media = suma/5
    #media = suma/alcance

print(f"La media de los nùmeros ingresados es de {media}")