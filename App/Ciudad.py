class Ciudad:
    numero = 0
    nombre = ''
    visitado = False

    def __init__(self, number, name):
        self.numero = number
        self.nombre = name
    
    def getNumero(self):
        return self.numero

    def setVisitado(self, newNumber):
        self.visitado = newNumber

    def getVisitado(self):
        return self.visitado

    def setVisitado(self, newVisited):
        self.visitado = newVisited
 
    def getNombre(self):
        return self.nombre

    def setNombre(self, newName):
        self.nombre = newName