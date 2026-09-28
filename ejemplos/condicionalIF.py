numero = int(input("Introduce un número: "))

if numero > 0: 
    print("Positivo")
elif numero < 0: 
    print("Negativo")
else:
    print("Cero")

dia = input("Introduce un día: ")

if dia == "lunes" or dia == "miercoles":
    print("Hay clase")
elif dia == "martes" or dia == "jueves" or dia == "viernes":
    print("No hay clase")
else: 
    print("ERROR")