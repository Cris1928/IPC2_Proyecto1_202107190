from ListaCelda import ListaC
class pacienten:
    def __init__(self, nombre=None,edad=None,periodo=None,m=None):
        self.nombre=nombre
        self.edad=edad
        self.periodo=periodo
        self.m=m
        self.celdas=ListaC()
        self.siguiente=None


