# Crear una función llamada tabla_multiplicar(numero) que reciba un
#  número como parámetro y imprima la tabla de multiplicar de ese
#  número del 1 al 10. Pedir al usuario el número y llamar a la fun
# ción.
def tabla_multiplicar(num):
    tabla = []
    for i in range(11):
        multiplicacion_tabla = num * i
        tabla.append(f"{num} x {i} = {multiplicacion_tabla}")
    return tabla

def validar_num(): #valido qu el numero no sea negativo o flotante
    while True:
        num = input("Ingresé el número de la tabla que quiere saber: ")
        if num.isdigit():
            num = int(num)
            return num
        else:
            print("Ingresé un numero entero positivo(no negativos ni caracteres especiales y/o letras)")
            continue


num = validar_num()     
resultado = tabla_multiplicar(num)
print(f"Tabla del {num}")
for linea in resultado:
    print(linea)