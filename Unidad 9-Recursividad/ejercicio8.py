def contar_digito(numero, digito): #Función recursiva
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)









while True:
    try: #Solicito los usuarios al usuario
        num = int(input("Ingrese una serie de digitos: "))

        if num < 0:
            print("Ingrese un numero entero positivo")
            continue

        try:
            buscar_d = int(input("Que número quiere buscar (0-9): "))

            if buscar_d < 0 or buscar_d > 9:
                print("Ingrese un numero entero positivo entre el rango (0-9)")
                continue
        ##Llamo a la función recursiva #####
            print(f"El numero {buscar_d} aparece un total de: {contar_digito(num, buscar_d)} veces en el número ingresado: -[{num}]-")
            break   
        except ValueError:
            print("Intente con un numero positivo")

    except ValueError:
        print("Intente con un número valido válido")
        continue
    break
