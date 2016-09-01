class Casa(object):
    def __init__(self,costo,direccion,numero):
        self.__costo = costo
        self.__direccion   = direccion
        self.__numero = numero
    def getCosto(self):
        return self.__costo
    def getDireccion(self):
        return self.__direccion
    def getNumero(self):
        return self.__numero
    def setCosto(self,costo):
        self.__costo = costo
    def setDireccion(self,direccion):
        self.__direccion = direccion
    def setNumero(self,numero):
        self.__numero = numero
    def toString(self):
        return self.__costo+' - '+str(self.__direccion)+' - '+self.__numero