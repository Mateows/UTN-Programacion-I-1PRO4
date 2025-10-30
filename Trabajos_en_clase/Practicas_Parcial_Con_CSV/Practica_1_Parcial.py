import os
import csv
CSV_PATH = "inventario_ferreteria"
CAMPOS =  ["nombre", "stock", "precio"]


def inicializar_CSV():
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, "w", newline= "") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writeheader()

def cargar_CSV():
    inicializar_CSV()
    ferreteria = []
    with open(CSV_PATH, "r") as archivo:
        lector = csv.DictReader(archivo, fieldnames=CAMPOS)
        next(lector)
        for fila in lector:
            try:
                nombre = str(fila["nombre"])
                stock = int(fila["stock"])
                precio = float(int["precio"])
                ferreteria.append({"nombre": nombre}, {"stock": stock}, {"precio": precio})
            except ValueError:
                print("Dato invalido")
        return ferreteria
    

def actualizar_datos(ferreteria):
    with open(CSV_PATH, 'w', newline='') as archivo:
    escritor= csv.DictWriter(archivo, fieldnames=CAMPOS)
    escritor.writeheader()
    escritor.writerows(ferreteria)




def cargar_herramientas(ferreteria):
    while True:
        try:
            agregar = int(input("¿Cuantas herramientas desea agregar?"))

            for herramientas

        except ValueError:
            print("ERROR. Ingrese un dato válido")







def mostrar_menu():
    print("---MENÚ---")
    print("1. Cargar Herramientas")
    print("2. Mostrar herramientas registradas")
    print("3. Modificar herramienta")
    print("4. Eliminar herramienta")
    print("5. Consultar disponibilidad")
    print("6. Listar productos sin stock")
    print("7. Salir")



ferreteria = cargar_CSV()


while True:
    mostrar_menu()
    try:
        opc = int(input("Ingrese una opcion: "))
        match opc:
            case 1:
                cargar_herramientas(ferreteria)
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
                print("Ingrese un valor valido")
    except ValueError:
        print("Ingrese un valor valido")
