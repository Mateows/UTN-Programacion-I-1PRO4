#Listas
ordenes = ["ORD-001"]
horas = [2.5]



while True:
    print("Menú")
    print("1. Ingresar Ordenes")
    print("2. Ingresar horas estimadas por orden")
    print("3. Mostar agenda del Taller")
    print("4. Consultar horas por orden")
    print("5. Listar ordenes con 0 horas")
    print("6. Agregar nueva orden")
    print("7. Actualizar horas")
    print("8. Salir")

    opcion = input("Ingrese una opcion: ")

    match opcion:
        case "1":
            i_agregar_orden = input("Ingrese la cantidad de ordenes a ingresar: ")
            if not i_agregar_orden.isdigit():
                print("ERROR. Volviendo al menu")
                continue

            i_agregar_orden = int(i_agregar_orden)
            for i in range(i_agregar_orden):
                while True:
                    agregar_orden = input(f"Ingrese el nombre de la orden N°{i+1}: ").upper().strip()
                    if agregar_orden in ordenes:
                        print("ERROR. Intente agregar una orden no existente")
                    else:
                        ordenes.append(agregar_orden)
                        horas.append(0)
                        print(f"Nueva orden agregada correctamente! ")
                        break

        case "2":
            if not ordenes:
                print("ERROR. No hay ordenes cargadas")
                continue
            for orden in range(len(ordenes)):
                while True:
                    agregar_horas = input(f"Ingrese la hora estimada para la orden {ordenes[orden]}: ")
                    agregar_horas = float(agregar_horas)
                    if agregar_horas < 0:
                        print("Ingrese una hora válida")
                    else:
                        horas[orden] = agregar_horas
                        print(f"Horas cargadas para la orden {ordenes[orden]} correctamente")
                        break

        case "3":
            if not ordenes:
                print("ERROR. No hay ordenes cargadas")
                continue
            for orden in range(len(ordenes)):
                print(f"{ordenes[orden]}, Tiempo estimado {horas[orden]}")
        case "4":
            if not ordenes:
                print("ERROR. No hay ordenes cargadas")
                continue
            consultar_orden = input("¿De qué orden desea saber la hora?: ").upper().strip()
            if not consultar_orden in ordenes:
                print("ERROR. Orden no encontrada, volviendo al menú")
            else:
                ind = ordenes.index(consultar_orden)
                print(f"La orden {ordenes[ind]} tiene una hora estimada de: {horas[ind]}")

        case "5":
            if not ordenes:
                print("ERROR. No hay ordenes cargadas")
                continue
            for orden in range(len(ordenes)):
                if horas[orden] == 0:
                    print(ordenes[orden])
        case "6":
            if not ordenes:
                print("ERROR. No hay ordenes cargadas")
                continue

            nueva_orden = input("¿Nombre de la nueva orden a agregar?").strip().upper()
            if nueva_orden in ordenes:
                print("ERROR. No puede ingresar una orden ya existente, intente con otra")
                continue
            else:
                while True:
                    agregar_horas = input(f"Ingrese la hora estimada para la orden {nueva_orden}: ")
                    agregar_horas = float(agregar_horas)
                    if agregar_horas < 0:
                        print("Ingrese una hora válida")
                    else:
                        ordenes.append(nueva_orden)
                        horas.append(agregar_horas)
                        print(f"Nueva orden cargada al sistema correctamente")
                        break

        case "7":
            if not ordenes:
                print("ERROR. No hay ordenes cargadas")
                continue
            print ("1. Agregar horas a XºOrden")
            print ("2. Quitar horas a XºOrden")
            opc = input("Ingrese una opción: ")
            match opc:
                case "1":
                    buscar_orden = input("¿Qué orden desea agregarle horas?: ").strip().upper()
                    if buscar_orden not in ordenes:
                        print("Error al buscar el Nº de orden")
                    else:
                        while True:
                            agregar_horas = input(f"Ingrese la hora a agregar para {buscar_orden}: ")
                            agregar_horas = float(agregar_horas)
                            if agregar_horas < 0:
                                print("Ingrese una hora válida")
                            else:
                                ind = ordenes.index(buscar_orden)
                                horas[ind] += agregar_horas
                                print("Horas a la orden cargadas correctamente")
                                break
                case "2":
                    buscar_orden = input("¿Qué orden desea quitarle horas?: ").strip().upper()
                    if buscar_orden not in ordenes:
                        print("Error al buscar el Nº de orden")
                    else:
                        while True:
                            quitar_horas = input(f"Ingrese la hora a quitar para {buscar_orden}: ")
                            quitar_horas = float(quitar_horas)
                            ind = ordenes.index(buscar_orden)
                            if horas[ind] - quitar_horas < 0:
                                print("Esta intentando quitar una hora mayor a la hora que tiene la orden")
                            else:
                                ind = ordenes.index(buscar_orden)
                                horas[ind] -= quitar_horas
                                print("Horas a la orden cargadas correctamente")
                                break
        case "8":
            pass
        case _:
            print("Opcion invalida, vuelva a intentar")
            continue