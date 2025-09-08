#random.sample(range(1,51),25)
import random
carton_bingo = random.sample(range(1,50),25)
eleccion_numero_maquina = random.sample(range(1,51),25)
carton_usuario = []


for i in range(5):
    for j in range(5):
        carton_usuario[i][j] = [random.choice(carton_bingo)] #Fuera de rango
        print (carton_usuario, end = " ")
    print()
    