
"""








 <paciente>


        <datospersonales>
            <nombre>Daniel</nombre>
            <edad>14</edad>
        </datospersonales>
        <periodos>6</periodos>
        <m>15</m>
        <rejilla>
            <celda f="2" c="1" />
            <celda f="3" c="2" />
            <celda f="4" c="1" />
            <celda f="5" c="2" />
            <celda f="3" c="6" />
            <celda f="3" c="7" />
            <celda f="3" c="6" />
            <celda f="2" c="7" />
        </rejilla>


 </paciente>


































 #ruta = input('ingrese la dirección de su archivo XML: ')
        try:
            xmlfile=open('C:\Users\USER\Desktop\IPC2_Proyecto1_202107190\archivo de prueba\prueba.xml')
            if xmlfile.readable():
                xmldata= ET.fromstring(xmlfile.read())
                lstcel=xmldata.findall('datospersonales')
                for rejilla in lstcel:

                    print(f"...{rejilla.find('nombre').text}")
                    print("------------------------------------------")


                    #if rejilla.tag.lower() == 'c':
                
                     #   r = int(subelement.text)
                      #  #print(r)
            
                   # elif rejilla.tag.lower() == 'f':
                
                    #     c = int(subelement.text)
                     #    #print(c)

            
            
        except Exception as err:    
            print("Error: ", err)   
        finally:
            xmlfile.close()






-----------------------------------------------
tree=ET.parse('prueba.xml')
        root=tree.getroot()
        def nombres(nombre):
            return nombre.text
            
        def Edades(edad):
            return edad.text

        def rango(m):
            return m.text
        
        def celdas(celda):
            return celda.attrib
        print("----------------------------------------")
        nombress=list(map(nombres,root.iter('nombre: ')))
        edadess=list(map(Edades,root.iter('edad: ')))
        rangos=list(map(rango,root.iter('rango: ')))
        celdass=list(map(celdas,root.iter('celdas: ')))
        print(nombress)
        print(edadess)
        print(rangos)
        print(celdass)

------------------------------------------------------------------
try:

            ruta="prueba.xml"
           # ruta = input('ingrese la dirección de su archivo XML: ')
            tree = ET.parse(ruta)
            root = tree.getroot()
            
        except:
                
            print('|---------- ERROR: Datos no cargados-----------|')    

    elif n == '2':
        ruta="prueba.xml"
        tree=ET.parse(ruta)
        root = tree.getroot()
        for elemento in root:
            for datos in elemento.findall('.//paciente/datospersonales'):
                nombre=datos.text
                print(nombre)





------------------------------------------------------------------------------------------------------
    def enfermedad(self,numero):
        niveldeenfermedad=0
        actual = self.primero
        m=0
        contador=0  
        while actual is not None:
            m=m+1
            actual=actual.siguiente

     #   while contador <=numero:
      #      busqueda1=nuevonumero.buscarnumero(contador)
       #     actual=busqueda1.celdas.primero
        while contador<=numero:
            periodorepetido=0
            contador2=contador+1
            while contador2 <=numero:
                n=0
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
                    print("El patron {}".format(contador)+" se repite en los periodos: ")
                    while aux <=numero:
                        print("periodo {}".format(aux),"\n")
                        aux=aux+periodorepetido
                    return periodorepetido
                else: 
                    pass   
               # print(" ")
                contador2=contador2+1
            contador=contador+1
        nuevonumero.limpiarList()
        return periodorepetido
-----------------------------------------------------------------------------------------------------
    def retornarcelda(self,fila,columna,tipo):

        actual=self.primero
        while actual is not None:
            if fila == actual.fila and columna==actual.columna and tipo==actual.tipo:
                return True
            else: 
                pass
            actual=actual.siguiente
        return False






"""