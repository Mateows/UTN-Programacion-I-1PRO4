import os
import csv
def inicializar_archivo():
    if not os.path.exists("inventario.csv"):
        with open("inventario.csv", "w", newline="", encoding="utf-8") as archivo:
            encabezado = ["nombre", "stock"]
            escritor = csv.DictWriter(archivo, fieldnames=encabezado)
            escritor.writeheader()

def cargar_datos():
    try:
        lista = []
        with open("inventario.csv", "r" ) as archivo:
            lector = csv.DictReader(archivo, fieldnames=["nombre", "stock"])
            for fila in lector:
                try:
                    fila["stock"] = int(fila["stock"])
                    lista.append(fila)
                except ValueError:
                    print("Dato invalido")
        return lista
    except FileExistsError:
        print("CSV Incorrecto")

def actualizar_datos():
    with open("inventario.csv", "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre","stock"])
        escritor.writeheader
        escritor.writerows()

def mostrar_menu():
    print("1- Cargar herramientas")
    print("2- Mostrar herramientas registradas")
    print("3- Modificar herramienta")
    print("4- Eliminar herramienta")
    print("5- Consultar disponibilidad")
    print("6- Listar productos sin stock")
    print("7- Salir")




def cargar_herramientas(inventario):
    while True:
        try:
            herramientas_para_cargar = int(input("Ingrese cuantas herramientas queire cargar"))
            for herramientas in range(herramientas_para_cargar):
                nombre_herramienta = input(f"Nombre de la herramienta N°{herramientas+1}").title().strip()
                if not nombre_herramienta.isalpha():
                    print("ERROR. Intente con un caracter (a-z)")
                    continue
                nombre_herramienta = str(nombre_herramienta)
                while True:
                    
        except ValueError:
            print("Intente un número positivo")



def programa_principal():
    inicializar_archivo()
    inventario = cargar_datos()
    mostrar_menu()
    while True:
        try:
            opc = ("Ingrese una opcion")
            match opc:
                case 1:
                    inventario = cargar_herramientas(inventario)
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    print("Adios")
                    break
                case _:
                    print("Valor invalido, intente de nuevo")

        except ValueError:
            print("Valor Invalido")















if __name__ == "__main__":
    programa_principal()