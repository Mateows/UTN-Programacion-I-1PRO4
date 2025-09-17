#Mi biblioteca
titulos = ["Cenicienta", "Programacion", "Matematicas", "Rachel"]
ejemplares=[10,55,9,14]
#Listas Vacias, donde se llenaran con datos segun avance el programa y se agregaran a la Biblioteca Escolar
titulo_nuevo = []
copias = []
quitar_ejemplar=[]
agregar_ejemplar=[]
#Booleanos para finalizar el bucle while
bandera = True
#Variables
opcion = 0
opcion_ejemplares = 0
indice_buscar_libros = 0
indice_quitar_libros = 0
indice_agregar_libros = 0
while bandera == True:
    print("*"*40)
    print("¡Bienvenido a la Biblioteca Escolar!")
    print("*"*40)
    print("¿Qué acción desea realizar hoy?")
#VALIDACION DE ENTRADA OPCION (1, 2, 3 &  4) 0 PARA SALIR
    entrada = input("0-Salir\n1-Agregar Nuevos Libros\n2-Ver Catologo de la Biblioteca\n3-Disponibilidad de Libros\n4-Actualizar Ejemplares(Pedir/Devolver Libros)\n")
    if not entrada.isdigit():
        print("ERROR. ¡Por favor seleccione una opción Valida!")
        continue
    opcion = int(entrada)
    #SE AGREGAN NUEVOS TITULOS, SI HAY ALGUN TITULO QUE YA EXISTA O NO INTENTE AGREGAR NADA, EL PROGRAMA NO LO DEJARA
    if opcion == 1:
        print("*"*30)
        titulo_nuevo = str(input("Ingrese el titulo del nuevo libro\n")).capitalize()
        if titulo_nuevo in titulos: #Valida si el libro existé en el catalogo
            print("No pueden agregarse libros ya existentes, intente otro nombre")
        elif titulo_nuevo == "": #Valida si se ingresa no se ingresa nada
            print("No puede agregar un nombre vacio al catalogo")
        else: #En caso de que sea False, se agrega el nuevo libro al catalogo
            titulos.append(titulo_nuevo)
            copias = int(input("Ingrese las copias del libro\n"))
            ejemplares.append(copias)
    #MUESTRA EL CATALOGO DE LA BIBLIOTECA CON SUS RESPECTIVAS COPIAS
    elif opcion == 2:
        print("*"*30)
        for i in range(len(titulos)):
            print(f"{titulos[i]}: {ejemplares[i]} copias")
    #MUESTRA LA DISPONIBILIDAD DE LAS COPIAS DEL LIBRO SELECCIONADO, EN CASO DE QUE ELIGA UN LIBRO QUE NO EXISTA, EL PROGRAMA NO LO DEJARA
    elif opcion == 3:
        print("*"*30)
        libro = input("¿Nombre del libro que busca?\n").capitalize()
        if libro in titulos: #Recorre el índice de los libros para verificar si se encuentra el nombre del libro
            indice_buscar_libros = titulos.index(libro)
            print(f"{libro} Tiene {ejemplares[indice_buscar_libros]} copias")
        else: #En caso de que el libro no se encuentre
            print("El libro no se encuentra en la biblioteca")
    #CUENTA PARA QUITAR/AGREGAR COPIAS A UN LIBRO EXISTENTE EN LA BIBLIOTECA, SI QUIERE AGREGAR UNO QUE NO SE ENCUENTRE, EL PROGRAMA NO LO DEJJARA
    elif opcion == 4:
        print("*"*30)
        opcion_ejemplares = int(input("1-Pedir Libro / 2-Devolver Libro\n"))
        if opcion_ejemplares == 1:
            libro = input("Ingrese el nombre del libro que va a pedir\n").capitalize() ##VALIDACION DEL LIBRO INGRESADO
            if libro not in titulos: ##SI EL LIBRO  SELECCIONAD NO SE ENCUENTRA EN LA BIBLIOTECA SALTA ESTE PRINT
                print("No puede pedir libros que no se encuentran")
            else: ##VALIDACION PARA QUE SE QUITEN COPIAS DEL LIBRO QUE HUBIESE ESCRITO EL USUARIO, VALIDANDO NUMEROS NEGATIVOS Y/O MAYORES A LA CANTIDAD DE COPIAS EXISTENTES
                quitar_copia = int(input("¿Cuantas copias quiere del libro?\n"))
                indice_quitar_libros = titulos.index(libro)
                if quitar_copia < 0:
                    print("ERROR. No se permite el ingreso de números negativos")
                elif ejemplares[indice_quitar_libros] >= quitar_copia:
                    ejemplares[indice_quitar_libros] -= quitar_copia
                    print(f"Se quitaron {quitar_copia} copias del libro {libro}")
                elif ejemplares[indice_quitar_libros] == 0:
                    print("Ya no quedan copias del libro solicitado ¡Por favor avisar al encargado!")
                else:
                    print("Ha ingresado una cantidad a retirar que excede las copias actuales")
        #VALIDACIÓN PARA AGREGAR COPIAS AL LIBRO QUE HUBIESE ESCRITO EL USUARIO
        elif opcion_ejemplares == 2:
            libro = input("Ingrese el nombre del libro que va a devolver\n").capitalize()
            if libro not in titulos:
                print("No puede pedir libros que no se encuentran")
            else:
                agregar_copia = int(input("¿Cuantas copias quiere agregar del libro?\n"))
                indice_agregar_libros = titulos.index(libro)
                if agregar_copia > 0:
                    ejemplares[indice_agregar_libros] += agregar_copia
                    print(f"¡Se agregaron {agregar_copia} copias del libro {libro}!")
                else:
                    print("ERROR. No se permiten el ingreso de números negativos")
    elif opcion == 0:
        print("¡Adios!")
        bandera = False
    else:
        print("ERROR. ¡Seleccione una opción válida!")

##Muy dificil aaaaaa 