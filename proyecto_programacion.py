from funciones import un_jugador, dos_jugadores

def main():
    while True:
        print("1 Jugador")
        print("2 Jugadores")
        no_jugadores = int(input("Cuántos jugadores van a jugar (Escriba 1/2)"))
        if no_jugadores == 1:
            un_jugador()
        elif no_jugadores == 2:
            dos_jugadores()
        else:
            pass


if __name__ == "__main__":
    main()