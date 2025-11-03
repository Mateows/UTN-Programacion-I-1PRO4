import os
import csv


def inicializar_archivo():
    if not os.path.exists("deposito.csv"):
        with open("deposito.csv", "w", encoding="utf-8", newline="")as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "cantidad"])
            escritor.writeheader()




def cargar_archivo():
        try:
            lista = []
            with open("deposito.csv", "r", encoding="utf-8")as archivo:
                lector = csv.DictReader(archivo, fieldnames=["nombre", "cantidad"])
                next(lector)
                for fila in lector:
                    try:
                        fila["cantidad"] = int(fila["cantidad"])
                        lista.append(fila)
                    except ValueError:
                        print("Saltando linea")

            return lista
        except FileNotFoundError:
            print("Archivo no encontrado")


def actualizar_archivo(lista):
    with open("deposito.csv", "w", encoding="utf-8", newline="")as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "cantidad"])
        escritor.writeheader()
        escritor.writerows(lista)
        print("Archivo Actualizado Correctamente")



def cargar_bebidas(lista):
    try:
        cant = int(input("Ingrese la cantidad de bebidas: "))
        for i in range(cant):
            bebida = input("Ingrese el nombre de la bebida: ").capitalize().strip()
            if not bebida.isalpha():
                print("Nombre invalido, volviendo al menú")
                return lista
            while True:
                bebida_c = input("Ingrese la cantidad de bebidas: ")
                if bebida_c.isdigit():
                    bebida_c = int(bebida_c)
                    break
            lista.append({"nombre":bebida, "cantidad":bebida_c})
        actualizar_archivo(lista)
        return lista
    except ValueError:
        print("Ingrese un numero valido")




def mostrar(lista):
    for elem in lista:
        if(elem["cantidad"] > 1):
            print(f"La bebida {elem["nombre"]} tiene {elem["cantidad"]} unidades")

def mostrar_sin_stock(lista):
    for elem in lista:
        if(elem["cantidad"] == 0):
            print(f"La bebida {elem["nombre"]} tiene {elem["cantidad"]} unidades")

def consultar_stock(lista):
    for elem in lista:
        print(f"La bebida {elem["nombre"]} tiene {elem["cantidad"]} unidades")





def modificar(lista):
    if not lista:
        print("No hay productos cargados")
        return lista
    
    buscar = input("Nombre del producto a buscar: ").capitalize().strip()
    if not buscar.isalpha():
        print("Nombre invalido, volviendo al menú")
        return lista
    

    while True:
        for elem in lista:
            if(buscar == elem["nombre"]):
                try:
                    nuevo_stock = int(input("Ingrese la nueva cantidad para el producto: "))
                    elem["cantidad"] = nuevo_stock
                    actualizar_archivo(lista)
                    return lista
                except ValueError:
                    print("Numero invalido, intente de nuevo")

def eliminar(lista):
    if not lista:
        print("No hay nada cargado")
        return lista
    

    buscar = input("Ingrese el nombre de la bebida a buscar: ").capitalize().strip()
    if not buscar.isalpha():
        print("Nombre invalido, volviendo al menú")
        return lista
    


    lista_nva = []
    for elem in lista:
        if(buscar == elem["nombre"]):
            continue
        lista_nva.append(elem)
    actualizar_archivo(lista_nva)
    return lista_nva


def retirar_agregar_bebida(lista):
    if not lista:
        print("No hay nada cargado")
        return lista
    
    buscar = input("Ingrese el nombre de la bebida a buscar: ").capitalize().strip()
    if not buscar.isalpha():
        print("Nombre invalido, volviendo al menú")
        return lista
    

    try:
        for elem in lista:
            if(buscar == elem["nombre"]):
                opc = int(input("Ingrese una opcion (1. Vender / 2. Comprar)"))
                match opc:
                    case 1:
                        if(elem["cantidad"]== 0):
                            print("No hay existencias")
                            return lista
                        else:
                            while True:
                                try:
                                    quitar = int(input("¿Cuantas bebidas va a comprar?: "))
                                    if(elem["cantidad"] < quitar):
                                        print("No puede quitar más unidades de las que existen")
                                    else:
                                        elem["cantidad"] -= quitar
                                        actualizar_archivo(lista)
                                        return lista
                                except ValueError:
                                    print("Solo hay numeros enteros")
                    case 2:
                        while True:
                            try:
                                agregar = int(input("¿Cuantas unidades va a agregar?: "))
                                elem["cantidad"] += agregar
                                actualizar_archivo(lista)
                                return lista
                            except ValueError:
                                print("Numero invalido")
            else:
                print("No hay coincidencias")
    except ValueError:
        print("Dato invalido")

def menu():
    print("1. Cargar bebidas")
    print("2. Mostrar bebidas")
    print("3. Modificar cantidad")
    print("4. Eliminar bebida")
    print("5. Consultar disponibiliadd de bebidas")
    print("6. Listar sin stock")
    print("7. Comprar bebida/cargar bebida")
    print("8. Salir")




def programa_principal():
    inicializar_archivo()
    inventario = cargar_archivo()
    while True:
        try:
            menu()
            opc=int(input("Ingrese una opcion: "))
            match opc:
                case 1:
                    inventario = cargar_bebidas(inventario)
                case 2:
                    mostrar(inventario)
                case 3:
                    inventario = modificar(inventario)
                case 4:
                    inventario = eliminar(inventario)
                case 5:
                    consultar_stock(inventario)
                case 6:
                    mostrar_sin_stock(inventario)
                case 7:
                    inventario = retirar_agregar_bebida(inventario)
                case 8:
                    print("Adios")
                    break
                case _:
                    print("Ingrese una opcion valida")
        except ValueError:
            print("Intente con un numero")






if __name__ == "__main__":
    programa_principal()