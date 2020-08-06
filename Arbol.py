
class Arbol:
    def __init__(self, elem, padre=None):
        self.hijos = []
        self.val = elem
        self.padre = padre

    def getRango(self):
        return len(self.hijos)

    def setPadre(self, padre):
        self.padre = padre

    def getValor(self):
        return self.val

    def getHijos(self):
        return self.hijos

    def getMinHijo(self):
        pos = 0
        mini = float("inf")
        posmin = 0
        while pos < len(self.hijos):
            if self.hijos[pos][2] < mini:
                mini = self.hijos[pos][2]
                posmin = 0
            pos += 1
        return posmin, self.hijos[pos]

    def añadir(self, elem):
        self.hijos.append(Arbol(elem, self))
