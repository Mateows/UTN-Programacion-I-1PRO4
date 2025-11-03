import os
import csv


def inicializar_archivo():
    if not os.path.exists("biblioteca.csv"):
        with open("biblioteca.csv", "w", encoding="utf-8", newline= "") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["libro", "cantidad"])
            escritor.writeheader()

def cargar_archivo():
    try:
        lista = []
        with open("biblioteca.csv","r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, fieldnames=["libro", "cantidad"])
            next(lector)
            for fila in lector:
                try:
                    fila["cantidad"] = int(fila["cantidad"])
                    lista.append(fila)
                except ValueError:
                    print("No se pudo cargar la fila, saltando linea")
        return lista
    except FileNotFoundError:
        print("Archivo no encontrado")


def actualizar_archivo(lista):
    with open("biblioteca.csv", "w", encoding="utf-8", newline= "") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["libro", "cantidad"])
        escritor.writeheader()
        escritor.writerows(lista)

def menu():
    print("1. Agregar libros")
    print("2. Mostrar libros")
    print("3. Modificar cantidad")
    print("4. Eliminar libro")
    print("5. Consultar disponibilidad")
    print("6. Listar sin ejemplares")
    print("7. Salir")

def cargar_libros(lista):
    while True:
        cant = input("¿Cuantos libros desea agregar?: ")
        if not cant.isdigit():
            print("Intente con un numero entero positivo")
            continue
        cant = int(cant)
        for i in range(cant):
            while True:
                nombre_libro = input(f"Ingresé el nombre del libro{i+1}: ").capitalize().strip()
                if not nombre_libro.isalpha():
                    print("Intente con una letra (a-z)")
                    continue

                while True:
                    cant_libro = input(f"Ingrese la cantidad de libros para {nombre_libro}: ")
                    if not cant_libro.isdigit():
                        print("Intente con un numero entero positivo")
                        continue
                    else:
                        lista.append({"libro":str(nombre_libro), "cantidad":int(cant_libro)})
                        actualizar_archivo(lista)
                        break
                print("Lista actualizada")
                return lista



def mostrar_libros(lista):
    if not lista:
        print("No hay nada cargado")

    for elem in lista:
        print(f"El libro {elem["libro"]} tiene {elem["cantidad"]} copias")


def modificar(lista):
    if not lista:
        print("No hay nada cargado")
    while True:
        b_libro = input("Ingrese el nombre del libro a buscar: ").strip().capitalize()
        if not b_libro.isalpha():
            print("Intente con un caracter (a-z)")
            continue
        for elem in lista:
            if(b_libro == elem["libro"]):
                print("Libro encontrado!")
                try:
                    agregar = int(input(f"Nueva cantidad de libros para {b_libro}: "))
                    elem["cantidad"] = agregar
                    actualizar_archivo(lista)
                    print("Lista actualizada")
                    return lista
                except ValueError:
                    print("ERROR. Intente un numero válido")
            else:
                print("No se encontraron coincidencias")
                return



def eliminar_libro(lista):
    if not lista:
        print("No hay nada cargado")
    lista_nva = []
    while True:
        b_libro = input("Ingrese el nombre del libro a eliminar: ").capitalize()
        if not b_libro.isalpha():
            print("Intente con un caracter (a-z)")
            continue
        for elem in lista:
            if(b_libro == elem["libro"]):
                continue
            lista_nva.append(elem)
        actualizar_archivo(lista_nva)
        print("Datos actualizados")
        return lista_nva
        


def consultar_stock(lista):
    while True:
        b_libro = input("¿De qué libro desea saber su stock?").capitalize()
        if not b_libro.isalpha():
            print("Intente con una letra (a-z)")
            continue
        for elem in lista:
            if(b_libro == elem["libro"]):
                print(f"El libro {elem["libro"]} tiene {elem["cantidad"]} copias")
        break
    print("No se encontraron coincidencias")
    return



def sin_stock(lista):
    if not lista:
        print("No hay nada cargado")

    for elem in lista:
        if(elem["cantidad"] == 0):
            print(f"El libro {elem["libro"]} tiene {elem["cantidad"]} copias")

def main():
    inicializar_archivo()
    inventario = cargar_archivo()
    while True:
        try:
            menu()
            opc = int(input("Ingrese una opción"))
            match opc:
                case 1:
                    inventario = cargar_libros(inventario)
                case 2: #Mostrar
                    mostrar_libros(inventario)
                case 3: #Modificar
                    inventario = modificar(inventario)
                case 4: #Eliminar
                    inventario = eliminar_libro(inventario)
                case 5: #Consultar
                    inventario = consultar_stock(inventario)
                case 6: #Listar
                    inventario = sin_stock(inventario)
                case 7:
                    print("Adios")
                    break
                case _:
                    print("Valor invalido. . .")
        except ValueError:
            print("Ingrese un número válido")






if __name__ == "__main__":
    main()