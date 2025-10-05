# Crear una función llamada operaciones_basicas(a, b) que reciba
#  dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.
def operaciones_basicas(a,b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    division = a/b
    return(suma,resta,multiplicacion, division)


num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese segundo valor: "))
suma, resta, multiplicacion, division = operaciones_basicas(num1, num2)

print(f"La suma de los dos valores es: {suma}")
print(f"La resta de los dos valores es: {resta}")
print(f"La multiplicación de los dos valores es: {multiplicacion}")
print(f"La división de los dos valores es: {division}")