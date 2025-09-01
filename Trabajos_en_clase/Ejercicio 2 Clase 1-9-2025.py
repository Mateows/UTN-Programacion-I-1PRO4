# Vas a programar un juego clásico contra la computadora: Piedra, papel o tijeras. 
# Reglas: 
# 1. El programa debe mostrar un menú con las opciones: 
# o Piedra 
# o Papel 
# o Tijera 
# 2. El jugador elegirá una opción. 
# 3. La computadora elegirá su jugada al azar. 
# 4. El programa debe comparar ambas jugadas y mostrar quién gana: 
# o Piedra vence a Tijera. 
# o Tijera vence a Papel. 
# o Papel vence a Piedra. 
# o Si ambos eligen lo mismo, es empate. 
# Extra (para hacerlo más divertido): 
# • Llevar un marcador de cuántas partidas gana el jugador y cuántas gana la 
# computadora. 
# • El juego termina cuando el jugador elija salir, mostrando el resultado final. 


import random #Importe esta funcion de Python para que la maquina eliga una opcion al azar entre piedra, papel o tijera

#Se crea una lista donde eligó el número para cada acción que tomara la máquina
opciones = {"piedra" : 1,
            "papel" : 2,
            "tijera": 3} 

#variables que utilizo y su valor se va actulizando
jugada_usuario = 0
maquina_wins = 0
usuario_wins = 0
empate_man_machine= 0

while jugada_usuario != 4: #Siempre y cuando la condición ingresada por el usuario no sea 4 el bucle se seguira ejecutando (puede probar hasta con numeros negativos)
    print("-----OPCIONES-----")
    print("1-Piedra")
    print("2-Papel")
    print("3-Tijera")
    print("4-Salir")

    jugada_maquina = random.choice(list(opciones.values())) #Hago que la máquina eliga un VALOR(ya que estoy trayendo los valores del diccionario), aleatorio del diccionario creado más arriba

    jugada_usuario= int(input("Que jugada realizara:\n"))

    if jugada_usuario == 4: #Se verifica que la opcion no sea 4, ya que si grato caso lo llegase a ser y este "if-else" no estuviera, el bucle se ejecutaria de igual forma
        break
    elif jugada_usuario == jugada_maquina: ##Por cada victoria del usuario, al valor: usuario_wins se le estara sumando +1 victoria
        print("Empate")
        empate_man_machine = empate_man_machine + 1
    elif jugada_usuario == 1 and jugada_maquina == 3 :
        print("Piedra vence a Tijera")
        usuario_wins = usuario_wins + 1
    elif jugada_usuario == 3 and jugada_maquina == 2:
        print("Tijera vence a Papel")
        usuario_wins = usuario_wins + 1
    elif jugada_usuario == 2 and jugada_maquina == 1:
        print("Papel vence a Piedra")
        usuario_wins = usuario_wins + 1
    else:
        print("Gano la maquina, big L ggEZ") ##Caso de que lo qué ingresase el usuario (incluyendo numeros negativos ó mayores a los que pide el programa), se le sumara una victoria a la maquina
        maquina_wins = maquina_wins + 1

print(f"El usuario ha ganado un total de: {usuario_wins}, veces. La maquina un total de: {maquina_wins} veces, y un total de {empate_man_machine} empates.")