from NodoNumeral import numeralnodo
class ListadoNumeral:
        def __init__(self)-> None:
                self.primero=numeralnodo()
                self.ultimo=numeralnodo()

        def append(self,nuevonumeral):
                if self.primero.numeral is None:
                        self.primero=nuevonumeral
                        self.ultimo=nuevonumeral
                elif self.primero.siguiente is None:
                        self.primero.siguiente=nuevonumeral
                        self.ultimo=nuevonumeral
                else:
                        self.ultimo.siguiente=nuevonumeral
                        self.ultimo=nuevonumeral
        def buscarnumero(self,nuevonumeral):
                nodoaux=self.primero
                while nodoaux.numeral != nuevonumeral:
                        if nodoaux.siguiente is not None:
                                
                                nodoaux=nodoaux.siguiente
                        else:
                                return None
                return nodoaux

        def limpiarList(self):
            i = 1
            actual = self.primero
            while actual is not None:
                self.primero = None
                actual=actual.siguiente
                
                i += 1