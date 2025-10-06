clases = ["Mambo"]
cupos = [3]

while True:
    print("Menú")
    print("1. Registrar lista de Clases")
    print("2.Ingresar cupos para cada clase")
    print("3. Mostrar clases con cupos")
    print("4. Consultar cupo de una clase")
    print("5. Listar clases sin cupos")
    print("6. Agregar clase nueva")
    print("7. Actualizar cupos(Inscribirse/Bajarse)")
    print("8. Salir")
    opcion = input("Seleccione una opción: ")
    match opcion:
        case "1":
            i_registrar_clases = input("Ingrese cuantas clases desea registrar: ")
            if not i_registrar_clases.isdigit():
                print("ERROR. No se pudo registrar ese número. Volviendo al menú")
                continue

            i_registrar_clases = int(i_registrar_clases)
            for i in range(i_registrar_clases):
                while True:
                    agregar_clase =input(f"Ingrese el nombre de la clase {i+1}: ").capitalize().strip()
                    if agregar_clase not in clases:
                        clases.append(agregar_clase)
                    else:
                        print("No puede ingresar clases existentes")
                        continue

                    cupos.append(0)
                    break


        case "2":
            if not clases:
                print("No hay clases registradas.")
                continue
            for clase in range(len(clases)):
                agregar_cupos = input(f"Ingrese cupos para clase de {clases[clase]} :")
                if not agregar_cupos.isdigit():
                    print("ERROR. No se pudo ingresar los cupos. Volviendo al menu")
                else:
                    agregar_cupos = int(agregar_cupos)
                    cupos[clase] = agregar_cupos
                    print(f"Cupos para la clase {clases[clase]} agregados correctamente")

        case "3":
            if not clases:
                print("No hay clases registradas.")
                continue
            for clase in range(len(clases)):
                print(f"{clases[clase]} : {cupos[clase]} cupos")

        case "4":
            if not clases:
                print("No hay clases registradas.")
                continue
            buscar_clase = input("¿De que clase desea saber los cupos? ").capitalize().strip()
            if buscar_clase in clases:
                ind = clases.index(buscar_clase)
                print(f"La clase{clases[ind]} tiene {cupos[ind]}")
            else:
                print("No se encontro la clase buscada")
        case "5":
            if not clases:
                print("No hay clases registradas.")
                continue
            for clase in range(len(clases)):
                if cupos[clase] == 0:
                    print(clases[clase])
        case "6":
            if not clases:
                print("No hay clases registradas.")
                continue
            while True:
                agregar_clase = input("¿Nombre de la nueva clase a agregar?").capitalize().strip()
                if agregar_clase in clases:
                    print("ERROR. No puede agregar una clase existente.")
                    continue

                agregar_cupos = input(f"¿Cuantos cupos desea agregar para la clase {agregar_clase}?")
                if not agregar_cupos.isdigit():
                    print("ERROR. No puede ingresar numeros negativos")
                else:
                    agregar_cupos = int(agregar_cupos)
                    clases.append(agregar_clase)
                    cupos.append(agregar_cupos)
                    print("Se agrego con exito la nueva clase")
                    break



        case "7":
            if not clases:
                print("No hay clases registradas.")
                continue
            print("1. Inscribirse a Clase")
            print("2. Bajarse de Clase")
            opc = input("Eliga su opcion: ")
            match opc:
                case "1":
                    anotarse_clase = input("¿A qué clase desea anotarse?: ").capitalize().strip()
                    if anotarse_clase not in clases:
                        print("No existe la clase buscada.")
                    else:
                        ind = clases.index(anotarse_clase)
                        if cupos[ind] == 0:
                            print("No puede anotarse a esta clase, no le quedan cupos")
                        else:
                            print(f"Se anoto a la clase {clases[ind]} con exito")
                        cupos[ind] -= 1
                case "2":
                    bajarse_clase = input("De cual clase deseea darse de baja?: ").capitalize().strip()
                    if bajarse_clase not in clases:
                        print("ERROR. Volviendo al menu.")
                    else:
                        ind = clases.index(bajarse_clase)
                        print(f"Se bajo de la clase {clases[ind]} con exito")
                        cupos[ind] += 1
        case "8":
            print("Adios")
            break
        case _:
            print("Opcion invalida, vuelva a intentar")
            continue