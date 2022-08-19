from NodoCelda import Celda

class ListaC:
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.size=0

    def insertar(self,fila,columna,tipo):
        nuevo=Celda(fila,columna,tipo)
        if self.primero is None:
            self.primero=nuevo
            self.ultimo=nuevo
            self.size +=1
        else: 
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
            self.size += 1

    def mostrarCeldas(self):
        
        actual = self.primero
        
        while actual is not None:
            
            print('fila: ' + str(actual.fila) + ' columna: ' + str(actual.columna) + ' tipo: ' + str(actual.tipo))
            print()
            
            actual = actual.siguiente
        print()
        print()

    def buscar(self, fil, column):
        actual=self.primero
        i=1
        while actual is not None:
            if fil==actual.fila and column==actual.columna:
                 print('fila: ' + str(actual.fila) + ' columna: ' + str(actual.columna) + ' tipo: ' + str(actual.tipo))
            
            actual=actual.siguiente


    def pop(self, fil, column):
        if fil  is None and column is None:
            if self.primero.siguiente is None:
                self.primero=Celda()
            

            else:
                aux=self.primero
                penultimo=aux
                while aux.siguiente is not None:
                    penultimo=aux
                    aux=aux.siguiente
                penultimo.siguiente=None
        else:
            if self.primero.fila is fil and self.primero.columna is column:
                if self.primero.siguiente is not None:
                    self.primero=self.primero.siguiente
                else:
                    self.primero=Celda()

            else:
                aux=self.primero
                anterior=aux
                while aux.fila is not fil and aux.columna is not column:
                    anterior=aux
                    if aux.siguiente is not None:
                        aux=aux.siguiente
                    else:
                        return None
                anterior.siguiente=aux.siguiente


        
        
        

        
                





   # def append(self, nuevacelda):
    #    if self.raiz.fila is None:
     #       self.raiz=nuevacelda
       # elif self.raiz.siguiente is None:
      #      self.raiz.siguiente=nuevacelda
       # else:
        #    self.ultimo.siguiente=nuevacelda
         #   self.ultimo=nuevacelda
"""






actual=self.primero
        anterior=actual
        while actual is not None:
            if fil==actual.fila and column==actual.columna:
                anterior.siguiente=actual.siguiente
                print("listo")
                break

            anterior=actual
            actual.siguiente






    def printt(self):
        nodoAux=self.raiz
        cadena=" "
        while True:
            if nodoAux.fila is not None:
                cadena += "(" + nodoAux.fila + "-"+ nodoAux.columna + nodoAux.tipo + ")"
                if nodoAux.siguiente is not None:
                    nodoAux = nodoAux.siguiente
                    cadena="->"
                else: 
                    break

            else:
                break
        print(cadena)
"""