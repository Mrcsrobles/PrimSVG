import webbrowser
from Punto import Punto
from random import randint
from time import sleep
from math import asin


def InicializarSVG(ancho, alto):
    nombre = "prueba.html"
    f = open(nombre, "w")
    f.close()
    f = open(nombre, "r+")
    cola = []
    cola.append("<html>\n")  # Escribimos las lineas de html necesarias
    cola.append("<head>\n")
    cola.append('<meta http-equiv="refresh" content="5">\n')
    cola.append("</head>\n")
    cola.append("<body>\n")
    cola.append('<svg width="' + str(ancho) + '" height="' + str(alto) + '">\n')  # Se inserta en el 6
    cola.append('<rect width="' + str(ancho) + '" height="' + str(
        alto) + '" style="fill:rgb(0,0,0);stroke-width:3;stroke:rgb(0,0,0)" />\n')
    cola.append("</svg>\n")
    cola.append("</body>\n")
    cola.append("</html>\n")
    f.writelines(cola)
    f.close()
    webbrowser.open(nombre)


def CrearPuntos(ancho, alto, numPuntos=50):  # Cambias el valor para decidir cuantos puntos habrá
    l = []  # lista de puntos
    g = []  # matriz de adyacencia
    for i in range(0, numPuntos):
        l.append(Punto(randint(0, alto), randint(0, ancho)))  # Se crea un punto aleatorio
        EscribirLinea(l[-1].GetSvg())  # Se dibuja en SVG el punto creado
        # sleep(0.25)#Se espera
    for j in range(len(l)):
        g.append([0] * len(l))
    for i in range(0, len(l)):
        print(i)
        for j in range(0, len(l)):
            if i == j:
                g[i][j] = float("inf")

            else:
                g[i][j] = l[i].CalcularDistancia(l[j])  # Se rellena la matriz con las distancias a todos los puntos
                g[j][i] = g[i][j]
    return l, g


def SacarAristas(g, elem, visitados, aristas=[]):
    cola = []
    for i in range(0, len(g[elem])):
        if not visitados[i]:
            cola.append((elem, i, g[elem][i]))  # Se devuelve i,j,distancia
    aristas.extend(cola)
    return aristas


def LimpiarVisitados(cola, visitados):
    Borrables = []
    for counter, elem, i, dist in enumerate(cola):
        if visitados[i]:
            Borrables.append(counter)
    Borrables.reverse()
    for i in Borrables:
        cola.pop(i)


def CrearLinea(p1, p2):
    i1, j1 = p1.GetPuntos()
    r1 = p1.GetRadio()
    r2= p2.GetRadio()
    i2, j2 = p2.GetPuntos()
    IncrementoJ1 = (j2 - j1)
    IncrementoJ2 = -IncrementoJ1
    IncrementoI1 = (i2 - i1)
    IncrementoI2 = -IncrementoI1

    h = (IncrementoI1 ** 2 + IncrementoJ1 ** 2) ** 0.5
    print(asin(IncrementoI1 / h))
    return '<line x1="' + str(j1 + r1 * (IncrementoJ1) / h) + '" y1="' + str(
        i1 + r1 * (IncrementoI1) / h) + '" x2="' + str(j2 + r2 * (IncrementoJ2) / h) + '" y2="' + str(
        i2 + r2 * (IncrementoI2) / h) + '" style="stroke:rgb(240,240,240);stroke-width:2" />'


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
    try:
        f = open("prueba.html", "w")
    except OSError:
        sleep(1)
        f = open("prueba.html", "w")
    f.writelines(cola)  # Se escribe el nuevo dibujo
    f.close()


def Prim(g, l):
    visitados = [False] * len(g)
    visitados[0] = True
    aristas = SacarAristas(g, 0, visitados)
    aristas.sort(key=lambda x: x[2])
    while not all(visitados) and aristas:
        linea = aristas.pop(0)
        if not visitados[linea[1]]:
            if randint(0,2)==1:
                EscribirLinea(CrearLinea(l[linea[0]], l[linea[1]]), True)  # Se dibuja la linea que une los puntos
            # sleep(1)
            visitados[linea[1]] = True
            SacarAristas(g, linea[1],visitados,aristas)  # Se añaden las aristas del nuevo punto
            aristas.sort(key=lambda x: x[2])  # Se ordenan las aristas por distancias

    input("end")


ancho = 1920
alto = 1080
puntos = 100

InicializarSVG(ancho, alto)
sleep(1)
l, g = CrearPuntos(ancho, alto, puntos)
"""
p1=Punto(200,300)
p2=Punto(100,200)
EscribirLinea(p1.GetSvg())
EscribirLinea(p2.GetSvg())
EscribirLinea(CrearLinea(p2,p1))
"""
Prim(g, l)
