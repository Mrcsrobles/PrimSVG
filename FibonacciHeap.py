from ColaPrioridad import Cola


class FH:
    def __init__(self):
        self.hijos = Cola()
        self.rangos = dict()

    def añadir(self, val):
        newTree = Tree(val, None)
        self.hijos.Añadir(newTree)

    def merge(self, newFH):
        self.hijos.merge(newFH.getHijos())

    def IsEmpty(self):
        return self.hijos.IsEmpty()

    def extractmin(self):
        minimunTree = self.hijos.Popleft()
        minimunVal = minimunTree.getFullData()
        hijos = minimunTree.getHijos()
        for val in hijos:  # Se añaden los hijos del nodo a la lista de árboles
            self.hijos.Añadir(val)
        contador = 0
        arboles = self.hijos.getCola()
        self.rangos = dict()
        while contador < self.hijos.length():
            try:
                if self.rangos[
                    arboles[contador].getRango()] is not None:  # Solo si la clave apunta a un lado que no sea -1 o None
                    arbolActual = arboles.pop(contador)  # Se coge el árbol
                    pos = arbolActual.getRango()  # Se le añade como hijo al minimo que debe ser el padre indicado por el rango
                    pos = self.rangos[pos]  # Se saca la posición
                    arboles[pos].añadirHijo(arbolActual)  # se añade el hijo
                    self.rangos[pos] = None  # Poner el valor de la pos a none
                    self.rangos[pos + 1] = pos  # Poner la nueva posición
                    continue

            except KeyError:  # Si no aparece la clave o no es -1
                pass
            self.rangos[arboles[contador].getRango()] = contador  # todo dudo que esto funcione al cambiar la lista
            contador += 1

        return minimunVal

    def getHijos(self):
        return self.hijos


class Tree:
    def __init__(self, val, padre=None):
        self.val = val
        #self.padre = padre
        self.hijos = []

    def añadirHijo(self, elem):
        self.hijos.append(elem)

    def getValor(self):
        return self.val[2]

    def getFullData(self):
        return self.val

    def getHijos(self):
        return self.hijos

    def getRango(self):
        return len(self.hijos)


