# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
valor_minimo = int(input("Ingrese el valor minimo de la iteracion\n"))
valor_maximo = int(input("Ingrese el valor máximo de la iteracion\n"))
suma = 0


for i in range(valor_minimo+1, valor_maximo): ##Utilizo solo un bucle para donde empezara desde el numero dado+1(para no incluirlo) hasta el valor máximo-1
    suma += i ##Por cada iteracion a la variable "suma" se le irá sumando el iterable "i"

print(f"La suma de los numeros comprendidos entre {valor_minimo} y {valor_maximo} exluyendos los mismos es = {suma}") #Valor esperado si se ingrease un 1 en (valor_minimo) y 9 en (valor_maximo) = 35


