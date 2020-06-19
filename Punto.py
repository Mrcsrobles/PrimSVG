from random import randint


class Punto:
    puntos = set()

    def __init__(self, i, j, r=10, aleatorio=True):
        if aleatorio:
            randomi, randomj = randint(0, i), randint(0, j)
            valido, pi, pj, radio = self.__Sol__(randomi, randomj, r)
            contador = 0
            while not valido:
                if contador == 3:
                    randomi = randint(0, i)
                    randomj = randint(0, j)
                else:
                    randomi, randomj = self.__Calculo__(i, j, r, pi, pj, radio)
                valido, pi, pj, radio = self.__Sol__(randomi, randomj, r)
                contador += 1
            self.i = randomi
            self.j = randomj
            self.radio = r
            self.puntos.add((randomi,randomj, r))

        else:
            self.i = i
            self.j = j
            self.radio = r
            self.puntos.add((i, j, r))

    def GetPuntos(self):
        return (self.i, self.j)  # Returns

    def __Sol__(self, i, j, r):
        for pi, pj, radio in self.puntos:
            if abs(i + j - pi - pj) >= max(radio, r) + radio + r:
                pass
            else:
                return (False, pi, pj, radio)
        return (True, 0, 0, 0)

    def __Calculo__(self, i, j, r, pi, pj, radio):
        IncrementoJ1 = abs(j - pj)
        IncrementoI1 = abs(i - pi)
        h = (IncrementoI1 ** 2 + IncrementoJ1 ** 2) ** 0.5
        newj = j + (r + radio) * (IncrementoJ1) / h
        newi = i + (r + radio) * (IncrementoI1) / h
        return (int(newi), int(newj))

    def GetRadio(self):
        return self.radio

    def GetSvg(self):
        l = []
        for i in (1, -1):
            for j in (1, -1):
                l.append('<circle cx="' + str(self.j + j * self.radio) + '" cy="' + str(
                    self.i + i * self.radio) + '" r="' + str(
                    self.radio) + '" stroke="black" stroke-width="3" fill="black" />\n')
        l.append('<circle cx="' + str(self.j) + '" cy="' + str(
            self.i) + '" r="' + str(self.radio) + '" stroke="black" stroke-width="3" fill="white" />\n')
        return l

    def CalcularDistancia(self, punto):
        i1 = self.i
        j1 = self.j
        i2, j2 = punto.GetPuntos()
        return ((i1 - i2) ** 2 + (j1 - j2) ** 2) ** 0.5
