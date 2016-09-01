from casa import Casa
class Propiedad(Casa):
    def __init__(self,costo,direccion,numero=None):
        Casa.__init__(self,costo,direccion,numero)
        if(numero is None):
            numero=[]
        self.__numero = numero
		
    def getMostrar(self):
        return self.__numero

    def toString(self):
        return super(Propiedad,self).toString()+' - '+str(self.__numero)