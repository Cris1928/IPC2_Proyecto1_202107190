from NodoPaciente import pacienten
from colorama import Fore
class passiente:
        def __init__(self)-> None:
                self.primero=pacienten()
                self.ultimo=pacienten()
                self.size=0

        def append(self,nuevopaciente):
                if self.primero.nombre is None:
                        self.primero=nuevopaciente
                        self.ultimo=nuevopaciente
                        self.size += 1
                elif self.primero.siguiente is None:
                        self.primero.siguiente=nuevopaciente
                        self.ultimo=nuevopaciente
                        self.size += 1
                else:
                        self.ultimo.siguiente=nuevopaciente
                        self.ultimo=nuevopaciente
                        self.size += 1
        def print(self):
                nodoaux=self.primero
                cadena= ""
                num=1
                while True:
                        if nodoaux.nombre is not None:
                                cadena +=Fore.LIGHTGREEN_EX+str(num)+". ("+nodoaux.nombre+")"
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
                
                while i < (self.size + 1):
                
                        actual = self.primero.siguiente
                        self.primero = None
                        self.primero = actual
                        
                        i += 1
                
                self.size = 0 

        def returnTamano(self):
                tamano=0
                actual=self.primero
                while actual is not None:
                        tamano=tamano+1
                        actual=actual.siguiente
                return tamano
