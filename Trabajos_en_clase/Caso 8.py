instrumentos = []
unidades = []

while True:
    #Menu
    print("1. Ingresar instrumentos")
    print("2. Ingresar unidades para instrumentos")
    print("3. Mostrar inventario")
    print("4. Consultar unidades por instrumento")
    print("5. Listar faltantes")
    print("6. Agregar instrumento")
    print("7. Actualizar unidades")
    print("8. Salir")
    opcion = input("Ingresé una opción: ")
    match opcion:
        #AGREGAR INSTRUMENTOS
        case "1":
            iteracion_instrumento = input("¿Cuantos instrumentos desea agregar?: ")
            if not iteracion_instrumento.isdigit():
                print("ERROR. Ingreso un número invalido")
                continue
            iteracion_instrumento = int(iteracion_instrumento)

            for i in range(iteracion_instrumento):
                while True:
                    agregar_instrumento = input(f"Ingrese el nombre del instrumento {i+1}: ").strip().title()
                    if agregar_instrumento in instrumentos:
                        print("No puede agregar instrumentos existentes, intente de nuevo")
                        continue
                    else:
                        print("Instrumento agregado correctamente")
                        instrumentos.append(agregar_instrumento)
                        unidades.append(0)
                        break
        #INGRESAR UNIDADES POR INSTRUMENTOS
        case "2":
            if not instrumentos:
                print("No hay instrumentos existentes.")
                continue

            for i in range(len(instrumentos)):
                while True:
                    agregar_instrumento = input("Ingrese el nombre del instrumento: ").strip().title()
                    if agregar_instrumento not in instrumentos:
                        print("ERROR. Instrumento no encontrado")
                        continue
                    agregar_unidad = input(f"Cuantas unidades desea ingresarle al instrumento {agregar_instrumento}: ")
                    if not agregar_unidad.isdigit():
                        print("ERROR. No pudo ingresarse la unidad.")
                        continue

                    agregar_unidad = int(agregar_unidad)
                    unidades[i] = agregar_unidad
                    break
        #MOSTRAR INVENTARIO
        case "3":
            if not instrumentos:
                print("No hay instrumentos existentes.")
                continue
            for i in range(len(instrumentos)):
                print(f"{instrumentos[i]}: {unidades[i]} unidades")
        case "4":
            if not instrumentos:
                print("No hay instrumentos existentes.")
            consultar_instrumentos = input("¿De qué instrumento desea saber las unidades?: ").strip().title()
            if consultar_instrumentos in instrumentos:
                ind = instrumentos.index(consultar_instrumentos)
                print(f"El instrumento {instrumentos[ind]} tiene {unidades[ind]} unidades")
            else:
                print("El instrumento no se encontro.")
                continue
        #Mostrar instrumentos faltantes
        case "5":
            if not instrumentos:
                print("No hay instrumentos existentes.")
                continue

            for i in range(len(instrumentos)):
                if unidades[i] == 0:
                    print(f"{instrumentos[i]}")
        #Agregar Instrumenttos
        case "6":
            if not instrumentos:
                print("No hay instrumentos existentes.")
                continue
            agregar_instrumento = input("¿Qué nuevo instrumento desea agregar?: ").strip().title()
            if agregar_instrumento in instrumentos:
                print("ERROR. No puede ingresar instrumentos existentes.")
                continue
            instrumentos.append(agregar_instrumento)

            while True:
                agregar_unidad = input(f"¿Cuántas unidades desea agregar del instrumento {agregar_instrumento}")
                if not agregar_unidad.isdigit():
                    print("ERROR. Nùmero invalido, intente de nuevo")
                    continue
                agregar_unidad = int(agregar_unidad)
                unidades.append(agregar_unidad)
                break
        #Actualizar Unidades
        case "7":
            if not instrumentos:
                print("No hay instrumentos existentes.")
                continue
            opc = input("1. Agregar Unidad a Instrumento\n2. Quitar Unidad a Instrumento\n")
            match opc:
                case "1":
                    pedir_instrumento = input("¿Qué instrumento quiere devolver?: ").strip().title()
                    if pedir_instrumento not in instrumentos:
                        print("Instrumento no encontrado.")
                        continue
                    ind = instrumentos.index(pedir_instrumento)
                    unidades[ind] += 1
                    print(f"Se agrego correctamente una unidad al instrumento{instrumentos[ind]}")
                case "2":
                    quitar_instrumento = input("¿Qué instrumento quiere prestar?: ").strip().title()
                    if quitar_instrumento not in instrumentos:
                        print("Instrumento no encontrado.")
                        continue
                    ind = instrumentos.index(quitar_instrumento)
                    if unidades[ind] == 0:
                        print("Sin existencias")
                    else:
                        unidades[ind] -= 1
                        print(f"Se presto correctamente una unidad del instrumento{instrumentos[ind]}")

        case "8":
            print("Adios")
            break
        case _:
            print("Opcion invalida. vuelva a intentar")
            continue