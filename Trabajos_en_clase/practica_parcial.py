# Asignatura: Programación I
# Tema: Estructuras Repetitivas con Listas
# Caso 1 – Biblioteca escolar – Préstamos de libros
# Enunciado / Descripción
# La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las copias disponibles. Se pide desarrollar un programa con una interfaz basada en menú que utilice listas paralelas (una para títulos[] y otra para ejemplares[]). Cada título debe estar vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas. Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario elija salir.
# Ejemplo:
# •	títulos[] = ["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor"]
# •	ejemplares[] = [5, 3, 7]
# En este ejemplo, "El Señor de los Anillos" tiene 5 copias, "Orgullo y Prejuicio" tiene 3 copias, y "Matar un Ruiseñor" tiene 7 copias.
# Opciones del Menú:
# 1.	Ingresar lista de títulos:
# o	Permite al usuario introducir los títulos de los libros en la biblioteca.
# o	Ejemplo: El usuario introduce "1984", "Rebelión en la Granja".
# 2.	Ingresar lista de ejemplares disponibles (por título):
# o	Permite al usuario introducir el número de copias disponibles para cada título de libro.
# o	Ejemplo: Si el título es "1984", el usuario podría introducir "4" (lo que significa que hay 4 copias).
# 3.	Mostrar catálogo con stock:
# o	Muestra una lista de todos los títulos y el número de copias disponibles para cada uno.
# o	Ejemplo de salida:
# 	"El Señor de los Anillos: 5 copias"
# 	"Orgullo y Prejuicio: 3 copias"
# 	"Matar un Ruiseñor: 7 copias"
# 4.	Consultar disponibilidad de un título específico:
# o	Permite al usuario introducir un título y ver cuántas copias están disponibles.
# o	Ejemplo: El usuario introduce "Orgullo y Prejuicio", y el programa muestra "3 copias disponibles".
# 5.	Listar agotados (0 ejemplares):
# o	Muestra una lista de todos los títulos que tienen 0 copias disponibles.
# 6.	Agregar título:
# o	Permite al usuario añadir un nuevo título al catálogo y especificar el número inicial de copias.
# 7.	Ver títulos agotados:
# o	Muestra una lista de los títulos con cero copias disponibles.
# 8.	Actualizar ejemplares (préstamo/devolución):
# o	Permite al usuario actualizar el número de copias cuando un libro es prestado (préstamo) o devuelto (devolución).
# o	Ejemplo: Si alguien toma prestada una copia de "El Señor de los Anillos", el usuario puede actualizar el conteo de 5 a 4.
# o	Muestra el catálogo entero de los títulos de libros.
# 10.	Salir:
# o	Sale del programa.
libros_biclioteca = ["Padrinos", "Principe de Persia", "Ruiseñor"]
existencias=[10,7,9]
lista_agotados = []
titulo_nuevo = []
copias = []
bandera = True
print("Los libros existentes son", libros_biclioteca, "\ny las existencias de cada uno son", existencias)
while bandera == True:
    print("Bienvenido a la biclioteca escolar")
    print("¿Que desea hoy?")
    opcion = int(input("1-Ingresar Titulos\n3-Mostrar Catalogo\n4-Disponibilidad de libros\n5-Libros Agotados\n6-Agregar nuevo titulo\n7-Titulos Agotados\n8-Actualizar Ejemplares"))
    if opcion == 1:
        titulo_nuevo = input("Ingrese el titulo del nuevo libro")
        libros_biclioteca.append(titulo_nuevo)
        copias = int(input("Ingrese las copias del libro"))
        existencias.append(copias)
    elif opcion == 2:
        for i in len(libros_biclioteca):
            for j in len(existencias):
                print(f{libros_biclioteca},:,{existencias}")
