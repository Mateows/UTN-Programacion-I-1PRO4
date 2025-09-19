validar_tarjeta = len("aaaaaaaaaaaaaaaa")
tarjetas = []
saldos = []

#Variables
agregar_saldo = 0








opcion = 0
opcion_tarjetas = 0
#Banderas
bandera = True

while bandera == True:
    opcion = int(input(f"{"#"*30}MENÚ SUBE\n1-Ingresar Tarjeta SUBE nueva al sistema\n2Mostrar Tarjetas SUBE registradas\n4Consultar saldo N°Tarjeta\n5-Consultar Tarjetas SUBE con saldo negativo\n6-Cargar/Debitar Saldo N°Tarjeta\n{"*"*30}"))
    if opcion == 1:
        
