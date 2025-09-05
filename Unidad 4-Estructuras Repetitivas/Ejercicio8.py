#Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
numeros = 0
num_negativos = 0
num_positivos = 0
num_pares = 0
num_impares = 0
nulos = 0
##Cantidad de veces que el usuario desea iterar en el bucle
# cant_iteracion = 0
# cant_iteracion = int(input("¿Cuantos numeros desea ingresar?\n"))

for i in range(10): #Bucle del 0 al 9 (se itera 10 veces). Si se desea iterar las veces que quiera el usuario cambiar la variable (10) a (cant_iteracion) -> for i in range(cant_iteracion)
    numeros = int(input(f"Ingrese el número nº{i+1}\n"))
    if numeros < 0 and numeros % 2 == 1: ##Caso de que el numero sea negativo & además sea impar
        num_negativos += 1
        num_impares += 1
    elif numeros < 0 and numeros % 2 == 0: ##Caso en el que el numero sea negativo & ademas sea par
        num_negativos += 1
        num_pares += 1
    elif numeros > 0 and numeros % 2 == 1: #Caso en el que el numero sea positivo y ademas sea impar
        num_positivos += 1
        num_pares += 1
    elif numeros > 0 and numeros % 2 == 0: #Caso en el que el numero sea positivo y ademas par
        num_positivos += 1
        num_impares += 1
    elif numeros < 0: #Solo si el numero es negativo
        num_negativos += 1
    elif numeros > 0: #Solo si el numero es positivo
        num_positivos += 1
    else: #En caso de ingresar ceros
        nulos += 1

print(f"Hay un total de {num_negativos} numeros negativos, {num_positivos} numeros positivos, {num_pares} numeros pares, {num_impares} numeros impares y {nulos} numeros nulos")