import random
opciones = {"piedra" : 1,
            "papel" : 2,
            "tijera": 3} 
#[]

jugada_usuario = 0

while jugada_usuario != 4:
    print("-----OPCIONES-----")
    print("1-Piedra")
    print("2-Papel")
    print("3-Tijera")
    print("4-Salir")

    jugada_maquina = random.choice(list(opciones.values()))

    jugada_usuario= int(input("Que jugada realizara:\n"))

    if jugada_usuario == 4:
        break

    if jugada_usuario == jugada_maquina:
        print("Empate")
    elif jugada_usuario > jugada_maquina and jugada_maquina == 3:
        print("Piedra vence a Tijera")
    elif jugada_usuario < jugada_maquina and jugada_maquina == 2:
        print("Tijera vence a Papel")
