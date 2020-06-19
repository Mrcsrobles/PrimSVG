class Cola:
    def __init__(self):
        self.cola = []

    def Añadir(self, elem):
        pos = self.BusquedaBinaria(self.cola, elem[2])
        self.cola.insert(pos, elem)

    def Popleft(self):
        return self.cola.pop(0)

    def IsEmpty(self):
        return len(self.cola) == 0

    def __bs__(self, l, elem, ini, fin):
        mitad = (ini + fin) // 2
        vmitad = l[mitad][2]
        if fin < ini:
            return -1
        elif l[mitad - 1][2] <= elem < vmitad:
            return mitad
        elif vmitad <= elem < l[mitad + 1][2]:
            return mitad + 1
        elif elem > vmitad:
            return self.__bs__(l, elem, mitad + 1, fin)
        elif elem < vmitad:
            return self.__bs__(l, elem, ini, mitad - 1)

    def BusquedaBinaria(self, l, peso):
        if len(l) == 0:
            return 0
        elif l[0][2] >= peso:
            return 0
        elif l[-1][2] <= peso:
            return len(l)
        else:
            return self.__bs__(l, peso, 0, len(l))
