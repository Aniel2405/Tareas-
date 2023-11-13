#Istitle

primer_nombre = input ("Nombre: ")
apllido = input ("Apellido: ")
full_name = f"{primer_nombre} {apllido}"

print()
print(f"El formato del metodo title() se ha aplicado?: {full_name.istitle()}")
print (f"Aplicando el meteto title(): {full_name.title()}")
print(f"Volvamos a imprimir el nombre: {full_name}")



#Practica 

oracion = input ("Ingresa una oracion: ")
if oracion.istitle():
    print("La oracion esta en formato de titulo")
else :
    print("La oracion no esta en formato de titulo")

print(f"Oracion corregida {oracion.title()}")

