#Clase 13/10/2025
import csv
import os
#Cabe recalcar que si utilice IA para la resolucion de este ejercicio, pero intento aplicar los conocimientos que voy aprendiendo durante la carrera, a veces se re contra complica con estos temas
#Creacion de archivos
CSV_PATH = "productos.csv"
LISTA = ["nombre", "precio"]

#Creo mi archivo CSV, en caso de que no se encuentre(o no exista) lo creo, y si existe lo uso
def asegurar_mi_csv():
    crear = (not os.path.exists(CSV_PATH)) or os.stat(CSV_PATH).st_size == 0
    if crear:
        with open(CSV_PATH, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=LISTA)
            writer.writeheader()

#Cargo mi archivo CSV al programa
def cargar_productos_en_mi_csv():
    asegurar_mi_csv()
    productos = []
    with open(CSV_PATH, "r", newline="", encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            try:
                precio = float(str(fila.get("precio", "")).replace(",", "."))
            except ValueError:
                continue
            nombre = (fila.get("nombre" or "")).strip()
            if not nombre:
                continue
            productos.append({"nombre": nombre, "precio": precio})
    return productos


#Muestro los productos cargados hasta el momento
def mostrar_productos():
    productos = cargar_productos_en_mi_csv()
    if not productos:
        print("No hay productos registrados")
        return
    print("Productos registrados:")
    total = 0.0
    for producto in productos:
        print(f"Producto: {producto["nombre"]} -> ${producto["precio"]:.2f}")
        total += producto["precio"]
    print(f"Total de precios: ${total:.2f}")


#Agrego productos al archivo csv
def agregar_producto():
    crear = (not os.path.exists(CSV_PATH)) or os.stat(CSV_PATH).st_size == 0
    if crear:
        with open(CSV_PATH, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=LISTA)
            writer.writeheader()
#Creo una lista para donde extraigo los productos del diccionario para verificar si hay repetidos
    productos_existentes = []
    with open (CSV_PATH, "r",newline="", encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            productos_existentes.append(fila["nombre"])


##Valido la entrada de datos para añadirlos al final al archivo
    while True:
            producto = input("Ingrese el nombre del producto: ").title().strip()
            if producto == "":
                print("No puede ingresar nombres vacios")
                continue

            if not producto.isalpha():
                print("Ingrese un caracter válido")
                continue

            producto = str(producto)

            if producto in productos_existentes:
                print(f"El producto {producto} ya esta cargado en el archivo")
                continue
            break
    while True:
        try:
            precio = float(input(f"Ingrese el precio del producto {producto}: "))
            if precio < 0:
                print(f"El precio del producto {producto} no puede ser menor a 0")
                continue
            break
        except ValueError:
            print("Error al ingresar el número, intente nuevamente")

#Una vez pasado por todo el procedimiento, añado el nuevo producto al archivo y retorno al programa principal
    try:
        with open(CSV_PATH, "a", newline="", encoding = "utf-8") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=LISTA)
            writer.writerow({"nombre": producto, "precio": f"{precio:.2f}"})
        print("Producto agregado correctamente")
    except OSError as e:
        print("Error al escribir en el archivo:", e)

#Funcion para borarr productos del registro
def borrar_producto():

    #Si no hay productos cargados en el archivo retorno el mensaje
    productos = cargar_productos_en_mi_csv()
    if not productos:
        print("No hay productos registrados")
        return
    

##Comenzamos a validar entradas para buscar el producto a borar
    while True:
        objetivo = input("Ingrese el nombre del producto a borrar: ").title().strip()
        if not objetivo.isalpha():
            print("Intente con un caracter válido")
            continue
        if objetivo == "":
            print("No puede ingresar nombres vacios")
            continue
        break


    objetivo = str(objetivo)
    #Recorro mi archivo para encontrar coincidencias
    encontrados = [p for p in productos if p["nombre"] == objetivo]

    if not encontrados:
        print(f"No se encontro el producto {objetivo}")
        return
    ##En que encontrados sea dis
    
    restantes = encontrados = [p for p in productos if p["nombre"] != objetivo]

    try:
        with open(CSV_PATH, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=LISTA)
            writer.writeheader()
            writer.writerows(restantes)
        print(f" Se elimino {objetivo} del registro correctamente")
        return
    except OSError as e:
        print("Error al escribir el archivo:", e)


##Esta funcion la cree solo con el fin de borrar todo el contenido de mi archivo(para prueba y error)
def limpiar_archivo():
    with open("productos.csv", "w", newline="", encoding="utf-8") as f:
        pass
    print("Archivo limpiado correctamente (contenido eliminado).")

#Menú
while True:
    print("*"*30)
    print("1. Mostrar productos registrados")
    print("2. Agregar nuevo producto")
    print("3. Eliminar un producto existente")
    print("4. Salir")
    opcion = input("Ingrese una opcion: ")
    match opcion:
        case "1":
            mostrar_productos()
        case "2":
            agregar_producto()
        case "3":
            borrar_producto()
        case "4":   
            print("Adios")
            break
        case "5":
            limpiar_archivo()            
        case _:
            print("Ingrese una opcion valida")
            continue





