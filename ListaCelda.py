from NodoCelda import Celda

class ListaC:
  
    def __init__(self)-> None:
        self.primero=Celda()
        self.ultimo=Celda()
        self.size=0
    
    def append(self, nuevasceldas):
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


    def evaluar(self,n):
        contador=0
        numeral=1
        while contador<=n:
     
            actual=self.primero

            actual=self.primero
            while actual is not None:
                if actual.tipo==0:
                    filarriba=(int(actual.fila) +1)
                    columnaderecha=(int(actual.columna)+1)
                    filabajo=(int(actual.fila)-1)
                    columnaizquierda=(int(actual.columna)-1)
                    filanactual=(int(actual.fila))
                    columnanactual=(int(actual.columna))
                    actual2=self.primero
                    cumple=0
                    #evalua cuales se contagian 
                    while actual2 is not None:

                        if actual2.fila== filarriba and actual2.columna==columnaizquierda:
                            if actual2.tipo==1:
                                cumple=cumple+1
                            elif actual2.tipo==2:
                                cumple=cumple+1
                            else:
                                pass
                        elif actual2.fila== filarriba and actual2.columna==columnanactual:
                            if actual2.tipo==1:
                                cumple=cumple+1
                            elif actual2.tipo==2:
                                cumple=cumple+1
                            else:
                                pass
                        elif actual2.fila==filarriba and actual2.columna==columnaderecha:
                            if actual2.tipo==1:
                                cumple=cumple+1
                            elif actual2.tipo==2:
                                cumple=cumple+1
                            else:
                                pass
                        elif actual2.fila==filanactual and actual2.columna==columnaizquierda:
                            if actual2.tipo==1:
                                cumple=cumple+1
                            elif actual2.tipo==2:
                                cumple=cumple+1
                            else:
                                pass
                        elif actual2.fila==filanactual and actual2.columna==columnaderecha:
                            if actual2.tipo==1:
                                cumple=cumple+1
                            elif actual2.tipo==2:
                                cumple=cumple+1
                            else:
                                pass
                        elif actual2.fila==filabajo and actual2.columna==columnaizquierda:
                            if actual2.tipo==1:
                                cumple=cumple+1
                            elif actual2.tipo==2:
                                cumple=cumple+1
                            else:
                                pass
                        elif actual2.fila==filabajo and actual2.columna==columnanactual:
                            if actual2.tipo==1:
                                cumple=cumple+1
                            elif actual2.tipo==2:
                                cumple=cumple+1
                            else:
                                pass
                        elif actual2.fila==filabajo and actual2.columna==columnaderecha:
                            if actual2.tipo==1:
                                cumple=cumple+1
                            elif actual2.tipo==2:
                                cumple=cumple+1
                            else:
                                pass
                        else:
                            pass
                        
                        if cumple == 3:
                            actual.tipo=3
                        else:
                            actual.tipo=0
                        actual2=actual2.siguiente

                    #evalua cuales sanaran
                elif actual.tipo==1:
                    filarriba=(int(actual.fila) +1)
                    columnaderecha=(int(actual.columna)+1)
                    filabajo=(int(actual.fila)-1)
                    columnaizquierda=(int(actual.columna)-1)
                    filanactual=(int(actual.fila))
                    columnanactual=(int(actual.columna))
                    actual2=self.primero
                    cumple=0
                    while actual2 is not None:

                        if actual2.fila== filarriba and actual2.columna==columnaizquierda:
                            if actual2.tipo==1:
                                cumple=cumple+1
                            elif actual2.tipo==2:
                                cumple=cumple+1
                            else:
                                pass
                            
                        elif actual2.fila== filarriba and actual2.columna==columnanactual:
                            if actual2.tipo==1:
                                cumple=cumple+1
                            elif actual2.tipo==2:
                                cumple=cumple+1
                            else:
                                pass
                        
                        elif actual2.fila==filarriba and actual2.columna==columnaderecha:
                            if actual2.tipo==1:
                                cumple=cumple+1
                            elif actual2.tipo==2:
                                cumple=cumple+1
                            else:
                                pass
                        
                        elif actual2.fila==filanactual and actual2.columna==columnaizquierda:
                            if actual2.tipo==1:
                                cumple=cumple+1
                            elif actual2.tipo==2:
                                cumple=cumple+1
                            else:
                                pass
                        
                        elif actual2.fila==filanactual and actual2.columna==columnaderecha:
                            if actual2.tipo==1:
                                cumple=cumple+1
                            elif actual2.tipo==2:
                                cumple=cumple+1
                            else:
                                pass
                            
                        elif actual2.fila==filabajo and actual2.columna==columnaizquierda:
                            if actual2.tipo==1:
                                cumple=cumple+1
                            elif actual2.tipo==2:
                                cumple=cumple+1
                            else:
                                pass
                        
                        elif actual2.fila==filabajo and actual2.columna==columnanactual:
                            if actual2.tipo==1:
                                cumple=cumple+1
                            elif actual2.tipo==2:
                                cumple=cumple+1
                            else:
                                pass
                        
                        elif actual2.fila==filabajo and actual2.columna==columnaderecha:
                            if actual2.tipo==1:
                                cumple=cumple+1
                            elif actual2.tipo==2:
                                cumple=cumple+1
                            else:
                                pass
                        
                        else:
                            pass
                        
                
                        if cumple ==2:
                            actual.tipo=1
                        elif cumple ==3:
                            actual.tipo=1
                        else:
                            actual.tipo=2

                        actual2=actual2.siguiente
                actual=actual.siguiente

            actual=self.primero       
            
            while actual is not None:
                if actual.tipo==2:
                    actual.tipo=0
                elif actual.tipo==3:
                    actual.tipo=1
                else:
                    pass
                actual=actual.siguiente
            contador=contador+1

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
            actual = actual.siguiente
        print()
        print()

    def buscar(self, fil, column):
        actual=self.primero
        comprobante=False
        while actual is not None:
            if fil==actual.fila and column==actual.columna:
                # print('fila: ' + str(actual.fila) + ' columna: ' + str(actual.columna) + ' tipo: ' + str(actual.tipo))
                comprobante=True
            else:
                pass   
            actual=actual.siguiente

        if  comprobante==False:
            new=Celda(fil,column,0)
            self.append(new)
                #print('fila: ' + str(actual.fila) + ' columna: ' + str(actual.columna) + ' tipo: ' + str(actual.tipo))
        else:
            pass


            

    def limpiarListaCelda(self):
        i = 1
        actual = self.primero
        while actual is not None:
            self.primero = None
            actual=actual.siguiente
                
            i += 1
        print("listo")


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
        


        
        
        

        
                


