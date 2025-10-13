#6 Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno. 
#Funcion para validar el nombre del alumno
def validar_nombre(nombre):
    print("*"*30)
    while True:
        if not nombre.isalpha():
            print("Ingresé un nombre válido")
            continue
        return str(nombre)

##Funcion para validar los numeros ingresados, itera hasta 3 notas, el valor puede cambiar en cant=3 (desde el programa principal solo cambie el valor de validar_notas)
def validar_notas(cant=3):
    notas = []
    for i in range(cant):
        print(f"Iteracion n°{i+1} para validar notas")
        while True:
            try:
                numero_nota = float(input(f"Ingrese la nota {i+1}: "))
                if numero_nota < 0 or numero_nota > 10:
                    print("La nota debe de estar en un rango de 0-10")
                else:
                    notas.append(numero_nota)
                    break
            except ValueError:
                print("Debe ingresar un numero valido")
    return tuple(notas)





###################################################Programa principal###
alumnos = {}

for i in range(2):
    print("*"*30)
    print(f"Iteracion N°{i+1} del programa principal")
    while True:
        nombres = validar_nombre(input("Ingrese el nombre del alumno: ")).title()
        notas_alumno = validar_notas(3) ##Este valor puede cambiar para pedir más o menos notas (si no ingresa nada por defecto va a pedir 3 notas igual)
        break
    alumnos[nombres] = notas_alumno

for nombres, notas_alumno in alumnos.items():
    promedio = sum(notas_alumno) / len(notas_alumno)
    print(f"{nombres}: promedio = {promedio:.2f}")