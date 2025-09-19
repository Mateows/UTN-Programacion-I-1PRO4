#Listas 
habitaciones = [101,102]
estados = [0,1]


#Variables
opcion_huespedes = 0
agregar_hab = 0
hab_estado= 0
quitar_huesped = 0
agregar_huesped = 0
indice_habitaciones_vacias = 0
indice_habitaciones_llenas = 0
indice_consulta_hab = 0
#.index(ve el indice de la lista)

#banderas
bandera = True

while bandera == True:
    opcion = int(input(f"{"*"*35}\nBienvenido al Hotel\n¿Qué desea realizar?\n1-Ingresar número de habitacion\n2-Ingresar estado de la habitacion\n3-Mostrar estado General de las habitaciones\n4-Consultar estado de Habitacion N° \n0-Salir\n{"*"*35}\n"))
    if opcion == 1:
        print("Opcion 1 Seleccionada con éxito. . .")
        agregar_hab = int(input("Ingrese el número de la habitación nueva\n"))
        if agregar_hab in habitaciones:
            print("No puede agregar habitaciones existentes\nRedirigiendo al menu de opciones")
        else:
            print(f"Se agrego la habitacion N°{agregar_hab} con exito")
            habitaciones.append(agregar_hab)
            estados.append(0)
    elif opcion == 2:
        print("Opcion 2 Seleccionada con éxito. . .")
        opcion_huespedes = int(input("1-Agregar estado (ocupado) a la habitacion N°\n2-Agregar estado (Vacio) a habitacion N°\n"))
        if opcion_huespedes == 1:
            print("Opcion 1 seleccionada. . .")
            agregar_huesped = int(input("¿Qué habitacion desea poner en estado (ocupado)?\n"))
            if agregar_huesped not in habitaciones:
                print("No puede agregar un estado en una habitacion que no existé\nRedirigiendo al menu de opciones")
            else:
                indice_habitaciones_llenas = habitaciones.index(agregar_huesped)
                estados[indice_habitaciones_llenas] = 1
                print(f"Se agrego correctamente el estado (Ocupado) a la habitacion n°{habitaciones[indice_habitaciones_llenas]}")
        elif opcion_huespedes == 2:
            print("Opcion 2 Seleccionada . . .")
            quitar_huesped = int(input("¿Qué habitacion desea poner en estado (desocupado)?\n"))
            if quitar_huesped not in habitaciones:
                print("No puede agregar un estado en una habitacion que no existé\nRedirigiendo al menu de opciones")
            else:
                indice_habitaciones_vacias = habitaciones.index(quitar_huesped)
                estados[indice_habitaciones_vacias] = 0
                print(f"Se agrego correctamente el estado (desocupado) a la habitacion n°{habitaciones[indice_habitaciones_vacias]}")
    elif opcion == 3:
        for i in range(len(habitaciones)):
            if estados[i] == 1:
                print(f"habitacion {habitaciones[i]}, ocupada")
            else:
                print(f"habitacion {habitaciones[i]}, libre ")    
    elif opcion == 4:
        hab_estado = int(input("¿De qué habitación desea saber el estado?\n"))
        if hab_estado in habitaciones:
            indice_consulta_hab = habitaciones.index(hab_estado)
            if estados[indice_consulta_hab] == 1:
                print(f"Habitacion nº{hab_estado} ocupada")
            else:
                print(f"Habitacion nº{hab_estado} libre")
    elif opcion == 0:
        print("Adios")
        bandera = False
    else:
        print("¡Introduzca una opción válida!")



