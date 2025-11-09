def potencia(base, exponente): #Funcion recursiva para calcular la potencia
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente -1)




while True:
    try:
        #Solicito los datos al usuario#
        num_bas = int(input("Ingrese un número para la base: "))

        if num_bas < 0:
            print("Ingrese un numero mayor a 0")
            continue


        try:
            num_exp = int(input("Ingrese un número para el exponene: "))

            if num_exp < 0:
                print("Ingrese un númer mayor a 0")
                continue
    ##########                                                         #########
        #Llamo a la funcion recursiva y muestro el resultado en pantalla
            resultado = potencia(num_bas, num_exp)
            print(f"{num_bas} elevado a la {num_exp} es {resultado}")
        except ValueError:
            print("Intente con un número enter positivo")

            
    except ValueError:
        print("Intente con un numero entero positivo")
        continue
    break