import os
import csv
def inicializar_archivo():
    if not os.path.exists("inventario.csv"):
        with open("inventario.csv", "w", newline="", encoding="utf-8") as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=["nombre", "stock"])
                escritor.writeheader()



def cargar_archivo():
    try:
        lista = []
        with open("inventario.csv", "r", encoding="utf-8")as archivo:
            lector = csv.DictReader(archivo, fieldnames=["nombre", "stock"])
            next(lector)
            for fila in lector:
                try:
                    fila["stock"] = int(fila["stock"])
                    lista.append(fila)
                except ValueError:
                    print(f"ERROR. Saltando fila{fila}")
        return lista
    except FileExistsError:
        print("ERROR. Archivo no encontrado")



def actualizar_archivo(lista):
    with open("inventario.csv", "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "stock"])
            escritor.writeheader()
            escritor.writerows(lista)


def agregar_herramientas(lista):
    while True:
        cant_i = input("Ingrese la cantidad de herramientas a ingresar: ")
        if not cant_i.isdigit():
            print("Intente con un numero entero positivo")
            continue
        cant_i = int(cant_i)

        for agregar in range(cant_i):
            while True:
                nombre_herr = input(f"Ingrese el nombre de la herramienta: {agregar+1}: ").strip().title()
                if not nombre_herr.isalpha():
                    print("Ingrese un nombre correcto")
                    continue

                nombre_herr = str(nombre_herr)
                while True:
                    cant_stock = input(f"Ingrese la cantidad de stock para la herramienta {nombre_herr}: ")
                    if not cant_stock.isdigit():
                        print("Intente con un numero entero positivo")
                        continue
                    else:
                        lista.append({"nombre": nombre_herr, "stock":cant_stock})
                        break
                break
        actualizar_archivo(lista)
        print("Datos actualizados")
        return lista
    


def mostrar(lista):
    for elem in lista:
        print(f"{elem["nombre"]} - {elem["stock"]}")


def modificar(lista):
    while True:
        buscar = input("Ingrese la herramienta a buscar:").title().strip()
        if not buscar.isalpha():
            print("Intente con una letra (a-z)")
            continue
        buscar = str(buscar)
        for elem in lista:
            if(buscar == elem["nombre"]):
                print("Herramienta encontrada")
                while True:
                    try:
                        agregar = int(input("Cuantas herramientas quiere agregar: "))
                        elem["stock"] += agregar
                        actualizar_archivo(lista)
                        print("Archivo actualizado")
                        return lista
                    except ValueError:
                        print("Numero invalido")

def eliminar(lista):
    lista_nueva = []
    quitar = input("Que herramienta desea quitar: ").title().strip()
    if not quitar.isalpha():
        print("Valor invalido. Volviendo al menu")
        return
    else:
        quitar = str(quitar)

        for elem in lista:
            if (quitar == elem["nombre"]):
                continue
            lista_nueva.append(elem)
        actualizar_archivo(lista_nueva)
        print("Elemento borrado correctamente")
        return lista_nueva

###CONTINUAR CON LA OPCION DE CONSULTAR DISPONIBILIDAD

def menu_principal():
    print("MENÚ")
    print("1. Agregar herramientas")
    print("2. Mostrar  herramientas")
    print("3. Modificar herramienta")
    print("4. Eliminar herramienta")
    print("5. Consultar disponibilidad")
    print("6. Listar productos sin stock")
    print("7. Salir")



def programa_principal():
    inicializar_archivo()
    inventario = cargar_archivo()
    while True:
        try:
            menu_principal()
            opc = int(input("Ingrese una opcion"))

            match opc:
                case 1:
                    inventario = agregar_herramientas(inventario)
                case 2:
                    inventario = mostrar(inventario)
                case 3:
                    inventario = modificar(inventario)
                case 4:
                    inventario = eliminar(inventario)
                case _:
                    print("Intente un numero valido")
        except ValueError:
            print("Intente con un valor válido")


if __name__ == "__main__":
    programa_principal()