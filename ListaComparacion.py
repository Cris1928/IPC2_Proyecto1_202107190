from NodoComparacion import Comparacion
class ListaComparar:
    def __init__(self)-> None:
        self.primero=Comparacion()
        self.ultimo=Comparacion()
        self.size=0

    def appendComparar(self, nuevasceldas):
        if self.primero.fila is None:
            self.primero=nuevasceldas
            self.ultimo=nuevasceldas
        elif self.primero.siguiente is None:
            self.primero.siguiente=nuevasceldas
            nuevasceldas.anterior=self.primero
            self.ultimo=nuevasceldas
        
        else:
            self.ultimo.siguiente=nuevasceldas
            nuevasceldas.anterior=self.ultimo
            self.ultimo=nuevasceldas

    def mostrarCeldas(self):
        
        actual = self.primero
        
        while actual is not None:
            print('fila: ' + str(actual.fila) + ' columna: ' + str(actual.columna) + ' tipo: ' + str(actual.tipo))
            actual = actual.siguiente
        print()
        print()
   
    def retornarcelda(self,fila,columna,tipo):

        actual=self.primero
        while actual is not None:
            if fila == actual.fila and columna==actual.columna and tipo==actual.tipo:
                return True
            else: 
                pass
            actual=actual.siguiente
        return False


    def limpiarListaComparar(self):
            i = 1
            actual = self.primero
            while actual is not None:
                self.primero = None
                actual=actual
                
                i += 1
  