from NodoNumeral import numeralnodo
class ListadoNumeral:
        def __init__(self)-> None:
                self.primero=numeralnodo()
                self.ultimo=numeralnodo()
                self.size=0

        def append(self,nuevonumeral):
                if self.primero.numeral is None:
                        self.primero=nuevonumeral
                        self.ultimo=nuevonumeral
                        self.size += 1
                elif self.primero.siguiente is None:
                        self.primero.siguiente=nuevonumeral
                        self.ultimo=nuevonumeral
                        self.size += 1
                else:
                        self.ultimo.siguiente=nuevonumeral
                        self.ultimo=nuevonumeral
                        self.size += 1
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
                
                while i < (self.size + 1):
                
                        actual = self.primero.siguiente
                        self.primero = None
                        self.primero = actual
                        
                        i += 1
                
                self.size = 0 