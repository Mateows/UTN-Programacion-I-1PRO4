# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.


#El ejercicio es muy parecido al 3, asi que reutilice el código 
valor_maximo = int(input("Ingrese el valor máximo de la iteracion\n"))
suma = 0
for i in range(0, valor_maximo+1): ##Inicia en el valor 0 hasta el numero ingresado por el usuario+1 porque necesito que el ultimo valor también lo tomé
    suma += i

print(suma) 
print(f"La suma de los numeros comprendidos entre el valor 0 y el valor {valor_maximo} ingresado es = {suma}")