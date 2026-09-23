def main():
    lista1 = ["Manzana", "Pera", "Melocotón"]
    lista2 = ["Kiwi", "Sandía", "Melón"]
    lista1.extend(lista2)
    print(lista1[-1])
    
    tupla = (3,5,7)
    print(tupla[0])

    inicio = int(input("Incio: "))
    fin = int(input("Fin: "))
    rango = range(inicio,fin)
    print(rango[3])

if __name__ == "__main__":
    main()