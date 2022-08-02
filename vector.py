class V3(object):
    def __init__(self, x, y, z = 0):
        #Recibiendo una lista de 3 elementos.
        self.x = x
        self.y = y
        self.z = z

    #OVerload de la suma.
    def __add__(self, other):
        return V3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.y
        )

    #Ovoerload de la resta.
    def __sub__(self, other):
        return V3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.y
        )

    def __repr__(self): #Overloading de la funcion __repr__
        #Devuelve una cadena que representa el objeto.
        return("V3(%s, %s, %s)" % (self.x, self.y, self.z))