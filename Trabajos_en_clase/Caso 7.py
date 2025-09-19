

#Variables
alumnos_lista = []
asistencias = []
nombre_nuevo_alumno = []
asistencias_por_alumno_nuevo = 0
indice_agregar_asistencias = ""
buscar_asistencias_alumno = ""
#Booleanos para finalizar bucle while
bandera = True

while bandera == True:
    print("*"*30)
    print("Bienvenido")
    print("¿Qué desea realizar hoy")
    print("*"*30)
    opcion = int(input("1-Tomar Lista\n2-Agregar Alumnos Nuevos\n3-Ver Asistencias de Alumnos\n4-Consultar Asistencias de Alumno\n0-Salir\n"))
    if opcion == 1:
        agregar_asistencia_alumno = input("¿A qué alumno le tomara asistencia?\n").capitalize()
        if agregar_asistencia_alumno not in alumnos_lista:
            print("ERROR. No puede marcarle asistencias a un alumno que no se encuentra")
        else:
            print(f"Se le agrego una asistencia a {agregar_asistencia_alumno}")
            indice_agregar_asistencias = alumnos_lista.index(agregar_asistencia_alumno)
            asistencias[indice_agregar_asistencias] += 1
    elif opcion == 2:
        nombre_nuevo_alumno = str(input("¿Nombre del nuevo alumno?\n")).capitalize()
        if nombre_nuevo_alumno in alumnos_lista or nombre_nuevo_alumno == " ":
            print("ERROR.No pueden agregarse los mismos alumnos")
        else:
            alumnos_lista.append(nombre_nuevo_alumno)
            asistencias.append(asistencias_por_alumno_nuevo)
    elif opcion == 3:
        for i in range(len(asistencias)):
            print(f"{alumnos_lista[i]} tiene {asistencias[i]} asistencias.")
    elif opcion == 4:
        buscar_asistencias_alumno = input("¿De cuál alumno desea saber las asistencias?\n").capitalize()
        if buscar_asistencias_alumno not in alumnos_lista:
            print("ERROR.No pueden buscarse alumnos que no se encuentran en la lista")
        else: 
            indice_alumno_encontrado = alumnos_lista.index(buscar_asistencias_alumno)
            print(f"{buscar_asistencias_alumno} tiene {asistencias[indice_alumno_encontrado]} asistencias")
    elif opcion == 0:
        print("¡Adios!")
        exit()
    else:
        print("Por favor utilice un valor válido entre las opciones")
#indice_quitar_libros = titulos.index(libro)
#  if libro in titulos: #Recorre el índice de los libros para verificar si se encuentra el nombre del libro
#             indice_buscar_libros = titulos.index(libro)
#             print(f"{libro} Tiene {ejemplares[indice_buscar_libros]} copias")