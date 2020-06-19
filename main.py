from DibujoSvg import Dibujo
from Punto import Punto
from ColaDePrioridad import Cola
from random import randint
from time import sleep
from math import asin



#iniciadores
def CrearPuntos(ancho, alto, numPuntos=50):  # Cambias el valor para decidir cuantos puntos habrá
    #Crea un número N de puntos aleatorios y su matriz de adyacencia
    dibujo=Dibujo(ancho,alto)
    l = []  # lista de puntos
    g = []  # matriz de adyacencia

    for i in range(0, numPuntos):
        l.append(Punto(randint(0, alto), randint(0, ancho),aleatorio=False))  # Se crea un punto aleatorio
        dibujo.EscribirLinea(l[-1].GetSvg())  # Se dibuja en SVG el punto creado
        # sleep(0.25)#Se espera
    for j in range(len(l)):
        g.append([0] * len(l))#Se inicializan a 0 las distancias
    for i in range(0, len(l)):
        for j in range(0, len(l)):
            if i == j:
                g[i][j] = float("inf")#La distancia de un punto a él mismo se pone infinita para que no sea factible nunca
            else:
                g[i][j] = l[i].CalcularDistancia(l[j])  # Se rellena la matriz con las distancias a todos los puntos
                g[j][i] = g[i][j]
    return l, g,dibujo

def CrearCuadrícula(ancho, alto, numPuntos,dibujo):
    l = []  # lista de puntos
    g = []  # matriz de adyacencia
    separación=50
    for i in range(0, numPuntos):
        for j in range(0, numPuntos):
            l.append(Punto(10+i*separación, 10+j*separación))  # Se crea un punto aleatorio
            dibujo.EscribirLinea(l[-1].GetSvg())  # Se dibuja en SVG el punto creado
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

def SacarAristas(g, elem, visitados, aristas=Cola()):#Devuelve en una lista todas las aristas del elemento indicado
    for i in range(0, len(g[elem])):
        if not visitados[i]:
            aristas.Añadir((elem, i, g[elem][i]))  # Se devuelve i,j,distancia
    return aristas


def CrearLinea(p1, p2):
    #Crea una línea entre dos puntos, además, deja un espacio vacío para que quede bonito
    i1, j1 = p1.GetPuntos()
    r1 = p1.GetRadio()
    r2 = p2.GetRadio()
    i2, j2 = p2.GetPuntos()
    IncrementoJ1 = (j2 - j1)
    IncrementoJ2 = -IncrementoJ1
    IncrementoI1 = (i2 - i1)
    IncrementoI2 = -IncrementoI1

    h = (IncrementoI1 ** 2 + IncrementoJ1 ** 2) ** 0.5#hipotenusa
    print(asin(IncrementoI1 / h))
    return '<line x1="' + str(j1 + r1 * (IncrementoJ1) / h) + '" y1="' + str(
        i1 + r1 * (IncrementoI1) / h) + '" x2="' + str(j2 + r2 * (IncrementoJ2) / h) + '" y2="' + str(
        i2 + r2 * (IncrementoI2) / h) + '" style="stroke:rgb(240,240,240);stroke-width:2" />'




def Prim(g, l,dibujo):
    visitados = [False] * len(g)
    visitados[0] = True
    aristas = SacarAristas(g, 0, visitados)
    while not all(visitados) and not aristas.IsEmpty():
        linea = aristas.Popleft()
        if not visitados[linea[1]]:
            dibujo.EscribirLinea(CrearLinea(l[linea[0]], l[linea[1]]), True)  # Se dibuja la linea que une los puntos
            # sleep(1)
            visitados[linea[1]] = True
            SacarAristas(g, linea[1], visitados, aristas)  # Se añaden las aristas del nuevo punto
    dibujo.Terminar()
    input("end")




def UnirTodo(g, l,dibujo):
    for i in range(0, len(g)):
        for j in range(0, len(g)):
            if not i == j:
                dibujo.EscribirLinea(CrearLinea(l[i], l[j]), True)
            else:
                break



ancho = 10000
alto = 10000
puntos = 500

sleep(1)
l, g ,d= CrearPuntos(ancho, alto, puntos)
"""
p1=Punto(200,300)
p2=Punto(100,200)
EscribirLinea(p1.GetSvg())
EscribirLinea(p2.GetSvg())
EscribirLinea(CrearLinea(p2,p1))
"""
d.Mostrar()
Prim(g, l,d)