#Recorrer un rango

for i in range(1,10):
    print(i)

#Recorrer lista de elementos
frutas = ["Melón", "Uva", "Sandía"]

for fruta in frutas:
    print(fruta)

peliculas =(
    {"titulo" : "Resident Evil", "nota" : 6},
    {"titulo" : "robocop", "nota" : 8},
    {"titulo" : "predator", "nota" : 1},
    {"titulo" : "terminator", "nota" : 4}
)

for pelicula in peliculas:
    if pelicula["nota"] >= 7:
        print(pelicula["titulo"])

texto = "Hola mundo"
for letra in texto:
    print(letra)