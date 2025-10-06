#CLASE 6/10/2025 Ejercicio practica Try/Except -> Mochila del Aventurero

# Ejercicio Datos complejos - Excepciones 
# Un aventurero quiere organizar su mochila con objetos mágicos. Tu tarea será ayudarlo a 
# programar su mochila en Python. 
# Parte 1 – Crear la mochila 
# 1. El programa debe pedir al usuario cuántos espacios tendrá la mochila (usar una lista 
# de ese tamaño). 
# o Si el usuario ingresa un valor inválido (texto o número negativo/cero), el 
# programa debe mostrar un mensaje de error y volver a pedir el dato. 
# Parte 2 – Menú principal 
# El programa debe mostrar un menú con opciones: 
# 1. Guardar objeto → El usuario ingresa la posición en la mochila y el nombre del objeto 
# mágico. 
# o Si intenta guardar en una posición que no existe, debe manejarse con 
# IndexError. 
# o Si no escribe nada (cadena vacía), debe mostrar un mensaje de error. 
# o Si ingresa texto donde debía ingresar un número, manejar con ValueError. 
# 2. Ver mochila → Muestra el contenido de cada espacio de la mochila (si está vacío, 
# mostrar "--- vacío ---"). 
# 3. Salir → Termina el programa mostrando un mensaje de despedida. 
# Ejemplo de ejecución 
#        Ingresa cuántos espacios tendrá la mochila: 4 

# --- Menú de la Mochila --- 
# 1. Guardar objeto 
# 2. Ver mochila 
# 3. Salir 
#      Elige una opción: 1 
#      Ingresa la posición (0-3): 0 
#     Ingresa el objeto mágico: espada 
#    espada guardado en el espacio 0 

#      Elige una opción: 2 

# Opcion 2
#        Contenido de la mochila: 
#  Espacio 0: espada 
#  Espacio 1: --- vacío --- 
#  Espacio 2: --- vacío --- 
#  Espacio 3: --- vacío ---


#Recorro el inventario con un bucle for y el rango de mochila
def ver_mi_inventario(mochila): 
    print("Mi Inventario :D")
    for espacios in range(len(mochila)):
        print(f"Posicion {espacios} Item: {mochila[espacios]}")




#Guardar los objetos en el inventario del aventurero
def guardar_objetos(mochila):
    try:
        posicion_inventario = input(f"Ingrese la posicion (0-{len(mochila)-1}): ")
        if not posicion_inventario.isdigit():
            raise ValueError("No puede acceder a espacios vacios ó ingresar caracteres, intente con un rango válido") #se guarda en la posicion e
        
        posicion_inventario = int(posicion_inventario)

        if mochila[posicion_inventario] == "-Vacio-": #Me fijo que mi inventario en la posicion elegida este vacio, caso contrario se ejecuta la linea 71
            item = input("Ingresé el nombre del objeto: ").strip().title()
            if item == "" or not item.isalpha():
                raise ValueError("El nombre del objeto no puede contener ni números, ni caracteres especiales y/o nombres vacios. . .") #se guarda en la variable "e"
            else:
                mochila[posicion_inventario] = item
                print((f"El objeto {item} se guardo correctamente en la posicion {posicion_inventario}"))
                return mochila
        else:
            print(f"Esa posicion ya está ocupada por el siguiente item: {mochila[posicion_inventario]}")

    except IndexError: #En caso de que el usuario intente meterse a una posicion de la lista no cargada/añadida
        print("Accediendo a un espacio vacio, intente nuevamente")

    except ValueError as e:
        print(f"ERROR. {e}") #Imprimo cualquiera de los errores Raise que hubiesen surgido durante la ejecucion especificando qué error ocurio


#Validacion de espacios en la mochila#
def validar_mochila():
    while True:
        try: 
            espacios =input("Cuantos espacios tiene la mochila: ").strip()
            if not espacios.isdigit():
                raise ValueError("Tiene que ser un numero entero positivo") #Se guarda en la variable e
            
            espacios = int(espacios)

            if espacios == 0:
                raise ValueError("Tiene que ser mayor que 0") #Se guarda en la variable e
            

            return ["-Vacio-"] * espacios ##RETORNO DEL INVENTARIO CREADO AL PROGRAMA PRINCIPAL. . . .
        
        except ValueError as e:
            print(f"ERROR. {e}") #Imprime los errores que ocurrieron en la ejecucion, por ejemplo "ERROR. Tiene que ser mayor que 0" en caso de que el número ingresado fuese 0







#[-----------------------CREACION DE LA MOCHILA-------------------]
mochila = validar_mochila()
print(f"Espacio de  la mochila: {mochila}")
#[------------------------Menú del Aventurero--------------------]
while True:
    print("--->Inventario<---")
    print("1. Guardar Objetos ")
    print("2. Ver mi Inventario")
    print("3. Salir")
    opcion = input("Opcion: ")
    match opcion:
        case "1":
            guardar_objetos(mochila)
        case "2":
            ver_mi_inventario(mochila)
        case "3":
            print("Saliendo del Inventario. . .")
            break
        case _:
            print("Intente una opcion válida")
            continue



