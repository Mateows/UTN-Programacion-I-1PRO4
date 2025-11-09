def factorial(num_usuario):
    if num_usuario == 0:
        return 1
    else:
        return num_usuario * factorial(num_usuario-1)




while True:
    try:
        num = int(input("Ingrese un número: "))
        if num < 0:
            print("Ingrese un numero mayor a 0")
            continue

        for i in range(1, num+1):
            print(f"El factorial de {i} es: {factorial(i)}")

    except ValueError:
        print("Intente con un numero entero posiivo")
        continue
    break






Visua