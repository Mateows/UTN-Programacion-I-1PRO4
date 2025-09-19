ordenes = []
horas = []

#Variables
orden_nueva = ""
horas_orden = 0
horas_estimadas_orden = 0
buscar_orden = " "
indice_agregar_horas = 0
opcion_ordenes = 0
iteracion_orden = 0
indice_encontrar_orden = 0

#Banderas
bandera = True

while bandera == True:
    opcion = int(input(f"{"*"*30}\nMENU\n1-Ingresar Ordenes\n2-Ingresar horas estimadas por Orden\n3-Mostrar Agenda\n4-Consultar horas de N°Orden\n5-Ordenes con hora 0\n{"*"*30}\n"))
    if opcion == 1:
        print("ENTRANDO A (1)INGRESAR ORDENES")
        opcion_ordenes = int(input("1-Ingresar una lista de ordenes\n2-Agregar una única orden\n"))
        if opcion_ordenes == 1:
            print("OPCION 1 SELECCIONADA CORRECTAMENTE")
            iteracion_orden = int(input("¿Cuantas ordenes desea agregar?\n"))
            for i in range(iteracion_orden):
                orden_nueva = str(input(f"Ingrese el nombre de la orden n°{i+1}\n")).upper()
                if orden_nueva in ordenes:
                    print("No puede agregar ordenes ya existentes al sistema")
                else:
                    ordenes.append(orden_nueva)
                    horas.append(0.0)
        elif opcion_ordenes == 2:
            print("OPCION 2 SELECCIONADA CORECCTAMENTE")
            orden_nueva = str(input("Ingrese el nombre de la nueva orden\n")).upper()
            if orden_nueva in ordenes:
                print("No puede agregar ordenes existentes al sistema")
            else:
                print("¡Orden y hora agregados correctamente!")
                ordenes.append(orden_nueva)
                horas.append(0.0)
        else:
            print("Opcion invalida, redirigiendo al menu")
    elif opcion == 2:
        buscar_orden = input("¿A qué orden desea agregarle una hora estimada?\n").upper()
        if buscar_orden in ordenes:
            horas_estimadas_orden = float(input("Agregar hora estimada para la orden\n"))
            indice_agregar_horas = ordenes.index(buscar_orden)
            horas[indice_agregar_horas] = horas_estimadas_orden
    elif opcion == 3:
        print("ENTRANDO A (3)MOSTRAR AGENDA")
        for i in range(len(ordenes)):
            print(f"{ordenes[i]} horas estimadas: {horas[i]}")
    elif opcion == 4:
        print("ENTRANDO A (4)CONSULTAR HORAS N°ORDEN")
        buscar_orden = str(input("¿De orden desea saber la hora estimada?\n")).upper()
        if buscar_orden not in ordenes:
            print("No se pudo encontrar la orden seleccionado, redirigiendo al menu. .. ")
        else:
            indice_encontrar_orden = ordenes.index(buscar_orden)
            print(f"La orden n°{ordenes[indice_encontrar_orden]} tiene una estimacion de {horas[indice_encontrar_orden]}")
    else:
        exit