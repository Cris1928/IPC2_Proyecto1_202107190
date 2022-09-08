from ListaComparacion import ListaComparar
class numeralnodo:
    def __init__(self,numeral=None):
        self.numeral=numeral
        self.celdas=ListaComparar()
        self.siguiente=None