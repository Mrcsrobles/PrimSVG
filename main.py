import webbrowser
from Punto import Punto
from random import randint
from time import sleep
from math import asin

def InicializarSVG():
    nombre = "prueba.html"
    f = open(nombre, "w")
    f.close()
    f = open(nombre, "r+")
    cola = []
    cola.append("<html>\n")  # Escribimos las lineas de html necesarias
    cola.append("<head>\n")
    cola.append('<meta http-equiv="refresh" content="1">\n')
    cola.append("</head>\n")
    cola.append("<body>\n")
    cola.append('<svg width="1980" height="1080">\n')  # Se inserta en el 6
    cola.append('<rect width="1920" height="1080" style="fill:rgb(0,0,0);stroke-width:3;stroke:rgb(0,0,0)" />\n')
    cola.append("</svg>\n")
    cola.append("</body>\n")
    cola.append("</html>\n")
    f.writelines(cola)
    f.close()
    webbrowser.open(nombre)


def CrearPuntos(numPuntos=3):  # Cambias el valor para decidir cuantos puntos habrá
    l = []  # lista de puntos
    g = []  # matriz de adyacencia
    for i in range(0, numPuntos):
        l.append(Punto(randint(0, 900), randint(0, 1800)))  # Se crea un punto aleatorio
        EscribirLinea(l[-1].GetSvg())  # Se dibuja en SVG el punto creado
        sleep(0.25)#Se espera
    for i in l:
        EscribirLinea(i.GetSvg())
    for i in range(0, len(l)):
        g.append([])
        for j in range(0, len(l)):
            if i == j:
                g[-1].append(float("inf"))
            else:
                g[-1].append(l[i].CalcularDistancia(l[j]))  # Se rellena la matriz con las distancias a todos los puntos
    return l, g


def SacarAristas(g, elem):
    cola = []
    for i in range(0, len(g[elem])):
        cola.append((elem, i, g[elem][i]))  # Se devuelve i,j,distancia
    return cola


def CrearLinea(p1, p2):
    i1, j1 = p1.GetPuntos()
    r = p1.GetRadio()
    i2, j2 = p2.GetPuntos()
    IncrementoJ1 = abs(j2 - j1)
    IncrementoJ2 = -IncrementoJ1
    IncrementoI1 = abs(i2 - i1)
    IncrementoI2 = -IncrementoI1
    h = (IncrementoI1 ** 2 + IncrementoJ1 ** 2) ** 0.5
    print(asin(IncrementoI1/h))
    return '<line x1="' + str(j1 + r * (IncrementoJ1) / h) + '" y1="' + str(
        i1 + r * (IncrementoI1) / h) + '" x2="' + str(j2 + r * (IncrementoJ2) / h) + '" y2="' + str(
        i2 + r * (IncrementoI2) / h) + '" style="stroke:rgb(240,240,240);stroke-width:2" />'


def EscribirLinea(linea, final=False):
    f = open("prueba.html", "r")
    cola = f.readlines()
    f.close()  # Se toman las lineas hasta ahora escritas
    if final:
        pos = -3
    else:
        pos = 7
    if isinstance(linea, str):
        cola.insert(pos, linea + "\n")  # Se añade la nueva
    else:
        for elem in linea:
            cola.insert(pos, elem + "\n")  # En caso de ser una lista se añaden todos
    f = open("prueba.html", "w")
    f.writelines(cola)  # Se escribe el nuevo dibujo
    f.close()


def Prim(g, l):
    aristas = SacarAristas(g, 0)
    aristas.sort(key=lambda x: x[2])
    visitados = [False] * len(g)
    visitados[0] = True
    while not all(visitados) and aristas:
        linea = aristas.pop(0)
        if not visitados[linea[1]]:
            EscribirLinea(CrearLinea(l[linea[0]], l[linea[1]]), True)  # Se dibuja la linea que une los puntos
            sleep(1)
            aristas.extend(SacarAristas(g, linea[1]))  # Se añaden las aristas del nuevo punto
            aristas.sort(key=lambda x: x[2])  # Se ordenan las aristas por distancias
            visitados[linea[1]] = True
    input("end")

InicializarSVG()
sleep(1)
l, g = CrearPuntos()
Prim(g, l)
