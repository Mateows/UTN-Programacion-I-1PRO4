def factorial(num_usuario): #Función recursiva
    if num_usuario == 0:
        return 1
    else:
        return num_usuario * factorial(num_usuario-1)




while True:
    try: #Solicito los datos al usuario
        num = int(input("Ingrese un número: "))
        if num < 0:
            print("Ingrese un numero mayor a 0")
            continue
        ##Llamo a la función recursiva
        for i in range(1, num+1):
            print(f"El factorial de {i} es: {factorial(i)}")

    except ValueError:
        print("Intente con un numero entero posiivo")
        continue
    break


