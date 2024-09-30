import random

class Bloque:
    def __init__(self, bomb=False, flag=False, show=False, no_bomba=0):
        self.bomb = bomb
        self.flag = flag
        self.show = show
        self.no_bomba = no_bomba

    def __str__(self):
        if not(self.show):
            return "🟩"
        if self.show and self.bomb:
            return "💣"
        if self.show and self.no_bomba > 0:
            numeros = ["1️⃣ ", "2️⃣ ", "3️⃣ ", "4️⃣ ", "5️⃣ ", "6️⃣ ", "7️⃣ ", "8️⃣ "]
            return numeros[self.no_bomba - 1]
        if self.show:
            return "🟫"

ALTURA_TABLERO = 9
ANCHO_TABLERO = 9

def main():
    tablero = crear_tablero()
    while True:
        tablero = movimiento(tablero)
        """
        if perder(tablero):
            for i in range(ALTURA_TABLERO):
                    for j in range(ANCHO_TABLERO):
                        if tablero[i][j].bomb:
                            tablero[i][j].show = True
            dibujar_tablero(tablero)
            print("Perdiste :(")
            break
        """


def crear_tablero():
    tablero = []
    for i in range(9):
        fila = []
        for j in range(9):
            fila.append(Bloque())
        tablero.append(fila)
    return tablero


def movimiento(tablero):
    dibujar_tablero(tablero)
    while True:
        try:
            coord = input("Escriba una coordenada: ")
            x , y = convertirCoord(coord)
            tablero[y][x].no_bomb = contar_bombas(tablero, x, y)
            tablero[y][x].show = True
            break
        except (IndexError, ValueError):
            pass
    if primerMovimiento(tablero):
        return(setGame(tablero))
    return tablero



def primerMovimiento(tablero):
    count = 0
    for i in range(ALTURA_TABLERO):
        for j in range(ANCHO_TABLERO):
            if tablero[i][j].bomb:
                count += 1
    if count == 0:
        return True
    else:
        return False
    

def setGame(tablero):
    for i in range(10):
        while True:
            try:
                x = random.randint(0, ANCHO_TABLERO - 1)
                y = random.randint(0, ALTURA_TABLERO - 1)
                if tablero[y][x].bomb:
                    raise ValueError
                elif revelado(tablero, x, y):
                    raise ValueError
                else:
                    break
            except ValueError:
                pass
        tablero[y][x].bomb = True
        tablero[y][x].show = True
    return tablero


def dibujar_tablero(tablero):
    for i in range(ALTURA_TABLERO):
        for j in range(ANCHO_TABLERO):
            print(tablero[i][j], end="")
        print()
    

def convertirCoord(coord):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    x, y = list(coord)
    y = int(y) - 1
    if x.lower() in letters:
        x = letters.index(x.lower())
    else:
        raise ValueError
    if y < 0 or y > 9:
        raise ValueError
    return x, y


def revelado(tablero, x, y):
    for i in range(-1, 1):
        try:
            if tablero[y - 1][x + i].show:
                return True
        except IndexError:
            pass
    for i in range(-1, 1):
        try:
            if tablero[y][x + i].show:
                return True
        except IndexError:
            pass
    for i in range(-1, 1):
        try:
            if tablero[y + 1][x + i].show:
                return True
        except IndexError:
            pass
    return False


def contar_bombas(tablero, y, x):
    count = 0
    for i in range(-1, 1):
        try:
            if tablero[y - 1][x + i].bomb:
                count += 1
        except IndexError:
            pass
    for i in range(-1, 1,):
        try:
            if tablero[y][x + i].bomb:
                count += 1
        except IndexError:
            pass
    for i in range(-1, 1):
        try:
            if tablero[y + 1][x + i].bomb:
                count += 1
        except IndexError:
            pass
    if not(tablero[y][x].bomb):
        tablero[y][x].no_bomba = count
    return tablero[y][x].no_bomba


def perder(tablero):
    for i in range(ALTURA_TABLERO):
        for j in range(ANCHO_TABLERO):
            if tablero[i][j].bomb and tablero[i][j].show:
                return True

if __name__ == "__main__":
    main()