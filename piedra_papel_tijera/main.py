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

print("Piedra = 0")
print("Papel = 1")
print("Tijera = 2")

puntos_jugador = 0
puntos_computador = 0

while puntos_jugador < 3 and puntos_computador < 3:
    jugador_1 = int(input("Jugador #1 ingrese su opción:"))
    # jugador_2 = input("Jugador #1 ingrese su opción: ")
    computador = int(random.randint(0, 2))

    opcion_jugador = juego[jugador_1]
    opcion_computador = juego[computador]

    print(f"La opcion del jugador es: {opcion_jugador}")
    print(f"La opcion del computador es: {opcion_computador}")

    if puntos_jugador >= puntos_computador or puntos_computador >= puntos_jugador:
        if jugador_1 == computador:
            print("Es un empate")
            print(
                f"Así va el puntaje, tu tienes {puntos_jugador} y el computador {puntos_computador}"
            )

        elif jugador_1 == 0 and computador == 2:
            print("Piedra gana a tijera y ganas un punto")
            puntos_jugador += 1
            print(
                f"Así va el puntaje, tu tienes {puntos_jugador} y el computador {puntos_computador}"
            )

        elif jugador_1 == 1 and computador == 0:
            print("Papel cubre a la piedra y ganas un punto")
            puntos_jugador += 1
            print(
                f"Así va el puntaje, tu tienes {puntos_jugador} y el computador {puntos_computador}"
            )

        elif jugador_1 == 2 and computador == 1:
            print("Tijera corta papel y ganas un punto")
            puntos_jugador += 1
            print(
                f"Así va el puntaje, tu tienes {puntos_jugador} y el computador {puntos_computador}"
            )

        elif jugador_1 == 2 and computador == 0:
            print("Piedra gana a tijera y gana el computador")
            puntos_computador += 1
            print(
                f"Así va el puntaje, tu tienes {puntos_jugador} y el computador {puntos_computador}"
            )

        elif jugador_1 == 0 and computador == 1:
            print("Papel cubre a la piedra y gana el computador")
            puntos_computador += 1
            print(
                f"Así va el puntaje, tu tienes {puntos_jugador} y el computador {puntos_computador}"
            )

        elif jugador_1 == 1 and computador == 2:
            print("Tijera corta papel y gana el computador")
            puntos_computador += 1
            print(
                f"Así va el puntaje, tu tienes {puntos_jugador} y el computador {puntos_computador}"
            )

    elif puntos_jugador == 3:
        print("Gana el jugador")
        break

    else:
        print("Gana el computador")
