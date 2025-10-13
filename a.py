import csv


def agregar_producto(archivo):
    archivo_agregar = {}
    while True:
        try:
            nombre_producto = str(input("Ingrese el nombre del producto: "))
            archivo_agregar["nombre"]=nombre_producto
            break
        except ValueError:
            print("Ingresé un dato válido")
    while True:
        try:
            precio_producto = float(input(f"Ingrese el valor del producto {nombre_producto}: "))
            archivo_agregar["precio"] = precio_producto
            break
        except ValueError:
            print("Ingresé un dato válido")

        archivo.writerow(archivo_agregar)
        return archivo_agregar








#Menú
with open("productos.csv", "w", newline = "") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre","precio"])
while True:
    
    print("1. Mostrar productos registrados")
    print("2. Agregar nuevo producto")
    print("3. Eliminar un producto existente")
    print("4. Salir")
    opcion = input("Ingrese una opcion: ")
    match opcion:
        case "1":
            mostrar_productos(archivo)

        case "2":
            agregar_producto(archivo)

        case "3":
            if not productos:
                print("No hay datos cargados")

        case "4":
            print("Adios")
            break
        case _:
            print("Ingrese una opcion valida")
            continue


with open("productos.csv", "r") as archivo:
    escritor = csv.reader(archivo)
    for fila in escritor:
        print(fila)