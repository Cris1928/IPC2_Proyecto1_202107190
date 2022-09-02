from NodoCelda import Celda
import math
import webbrowser
from os import system,startfile
from ListaComparacion import Comparacion
from NodoNumeral import numeralnodo
from ListaNumeral import ListadoNumeral

class ListaC:
    global nuevonumero
    nuevonumero=ListadoNumeral()
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
        
        contador=1
        numeral=1
        while contador<=n:
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
            nuevonumeral=numeralnodo(contador)
            nuevonumero.append(nuevonumeral)
            busqueda=nuevonumero.buscarnumero(contador)
            
            while actual is not None:
                if actual.tipo==2:
                    actual.tipo=0
                elif actual.tipo==3:
                    actual.tipo=1
                else:
                    pass
                nuevasceldas=Comparacion(actual.fila,actual.columna, actual.tipo)
                busqueda.celdas.appendComparar(nuevasceldas)
                actual=actual.siguiente
            self.graficar(contador)
            busqueda.celdas.mostrarCeldas()


            contador=contador+1


        





    def enfermedad(self,numero):
        niveldeenfermedad=0
        actual = self.primero
        m=0
        contador=1
        while actual is not None:
            m=m+1
            actual=actual.siguiente

        while contador<=numero:
            n=0
            busqueda=nuevonumero.buscarnumero(contador)
            actual = self.primero
            while actual is not None:
                prueba=busqueda.celdas.retornarcelda(actual.fila,actual.columna, actual.tipo)
                if prueba== True:
                    n=n+1
                else:
                    pass
                actual=actual.siguiente
            if n == m:
                niveldeenfermedad=niveldeenfermedad+1
            else:
                pass
            contador=contador+1

        return niveldeenfermedad
        
            




















      #      while actual is not None:
       #         if actual.fila == actual2.fila and actual.columna == actual2.columna and actual.tipo== actual2.tipo:
        #            n=n+1
         #       else:
          #          pass
           #     actual=actual.siguiente
            #    actual2=actual2.siguiente

       #     if n==m:
        #        niveldeenfermedad=niveldeenfermedad+1
         #   else:
          #      pass

       # return niveldeenfermedad



    

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


# añadir p dentro de graficar para que sea el nombre de la grafica 

  #  def generarpdf(self,graphviz,p):
   #     i=0
     #   documento = 'grafica' + str(1) +'.txt'
    #    pdf = 'grafica' + str(1) +'.pdf'

      #  with open(documento, 'w') as grafica:
       #     grafica.write(graphviz)

        #system("dot.exe -Tpdf " + documento + " -o " + pdf )
        #webbrowser.open(pdf)  


    def graficar(self,p):
        actual=self.primero
        i=1
        graphviz = 'digraph Patron{ \n node[shape=box fillcolor="#FFEDBB" style=filled];  \n subgraph cluster_p{ \n label = "nombrelabel"   \n bgcolor="#398D9C" \n raiz[label="0,0"]\n edge[dir="none" style=invisible] \n '
        while actual is not None:
            i=i+1
            actual=actual.siguiente
        tamano=int(math.sqrt(i))+1
        for n in range(1,tamano):
            graphviz += 'Fila{}'.format(n)+'[label="{}"'.format(n)+',group=1];\n'
        for n in range(1,tamano-1):
            graphviz += 'Fila{}'.format(n)+'->Fila{};\n'.format(n+1)
        for n in range(1,tamano):
            graphviz += 'Columna{}'.format(n)+'[label="{}"'.format(n)+',group={}'.format(n+1)+',fillcolor=yellow];\n'
        for n in range(1,tamano-1):
            graphviz += 'Columna{}'.format(n)+'-> Columna{};\n'.format(n+1)
        graphviz += 'raiz -> Fila1;\n'
        graphviz += 'raiz -> Columna1;\n'
        graphviz += '{rank=same;raiz;'
        for n in range(1,tamano):
            graphviz += 'Columna{};'.format(n)
        graphviz += '}'
        actual=self.primero
        f=1
        
        while actual is not None:
            if actual.fila==f:
                actual2=self.primero
                c=1
                while actual2 is not None:
                    if actual2.fila==actual.fila:
                        if actual2.tipo==1:
                            graphviz += 'nodo{}'.format(f)+'_{}'.format(actual2.columna)+ '[label="{}'.format(f)+',{}"'.format(actual2.columna)+',fillcolor=blue,'+'group={}]'.format(int(actual2.columna)+1)  +'\n'
                        elif actual2.tipo==0:
                            graphviz += 'nodo{}'.format(f)+'_{}'.format(actual2.columna)+ '[label="{}'.format(f)+',{}"'.format(actual2.columna)+',fillcolor=white,'+'group={}]'.format(int(actual2.columna)+1)  +'\n'
                        else:
                            pass
                        c=c+1
                    actual2=actual2.siguiente

                f=f+1
            else:
                pass
            actual=actual.siguiente
        for n in range(1,tamano):
            graphviz += 'Fila{}'.format(n)+'->'+'nodo{}'.format(n) +'_1;' +'\n'
        for n in range(1,tamano): #fila
            for m in range(1,tamano-1):#columna
                graphviz +='nodo{}'.format(n)+'_{}'.format(m)+' -> '+'nodo{}'.format(n)+'_{};'.format(m+1)+'\n'
        
        for n in range(1,tamano): #fila
            graphviz += '{' 
            graphviz +='rank=same;Fila{};'.format(n)
            for m in range(1,tamano):#columna
                graphviz +='nodo{}'.format(n)+'_{};'.format(m)
            graphviz += '}'+'\n'

        for n in range(1,tamano):
            graphviz += 'Columna{}'.format(n)+'->'+'nodo1_'+'{};\n'.format(n)

        for m in range(1,tamano):#columna
            for n in range(1,tamano-1):#fila
                graphviz += 'nodo{}'.format(n)+'_{}'.format(m)+'->'+'nodo{}'.format(n+1)+'_{};\n'.format(m)
        graphviz +='}'+'}'


        #documento = 'grafica' + str(1) +'.txt'
        #pdf = 'grafica' + str(1) +'.pdf'
        #with open(documento, 'w') as grafica:
        #    grafica.write(graphviz)
        #system("dot.exe -Tpdf " + documento + " -o " + pdf )
        #webbrowser.open(pdf) 



        
        miArchivo=open("graphviz{}.dot".format(p),"w")
        miArchivo.write(graphviz)
        miArchivo.close()
        system("dot -Tpng graphviz{}.dot".format(p)+" -o graphviz{}.png".format(p))
       # ###########print(graphviz)

            
    def generarpdf(self):
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
        


        
        
        

        
                

