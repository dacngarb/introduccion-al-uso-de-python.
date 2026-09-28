dia = input("Introduce un día: ")

match dia:
    case "lunes"  | "miercoles":
        print("Hay clase")
    case "martes" | "jueves" | "viernes":
        print("No hay clase")
    case _:
        print("Error")

numero = int(input("Introduce un número: "))
match numero:
    case n if n < 0:
        print("Negativo")
    case n if n > 0:
        print("Positivo")
    case _:
        print("Error")