from NodoCelda import Celda
import math
import webbrowser
from os import system,startfile
from ListaComparacion import Comparacion
from NodoNumeral import numeralnodo
from ListaNumeral import ListadoNumeral
from fpdf import FPDF
from colorama import Fore
class ListaC:
#    global nuevonumero
 #   nuevonumero=ListadoNumeral()
    def __init__(self)-> None:
        self.primero=Celda()
        self.ultimo=Celda()
        self.size=0
    
    def append(self, nuevasceldas):
        if self.primero.fila is None:
            self.primero=nuevasceldas
            self.ultimo=nuevasceldas
            self.size += 1
        elif self.primero.siguiente is None:
            self.primero.siguiente=nuevasceldas
            nuevasceldas.anterior=self.primero
            self.ultimo=nuevasceldas
            self.size += 1

        
        else:
            self.ultimo.siguiente=nuevasceldas
            nuevasceldas.anterior=self.ultimo
            self.ultimo=nuevasceldas
            self.size += 1


    def evaluar(self,n):
        global nuevonumero
        nuevonumero=ListadoNumeral()
        
        contador=0
        numeral=1
        while contador<=n:
            
            nuevonumeral=numeralnodo(contador)
            nuevonumero.append(nuevonumeral)
            busqueda=nuevonumero.buscarnumero(contador)
            actual=self.primero
            while actual is not None:

                nuevasceldas=Comparacion(actual.fila,actual.columna, actual.tipo)
                busqueda.celdas.appendComparar(nuevasceldas)
                actual=actual.siguiente
            self.graficar(contador)

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


    def enfermedad(self,numero):
        niveldeenfermedad=0
        actual = self.primero
        m=0
        enfermedadleve=0
        contador=0  
        while actual is not None:
            m=m+1
            enfermedadleve=enfermedadleve+1
            actual=actual.siguiente
        while contador<=numero:
            periodorepetido=0
            contador2=contador+1
            while contador2 <=numero:
                n=0
                comprobante_de_enfermedad_leve=0
                busqueda=nuevonumero.buscarnumero(contador)
               
                actual2 = busqueda.celdas.primero
                busqueda2=nuevonumero.buscarnumero(contador2)
                while actual2 is not None:
                 #   print('fila: ' + str(actual2.fila) + ' columna: ' + str(actual2.columna) + ' tipo: ' + str(actual2.tipo))
                    prueba=busqueda2.celdas.retornarcelda(actual2.fila,actual2.columna, actual2.tipo)
                    if prueba== True:
                        n=n+1
                    else:
                        pass
                    actual2=actual2.siguiente
                if n != m:
                    periodorepetido=periodorepetido+1   
                elif n== m:
                    aux=contador
                    periodorepetido=periodorepetido+1
                    print(Fore.MAGENTA+"El patron {}".format(contador)+" se repite en los periodos: \n")
                    while aux <=numero:
                        print("periodo {}".format(aux))
                        aux=aux+periodorepetido
                    return periodorepetido
                else: 
                    pass   
               # print(" ")
                contador2=contador2+1
            contador=contador+1
        nuevonumero.limpiarList()
        return periodorepetido
        


    def enfermedadXML(self,numero):
        niveldeenfermedad=0
        actual = self.primero
        m=0
        enfermedadleve=0
        contador=0  
        while actual is not None:
            m=m+1
            enfermedadleve=enfermedadleve+1
            actual=actual.siguiente
        while contador<=numero:
            periodorepetido=0
            contador2=contador+1
            while contador2 <=numero:
                n=0
                comprobante_de_enfermedad_leve=0
                busqueda=nuevonumero.buscarnumero(contador)
               
                actual2 = busqueda.celdas.primero
                busqueda2=nuevonumero.buscarnumero(contador2)
                while actual2 is not None:
                    prueba=busqueda2.celdas.retornarcelda(actual2.fila,actual2.columna, actual2.tipo)
                    if prueba== True:
                        n=n+1
                    else:
                        pass
                    actual2=actual2.siguiente
                if n != m:
                    periodorepetido=periodorepetido+1   
                elif n== m:
                    aux=contador
                    periodorepetido=periodorepetido+1
                    while aux <=numero:
                        aux=aux+periodorepetido
                    return periodorepetido
                else: 
                    pass   
               # print(" ")
                contador2=contador2+1
            contador=contador+1
        nuevonumero.limpiarList()
        return periodorepetido

    def RetornarPatron(self,numero):
        niveldeenfermedad=0
        actual = self.primero
        m=0
        enfermedadleve=0
        contador=0  
        while actual is not None:
            m=m+1
            enfermedadleve=enfermedadleve+1
            actual=actual.siguiente
        while contador<=numero:
            periodorepetido=0
            contador2=contador+1
            while contador2 <=numero:
                n=0
                comprobante_de_enfermedad_leve=0
                busqueda=nuevonumero.buscarnumero(contador)
               
                actual2 = busqueda.celdas.primero
                busqueda2=nuevonumero.buscarnumero(contador2)
                while actual2 is not None:
                 #   print('fila: ' + str(actual2.fila) + ' columna: ' + str(actual2.columna) + ' tipo: ' + str(actual2.tipo))
                    prueba=busqueda2.celdas.retornarcelda(actual2.fila,actual2.columna, actual2.tipo)
                    if prueba== True:
                        n=n+1
                    else:
                        pass
                    actual2=actual2.siguiente
                if n != m:
                    periodorepetido=periodorepetido+1   
                elif n== m:
                    return contador
                else: 
                    pass   
               # print(" ")
                contador2=contador2+1
            contador=contador+1
        return " "


    def evaluarXML(self,n):
        global nuevonumero
        nuevonumero=ListadoNumeral()
        
        contador=0
        numeral=1
        while contador<=n:
            
            nuevonumeral=numeralnodo(contador)
            nuevonumero.append(nuevonumeral)
            busqueda=nuevonumero.buscarnumero(contador)
            actual=self.primero
            while actual is not None:

                nuevasceldas=Comparacion(actual.fila,actual.columna, actual.tipo)
                busqueda.celdas.appendComparar(nuevasceldas)
                actual=actual.siguiente

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


    def graficar(self,p):
        actual=self.primero
        i=1
        graphviz = 'digraph Patron{ \n node[shape=box fillcolor="#FFEDBB" style=filled];  \n subgraph cluster_p{ \n label ='+ '"periodo-{}"'.format(p)+'\n bgcolor="#398D9C" \n raiz[label="0,0"]\n edge[dir="none" style=invisible] \n '
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




      #           def enfermedad(self,numero):
       # niveldeenfermedad=0
        #actual = self.primero
 #       m=0
  #      enfermedadleve=0
   #     contador=0  
    #    while actual is not None:
     #       m=m+1
      #      enfermedadleve=enfermedadleve+1
       #     actual=actual.siguiente
 #       while contador<=numero:
  #          periodorepetido=0
   #         contador2=contador+1
    #        while contador2 <=numero:
     #           n=0
      #          comprobante_de_enfermedad_leve=0
       #         busqueda=nuevonumero.buscarnumero(contador)
        #        actual2 = busqueda.celdas.primero
         #       while actual2 is not None:
          #          if actual2.tipo==0:
           #             comprobante_de_enfermedad_leve=comprobante_de_enfermedad_leve+1
            #        actual2=actual2.siguiente
             #   if comprobante_de_enfermedad_leve==enfermedadleve:
              #      return 0
                #else:
               #     pass
           #     actual2 = busqueda.celdas.primero
            #    busqueda2=nuevonumero.buscarnumero(contador2)
    #            while actual2 is not None:
     #            #   print('fila: ' + str(actual2.fila) + ' columna: ' + str(actual2.columna) + ' tipo: ' + str(actual2.tipo))
      #              prueba=busqueda2.celdas.retornarcelda(actual2.fila,actual2.columna, actual2.tipo)
       #             if prueba== True:
         #               n=n+1
        #            else:
          #              pass
           #         actual2=actual2.siguiente
            #    if n != m:
             #       periodorepetido=periodorepetido+1   
              #  elif n== m:
               #     aux=contador
          #          periodorepetido=periodorepetido+1
           #         print(Fore.MAGENTA+"El patron {}".format(contador)+" se repite en los periodos: \n")
        #            while aux <=numero:
         #               print("periodo {}".format(aux))
       #                 aux=aux+periodorepetido
      #              return periodorepetido
     #           else: 
    #                pass   
   #            # print(" ")
  #              contador2=contador2+1
 #           contador=contador+1
#        nuevonumero.limpiarList()
       # return periodorepetido