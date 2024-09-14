tablero = []


def transformar_coordenada(coord):
    x, y = coord.split()
    if x.upper() == "A":
        x = 1
    elif x.upper() == "B":
        x = 3
    elif x.upper() == "C":
        x = 5
    else:
        raise ValueError
    if y > 3:
        raise ValueError
    y = int(y)
    if tablero[y][x] != "_":
        raise ValueError
    return x, y




def movimiento():
    while True:
        with open("tablero.txt", "r") as file:
            for row in file:
                print(row, end="")
                tablero.append(row.strip().split())
            print()
            print(tablero)
        while True:
            try:
                x, y = transformar_coordenada(input("Escriba la coordenada de donde pondrá su movimiento (xy)"))
                tablero[y][x] = "O"
                break
            except ValueError:
                pass


def dos_jugadores():
    movimiento()

def un_jugador():
    ...