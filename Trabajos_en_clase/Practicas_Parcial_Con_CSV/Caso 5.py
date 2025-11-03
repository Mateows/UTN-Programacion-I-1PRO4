import os
import csv
# Pizza,23
# Loco,44
# Hamburguesa,55
def inicializar_archivo():
    if not os.path.exists("supermecado.csv"):
        with open("supermercado.csv", "w", encoding="utf-8", newline="")as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["producto", "cantidad"])
            escritor.writeheader()

def cargar_archivo():
    try:
        lista = []
        with open("supermercado.csv", "r", encoding="utf-8")as archivo:
            lector = csv.DictReader(archivo, fieldnames=["producto", "cantidad"])
            next(lector)
            for fila in lector:
                try:
                    fila["cantidad"] = int(fila["cantidad"])
                    lista.append(fila)
                except ValueError:
                    print("Saltando linea")
        return lista
    except FileExistsError:
        print("No se encontro el archivo")


def actualizar_archivo(lista):
    with open("supermercado.csv", "w", encoding="utf-8", newline="")as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["producto", "cantidad"])
        escritor.writeheader()
        escritor.writerows(lista)
        print("Lista Actualizada")

def menu():
    print("1. Cargar varios productos")
    print("2. Sumarle más unidades a un producto existente ")
    print("3. Mostrar inventario") 
    print("4. Consultar stock de X producto")
    print("5. Listar productos agotados")
    print("6. Agregar producto individual")
    print("7. Actualizar unidades por venta/reposicion")
    print("8. Salir")







def cargar_productos(lista):
    try:
        cant = int(input("Ingrese la cantidad de productos a cargar: "))
        for i in range(cant):
            nombre = input(f"Ingrese el nombre del producto N°{i+1}: ").capitalize().strip()
            if not nombre.isalpha():
                print("Nombre invalido volvienddo al menú")
                return lista
            for elem in lista:
                if(nombre == elem["producto"]):
                    print("Este producto ya estaba cargado, volviendo al menú")
                    return lista
            while True:
                agregar = input(f"Ingrese la cantidad de productos para {nombre}: ")
                if agregar.isdigit():
                    lista.append({"producto":nombre, "cantidad":agregar})
                    break
                else:
                    print("Intente un numero valido")
                    continue
        actualizar_archivo(lista)
        return lista
    except ValueError:
        print("Intente con un numero")




def cargarle_unidades(lista):
    if not lista:
        print("No hay nada cargado")
        return lista
    

    nombre = input("Ingrese el nombre del producto para agregarle mas unidades: ").capitalize().strip()
    if not nombre.isalpha():
        print("Nombre invalido, volviendo al menú")
        return lista
    
        
    while True:
        for elem in lista:
            if(nombre == elem["producto"]):
                try:
                    agregar = input("Ingrese la cantidad de unidades nuevas para el producto: ")
                    if agregar.isdigit():
                        elem["cantidad"] += int(agregar)
                        actualizar_archivo(lista)
                        return(lista)
                    else:
                        print("Intente con un numero entero positivo")
                        continue
                except ValueError:
                    print("Intente con un caracter")


def mostrar(inventario):
    if not inventario:
        print("No hay nada cargado")
        return inventario
    else:
        for elem in inventario:
            print(f"{elem["producto"]} - {elem["cantidad"]}")


def programa_principal():
    inicializar_archivo()
    inventario = cargar_archivo()
    while True:
        try:
            menu()
            opc = int(input("Ingrese una opcion: "))
            match opc:
                case 1: #Cargar varios productos
                    inventario = cargar_productos(inventario)
                case 2: #Sumarle unidades a X productos
                    inventario = cargarle_unidades(inventario)
                case 3: #Mostrar todo
                    mostrar(inventario)
                case 4: #Consultar stock de X producto
                    pass
                case 5: #Listar productos agotados
                    pass
                case 6: #Agregar producto individual
                    pass
                case 7: #Actualizar unidades (agregar/quitar)
                    pass
                case 8:
                    print("Adios")
                    break
                case _:
                    print("Ingrese un valor dentro del rango (1-8)")
        except ValueError:
            print("Intente un número válido")


if __name__ == "__main__":
    programa_principal()