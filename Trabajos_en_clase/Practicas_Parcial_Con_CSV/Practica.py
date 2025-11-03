import os
import csv



def inicializar_archivo():
    if not os.path.exists("biblioteca.csv"):
        with open("biblioteca.csv", "w", encoding="utf-8", newline="") as archivo:
            escritor=csv.DictWriter(archivo, fieldnames=["titulo", "cantidad"])
            escritor.writeheader()



def cargar_archivo():
    try:
        lista = []
        with open("biblioteca.csv", "r", encoding="utf-8")as archivo:
            lector = csv.DictReader(archivo, fieldnames=["titulo", "cantidad"])
            next(lector)
            for fila in lector:
                try:
                    fila["cantidad"] = int(fila["cantidad"])
                    lista.append(fila)
                except ValueError:
                    print("Saltando fila")
        return lista
    except FileExistsError:
        print("Archivo no encontrado")



def actualizar_archivo(lista):
    with open("biblioteca.csv", "w", encoding="utf-8", newline="") as archivo:
        escritor=csv.DictWriter(archivo, fieldnames=["titulo", "cantidad"])
        escritor.writeheader()
        escritor.writerows(lista)
        print("Biblioteca Actualizada")



def menu():
    print("1. Ingresar Titulos")
    print("2. Agregar Ejemplar x Titulo")
    print("3. Mostrar Catalogo")
    print("4.Consultar Disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar Titulo")
    print("7. Actualizar Ejemplares(Prestamo/Devolucion)")
    print("8. Salir")





def mostrar_catalogo(lista):
    if not lista:
        print("No hay datos cargados")
        return lista
    else:
        for elem in lista:
            print(f"{elem["titulo"]} - {elem["cantidad"]}")


def mostrar_sin_stock(lista):
    if not lista:
        print("No hay nada cargado aun")
        return lista
    else:
        for elem in lista:
            if(elem["cantidad"]== 0):
                print(f"{elem["titulo"]} - {elem["cantidad"]}")

def agregar_libros(lista):
    try:
        cant = int(input("Ingrese la cantidad de libros: "))
        for i in range(cant):
            libro = input(f"Ingrese el nombre del libro {i+1}").capitalize().strip()
            if not libro.isalpha():
                print("Nombre invalido, volviendo al menú")
                return lista
            for elem in lista:
                if(libro == elem["titulo"]):
                    print("Libro ya existente, volviendo al menú")
                    return lista
            while True:
                agregar = input("Ingrese la cantidad de libros: ")
                if agregar.isdigit():
                    lista.append({"titulo":libro, "cantidad":agregar})
                    break
        actualizar_archivo(lista)
        return(lista)
    except ValueError:
        print("Valor invalido")




def agregar_ejemplares(lista):
    if not lista:
        print("No hay nada cargado")
        return lista
    buscar = input("¿Que libro quiere buscar?: ").capitalize().strip()
    if not buscar.isalpha():
        print("Nombre invalido. Volviendo al menú")
        return lista
    for elem in lista:
        if(buscar == elem["titulo"]):
            while True:
                try:
                    agregar = int(input("Cuantos ejemplares le desea agregar: "))
                    elem["cantidad"] += agregar
                    actualizar_archivo(lista)
                    return lista
                except ValueError:
                    print("Intente un numero")
            
    print("No se encontraron coincidencias")
    return lista


def consultar(lista):
    if not lista:
        print("No hay nada cargado")
        return lista
    buscar = input("¿Que libro quiere buscar?: ").capitalize().strip()
    if not buscar.isalpha():
        print("Nombre invalido. Volviendo al menú")
        return lista
    
    for elem in lista:
        if(buscar == elem["titulo"]):
            print(f"{elem["titulo"]} - {elem["cantidad"]}")
    print("No se encontraron coincidencias")
    return lista



def quitar_agregar(lista):
    if not lista:
        print("No hay nada cargado")
        return lista
    
    try:
        buscar = input("Ingrese el libro a buscar: ")
        for elem in lista:
            if(buscar == elem["titulo"]):
                try:
                    while True:
                        opc = int(input("Ingrese una opcion (1. Pedir / 2. Devolver): "))
                        match opc:
                            case 1:
                                if(elem["cantidad"]== 0):
                                    print("No hay existencias")
                                    return lista
                                else:
                                    try:
                                        quitar = int(input("Cuantos libros quiere pedir prestados: "))
                                        if(elem["cantidad"] < quitar):
                                            print("La cantidad solicitada excede el limite")
                                            return lista
                                        else:
                                            elem["cantidad"] -= quitar
                                            actualizar_archivo(lista)
                                            return lista
                                    except ValueError:
                                        print("Intente con numero")
                            case 2:
                                while True:
                                    try:
                                        agregar = int(input("Ingrese la cantidad de libros a devolver: "))
                                        elem["cantidad"] += agregar
                                        actualizar_archivo(lista)
                                        return lista
                                    except ValueError:
                                        print("Intente con una letra")
                            case _:
                                print("Opcion invalida")
                except ValueError:
                    print("Ingreso una letra")
    except ValueError:
        print("Valor invalido")



#  try:
#         cant = int(input("Ingrese la cantidad de libros: "))
#         for i in range(cant):
#             libro = input(f"Ingrese el nombre del libro {i+1}").capitalize().strip()
#             if not libro.isalpha():
#                 print("Nombre invalido, volviendo al menú")
#                 return lista
#             for elem in lista:
#                 if(libro == elem["titulo"]):
#                     print("Libro ya existente, volviendo al menú")
#                     return lista
#             while True:
#                 agregar = input("Ingrese la cantidad de libros: ")
#                 if agregar.isdigit():
#                     lista.append({"titulo":libro, "cantidad":agregar})
#                     break
#         actualizar_archivo(lista)
#         return(lista)
#     except ValueError:
#         print("Valor invalido")


def agregar_titulo(lista):
    libro = input("Ingrese el nombre del libro: ").capitalize().strip()
    if not libro.isalpha():
        print("Nombre invalido, volviendo al menú")
        return lista
    for elem in lista:
        if(libro ==elem["titulo"]):
            print("Este nombre ya existe, volviendo al menú")
            return lista
    try:
        while True:
            agregar = int(input("Ingrese la cantidad de ejemplares: "))
            if agregar < 0:
                print("Intente con un numero mayor a 0")
                continue
            else:
                lista.append({"titulo":libro, "cantidad": agregar})
                break
        actualizar_archivo(lista)
        return lista
    except ValueError:
        print("Ingrese un numero")





def programa_principal():
    inicializar_archivo()
    inventario = cargar_archivo()
    while True:
        try:
            menu()
            opc = int(input("Ingrese una opcion: "))
            match opc:
                case 1:
                    inventario = agregar_libros(inventario)
                case 2:
                    inventario = agregar_ejemplares(inventario)
                case 3:
                    mostrar_catalogo(inventario)
                case 4:
                    inventario = consultar(inventario)
                case 5:
                    mostrar_sin_stock(inventario)
                case 6:
                    inventario = agregar_titulo(inventario)
                case 7:
                    inventario = quitar_agregar(inventario)
                case 8:
                    print("Adios")
                    break
        except ValueError:
            print("Numero invalido")

if __name__ == "__main__":
    programa_principal()
