# Crear una función llamada calcular_promedio(a, b, c) que reciba
#  tres números como parámetros y devuelva el promedio de ellos.
#  Solicitar los números al usuario y mostrar el resultado usando esta
#  función

def validar_nums(mensaje): #Valido cada número que el usuario ingrese. "mensaje" Es un parametro que proviene del texto "ingrese el X número"
    while True:
        num_valido = input(mensaje)
        if num_valido.isdigit():
            return int(num_valido)
        else:
            print("Ingresé un valor entero positivo")


def calcular_promedio(a,b,c):
    promedio = (a+b+c) / 3
    return promedio

num1 = validar_nums("Ingrese el primer número: ")
num2 = validar_nums("Ingrese el segundo número: ")
num3 = validar_nums("Ingrese el tercer número: ")


print(f"El promedio de {num1}, {num2} & {num3} es de: {calcular_promedio(num1,num2,num3)}")




