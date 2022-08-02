class V3(object):
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self): 
        return("V3(%s, %s, %s)" % (self.x, self.y, self.z))