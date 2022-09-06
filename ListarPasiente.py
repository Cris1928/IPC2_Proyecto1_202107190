from NodoPaciente import pacienten
class passiente:
        def __init__(self)-> None:
                self.primero=pacienten()
                self.ultimo=pacienten()

        def append(self,nuevopaciente):
                if self.primero.nombre is None:
                        self.primero=nuevopaciente
                        self.ultimo=nuevopaciente
                elif self.primero.siguiente is None:
                        self.primero.siguiente=nuevopaciente
                        self.ultimo=nuevopaciente
                else:
                        self.ultimo.siguiente=nuevopaciente
                        self.ultimo=nuevopaciente
        def print(self):
                nodoaux=self.primero
                cadena= ""
                num=1
                while True:
                        if nodoaux.nombre is not None:
                                #cadena +="("+nodoaux.nombre+" "+nodoaux.edad+" "+nodoaux.periodo+" "+nodoaux.m +")"
                                cadena +=str(num)+". ("+nodoaux.nombre+")"
                                if nodoaux.siguiente is not None:
                                        nodoaux=nodoaux.siguiente
                                        cadena+="\n"
                                        num=num+1
                                else:
                                        break
                        else:
                                break
                print(cadena)

        def buscarpaciente(self,nombre):
                nodoaux=self.primero
                while nodoaux.nombre != nombre:
                        if nodoaux.siguiente is not None:
                                nodoaux=nodoaux.siguiente
                        else:
                                return None
                return nodoaux

        

        def returnNombrePaciente(self, numero):
                
                actual = self.primero
                i = 1
                
                while actual is not None:
                
                        if i == numero:
                                #returnpasciente = pacienten(actual.nombre,actual.edad,actual.periodo,actual.m)
                                returnpasciente = actual.nombre
                                return returnpasciente
                
                        actual = actual.siguiente
                        i += 1             




        def limpiarList(self):
            i = 1
            actual = self.primero
            while actual is not None:
                self.primero = None
                actual=actual.siguiente
                
                i += 1
  