def suma_digitos(n): #Función recursiva
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10) ##La división con doble "//" es una división exacta, o sea, retorna un número entero, sin decimales





while True:
    try: #Solicito los usuarios al usuario
        num = int(input("Ingrese un número: "))
        if num < 0:
            print("Ingrese un numero entero positivo")
            continue
        ##Llamo a la función recursiva
        print(f"La suma de los digitos es: {suma_digitos(num)}")

    except ValueError:
        print("Intente con un número valido válido")
        continue
    break
