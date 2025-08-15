# Piedra, papel o tijera

# Piedra le gana a tijera
# Tijera le gana a papel 
# Papel le gana a piedra

# Si la persona gana 2 de 3, gana la partida. O si gana 4 de 5 

# Si los jugadores eligen lo mismo es un empate

# Replicar el juego para jugar contra el computador o contra una personas

# Se cuenta 1, 2, 3, piedra papel o tijera y sale

import random

juego = ["Piedra", "Papel", "Tijera"]

piedra = "Piedra"
papel = "Papel"
tijera = "Tijera"

jugador_1 = input("Jugador #1 ingrese su opción: ")
jugador_2 = input("Jugador #1 ingrese su opción: ")
computador = random.randint(juego)

if jugador_2 == True:
    print(jugador_1)
    print(jugador_2)





