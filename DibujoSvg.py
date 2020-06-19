import webbrowser
from time import sleep


class Dibujo:
    def __init__(self, ancho, alto):
        self.dibujo = []
        self.nombre = "prueba.html"
        self.dibujo = []
        self.dibujo.append("<html>\n")  # Escribimos las lineas de html necesarias
        self.dibujo.append("<head>\n")
        self.dibujo.append('<meta http-equiv="refresh" content="5">\n')
        self.dibujo.append("</head>\n")
        self.dibujo.append("<body>\n")
        self.dibujo.append('<svg width="' + str(ancho) + '" height="' + str(alto) + '">\n')  # Se crea el svg
        self.dibujo.append('<rect width="' + str(ancho) + '" height="' + str(  # Se pone un fondo negro
            alto) + '" style="fill:rgb(0,0,0);stroke-width:3;stroke:rgb(0,0,0)" />\n')
        self.dibujo.append("</svg>\n")
        self.dibujo.append("</body>\n")
        self.dibujo.append("</html>\n")

        webbrowser.open(self.nombre)  # Se abre el navegador

    def GetSvg(self):
        return self.dibujo[5:-4]

    def GetHTML(self):
        return self.dibujo

    def EscribirLinea(self, linea, final=False):
        if final:
            pos = -3
        else:
            pos = 7
        if isinstance(linea, str):
            self.dibujo.insert(pos, linea + "\n")  # Se añade la nueva
        else:
            for elem in linea:
                self.dibujo.insert(pos, elem + "\n")  # En caso de ser una lista se añaden todos

    def Mostrar(self):
        f = open("prueba.html", "w")
        f.writelines(self.dibujo)
        f.close()

    def Terminar(self):
        self.dibujo[2] = '<meta http-equiv="refresh" content="500">\n'
        self.Mostrar()
