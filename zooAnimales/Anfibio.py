from zooAnimales.Animal import Animal

class Anfibio (Animal):
    _listado=[]
    ranas=0
    salamandras=0
    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPiel=None, venenoso=None) :
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel= colorPiel
        self._venenoso= venenoso
        Anfibio._listado.append (self)
    def movimiento():
        return "saltar"
    
    @classmethod
    def crearRana (cls, nombre, edad, genero) :
        Anfibio.ranas+=1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)
        
    @classmethod
    def crearSalamandra (cls,nombre, edad, genero) :
        Anfibio.salamandras+=1
        return Anfibio (nombre, edad, "selva", genero, "negro y amarillo", False)
    
    @classmethod
    def cantidadAnfibios (cls) :
        return len (Anfibio._listado)
    def setListado (cls, listado) :
        Anfibio._listado= listado
    def getListado (cls) :
        return Anfibio._listado
    def setColorPiel (self, color) :
        self._colorPiel= color
    def getColorPiel (self) :
        return self._colorPiel
    def setVenenoso (self, veneno) :
        self._venenoso= veneno
    def isVenenoso (self) :
        return self._venenoso