
tarjetas = ["1234"]
saldos = [150.0]




#Validacion
validar_tarjeta = len("aaaa")
#Banderas


while True:
    print("Menú")
    print("1. Ingresar números de tarjeta")
    print("2. Ingresar Saldos correspondientes")
    print("3. Mostrar todas las tarjetas y saldos")
    print("4. Consultar saldo por número")
    print("5. Listar saldos en negativo o cero")
    print("6. Agregar Tarjeta con Saldo Inicial")
    print("7. Cargar/Debitar Saldo")
    print("8. Salir")

    opcion = input("Por favor eliga una opción: ")

    match opcion:
        #Cargar Tarjetas nuevas al Sistema
        case "1": 
            i_tarjetas = input("¿Cuantas tarjetas va a ingresar?: ")
            if not i_tarjetas.isdigit():
                print("Valor invalido, volviendo al menú")
                continue

            i_tarjetas = int(i_tarjetas)

            for i in range(i_tarjetas):
                while True:
                    val_tarjeta = input(f"Ingrese N°Tarjeta{i+1}: ")
                    agregar_tarjeta = len(val_tarjeta)

                    if agregar_tarjeta != validar_tarjeta or val_tarjeta in tarjetas:
                        print("ERROR. Intente nuevamente")
                        continue
                    else:
                        tarjetas.append(val_tarjeta)
                        saldos.append(0)
                        print(f"Tarjeta {val_tarjeta} agregada correctamente")
                        break
        #Cargar saldo iniciales a las tarjetas en el sistema
        case "2":
            if not tarjetas:
                print("No hay tarjetas disponibles")
                continue
            for i in range(len(tarjetas)):
                    agregar_saldo = float(input(f"¿Cuanto saldo desea ingrearle a la tarjeta {tarjetas[i]}?: "))
                    saldos[i] = agregar_saldo
                    print(f"Saldo ingresado correctamente a la tarjeta {tarjetas[i]}")
                    print()
        #Mostrar todas las tarjetas y saldos cargados
        case "3":
            if not tarjetas:
                print("No hay tarjetas disponibles")
                continue
            
            for i in range(len(tarjetas)):
                print(f"Tarjeta: {tarjetas[i]} - Saldo: {saldos[i]}")
        #Consultar saldo de X tarjeta
        case "4":
            if not tarjetas:
                print("No hay tarjetas disponibles")
                continue

            buscar_tarjeta = input("¿De qué tarjeta desea saber el saldo?")
            if buscar_tarjeta in tarjetas:
                ind = tarjetas.index(buscar_tarjeta)
                print(f"La tarjeta {tarjetas[ind]} tiene un saldo de: {saldos[ind]}")
        #Listar saldo negativos o con ceros
        case "5":
            if not tarjetas:
                print("No hay tarjetas disponibles")
                continue

            for buscar_saldo_neg in range(len(tarjetas)):
                if saldos[buscar_saldo_neg] <= 0:
                    print(f"Tarjeta : {tarjetas[buscar_saldo_neg]}  saldo: {saldos[buscar_saldo_neg]}")
        #Agregar tarjeta nueva al sistema con un saldo
        case "6":
            if not tarjetas:
                print("No hay tarjetas disponibles")
                continue
            agregar_tarjeta = input("Ingrese el Nº de la tarjeta")
            if agregar_tarjeta in tarjetas:
                print("ERROR. No puede agregar tarjetas existentes")
                continue

            tarjetas.append(agregar_tarjeta)
            agregar_saldo = float(input(f"Agregue el saldo de la tarjeta{agregar_tarjeta}"))
            print("Nueva tarjeta cargada al sistema con exito.")
        #Quitar/Añadir saldo a la tarjeta
        case "7":
            if not tarjetas:
                print("ERROR. No hay tarjetas disponibles")
                continue
            opc = input("1. Agregar Sueldo\n2. Quitar Sueldo\n")
            if not opc.isdigit():
                print("ERROR. Oopcion invalida")
                continue
            opc = int(opc)

            match opc:
                case 1:
                    buscar_tarjeta = input("¿A que tarjeta desea ingresarle un saldo?: ")
                    if buscar_tarjeta in tarjetas:
                        agregar_saldo = float(input("¿Cuanto saldo desea ingresarle?: "))
                        ind = tarjetas.index(buscar_tarjeta)
                        saldos[ind] += agregar_saldo
                case 2:
                    buscar_tarjeta = input("¿A que tarjeta desea quitarle saldo?: ")
                    if buscar_tarjeta in tarjetas:
                        quitar_saldo = float(input("¿Cuanto saldo desea quitarle?: "))
                        ind = tarjetas.index(buscar_tarjeta)
                        saldos[ind] -= agregar_saldo
        case "8":
            print("Adios")
            break
        case _:
            print("Opcion invalida, vuelva a intentar")
            continue

