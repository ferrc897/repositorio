from funciones import un_jugador, dos_jugadores

def main():
    while True:
        print("1 Jugador")
        print("2 Jugadores")
        no_jugadores = int(input("Cuántos jugadores van a jugar (Escriba 1 o 2)"))
        if no_jugadores == 1:
            ganador = un_jugador()
        elif no_jugadores == 2:
            ganador = dos_jugadores()
        else:
            pass
        print(ganador)
        break


if __name__ == "__main__":
    main()