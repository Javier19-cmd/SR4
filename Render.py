from utilidades import * #Archivo de utilidades.

class Render(object):

    #Estas variables son globales y tienen valores por defecto y arbitrarios.
    WHITE = color(1, 1, 1) #Color blanco hecho con las utilidades.
    colorFondo = 0 #Asignando el color blanco al framebuffer.
    #print("Color del fondo: ", colorFondo)
    colorViewPort = WHITE #Asignando el color blanco al viewport. Esto es temporal-
    width = 0 #Ancho de la pantalla. Esto es temporal.
    height = 0 #Alto de la pantalla. Esto es temporal.
    
    widthV = 0 #Ancho del viewport. Esto es temporal.
    heightV = 0 #Alto del viewport. Esto es temporal.

    xV = 0 #Posición en x del viewport.
    yV = 0 #Posición en y del viewport.
    colorP = 0 #Asignando el color blanco al punto. Esto es temporal.

    framebuffer = [] #Framebuffer.

    zBuffer = [] #Zbuffer.


    #Método que dibuja un punto.
    def punto(self,x, y):
        #En este método se dibuja un punto en la pantalla.
        global equis, ye #Instanciando las variables globales de las posiciones del punto.

        #Llenando las variables globales.
        equis = x
        ye = y

        #Esta función dibuja un punto en la pantalla.
        #print(framebufobsfer[x][y])

        self.framebuffer[y][x] = self.colorP #El color del punto es el color actual.


    #Método que hace el viewport del archivo.
    def View(self, posX, posY, ancho, alto):
        #En este método se hace el viewport del archivo.

        #print(Posx, Posy)
        self.xV = posX
        self.yV = posY
        self.widthV = ancho
        self.heightV = alto

        #Probando la lista.
        lista = [
                [self.colorViewPort for x in range(ancho)]
                for y in range(alto)
            ]

        #print("Lista del viewport", lista)

        #Hacer una copia del viewport en el framebuffer con los índices iguales.
        for i in range(ancho):
            for j in range(alto):
                self.framebuffer[posY + j][posX + i] = lista[j][i]
        
        #print(framebuffer)

        #Hacer un cuadrado en el framebuffer.
        # for x in range(Ancho):
        #     for y in range(Alto):
        #         #print(Posx, Posy)
        #         #print(framebuffer[x][y])
        #         framebuffer[x][y] = colorV

        #framebuffer[Posx][Posy] = colorV #El color del viewport es el color actual.

    def Vertex(self,x, y):
        #En este método se dibuja un punto en el viewport.

        #Colocar el punto en el viewport.
        self.framebuffer[y][x] = self.colorP #El color del punto es el color actual.


        #print("Coordenadas del punto: ", ye, equis)
        #print("Punto: ", framebuffer[ye][equis])


    #Método que escribe el archivo bmp.
    def write(self):
            
            #Se abre el archivo con la forma de bw.
            f = open("SR4.bmp", "bw")

            #Se escribe el encabezado del archivo.

            #Haciendo el pixel header.
            f.write(char('B'))
            f.write(char('M'))
            #Escribiendo el tamaño del archivo en bytes.
            f.write(dword(14 + 40 + self.width * self.height * 3))
            f.write(dword(0)) #Cosa que no se utilizará en este caso.
            f.write(dword(14 + 40)) #Offset a la información de la imagen. 14 bytes para el header, 40 para la información de la imagen. Aquí empieza la data.
            #Lo anterior suma 14 bytes.

            #Información del header.
            f.write(dword(40)) #Este es el tamaño del header. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(dword(self.width)) #Ancho de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(dword(self.height)) #Alto de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(word(1)) #Número de planos. Esto es de 2 bytes, por eso se utiliza el word.
            f.write(word(24)) #24 bits por pixel. Esto es porque usa el true color y el RGB.
            f.write(dword(0)) #Esto es la compresión. Esto es de 4 bytes, por eso se utiliza el dword.
            f.write(dword(self.width * self.height * 3)) #Tamaño de la imagen sin el header.
            #Pixels que no se usarán mucho.
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))
            #Lo anterior suma 40 bytes.

            #print("Framebuffer", framebuffer)
            #Pintando el archivo de color negro.
            for y in range(self.height):
                for x in range(self.width):
                    f.write(self.framebuffer[y][x])

            #print("Archivo escrito")

            f.close() #Cerrando el archivo que se escribió.