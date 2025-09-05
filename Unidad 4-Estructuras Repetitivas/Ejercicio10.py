# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese un número que quiera invertir\n"))
invertido = 0
digito = 0

while numero > 0: ##Mientras el número ingresado sea mayor a 0 se ejecutara el bucle
    digito = numero % 10 
    invertido = invertido * 10 + digito 
    numero = numero // 10

print(f"Numero invertido = {invertido}")
