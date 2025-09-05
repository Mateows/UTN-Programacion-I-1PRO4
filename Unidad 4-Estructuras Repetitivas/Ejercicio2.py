# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = abs(int(input("Ingrese el número que desee saber la cantidad de digitos\n")))
contador = 0


while numero > 0: #4567 Se va a dividir en 10 hasta que el resultado sea menor que 0, cada iteracion a la variable (contador) se le sumara 1
    numero //= 10
    contador += 1

print(f"La cantidad de digitos que contiene el numero ingresado es de: {contador}")

