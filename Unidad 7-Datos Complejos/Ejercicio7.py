# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
# y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

parcial_1 = {"Mateo", "Lucia", "Florencia", "Azul", "Juliana"}
parcial_2 = {"Mateo", "Azul", "Florencia", "Bruno"}

ambos = parcial_1.intersection(parcial_2)
al_menos_uno = parcial_1.symmetric_difference(parcial_2)
solo_uno = parcial_1.union(parcial_2)


print(f"Alumnos que aprobaron ambos parciales {ambos}")
print(f"Alumnos que aprobaron solo uno delos 2 parciales {al_menos_uno}")
print(f"Alumnos que aprobaron al menos un parcial {solo_uno}")