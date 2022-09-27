from gestion.Zona import Zona

class Animal:
    _totalAnimales=0
    def __init__(self, nombre, edad, habitat, genero, Zona=None) :
        self._nombre= nombre
        self._edad= edad
        self._habitat= habitat
        self._genero= genero
        self._Zona= Zona
        Animal._totalAnimales +=1
    
    def movimiento() :
        return "desplazarse"
    
    @classmethod
    def totalPorTipo(cls) :
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio
        return f"Mamiferos : {Mamifero.cantidadMamiferos()}\nAves : {Ave.cantidadAves()}\nReptiles : {Reptil.cantidadReptiles()}\nPeces : {Pez.cantidadPeces()}\nAnfibios : {Anfibio.cantidadAnfibios()}"

    def toString(self) :
        if self._Zona != None:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._Zona.getNombre()} en el {self._Zona.getZoo().getNombre()}"
        else:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
    def setNombre(self, nombre) :
        self._nombre= nombre
    def getNombre(self) :
        return self._nombre 
    def setEdad(self, edad) :
        self._edad= edad
    def getEdad(self) :
        return self._edad
    def setHabitat(self, habitat) :
        self._habitat= habitat
    def getHabitat(self) :
        return self._habitat 
    def setGenero(self, genero) :
        self._genero= genero
    def getGenero(self) :
        return self._genero
    def setZona(self, zona) :
        self._Zona[0]= Zona
    def getZona(self) :
        return self._Zona[0] 