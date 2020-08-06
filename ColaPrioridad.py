class Cola:
    def __init__(self):
        self.cola = []

    def Añadir(self, elem):
        pos = self.BusquedaBinaria(self.cola, elem.getValor())
        self.cola.insert(pos, elem)

    def getCola(self):
        return self.cola

    def Popleft(self):
        return self.cola.pop(0)
    def getMin(self):
        return self.cola[0].getValor()
    def pop(self, pos):
        self.cola.pop(pos)

    def IsEmpty(self):
        return len(self.cola) == 0

    def length(self):
        return len(self.cola)

    def merge(self, newCola):
        if newCola.length()<self.length():
            for val in newCola.getCola():
                self.Añadir(val)
        else:
            for val in self.cola:
                newCola.Añadir(val)
            self.cola=newCola.getCola()

    def __bs__(self, l, elem, ini, fin):
        mitad = (ini + fin) // 2
        vmitad = l[mitad].getValor()
        if fin < ini:
            return -1
        elif l[mitad - 1].getValor() <= elem < vmitad:
            return mitad
        elif vmitad <= elem < l[mitad + 1].getValor():
            return mitad + 1
        elif elem > vmitad:
            return self.__bs__(l, elem, mitad + 1, fin)
        elif elem < vmitad:
            return self.__bs__(l, elem, ini, mitad - 1)

    def BusquedaBinaria(self, l, peso):
        if len(l) == 0:
            return 0
        elif l[0].getValor() >= peso:
            return 0
        elif l[-1].getValor() <= peso:
            return len(l)
        else:
            return self.__bs__(l, peso, 0, len(l))
