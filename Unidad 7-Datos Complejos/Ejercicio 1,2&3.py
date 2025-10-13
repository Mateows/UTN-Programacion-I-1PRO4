#Dado el diccionario precios_frutas 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450}
print(f"DICCIONARIO SIN MODIFICAR:\n{precios_frutas} ")


#1)Añadir las siguientes frutas
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print (f"DICCIONARIO AÑADIENDO 3 NUEVAS FRUTAS: \n{precios_frutas}")


#2)Reemplazar los valores de las siguientes frutas
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(f"DICCIONARIO MODIFICANDO LOS VALORES:\n{precios_frutas}")

#3)Crear una lista solo con los valores del diccionario
print(f"DICCIONARIO SOLO MOSTRANDO LOS PRECIOS:\n{precios_frutas.values()}")
