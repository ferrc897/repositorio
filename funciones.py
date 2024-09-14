def movimiento():
    tablero = []
    with open("tablero.txt", "r") as file:
        for row in file:
            print(row, end="")
            tablero.append(row.strip())
        print()
        print(tablero)
    try:
        coordenada = input("Escriba la coordenada donde quiere colocar su movimiento (x)")

    except:
        ...


def dos_jugadores():
    movimiento()

def un_jugador():
    ...